# compress-action

Github Action to create a various format archive file for your artifacts, and it works on any platform. This action is powered by python's `shutil.make_archive`, and probably lightweight because it works without docker build.

## Supported format

- zip
- tar
- tar.gz (tgz)
- tar.bz2 (tbz2)
- tar.xz (txz)

## Usage

```yaml
      - name: Create zip
        uses: ihiroky/archive-action@v1
        with:
          root_dir: path_to_arhive_root_directory
          file_path: path_to_archive.zip
```
If you set like [this](https://github.com/ihiroky/compress-action/blob/main/.github/workflows/test.yml), the archive file contains `hoge/fuga/file` and `file` 

### Arguments

- root_dir (required)

  Root directory to archive.

- base_dir (optional, default: `'.'`)

  Base directory; common prefix of all files and directories in the archive, relative to root_dir. See also [Archiving example with base_dir](https://docs.python.org/ja/3/library/shutil.html#shutil-archiving-example-with-basedir)
 
- file_path (optional, default: `'output.zip'`)

  Output file path. This extension determines the format of the archive.

- verbose: (optional, default: `false`)

  Shows details about the result of running this action.
