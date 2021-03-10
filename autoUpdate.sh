timestamp=$(date +'%Y%m%d %H%M%S')
echo $timestamp
git add -A
git commit -m "auto update $timestamp"
git push origin master
