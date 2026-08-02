---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/additional-resources.html
---

# Additional resources
<a name="additional-resources"></a>

## Grafana
<a name="grafana"></a>

This section introduces how to set up a Grafana environment. If you want the solution to generate dashboards in Grafana automatically, you must perform the following deployment. If you only want to store the data in Amazon S3 without creating dashboards, you can skip this section.

 **Step 1: Install Grafana**

**Note**
Skip this step if you already have a Grafana environment.

 **Prerequisite:**

An EC2 instance has been launched, supporting both x86 and ARM architecture.

The following steps provide an example using m6g.medium instance type, ARM architecture, and Amazon 2023. For more details, refer to [Install Grafana](https://grafana.com/docs/grafana/latest/setup-grafana/installation/).

```
# Edit/etc/yum.repos.d/grafana.repo file，input below content
[grafana]
name=grafana
baseurl=https://rpm.grafana.com
repo_gpgcheck=1
enabled=1
gpgcheck=1
gpgkey=https://rpm.grafana.com/gpg.key
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt

# install grafana
yum install -y grafana

# Start grafana，and check its running status
systemctl start grafana-server
systemctl status grafana-server

# grafana listens on port 3000 by default, Users can edit /etc/grafana/grafana.ini to modify the configuration

# Acccess grafana，using the default credentials admin / admin，you will be promoted to change the password on the first login.
http://{instance-ip}:3000/

# If you need public access, please configure an Application Load Balancer (ALB) on your own.
# When configuring the ALB, modify the Idle timeout to 1800 to avoid the following error during large data queries (when a single API call exceeds 60 seconds)：
# "a padding to disable MSIE and Chrome friendly error page"
```

 **Step 2: Authorize the EC2 where Grafana is located to access Athena**

 **Prerequisites:**
+ You have deployed Grafana on EC2.
+ EC2 has been configured with an IAM Instance Profile. You must record the corresponding **role ARN** of the Instance Profile.

Follow these steps:

1. Access [IAM Management Console](https://console.aws.amazon.com/iam/home).

1. Search for "AthenaPublicAccessRole" and choose it to access the details page. Record the role ARN, which will be used later.

1. Choose the **Trust relationships** tab.

1. Choose **Edit trust policy**.

1. Choose **Add** next to **Add a principal**.

1. Select **IAM Roles** from the **Principal type** dropdown list.

1. Enter the role ARN that you recorded in Step 2.

1. Choose **Add principal**.

1. Choose **update policy**.

 **Step 3: Install Amazon Athena plugins**

 **Prerequisites:**
+ Grafana is installed.
+ Grafana is accessible over the public network.

Follow these steps:

1. Access the Grafana console.

1. Select **Administration** from the left navigation pane, and then choose **Plugins**.

1. Select **All** in the **State** section on the right side.

1. In the search box, enter Athena and choose the\* Amazon Athena\* to access the details page.

1. Choose **Install** on the page and wait for the plugin installation to complete.

 **Step 4: Create service accounts**

Follow these steps:

1. Access the Grafana console.

1. Select **Administration** from the left navigation pane, and then choose **Service accounts**.

1. Select **Add service account**.

1. Enter a display name. For example, "johndoe".

1. Select the role as Admin.

1. Choose **Create**.

1. Choose **Add service account token**.

1. Choose **Generate token**.

1. Choose **Copy to clipboard and close**.

1. Save and record this token, which will be used when you must create a pipeline.

## OpenSSL 1.1 Installation
<a name="openssl-1.1-installation"></a>

Centralized Logging with OpenSearch uses Fluent Bit as the log agent, which requires [OpenSSL 1.1](https://www.openssl.org/source/) or later. You can install the dependency according to your operating system (OS). It is recommended to make your own AMI with OpenSSL 1.1 installed.

**Important**
Important If your OS is not listed in the following sections, you can follow the official installation guide to install OpenSSL.

### Amazon Linux 2
<a name="amazon-linux-2"></a>

```
sudo yum install openssl11
```

### Ubuntu
<a name="ubuntu"></a>

 **22.04**

```
ln -s /usr/lib/x86_64-linux-gnu/libsasl2.so.2 /usr/lib/libsasl2.so.3
ln -s /snap/core18/current/usr/lib/x86_64-linux-gnu/libssl.so.1.1 /usr/lib/libssl.so.1.1
ln -s /snap/core18/current/usr/lib/x86_64-linux-gnu/libcrypto.so.1.1 /usr/lib/libcrypto.so.1.1
```

 **20.04**

```
ln -s /usr/lib/x86_64-linux-gnu/libsasl2.so.2 /usr/lib/libsasl2.so.3
```

 **18.04**

```
ln -s /usr/lib/x86_64-linux-gnu/libsasl2.so.2 /usr/lib/libsasl2.so.3
```

### Debian
<a name="debian"></a>

 **GNU/10**

```
ln -s /usr/lib/x86_64-linux-gnu/libsasl2.so.2 /usr/lib/libsasl2.so.3
```

 **GNU/11**

```
ln -s /usr/lib/x86_64-linux-gnu/libsasl2.so.2 /usr/lib/libsasl2.so.3
```

### Red Hat Enterprise Linux
<a name="red-hat-enterprise-linux"></a>

 **8.X**

OpenSSL 1.1 is installed by default.

 **7.X**

```
sudo su -

yum install -y https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_amd64/amazon-ssm-agent.rpm

systemctl enable amazon-ssm-agent
systemctl start amazon-ssm-agent

yum install -y wget perl unzip gcc zlib-devel
mkdir /tmp/openssl
cd /tmp/openssl
wget https://www.openssl.org/source/openssl-1.1.1s.tar.gz
tar xzvf openssl-1.1.1s.tar.gz
cd openssl-1.1.1s
./config --prefix=/usr/local/openssl11 --openssldir=/usr/local/openssl11 shared zlib
make
make install

echo /usr/local/openssl11/lib/ >> /etc/ld.so.conf
ldconfig
```

### SUSE Linux Enterprise Server
<a name="suse-linux-enterprise-server"></a>

 **15**

OpenSSL 1.1 is installed by default.

## Create Instance Group for CentOS 7
<a name="create-instance-group-for-centos-7"></a>

**Note**
Note: CentOS Linux 7 will reach end of life (EOL) on June 30, 2024. It is not an OS well tested with this solution. Consider this guide as a reference only.

1. Log in to your CentOS 7 machine and install SSM Agent manually.

   ```
   sudo yum install -y https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_amd64/amazon-ssm-agent.rpm
   sudo systemctl enable amazon-ssm-agent
   sudo systemctl start amazon-ssm-agent
   ```

1. Go to the **Instance Group** panel of Centralized Logging with OpenSearch console, create **Instance Group**, select the CentOS 7 machine, choose **Install log agent**, and wait for its status to be **offline**.

1. Log in to CentOS 7 and install fluent-bit 1.9.3 manually.

   ```
   export RELEASE_URL=${FLUENT_BIT_PACKAGES_URL:-https://packages.fluentbit.io}
   export RELEASE_KEY=${FLUENT_BIT_PACKAGES_KEY:-https://packages.fluentbit.io/fluentbit.key}

   sudo rpm --import $RELEASE_KEY
   cat << EOF | sudo tee /etc/yum.repos.d/fluent-bit.repo
   [fluent-bit]
   name = Fluent Bit
   baseurl = $RELEASE_URL/centos/VERSION_ARCH_SUBSTR
   gpgcheck=1
   repo_gpgcheck=1
   gpgkey=$RELEASE_KEY
   enabled=1
   EOF
   sudo sed -i 's|VERSION_ARCH_SUBSTR|\$releasever/\$basearch/|g' /etc/yum.repos.d/fluent-bit.repo
   sudo yum install -y fluent-bit-1.9.3-1

   # Modify the configuration file
   sudo sed -i 's/ExecStart.*/ExecStart=\/opt\/fluent-bit\/bin\/fluent-bit -c \/opt\/fluent-bit\/etc\/fluent-bit.conf/g' /usr/lib/systemd/system/fluent-bit.service
   sudo systemctl daemon-reload
   sudo systemctl enable fluent-bit
   sudo systemctl start fluent-bit
   ```

1. Go back to the **Instance Groups** panel of the Centralized Logging with OpenSearch console and wait for the CentOS 7 machine status to be **Online** and proceed to create the instance group.

## Upload SSL Certificate to IAM
<a name="upload-ssl-certificate-to-iam"></a>

Upload the SSL certificate by running the AWS CLI command upload-server-certificate similar to the following:

```
aws iam upload-server-certificate --path /cloudfront/ \
--server-certificate-name YourCertificate \
--certificate-body file://Certificate.pem \
--certificate-chain file://CertificateChain.pem \
--private-key file://PrivateKey.pem
```

Replace the file names and Your Certificate with the names for your uploaded files and certificate. Specify the file:// prefix in the certificate-body, certificate-chain, and private key parameters in the API request. Otherwise, the request fails with a MalformedCertificate: Unknown error message.

**Note**
You must specify a path using the --path option. The path must begin with /cloudfront and must include a trailing slash (for example, /cloudfront/test/).

After the certificate is uploaded, the AWS command upload-server-certificate returns metadata for the uploaded certificate, including the certificate’s Amazon Resource Name (ARN), friendly name, identifier (ID), and expiration date.

To view the uploaded certificate, run the AWS CLI command list-server-certificates:

```
aws iam list-server-certificates
```

For more information, see [uploading a server certificate](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html#upload-server-certificate) to IAM.

## Fix version `GLIBC\_2.25' not found issue
<a name="fix-version-glibc-2.25-not-found-issue"></a>

This error is caused by the old version of glibc. Centralized Logging with OpenSearch with a version later than 1.2 requires glibc-2.25 or above. So you must upgrade the existing version in EC2 first. The upgrade command for different kinds of OS is shown as follows:

**Important**
We strongly recommend you run the commands with environments first. Any upgrade failure may cause severe loss.

 **Redhat 7.9**

For Redhat 7.9, the whole process will take about 2 hours, and at least 10 GB storage is needed.

```
# install library
yum install -y gcc gcc-c++ m4 python3 bison  fontconfig-devel  libXpm-devel texinfo bzip2 wget
echo /usr/local/lib  >> /etc/ld.so.conf

# create tmp directory
mkdir -p /tmp/library
cd /tmp/library

# install gmp-6.1.0
wget https://ftp.gnu.org/gnu/gmp/gmp-6.1.0.tar.bz2
tar xjvf gmp-6.1.0.tar.bz2
cd gmp-6.1.0
./configure --prefix=/usr/local
make && make install
ldconfig
cd ..

# install mpfr-3.1.4
wget https://gcc.gnu.org/pub/gcc/infrastructure/mpfr-3.1.4.tar.bz2
tar xjvf mpfr-3.1.4.tar.bz2
cd mpfr-3.1.4
./configure --with-gmp=/usr/local --prefix=/usr/local
make && make install
ldconfig
cd ..

# install mpc-1.0.3
wget https://gcc.gnu.org/pub/gcc/infrastructure/mpc-1.0.3.tar.gz
tar xzvf mpc-1.0.3.tar.gz
cd mpc-1.0.3
./configure --prefix=/usr/local
make && make install
ldconfig
cd ..

# install gcc-9.3.0
wget https://ftp.gnu.org/gnu/gcc/gcc-9.3.0/gcc-9.3.0.tar.gz
tar xzvf gcc-9.3.0.tar.gz
cd gcc-9.3.0
mkdir build
cd build/
../configure --enable-checking=release --enable-language=c,c++ --disable-multilib --prefix=/usr
make -j4 && make install
ldconfig
cd ../..

# install make-4.3
wget https://ftp.gnu.org/gnu/make/make-4.3.tar.gz
tar xzvf make-4.3.tar.gz
cd make-4.3
mkdir build
cd build
../configure --prefix=/usr
make && make install
cd ../..

# install glibc-2.31
wget https://ftp.gnu.org/gnu/glibc/glibc-2.31.tar.gz
tar xzvf glibc-2.31.tar.gz
cd glibc-2.31
mkdir build
cd build/
../configure  --prefix=/usr --disable-profile --enable-add-ons --with-headers=/usr/include --with-binutils=/usr/bin --disable-sanity-checks --disable-werror
make all && make install
make localedata/install-locales

# clean tmp directory
cd /tmp
rm -rf /tmp/library
```

 **Ubuntu 22**

```
sudo ln -s /snap/core20/1623/usr/lib/x86_64-linux-gnu/libcrypto.so.1.1 /usr/lib/x86_64-linux-gnu/libcrypto.so.1.1
sudo ln -s /snap/core20/1623/usr/lib/x86_64-linux-gnu/libssl.so.1.1 /usr/lib/x86_64-linux-gnu/libssl.so.1.1
sudo ln -s /usr/lib/x86_64-linux-gnu/libsasl2.so.2 /usr/lib/libsasl2.so.3
```

 **Amazon Linux 2023**

```
sudo su -

yum install -y wget perl unzip gcc zlib-devel
mkdir /tmp/openssl
cd /tmp/openssl
wget https://www.openssl.org/source/openssl-1.1.1s.tar.gz
tar xzvf openssl-1.1.1s.tar.gz
cd openssl-1.1.1s
./config --prefix=/usr/local/openssl11 --openssldir=/usr/local/openssl11 shared zlib
make
make install

echo /usr/local/openssl11/lib/ >> /etc/ld.so.conf
ldconfig
```
