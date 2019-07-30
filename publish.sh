case "$1" in
prod|stg)
    echo "\n\nEnvironment: $1\n\n"
    ;;
*)
    echo 'prod or stg?'
    exit 1
esac

check_err()
{
    if [ $? -ne 0 ];
    then
        >&2 echo "\n\n$1"
        exit 1
    fi
}

python3 -m unittest discover --start-directory tests

check_err 'Fix tests and try again!'

rm -rf dist/*
rm -rf build/*
rm -rf m10s.egg-info/*

case "$1" in
prod)
    python3 setup.py sdist bdist_wheel
    ;;
stg)
    python3 setup.py egg_info --tag-build=.rc$(date +%s) sdist bdist_wheel
    ;;
esac

check_err 'Trouble generating package'

twine check dist/*

check_err 'Package malformed'

case "$1" in
prod)
    twine upload dist/*
    check_err 'Trouble uploading package to pypi.org'
    ;;
stg)
    python3 -m twine upload --verbose --repository-url https://test.pypi.org/legacy/ dist/*
    check_err 'Trouble uploading package to test.pypi.org'
    ;;
esac
