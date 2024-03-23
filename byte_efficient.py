import argparse
import gzip
import shutil
import os

def compress_file(input_file, output_file, overwrite=False):
    """
    Compresses the input file using gzip compression and saves it as the output file.
    
    Args:
    - input_file: Path to the input file.
    - output_file: Path to save the compressed output file.
    - overwrite: Flag to allow overwriting the output file if it already exists.
    """
    if overwrite or not os.path.exists(output_file):
        with open(input_file, 'rb') as f_in:
            with gzip.open(output_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
    else:
        print(f"Output file '{output_file}' already exists. Use --overwrite option to overwrite.")

def main(input_file, output_file, overwrite=False):
    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Input file '{input_file}' not found.")
        return
    
    # Compress the file
    compress_file(input_file, output_file, overwrite)
    
    # Get file sizes
    input_file_size = os.path.getsize(input_file)
    output_file_size = os.path.getsize(output_file)
    
    # Calculate compression ratio
    compression_ratio = input_file_size / output_file_size
    
    # Print compression information
    print(f"Compression complete:")
    print(f"Original file size: {input_file_size} bytes")
    print(f"Compressed file size: {output_file_size} bytes")
    print(f"Compression ratio: {compression_ratio:.2f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compress data files using gzip compression')
    parser.add_argument('input_file', type=str, help='Path to the input file')
    parser.add_argument('output_file', type=str, help='Path to save the compressed output file')
    parser.add_argument('--overwrite', action='store_true', help='Allow overwriting the output file if it already exists')
    args = parser.parse_args()
    
    main(args.input_file, args.output_file, args.overwrite)
