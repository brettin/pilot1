#!/usr/bin/perl -w
use strict;
use Cwd;

my $null_val = 'n/a';
my $transform = 'log2';
my $start_dir = getcwd;

# arguement: take in a set of directories. Each directory becomes a label.
my @types = qw(Mesothelioma Neuroblastoma);
# my @types = qw(Acute_Myeloid_Leukemia Adrenocortical_Carcinoma Bladder_Urothelial_Carcinoma Brain_Lower_Grade_Glioma Breast_Invasive_Carcinoma Cervical_Squamous_Cell_Carcinoma_and_Endocervical_Adenocarcinoma Cholangiocarcinoma Colon_Adenocarcinoma Esophageal_Carcinoma Glioblastoma_Multiforme Head_and_Neck_Squamous_Cell_Carcinoma High-Risk_Wilms_Tumor Kidney_Chromophobe Kidney_Renal_Clear_Cell_Carcinoma Kidney_Renal_Papillary_Cell_Carcinoma Liver_Hepatocellular_Carcinoma Lung_Adenocarcinoma Lung_Squamous_Cell_Carcinoma Lymphoid_Neoplasm_Diffuse_Large_B-cell_Lymphoma Mesothelioma Neuroblastoma Ovarian_Serous_Cystadenocarcinoma Pancreatic_Adenocarcinoma Pheochromocytoma_and_Paraganglioma Prostate_Adenocarcinoma Rectum_Adenocarcinoma Rhabdoid_Tumor Sarcoma Skin_Cutaneous_Melanoma Stomach_Adenocarcinoma Testicular_Germ_Cell_Tumors Thymoma Thyroid_Carcinoma Uterine_Carcinosarcoma Uterine_Corpus_Endometrial_Carcinoma Uveal_Melanoma);
# my @types = qw(Adrenal_Gland Bile_Duct Bladder Blood Bone_Marrow Brain Breast Cervix Colorectal Esophagus Eye Head_and_Neck Kidney Liver Lung Lymph_Nodes Nervous_System Ovary Pancreas Pleura Prostate Skin Soft_Tissue Stomach Testis Thymus Thyroid Uterus);

# arguement: take in a problem directory name/location
my $prob_dir = "ByType.2";
# my $prob_dir = "BySite.2";

# create the prob_dir and open the output files
!system("mkdir -p $prob_dir") or die "could not mkdir $prob_dir";
open X, ">$prob_dir/X" or die "could not open $prob_dir/X for writing";
open Y, ">$prob_dir/y" or die "could not open $prob_dir/y for writing";
open ROW_H, ">$prob_dir/row.h" or die "";
open COL_H, ">$prob_dir/col.h" or die "";
open Y_MAP, ">$prob_dir/y.map" or die "";


my $X = []; # the matrix to use
my $y = []; # the labels to use
my @row_h;  # array of three-tuples [row_index, short_name, full_name]
my @col_h;  # array of three-tuples [col_index, short_name, full_name]
my @y_map;  # array of two-tuples [label_int, label]



# create the label map for types and write the y.map file
my $new_int = 0;
my %types;
my $label_int = 0;
foreach my $type (@types) {
  if (exists $types{$type}) {
    die "type not unique";
  }
  else {
    $label_int++;
    $types{$type} = $label_int;
  }
} 
my @keys = sort { $types{$a} <=> $types{$b} } keys(%types);
foreach my $key (@keys) {
  push @y_map, [$types{$key}, $key];
}
foreach my $label_map (@y_map) {
  print Y_MAP join("\t", @$label_map), "\n";
}
close Y_MAP;



# create the row map for the samples and write the row.h file
my %rows;
my $row_int = 0;

foreach my $type ( @types ) {
  chdir $type or die "can not chdir to $type";
  my @samples = split /\s+/, `ls`;
  foreach my $sample ( @samples ) {
    die "non unique sample $sample" if exists $rows{$sample};
    $row_int++;
    $rows{$sample} = $row_int;
  }
  chdir $start_dir or die "can not chdir to $start_dir";
}
my @keys = sort { $rows{$a} <=> $rows{$b} } keys(%rows);
foreach my $key (@keys) {
  push @row_h, [$rows{$key}, $key];
}
foreach my $row_map (@row_h) {
  print ROW_H join("\t", @$row_map), "\n";
}    
close ROW_H;


# create the column map and write the col.h file
my %cols;
my $col_int = 0;

foreach my $type ( @types ) {
  chdir $type;
  my @samples = split /\s+/, `ls`;
  foreach my $sample ( @samples ) {
    chdir $sample or die "can not chdir to $sample";
    my $file = `ls *FPKM-UQ.txt`; chomp $file;
    open F, $file or die "can not open $file";
    while(<F>) {
      my ($col, $val) = split /\s+/;
      if (! defined $cols{$col})  {
        $col_int++;
        $cols{$col} = $col_int;
      }
    }
    close F;
    chdir ("../") or die "cannot chdir to ../";
  }
  chdir $start_dir or die "can not chdir to $start_dir";
}
my @keys = sort { $cols{$a} <=> $cols{$b} } keys(%cols);
foreach my $key (@keys) {
  push @col_h, [$cols{$key}, $key];
}
foreach my $col_map (@col_h) {
  print COL_H join("\t", @$col_map), "\n";
}
close COL_H;


# write a row into the matrix, and add a type to y
my $row_int = 0;
foreach my $type (@types) {
  chdir $type;
  my @samples = split /\s+/, `ls`;

  foreach my $sample ( @samples ) {

    my @row;
    $row_int++;
    chdir $sample or die "can not chdir to $sample";
    my $file = `ls *FPKM-UQ.txt`; chomp $file;
    open F, $file or die "can not open $file";

    while(<F>) {
      my ($col, $val) = split /\s+/;
      $row[$cols{$col}-1] = round1( log2($val+1) );
    }
    close F;

    for (my $i=0; $i<@row; $i++) { $row[$i] = $null_val unless defined $row[$i]; }
    print X join("\t", @row), "\n";
    print Y $types{$type}, "\n";
    chdir ("../") or die "cannot chdir to ../";
  }
  chdir $start_dir or die "can not chdir to $start_dir";
}
close X;
close Y;






sub log2 {
  my $n = shift;
  return log($n)/log(2);
}

sub round1 {
  my $float = shift;
  die unless defined $float;
  return $float if $float == 0;
  return sprintf("%.1f", $float);
}


