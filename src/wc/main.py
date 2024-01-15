import sys
import os

class FileInfo:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.bytes = 0
        self.lines = 0
        self.words = 0
        self.chars = 0
        self.max_line_length = 0

    def __repr__(self):
        return "\nFile: " + self.filepath + \
        "\nTotal words: " +  str(self.words) +  \
        "\nTotal chars: " + str(self.chars) + \
        "\nTotal lines: " + str(self.lines) + \
        "\nMax line length: " + str(self.max_line_length) + \
        "\nTotal bytes: " + str(self.bytes)

def process_file(filepath: str) -> FileInfo:
    file_info = FileInfo(filepath)
    try:
        file_info.bytes = os.path.getsize(filepath)
        contents = open(filepath, "r")
        for line in contents.readlines():
            file_info.lines += 1
            file_info.chars += len(line)
            file_info.max_line_length = max(file_info.max_line_length, len(line))
            file_info.words += len(line.split())
            
    except FileNotFoundError | OSError:
        print("Filepath not present:", filepath, ":/")
    except Exception as e:
        print("Cannot open file", filepath, ":/ exception:", e)
    finally:
        contents.close()

    return file_info


def get_cli_args() -> list[str]:
    args = sys.argv
    if len(args) < 2:
        sys.exit("No filepaths provided :/")
    return args[1:]

def main():
    filepaths = get_cli_args()
    for filename in filepaths:
        file_info = process_file(filename)
        print(file_info)
    pass

if __name__ == '__main__':
    main()