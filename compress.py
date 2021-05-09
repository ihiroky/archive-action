import shutil
import os
import sys

def main(file_path, root_dir, base_dir, verbose):
  verbose = '${{ inputs.verbose }}'
  if file_path == '':
    file_path = 'output.zip'
  if root_dir == '':
    print('root_dir must be set.')
    sys.exit(1)
  if base_dir == '':
    base_dir = '.'
  verbose = verbose.lower() == 'true'

  if verbose:
    print('Print environment variables:')
    for k, v in os.environ.items():
      print(' ', k, v)

  def log(fmt, *args):
    if verbose:
      print(fmt.format(*args))

  log('Inputs => file_path:{}, root_dir:{}, base_dir:{}, verbose:{}', file_path, root_dir, base_dir, verbose)

  formats = {
    '.zip': 'zip',
    '.tar': 'tar',
    '.tar.gz': 'gztar',
    '.tgz': 'gztar',
    '.tar.bz2': 'bztar',
    '.tbz2': 'bztar',
    '.tar.xz': 'xztar',
    '.txz': 'xztar',
  }
  default_extensions = {
    'zip': 'zip',
    'tar': 'tar',
    'gztar': 'tar.gz',
    'bztar': 'tar.bz2',
    'xztar': 'tar.xz',
  }

  def split(s, n):
    return s[:-n], s[-(n - 1):]

  base, ext, fmt = '', '', ''
  lc_file_path = file_path.lower()
  for k, v in formats.items():
    if lc_file_path.endswith(k):
      base, ext = split(file_path, len(k))
      fmt = v
      break

  if fmt == '':
    print('Unexpected extension: {0}'.format(file_path))
    sys.exit(2)

  log('filepath => base:{}, ext:{}, fmt:{}', base, ext, fmt)

  archive_name = shutil.make_archive(base, fmt, root_dir, base_dir)
  log('Generated archive:{}', archive_name)
  if not archive_name.endswith(ext):
    os.rename(archive_name, file_path)
    log('Rename from:{} to {}', archive_name, file_path)

  print('{0} is created.'.format(file_path))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
