#FIRST=$(openssl rand -hex 1)
#SECOND=$(openssl rand -hex 1)

count=0
source ./environ
echo $count
if [[($count == 9)]]
then
	count=0
else
	count=$(($count+1))
fi
echo "count=$count" > ./environ

echo 00:00:00:00:00:0$count

sudo spoof-mac set 00:00:00:00:00:0$count "Wi-Fi" 
networksetup -setairportnetwork en0 _____
