# functions relating to manipulating pdfs

combine_pdfs() {
  # Script to combine all PDF files in a directory using Ghostscript
  # Usage: ./combine_pdfs.sh [directory] [output_filename]

  # Set directory (default to current directory if not provided)
  DIR="${1:-.}"

  # Set output filename (default to combined.pdf if not provided)
  OUTPUT="${2:-combined.pdf}"

  # Check if directory exists
  if [ ! -d "$DIR" ]; then
      echo "Error: Directory '$DIR' does not exist"
      exit 1
  fi

  # Find all PDF files in the directory
  PDF_FILES=("$DIR"/*.pdf)

  # Check if any PDF files were found
  if [ ! -e "${PDF_FILES[0]}" ]; then
      echo "Error: No PDF files found in '$DIR'"
      exit 1
  fi

  # Count PDF files
  COUNT=${#PDF_FILES[@]}
  echo "Found $COUNT PDF file(s) in '$DIR'"

  # Check if output file would conflict with input files
  for pdf in "${PDF_FILES[@]}"; do
      if [ "$(basename "$pdf")" == "$OUTPUT" ]; then
          echo "Error: Output filename '$OUTPUT' conflicts with an input file"
          exit 1
      fi
  done

  # Combine PDFs using Ghostscript
  echo "Combining PDFs into '$OUTPUT'..."
  gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile="$OUTPUT" "${PDF_FILES[@]}"

  # Check if the command was successful
  if [ $? -eq 0 ]; then
      echo "Success! Combined PDF saved as '$OUTPUT'"
  else
      echo "Error: Failed to combine PDFs"
      exit 1
  fi
}

