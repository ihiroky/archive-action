import shutil
import os
import sys

file_path = '${{ inputs.file_path }}'
root_dir = '${{ inputs.root_dir }}'
base_dir = '${{ inputs.base_dir }}'
debug = '${{ inputs.debug }}'
if file_path == '':
  file_path = 'output.zip'
if root_dir == '':
  print('root_dir must be set.')
  sys.exit(1)
if base_dir == '':
  base_dir = '.'
debug = True if debug.lower() == 'true' else False

def log(fmt, *args):
  if debug:
    print(fmt.format(*args))

log('file_path:{}, root_dir:{}, base_dir:{}, debug:{}', file_path, root_dir, base_dir, debug)

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

log('base:{}, ext:{}, fmt:{}', base, ext, fmt)

archive_name = shutil.make_archive(base, fmt, root_dir, base_dir)
log('Generated archive:{}', archive_name)
if not archive_name.endswith(ext):
  os.rename(archive_name, file_path)
  log('Rename from:{} to {}', archive_name, file_path)

print('{0} is created.'.format(file_path))
