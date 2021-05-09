#!/usr/bin/python

import shutil
import os
import sys

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
  'txtar': 'tar.xz',
}

def split(s, n):
  return s[:-n], s[-(n - 1):]

file_path = os.environ.get('INPUT_FILE_PATH', 'output.zip')
root_dir = os.environ.get('INPUT_ROOT_DIR')
base_dir = os.environ.get('INPUT_BASE_DIR', '.')
if root_dir is None:
  print('root_dir must be set.')
  sys.exit(1)

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

shutil.make_archive(base, fmt, root_dir, base_dir)
actual='{0}.{1}'.format(base, default_extensions[fmt])
if not actual.endswith(ext):
  os.rename(actual, file_path)
print('{0} is created.'.format(file_path))
