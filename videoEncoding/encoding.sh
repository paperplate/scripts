# Functions relating to manipulating video encodings

videosToAv1(){
  # Set directory (default to current directory if not provided)
  DIR="${1:-.}"
  
  # Check if directory exists
  if [ ! -d "$DIR" ]; then
      echo "Error: Directory '$DIR' does not exist"
      exit 1
  fi

  python convertDir.py $DIR
}
