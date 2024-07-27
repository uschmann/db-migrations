

```bash
apt install libaio1

# instant client herunterladen
wget https://download.oracle.com/otn_software/linux/instantclient/214000/instantclient-basic-linux.x64-21.4.0.0.0dbru.zip

# sqlplus herunterladen
wget https://download.oracle.com/otn_software/linux/instantclient/214000/instantclient-sqlplus-linux.x64-21.4.0.0.0dbru.zip 

mkdir -p /opt/oracle
unzip -d /opt/oracle instantclient-basic-linux.x64-21.4.0.0.0dbru.zip
unzip -d /opt/oracle instantclient-sqlplus-linux.x64-21.4.0.0.0dbru.zip

export LD_LIBRARY_PATH=/opt/oracle/instantclient_21_4
export PATH=$LD_LIBRARY_PATH:$PATH


# Ubuntu
ln -s /usr/lib/x86_64-linux-gnu/libaio.so.1t64 /opt/oracle/instantclient_21_4/libaio.so.1
```