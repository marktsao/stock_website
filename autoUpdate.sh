timestamp=$(date +'%Y%m%d %H%M%S')
echo $timestamp
/usr/bin/git add -A
/usr/bin/git commit -m "auto update $timestamp"
/usr/bin/git push origin master
