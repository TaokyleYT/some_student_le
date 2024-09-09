cd ~/${REPL_SLUG}
rm some_student_le_PyPI/some_student_le/really_not_good.py some_student_le_PyPI/pyproject.toml some_student_le_PyPI/README.md
python update.py
cd some_student_le_PyPI
rm -r dist
poetry update
poetry publish --build -vvv -u __token__ -p $PYPI_API_KEY_SSL
cd ../some_student_le
rm -r dist
poetry update
poetry publish --build -vvv -u __token__ -p $PYPI_API_KEY_RNG