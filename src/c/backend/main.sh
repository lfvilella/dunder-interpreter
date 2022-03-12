#!/bin/bash

# TODO:
# - create args parse
# - think if we should delete IR (.ll)

filepath=$1
ll_replace=".ll"
bin_replace=".out"

ll_filepath=${filepath//.c/$ll_replace}
bin_filepath=${filepath//.c/$bin_replace}

clang -emit-llvm -S $filepath -o $ll_filepath
clang -x ir $ll_filepath -o $bin_filepath
