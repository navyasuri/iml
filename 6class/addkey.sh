mkdir ~/.ssh
touch ~/.ssh/config
echo "Host colfax" > ~/.ssh/config
echo "User u25172" >> ~/.ssh/config
echo "IdentityFile ~/Downloads/colfax-access-key-25172" >> ~/.ssh/config
echo "ProxyCommand ssh -T -i ~/Downloads/colfax-access-key-25172 guest@cluster.colfaxresearch.com" >> ~/.ssh/config
chmod 600 ~/Downloads/colfax-access-key-25172
chmod 600 ~/.ssh/config
echo "Add key Done!"
