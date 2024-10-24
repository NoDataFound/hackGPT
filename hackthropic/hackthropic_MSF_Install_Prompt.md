```
1. Find then icon for a linux terminal and then open it , then run each command after the "#### comment". Run each command one at a time and make sure they complete.  I want to see the output as you run the command.

#### Switch to root user
sudo -i
whoami
#### Install basic tools
apt install -y iputils-ping nano
#### Check internet connectivity
ping -c 4 google.com

#### Clone the Metasploit repository
git clone https://github.com/rapid7/metasploit-framework.git

#### Navigate to the Metasploit directory
cd metasploit-framework

#### Update package list and install required dependencies
apt update
apt install -y \
    build-essential libssl-dev libreadline-dev zlib1g-dev \
    libsqlite3-dev libpq-dev curl git-core \
    libyaml-dev libxml2-dev libxslt1-dev libgmp-dev \
    libpcap-dev postgresql postgresql-contrib \
    libffi-dev libgdbm-dev

#### Install Ruby and Bundler
apt install -y ruby-full
gem install bundler

#### Install Metasploit dependencies
bundle install

#### Start and enable PostgreSQL service
systemctl start postgresql
systemctl enable postgresql

#### Create the Metasploit database user and database
sudo -u postgres createuser msf -P -R -S
sudo -u postgres createdb -O msf msf_database

#### Set the MSF_DATABASE_CONFIG environment variable
echo 'export MSF_DATABASE_CONFIG=/root/metasploit-framework/config/database.yml' >> ~/.bashrc

#### Reload .bashrc to apply the changes
source ~/.bashrc

#### Start Metasploit Console
./msfconsole

#### You should see the Metasploit prompt (`msf6 >`).

#### Test Metasploit Functionality
use auxiliary/scanner/portscan/tcp
set RHOSTS google.com
run

```
