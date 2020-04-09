echo "输入tag"
read versionTag
echo "输入提交信息"
read updateMessage

echo "[BeesKingLib]:开始"
sed -i "" "s/s.version          = .*/s.version          =  '$versionTag'/g" ../BeesKingLib/BeesKingLib.podspec

#git add BeesKingLib.podspec
cd ../BeesKingLib
git add . #全量提交
git commit -m "[更新]podspec,[提交信息]:$updateMessage,tag:$versionTag"
git push

git tag $versionTag
git push --tags
echo "BeesKingLib__tag:完成"

