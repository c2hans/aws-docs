---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Appendix.PHPAutoDiscoveryCompile.html
---

# Compiling the source code for the ElastiCache cluster client for PHP
<a name="Appendix.PHPAutoDiscoveryCompile"></a>

This section covers how to obtain and compile the source code for the ElastiCache Cluster Client for PHP.

There are two packages you need to pull from GitHub and compile; [aws-elasticache-cluster-client-libmemcached](https://github.com/awslabs/aws-elasticache-cluster-client-libmemcached) and [aws-elasticache-cluster-client-memcached-for-php](https://github.com/awslabs/aws-elasticache-cluster-client-memcached-for-php).

**Topics**
+ [Compiling the libmemcached library](#Appendix.PHPAutoDiscoveryCompile.Libmemcached)
+ [Compiling the ElastiCache Memcached auto discovery client for PHP](#Appendix.PHPAutoDiscoveryCompile.Client)

## Compiling the libmemcached library
<a name="Appendix.PHPAutoDiscoveryCompile.Libmemcached"></a>

**To compile the aws-elasticache-cluster-client-libmemcached library**

1. Launch an Amazon EC2 instance.

1. Install the library dependencies.
   + On Amazon Linux 201509 AMI

     ```
     sudo yum install gcc gcc-c++ autoconf libevent-devel
     ```
   + On Ubuntu 14.04 AMI

     ```
     sudo apt-get update
     sudo apt-get install libevent-dev gcc g++ make autoconf libsasl2-dev
     ```

1. Pull the repository and compile the code.

   ```
   Download and install [ https://github.com/awslabs/aws-elasticache-cluster-client-libmemcached/archive/v1.0.18.tar.gz]( https://github.com/awslabs/aws-elasticache-cluster-client-libmemcached/archive/v1.0.18.tar.gz)
   ```

## Compiling the ElastiCache Memcached auto discovery client for PHP
<a name="Appendix.PHPAutoDiscoveryCompile.Client"></a>

The following sections describe how to compile the ElastiCache Memcached Auto Discovery Client

**Topics**
+ [Compiling the ElastiCache Memcached client for PHP 7](#Appendix.PHPAudiscoveryCompile.Client.PHP7)
+ [Compiling the ElastiCache Memcached client for PHP 5](#Appendix.PHPAudiscoveryCompile.PHP5)

### Compiling the ElastiCache Memcached client for PHP 7
<a name="Appendix.PHPAudiscoveryCompile.Client.PHP7"></a>

Run the following set of commands under the code directory. In these commands, replace {{<libmemcached-install-directory>}} with the path where you installed the `aws-elasticache-cluster-client-libmemcached` library in the previous step. If you compiled and installed with the default prefix, this path is typically `/usr/local`.

```
git clone https://github.com/awslabs/aws-elasticache-cluster-client-memcached-for-php.git
cd aws-elasticache-cluster-client-memcached-for-php
git checkout php7
sudo yum install php70-devel
phpize
./configure --with-libmemcached-dir={{<libmemcached-install-directory>}} --disable-memcached-sasl
make
make install
```

**Note**
You can statically link the libmemcached library into the PHP binary so it can be ported across various Linux platforms. To do that, run the following command before `make`:

```
sed -i "s#-lmemcached#{{<libmemcached-install-directory>}}/lib/libmemcached.a -lcrypt -lpthread -lm -lstdc++ -lsasl2#" Makefile
```

### Compiling the ElastiCache Memcached client for PHP 5
<a name="Appendix.PHPAudiscoveryCompile.PHP5"></a>

Compile the `aws-elasticache-cluster-client-memcached-for-php` by running the following commands under the `aws-elasticache-cluster-client-memcached-for-php/` folder. In these commands, replace {{<libmemcached-install-directory>}} with the path where you installed the `aws-elasticache-cluster-client-libmemcached` library. If you compiled and installed with the default prefix, this path is typically `/usr/local`.

```
git clone https://github.com/awslabs/aws-elasticache-cluster-client-memcached-for-php.git
cd aws-elasticache-cluster-client-memcached-for-php
sudo yum install zlib-devel
phpize
./configure --with-libmemcached-dir={{<libmemcached-install-directory>}}
make
make install
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
