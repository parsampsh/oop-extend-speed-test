langs=`python3 generate_code.py --langs`
count=1000

for lang in $langs; do
	python3 generate_code.py $lang $count > tmp-$lang.code
	if [ $lang = 'python' ]; then
		lang_cmd=python3
	else
		lang_cmd=$lang
	fi
	echo $lang:
	echo
	time $lang_cmd tmp-$lang.code
	echo ========================
done

