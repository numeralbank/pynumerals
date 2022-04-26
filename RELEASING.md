# Releasing pynumerals

- Do platform test via tox:
  ```shell
  tox -r
  ```

- Make sure flake8 passes:
  ```shell
  flake8 src
  ```

- Update the version number, by removing the trailing `.dev0` in:
  - `setup.cfg`
  - `src/pynumerals/__init__.py`

- Create the release commit:
  ```shell
  git commit -a -m "release <VERSION>"
  git push origin
  ```

- Create a release tag:
  ```
  gh release create
  ```

- Release to PyPI:
  ```shell
  rm dist/*
  python -m build -n
  twine upload dist/* -u __token__ -p"..."
  ```

- Change version for the next release cycle, i.e. incrementing and adding .dev0
  - `setup.cfg`
  - `src/pynumerals/__init__.py`

- Commit/push the version change:
  ```shell
  git commit -a -m "bump version for development"
  git push origin
  ```
