---
source_url: https://docs.aws.amazon.com/linux/al1/ug/support-info-by-support-statement.html
---

# AL1 Package support statements
<a name="support-info-by-support-statement"></a>

The following topics provide package support statement information for packages in AL1.

This is current as of 2023-07-12T21:54:00.270245.

**Topics**
+ [2018.03 Deprecated Packages](#support-info-by-support-statement-alami2018.03_release)
+ [AL1 EOL December 31, 2023](#support-info-by-support-statement-eol)
+ [aws-apitools-\* packages deprecated March 1, 2017](#support-info-by-support-statement-eol_aws-apitools-common)
+ [Backwards compatibility packages](#support-info-by-support-statement-compat)
+ [Packages that are EOL as of January 1, 2020](#support-info-by-support-statement-eol202001)
+ [MySQL 5.5 EOL December 3, 2018](#support-info-by-support-statement-eol_mysql55)
+ [MySQL 5.6 EOL February 5, 2021](#support-info-by-support-statement-eol_mysql56)
+ [MySQL 5.7 EOL October 21, 2023](#support-info-by-support-statement-eol_mysql57)
+ [OpenJDK 1.7.0 EOL June 30, 2020](#support-info-by-support-statement-eol_java-1.7.0-openjdk)
+ [OpenJDK 1.8.0 EOL December 31, 2023](#support-info-by-support-statement-eol_java-1.8.0-openjdk)
+ [PHP 7.2 upstream EOL November 30, 2020](#support-info-by-support-statement-eol_php72-common)
+ [PHP 7.3 upstream EOL December 6, 2021](#support-info-by-support-statement-eol_php73-common)
+ [PostgreSQL 9.4 upstream EOL February 13, 2020](#support-info-by-support-statement-eol_postgresql94)
+ [PostgreSQL 9.5 upstream EOL February 11, 2021](#support-info-by-support-statement-eol_postgresql95)
+ [PostgreSQL 9.6 upstream EOL November 11, 2021](#support-info-by-support-statement-eol_postgresql96)
+ [Python 3.6 upstream EOL December 31, 2021](#support-info-by-support-statement-eol_python36)
+ [Python 3.8 upstream EOL is after AL1 EOL](#support-info-by-support-statement-eol_python38)
+ [Ruby 2.4 upstream EOL March 31, 2020](#support-info-by-support-statement-eol_ruby24)

## 2018.03 Deprecated Packages
<a name="support-info-by-support-statement-alami2018.03_release"></a>
+ Start Date: 2018-03-31
+ End Date:

The following packages were deprecated with the initial Amazon Linux 2018.03 release announcement and will not receive any further updates. Most were announced to be nearing EOL in the 2016.09 release notes. For more information, see [Amazon Linux AMI 2018.3 release notes](https://aws.amazon.com/amazon-linux-ami/2018.03-release-notes/)

### Packages
<a name="support-info-by-support-statement-packages-alami2018.03_release"></a>

| Package | Note |
| --- | --- |
|  apache-commons-daemon  | The java-1.6.0-openjdk package was deprecated with the AL1 2018.03 release |
|  apcu70-panel  | The php70 package was deprecated with the AL1 2018.03 release |
|  batik  | The java-1.6.0-openjdk package was deprecated with the AL1 2018.03 release |
|  bzr-doc-python26  | The python26 package was deprecated with the AL1 2018.03 release |
|  bzr-fastimport-python26  | The python26 package was deprecated with the AL1 2018.03 release |
|  bzr-python26  | The python26 package was deprecated with the AL1 2018.03 release |
|  collectd-java  | The java-1.6.0-openjdk package was deprecated with the AL1 2018.03 release |
|  compat-mpich  | The python26 package was deprecated with the AL1 2018.03 release |
|  cpp44  | The gcc44 package was deprecated with the AL1 2018.03 release |
|  dbus-python26  | The python26 package was deprecated with the AL1 2018.03 release |
|  fop  | The java-1.6.0-openjdk package was deprecated with the AL1 2018.03 release |
|  gcc44  | The gcc44 package was deprecated with the AL1 2018.03 release |
|  gcc44-c\+\+  | The gcc44 package was deprecated with the AL1 2018.03 release |
|  gcc44-gfortran  | The gcc44 package was deprecated with the AL1 2018.03 release |
|  gcc44-gnat  | The gcc44 package was deprecated with the AL1 2018.03 release |
|  gcc44-objc  | The gcc44 package was deprecated with the AL1 2018.03 release |
|  gcc44-objc\+\+  | The gcc44 package was deprecated with the AL1 2018.03 release |
|  geos-python26  | The python26 package was deprecated with the AL1 2018.03 release |
|  graphviz-php54  | The php54 package was deprecated with the AL1 2018.03 release |
|  graphviz-python26  | The python26 package was deprecated with the AL1 2018.03 release |
|  graphviz-ruby  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  java-1.6.0-openjdk  | The java-1.6.0-openjdk package was deprecated with the AL1 2018.03 release |
|  java-1.6.0-openjdk-demo  | The java-1.6.0-openjdk package was deprecated with the AL1 2018.03 release |
|  java-1.6.0-openjdk-devel  | The java-1.6.0-openjdk package was deprecated with the AL1 2018.03 release |
|  java-1.6.0-openjdk-javadoc  | The java-1.6.0-openjdk package was deprecated with the AL1 2018.03 release |
|  java-1.6.0-openjdk-src  | The java-1.6.0-openjdk package was deprecated with the AL1 2018.03 release |
|  jna  | The java-1.6.0-openjdk package was deprecated with the AL1 2018.03 release |
|  jss  | The java-1.6.0-openjdk package was deprecated with the AL1 2018.03 release |
|  libmudflap44-devel  | The gcc44 package was deprecated with the AL1 2018.03 release |
|  libreadline-java  | The java-1.6.0-openjdk package was deprecated with the AL1 2018.03 release |
|  libstdc\+\+44-devel  | The gcc44 package was deprecated with the AL1 2018.03 release |
|  libstdc\+\+44-static  | The gcc44 package was deprecated with the AL1 2018.03 release |
|  libwebp-java  | The java-1.6.0-openjdk package was deprecated with the AL1 2018.03 release |
|  libxml2-python26  | The python26 package was deprecated with the AL1 2018.03 release |
|  libxslt-python26  | The python26 package was deprecated with the AL1 2018.03 release |
|  mercurial-python26  | The python26 package was deprecated with the AL1 2018.03 release |
|  mod24\_wsgi-python26  | The python26 package was deprecated with the AL1 2018.03 release |
|  mod\_python26  | The python26 package was deprecated with the AL1 2018.03 release |
|  mod\_wsgi-python26  | The python26 package was deprecated with the AL1 2018.03 release |
|  MySQL-python26  | The python26 package was deprecated with the AL1 2018.03 release |
|  mysql51  | The mysql51 package was deprecated with the AL1 2018.03 release |
|  mysql51-bench  | The mysql51 package was deprecated with the AL1 2018.03 release |
|  mysql51-common  | The mysql51 package was deprecated with the AL1 2018.03 release |
|  mysql51-devel  | The mysql51 package was deprecated with the AL1 2018.03 release |
|  mysql51-embedded  | The mysql51 package was deprecated with the AL1 2018.03 release |
|  mysql51-embedded-devel  | The mysql51 package was deprecated with the AL1 2018.03 release |
|  mysql51-libs  | The mysql51 package was deprecated with the AL1 2018.03 release |
|  mysql51-server  | The mysql51 package was deprecated with the AL1 2018.03 release |
|  mysql51-test  | The mysql51 package was deprecated with the AL1 2018.03 release |
|  newt-python26  | The python26 package was deprecated with the AL1 2018.03 release |
|  OpenIPMI-python26  | The python26 package was deprecated with the AL1 2018.03 release |
|  openscap-utils  | The python26 package was deprecated with the AL1 2018.03 release |
|  openssl097a  | The openssl097a package was deprecated with the AL1 2018.03 release |
|  php54  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-bcmath  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-cli  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-common  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-dba  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-devel  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-embedded  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-enchant  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-fpm  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-gd  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-imap  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-intl  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-ldap  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-libpuzzle  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-mbstring  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-mcrypt  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-mssql  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-mysql  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-mysqlnd  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-odbc  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-pdo  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-pecl-amqp  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-pecl-apc  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-pecl-apc-devel  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-pecl-http  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-pecl-http-devel  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-pecl-igbinary  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-pecl-igbinary-devel  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-pecl-imagick  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-pecl-memcache  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-pecl-memcached  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-pecl-oauth  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-pecl-redis  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-pecl-ssh2  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-pecl-xdebug  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-pgsql  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-process  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-pspell  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-recode  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-snmp  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-soap  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-tidy  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-xcache  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-xml  | The php54 package was deprecated with the AL1 2018.03 release |
|  php54-xmlrpc  | The php54 package was deprecated with the AL1 2018.03 release |
|  php70  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-bcmath  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-cli  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-common  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-dba  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-dbg  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-devel  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-embedded  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-enchant  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-fpm  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-gd  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-gmp  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-imap  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-intl  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-json  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-ldap  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-mbstring  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-mcrypt  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-mysqlnd  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-odbc  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-opcache  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-pdo  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-pdo-dblib  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-pecl-apcu  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-pecl-apcu-devel  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-pecl-igbinary  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-pecl-igbinary-devel  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-pecl-imagick  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-pecl-imagick-devel  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-pecl-memcache  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-pecl-memcached  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-pecl-oauth  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-pecl-redis  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-pecl-ssh2  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-pecl-uuid  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-pecl-xdebug  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-pecl-yaml  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-pgsql  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-process  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-pspell  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-recode  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-snmp  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-soap  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-tidy  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-xml  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-xmlrpc  | The php70 package was deprecated with the AL1 2018.03 release |
|  php70-zip  | The php70 package was deprecated with the AL1 2018.03 release |
|  pl-jpl  | The java-1.6.0-openjdk package was deprecated with the AL1 2018.03 release |
|  postgresql8  | The postgresql8 package was deprecated with the AL1 2018.03 release |
|  postgresql8-contrib  | The postgresql8 package was deprecated with the AL1 2018.03 release |
|  postgresql8-devel  | The postgresql8 package was deprecated with the AL1 2018.03 release |
|  postgresql8-docs  | The postgresql8 package was deprecated with the AL1 2018.03 release |
|  postgresql8-libs  | The postgresql8 package was deprecated with the AL1 2018.03 release |
|  postgresql8-plperl  | The postgresql8 package was deprecated with the AL1 2018.03 release |
|  postgresql8-plpython  | The postgresql8 package was deprecated with the AL1 2018.03 release |
|  postgresql8-pltcl  | The postgresql8 package was deprecated with the AL1 2018.03 release |
|  postgresql8-server  | The postgresql8 package was deprecated with the AL1 2018.03 release |
|  postgresql8-test  | The postgresql8 package was deprecated with the AL1 2018.03 release |
|  ppl-java  | The java-1.6.0-openjdk package was deprecated with the AL1 2018.03 release |
|  protobuf-python26  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-argparse  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-babel  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-backports  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-backports-ssl\_match\_hostname  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-beaker  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-boto  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-boto3  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-botocore  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-cairosvg  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-certifi  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-chardet  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-cheetah  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-colorama  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-configobj  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-coverage  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-crypto  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-Cython  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-daemon  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-dateutil  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-decorator  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-decoratortools  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-devel  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-dns  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-docs  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-docutils  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-dtopt  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-ecdsa  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-elixir  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-enchant  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-epdb  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-ethtool  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-fastimport  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-formencode  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-fpconst  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-funcsigs  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-futures  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-genshi  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-gevent  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-greenlet  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-greenlet-devel  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-httplib2  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-httpretty  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-hwdata  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-imaging  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-imaging-devel  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-iniparse  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-inotify  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-inotify-examples  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-ipaddr  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-IPy  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-jinja2  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-jmespath  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-jsonpatch  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-jsonpointer  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-kerberos  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-kid  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-kitchen  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-kitchen-doc  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-krbV  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-ldap  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-libs  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-lockfile  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-lxml  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-lxml-docs  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-lzo  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-m2crypto  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-magic  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-mako  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-markdown  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-markupsafe  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-matplotlib  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-memcached  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-minimock  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-mock  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-mock13  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-nose  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-nose-docs  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-nose-exclude  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-numpy  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-numpy-doc  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-numpy-f2py  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-oauth2  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-paramiko  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-paste  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-paste-deploy  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-paste-script  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-pbr  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-peak-rules  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-peak-util-addons  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-peak-util-assembler  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-peak-util-extremes  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-peak-util-symbols  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-pep8  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-pexpect  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-pip  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-ply  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-prettytable  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-psycopg2  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-psycopg2-doc  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-py  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-pyasn1  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-pyasn1-modules  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-pycairo  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-pycairo-devel  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-pycurl  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-pygments  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-pygpgme  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-PyGreSQL  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-pyliblzma  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-pyOpenSSL  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-pyparsing  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-pyparsing-doc  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-pystache  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-pytest  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-pytz  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-pyudev  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-pyxattr  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-PyYAML  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-requests  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-rsa  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-scipy  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-setuptools  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-simplejson  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-six  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-SOAPpy  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-sphinx  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-sphinx-doc  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-sqlalchemy  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-sure  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-tempita  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-test  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-testtools  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-testtools-doc  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-tools  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-tornado  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-tornado-doc  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-toscawidgets  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-turbocheetah  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-turbokid  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-tw-forms  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-twisted  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-twisted-conch  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-twisted-core  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-twisted-core-doc  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-twisted-lore  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-twisted-mail  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-twisted-names  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-twisted-news  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-twisted-runner  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-twisted-web  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-twisted-words  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-unittest2  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-urlgrabber  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-urllib3  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-virtualenv  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-webob  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-webtest  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-which  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-wsgiproxy  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-zope-filesystem  | The python26 package was deprecated with the AL1 2018.03 release |
|  python26-zope-interface  | The python26 package was deprecated with the AL1 2018.03 release |
|  python27-matplotlib  | The python26 package was deprecated with the AL1 2018.03 release |
|  rpm-python26  | The python26 package was deprecated with the AL1 2018.03 release |
|  rrdtool-php  | The php54 package was deprecated with the AL1 2018.03 release |
|  rrdtool-php54  | The php54 package was deprecated with the AL1 2018.03 release |
|  rrdtool-python26  | The python26 package was deprecated with the AL1 2018.03 release |
|  rrdtool-ruby18  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  ruby18  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  ruby18-augeas  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  ruby18-devel  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  ruby18-irb  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  ruby18-libs  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  ruby18-rdoc  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  ruby18-ri  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  ruby18-shadow  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  ruby18-static  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  ruby19  | The ruby19 package was deprecated with the AL1 2018.03 release |
|  ruby19-devel  | The ruby19 package was deprecated with the AL1 2018.03 release |
|  ruby19-doc  | The ruby19 package was deprecated with the AL1 2018.03 release |
|  ruby19-irb  | The ruby19 package was deprecated with the AL1 2018.03 release |
|  ruby19-libs  | The ruby19 package was deprecated with the AL1 2018.03 release |
|  ruby21  | The ruby21 package was deprecated with the AL1 2018.03 release |
|  ruby21-devel  | The ruby21 package was deprecated with the AL1 2018.03 release |
|  ruby21-doc  | The ruby21 package was deprecated with the AL1 2018.03 release |
|  ruby21-irb  | The ruby21 package was deprecated with the AL1 2018.03 release |
|  ruby21-libs  | The ruby21 package was deprecated with the AL1 2018.03 release |
|  ruby22  | The ruby22 package was deprecated with the AL1 2018.03 release |
|  ruby22-devel  | The ruby22 package was deprecated with the AL1 2018.03 release |
|  ruby22-doc  | The ruby22 package was deprecated with the AL1 2018.03 release |
|  ruby22-irb  | The ruby22 package was deprecated with the AL1 2018.03 release |
|  ruby22-libs  | The ruby22 package was deprecated with the AL1 2018.03 release |
|  rubygem-linecache  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  rubygem18-aws-sdk  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  rubygem18-aws-sdk-doc  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  rubygem18-diff-lcs  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  rubygem18-diff-lcs-doc  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  rubygem18-json  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  rubygem18-json-doc  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  rubygem18-minitest  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  rubygem18-minitest-doc  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  rubygem18-nokogiri  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  rubygem18-nokogiri-doc  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  rubygem18-rake  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  rubygem18-rake-doc  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  rubygem18-rdoc  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  rubygem18-rdoc-doc  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  rubygem18-rspec  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  rubygem18-rspec-core  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  rubygem18-rspec-core-doc  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  rubygem18-rspec-expectations  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  rubygem18-rspec-expectations-doc  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  rubygem18-rspec-mocks  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  rubygem18-rspec-mocks-doc  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  rubygem18-uuidtools  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  rubygem18-uuidtools-doc  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  rubygem19-bigdecimal  | The ruby19 package was deprecated with the AL1 2018.03 release |
|  rubygem19-io-console  | The ruby19 package was deprecated with the AL1 2018.03 release |
|  rubygem19-json  | The ruby19 package was deprecated with the AL1 2018.03 release |
|  rubygem19-minitest  | The ruby19 package was deprecated with the AL1 2018.03 release |
|  rubygem19-rake  | The ruby19 package was deprecated with the AL1 2018.03 release |
|  rubygem19-rdoc  | The ruby19 package was deprecated with the AL1 2018.03 release |
|  rubygem21-bigdecimal  | The ruby21 package was deprecated with the AL1 2018.03 release |
|  rubygem21-io-console  | The ruby21 package was deprecated with the AL1 2018.03 release |
|  rubygem21-json  | The ruby21 package was deprecated with the AL1 2018.03 release |
|  rubygem21-json-doc  | The ruby21 package was deprecated with the AL1 2018.03 release |
|  rubygem21-minitest  | The ruby21 package was deprecated with the AL1 2018.03 release |
|  rubygem21-minitest-doc  | The ruby21 package was deprecated with the AL1 2018.03 release |
|  rubygem21-minitest5  | The ruby21 package was deprecated with the AL1 2018.03 release |
|  rubygem21-minitest5-doc  | The ruby21 package was deprecated with the AL1 2018.03 release |
|  rubygem21-nokogiri  | The ruby21 package was deprecated with the AL1 2018.03 release |
|  rubygem21-nokogiri-doc  | The ruby21 package was deprecated with the AL1 2018.03 release |
|  rubygem21-power\_assert  | The ruby21 package was deprecated with the AL1 2018.03 release |
|  rubygem21-power\_assert-doc  | The ruby21 package was deprecated with the AL1 2018.03 release |
|  rubygem21-psych  | The ruby21 package was deprecated with the AL1 2018.03 release |
|  rubygem21-rake  | The ruby21 package was deprecated with the AL1 2018.03 release |
|  rubygem21-rake-doc  | The ruby21 package was deprecated with the AL1 2018.03 release |
|  rubygem21-rdoc  | The ruby21 package was deprecated with the AL1 2018.03 release |
|  rubygem21-rdoc-doc  | The ruby21 package was deprecated with the AL1 2018.03 release |
|  rubygem22-bigdecimal  | The ruby22 package was deprecated with the AL1 2018.03 release |
|  rubygem22-io-console  | The ruby22 package was deprecated with the AL1 2018.03 release |
|  rubygem22-json  | The ruby22 package was deprecated with the AL1 2018.03 release |
|  rubygem22-json-doc  | The ruby22 package was deprecated with the AL1 2018.03 release |
|  rubygem22-minitest  | The ruby22 package was deprecated with the AL1 2018.03 release |
|  rubygem22-minitest-doc  | The ruby22 package was deprecated with the AL1 2018.03 release |
|  rubygem22-minitest5  | The ruby22 package was deprecated with the AL1 2018.03 release |
|  rubygem22-minitest5-doc  | The ruby22 package was deprecated with the AL1 2018.03 release |
|  rubygem22-nokogiri  | The ruby22 package was deprecated with the AL1 2018.03 release |
|  rubygem22-nokogiri-doc  | The ruby22 package was deprecated with the AL1 2018.03 release |
|  rubygem22-power\_assert  | The ruby22 package was deprecated with the AL1 2018.03 release |
|  rubygem22-power\_assert-doc  | The ruby22 package was deprecated with the AL1 2018.03 release |
|  rubygem22-psych  | The ruby22 package was deprecated with the AL1 2018.03 release |
|  rubygem22-rake  | The ruby22 package was deprecated with the AL1 2018.03 release |
|  rubygem22-rake-doc  | The ruby22 package was deprecated with the AL1 2018.03 release |
|  rubygem22-rdoc  | The ruby22 package was deprecated with the AL1 2018.03 release |
|  rubygem22-rdoc-doc  | The ruby22 package was deprecated with the AL1 2018.03 release |
|  rubygems18  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  rubygems18-devel  | The ruby18 package was deprecated with the AL1 2018.03 release |
|  rubygems19  | The ruby19 package was deprecated with the AL1 2018.03 release |
|  rubygems19-devel  | The ruby19 package was deprecated with the AL1 2018.03 release |
|  rubygems21  | The ruby21 package was deprecated with the AL1 2018.03 release |
|  rubygems21-devel  | The ruby21 package was deprecated with the AL1 2018.03 release |
|  rubygems22  | The ruby22 package was deprecated with the AL1 2018.03 release |
|  rubygems22-devel  | The ruby22 package was deprecated with the AL1 2018.03 release |
|  subversion-python26  | The python26 package was deprecated with the AL1 2018.03 release |
|  subversion-tools  | The python26 package was deprecated with the AL1 2018.03 release |
|  systemtap-devel  | The gcc44 package was deprecated with the AL1 2018.03 release |
|  systemtap-testsuite  | The gcc44 package was deprecated with the AL1 2018.03 release |
|  uuid-php54  | The php54 package was deprecated with the AL1 2018.03 release |
|  yum-metadata-parser-python26  | The python26 package was deprecated with the AL1 2018.03 release |
|  yum-python26  | The python26 package was deprecated with the AL1 2018.03 release |

## AL1 EOL December 31, 2023
<a name="support-info-by-support-statement-eol"></a>
+ Start Date: 2023-12-31
+ End Date:

 The maintenance support period of AL1 ends on December 31st, 2023. After this date, the remaining AL1 packages in the following table will no longer receive any updates from AWS.

 For more information, see [Amazon Linux AMI FAQs](https://aws.amazon.com/amazon-linux-ami/faqs/).

### Packages
<a name="support-info-by-support-statement-packages-eol"></a>

| Package |
| --- |
|  389-admin  |
|  389-admin-console  |
|  389-admin-console-doc  |
|  389-adminutil  |
|  389-adminutil-devel  |
|  389-console  |
|  389-ds  |
|  389-ds-base  |
|  389-ds-base-devel  |
|  389-ds-base-libs  |
|  389-ds-base-snmp  |
|  389-ds-console  |
|  389-ds-console-doc  |
|  389-dsgw  |
|  a2ps  |
|  aalib  |
|  aalib-devel  |
|  aalib-libs  |
|  ack  |
|  acl  |
|  acpid  |
|  adaptx  |
|  adaptx-doc  |
|  adaptx-javadoc  |
|  adcli  |
|  adjtimex  |
|  agg  |
|  agg-devel  |
|  agrep  |
|  aide  |
|  alsa-lib  |
|  alsa-lib-devel  |
|  alsa-utils  |
|  amanda  |
|  amanda-client  |
|  amanda-devel  |
|  amanda-server  |
|  amazon-efs-utils  |
|  amazon-ssm-agent  |
|  amtu  |
|  ant  |
|  ant-antlr  |
|  ant-apache-bcel  |
|  ant-apache-bsf  |
|  ant-apache-log4j  |
|  ant-apache-oro  |
|  ant-apache-regexp  |
|  ant-apache-resolver  |
|  ant-apache-xalan2  |
|  ant-commons-logging  |
|  ant-commons-net  |
|  ant-contrib  |
|  ant-contrib-javadoc  |
|  ant-javadoc  |
|  ant-javamail  |
|  ant-jdepend  |
|  ant-jmf  |
|  ant-jsch  |
|  ant-junit  |
|  ant-manual  |
|  ant-scripts  |
|  ant-swing  |
|  ant-testutil  |
|  antlr  |
|  antlr-javadoc  |
|  antlr-manual  |
|  apache-commons-beanutils  |
|  apache-commons-beanutils-javadoc  |
|  apache-commons-codec  |
|  apache-commons-codec-javadoc  |
|  apache-commons-collections  |
|  apache-commons-collections-javadoc  |
|  apache-commons-collections-testframework  |
|  apache-commons-daemon-javadoc  |
|  apache-commons-daemon-jsvc  |
|  apache-commons-dbcp  |
|  apache-commons-dbcp-javadoc  |
|  apache-commons-digester  |
|  apache-commons-digester-javadoc  |
|  apache-commons-discovery  |
|  apache-commons-discovery-javadoc  |
|  apache-commons-el  |
|  apache-commons-el-javadoc  |
|  apache-commons-io  |
|  apache-commons-io-javadoc  |
|  apache-commons-lang  |
|  apache-commons-lang-javadoc  |
|  apache-commons-logging  |
|  apache-commons-logging-javadoc  |
|  apache-commons-net  |
|  apache-commons-net-javadoc  |
|  apache-commons-parent  |
|  apache-commons-pool  |
|  apache-commons-pool-javadoc  |
|  apache-ivy  |
|  apache-ivy-javadoc  |
|  apache-tomcat-apis  |
|  apc-panel  |
|  apcu-panel  |
|  apr  |
|  apr-devel  |
|  apr-util  |
|  apr-util-devel  |
|  apr-util-freetds  |
|  apr-util-ldap  |
|  apr-util-mysql  |
|  apr-util-nss  |
|  apr-util-odbc  |
|  apr-util-openssl  |
|  apr-util-pgsql  |
|  apr-util-sqlite  |
|  arptables\_jf  |
|  arpwatch  |
|  asciidoc  |
|  asciidoc-doc  |
|  aspell  |
|  aspell-devel  |
|  aspell-en  |
|  aspell-nl  |
|  at  |
|  atlas  |
|  atlas-devel  |
|  atlas-sse3  |
|  atlas-sse3-devel  |
|  attr  |
|  audispd-plugins  |
|  audit  |
|  audit-libs  |
|  audit-libs-devel  |
|  audit-libs-python  |
|  audit-libs-static  |
|  augeas  |
|  augeas-devel  |
|  augeas-libs  |
|  authconfig  |
|  autoconf  |
|  autofs  |
|  autogen  |
|  autogen-libopts  |
|  autogen-libopts-devel  |
|  automake  |
|  automake14  |
|  automake15  |
|  automake16  |
|  automake17  |
|  automake19  |
|  avahi  |
|  avahi-autoipd  |
|  avahi-compat-howl  |
|  avahi-compat-howl-devel  |
|  avahi-compat-libdns\_sd  |
|  avahi-compat-libdns\_sd-devel  |
|  avahi-devel  |
|  avahi-dnsconfd  |
|  avahi-glib  |
|  avahi-glib-devel  |
|  avahi-gobject  |
|  avahi-gobject-devel  |
|  avahi-libs  |
|  avahi-tools  |
|  avalon-framework  |
|  avalon-framework-javadoc  |
|  avalon-framework-manual  |
|  avalon-logkit  |
|  avalon-logkit-javadoc  |
|  aws-amitools-ec2  |
|  aws-cfn-bootstrap  |
|  aws-cli  |
|  aws-cli-plugin-cloudwatch-logs  |
|  aws-cloudhsm-cli  |
|  aws-kinesis-agent  |
|  aws-scripts-ses  |
|  aws-vpc-nat  |
|  awslogs  |
|  axis  |
|  axis-javadoc  |
|  axis-manual  |
|  basesystem  |
|  bash  |
|  bash-doc  |
|  batik-demo  |
|  batik-javadoc  |
|  batik-rasterizer  |
|  batik-slideshow  |
|  batik-squiggle  |
|  batik-svgpp  |
|  batik-ttf2svg  |
|  bc  |
|  bcc  |
|  bcc-devel  |
|  bcc-doc  |
|  bcc-lua  |
|  bcel  |
|  bcel-javadoc  |
|  bcel-manual  |
|  bdftruncate  |
|  bea-stax  |
|  bea-stax-api  |
|  bea-stax-javadoc  |
|  beecrypt  |
|  beecrypt-apidocs  |
|  beecrypt-devel  |
|  beecrypt-python  |
|  bind  |
|  bind-chroot  |
|  bind-devel  |
|  bind-libs  |
|  bind-sdb  |
|  bind-utils  |
|  binutils  |
|  binutils-devel  |
|  bison  |
|  bison-devel  |
|  bison-runtime  |
|  blas  |
|  blas-devel  |
|  blas-static  |
|  blas64  |
|  blas64-devel  |
|  blas64-static  |
|  blktrace  |
|  bonnie\+\+  |
|  boost  |
|  boost-atomic  |
|  boost-build  |
|  boost-chrono  |
|  boost-context  |
|  boost-date-time  |
|  boost-devel  |
|  boost-doc  |
|  boost-examples  |
|  boost-filesystem  |
|  boost-graph  |
|  boost-graph-mpich  |
|  boost-graph-openmpi  |
|  boost-iostreams  |
|  boost-jam  |
|  boost-locale  |
|  boost-math  |
|  boost-mpich  |
|  boost-mpich-devel  |
|  boost-mpich-python  |
|  boost-openmpi  |
|  boost-openmpi-devel  |
|  boost-openmpi-python  |
|  boost-program-options  |
|  boost-python  |
|  boost-random  |
|  boost-regex  |
|  boost-serialization  |
|  boost-signals  |
|  boost-static  |
|  boost-system  |
|  boost-test  |
|  boost-thread  |
|  boost-timer  |
|  boost-wave  |
|  boost141  |
|  boost141-date-time  |
|  boost141-devel  |
|  boost141-doc  |
|  boost141-filesystem  |
|  boost141-iostreams  |
|  boost141-math  |
|  boost141-mpich2-devel  |
|  boost141-openmpi-devel  |
|  boost141-program-options  |
|  boost141-python  |
|  boost141-serialization  |
|  boost141-signals  |
|  boost141-static  |
|  boost141-system  |
|  boost141-test  |
|  boost141-thread  |
|  boost141-wave  |
|  bridge-utils  |
|  bsdcpio  |
|  bsdtar  |
|  bsf  |
|  bsf-javadoc  |
|  bsh  |
|  bsh-demo  |
|  bsh-javadoc  |
|  bsh-manual  |
|  btrfs-progs  |
|  btrfs-progs-devel  |
|  busybox  |
|  busybox-petitboot  |
|  byacc  |
|  byaccj  |
|  bzip2  |
|  bzip2-devel  |
|  bzip2-libs  |
|  c-ares  |
|  c-ares-devel  |
|  ca-certificates  |
|  cachefilesd  |
|  cacti  |
|  cairo  |
|  cairo-devel  |
|  cairo-gobject  |
|  cairo-gobject-devel  |
|  cairo-tools  |
|  cargo  |
|  cargo-doc  |
|  castor  |
|  castor-demo  |
|  castor-doc  |
|  castor-javadoc  |
|  castor-test  |
|  castor-xml  |
|  celt051  |
|  celt051-devel  |
|  check  |
|  check-devel  |
|  check-static  |
|  checkpolicy  |
|  chkconfig  |
|  chkrootkit  |
|  chrony  |
|  chrpath  |
|  cifs-utils  |
|  cifs-utils-devel  |
|  cjkuni-fonts-common  |
|  cjkuni-fonts-ghostscript  |
|  cjkuni-ukai-fonts  |
|  cjkuni-uming-fonts  |
|  clamav  |
|  clamav-data  |
|  clamav-data-empty  |
|  clamav-db  |
|  clamav-devel  |
|  clamav-filesystem  |
|  clamav-lib  |
|  clamav-milter  |
|  clamav-milter-sysvinit  |
|  clamav-scanner  |
|  clamav-scanner-sysvinit  |
|  clamav-server  |
|  clamav-server-sysvinit  |
|  clamav-update  |
|  clamd  |
|  clang  |
|  clang-analyzer  |
|  clang-devel  |
|  clang6.0  |
|  clang6.0-analyzer  |
|  clang6.0-devel  |
|  clang6.0-libs  |
|  clang6.0-tools-extra  |
|  classpathx-jaf  |
|  classpathx-jaf-javadoc  |
|  classpathx-mail  |
|  classpathx-mail-javadoc  |
|  clippy  |
|  cloog-ppl-devel  |
|  cloud-disk-utils  |
|  cloud-init  |
|  cloud-utils  |
|  cluster-glue  |
|  cluster-glue-libs  |
|  cluster-glue-libs-devel  |
|  cmake  |
|  cmake-doc  |
|  cmake3  |
|  cmake3-data  |
|  cmake3-doc  |
|  collectd  |
|  collectd-amqp  |
|  collectd-apache  |
|  collectd-bind  |
|  collectd-chrony  |
|  collectd-curl  |
|  collectd-curl\_xml  |
|  collectd-dbi  |
|  collectd-disk  |
|  collectd-dns  |
|  collectd-drbd  |
|  collectd-email  |
|  collectd-generic-jmx  |
|  collectd-hugepages  |
|  collectd-ipmi  |
|  collectd-iptables  |
|  collectd-ipvs  |
|  collectd-lua  |
|  collectd-lvm  |
|  collectd-mcelog  |
|  collectd-memcachec  |
|  collectd-mysql  |
|  collectd-netlink  |
|  collectd-nginx  |
|  collectd-notify\_email  |
|  collectd-openldap  |
|  collectd-postgresql  |
|  collectd-python  |
|  collectd-rrdcached  |
|  collectd-rrdtool  |
|  collectd-snmp  |
|  collectd-snmp\_agent  |
|  collectd-synproxy  |
|  collectd-utils  |
|  collectd-varnish  |
|  collectd-web  |
|  collectd-write\_http  |
|  collectd-write\_sensu  |
|  collectd-write\_tsdb  |
|  collectd-zookeeper  |
|  collectl  |
|  compiler-rt  |
|  conman  |
|  conntrack-tools  |
|  containerd  |
|  containerd-stress  |
|  copy-jdk-configs  |
|  coreutils  |
|  corosync  |
|  corosynclib  |
|  corosynclib-devel  |
|  cowsay  |
|  cpio  |
|  cpp  |
|  cpp48  |
|  cpp64  |
|  cpp72  |
|  cppunit  |
|  cppunit-devel  |
|  cppunit-doc  |
|  cpuspeed  |
|  cracklib  |
|  cracklib-devel  |
|  cracklib-dicts  |
|  cracklib-python  |
|  crash  |
|  crash-devel  |
|  crash-extensions  |
|  createrepo  |
|  createrepo\_c  |
|  createrepo\_c-devel  |
|  createrepo\_c-libs  |
|  cronie  |
|  cronie-anacron  |
|  cronie-noanacron  |
|  crontabs  |
|  crypto-utils  |
|  cryptsetup  |
|  cryptsetup-devel  |
|  cryptsetup-libs  |
|  cryptsetup-python  |
|  cryptsetup-reencrypt  |
|  cscope  |
|  ctags  |
|  ctags-etags  |
|  ctdb  |
|  ctdb-devel  |
|  ctdb-tests  |
|  CUnit  |
|  CUnit-devel  |
|  cups  |
|  cups-devel  |
|  cups-libs  |
|  cups-lpd  |
|  cups-php  |
|  curl  |
|  cvs  |
|  cvs-inetd  |
|  cvs2commons  |
|  cvs2git  |
|  cvs2svn  |
|  cvsps  |
|  cyrus-imapd  |
|  cyrus-imapd-devel  |
|  cyrus-imapd-utils  |
|  cyrus-sasl  |
|  cyrus-sasl-devel  |
|  cyrus-sasl-gssapi  |
|  cyrus-sasl-ldap  |
|  cyrus-sasl-lib  |
|  cyrus-sasl-md5  |
|  cyrus-sasl-ntlm  |
|  cyrus-sasl-plain  |
|  cyrus-sasl-sql  |
|  dash  |
|  db4  |
|  db4-cxx  |
|  db4-devel  |
|  db4-devel-static  |
|  db4-java  |
|  db4-tcl  |
|  db4-utils  |
|  db43  |
|  db43-utils  |
|  dbus  |
|  dbus-devel  |
|  dbus-doc  |
|  dbus-glib  |
|  dbus-glib-devel  |
|  dbus-libs  |
|  dbus-python27  |
|  dbus-python27-devel  |
|  ddate  |
|  debugmode  |
|  dejagnu  |
|  dejavu-fonts-common  |
|  dejavu-lgc-sans-fonts  |
|  dejavu-lgc-sans-mono-fonts  |
|  dejavu-lgc-serif-fonts  |
|  dejavu-sans-fonts  |
|  dejavu-sans-mono-fonts  |
|  dejavu-serif-fonts  |
|  deltaiso  |
|  deltarpm  |
|  desktop-file-utils  |
|  dev86  |
|  device-mapper  |
|  device-mapper-devel  |
|  device-mapper-event  |
|  device-mapper-event-devel  |
|  device-mapper-event-libs  |
|  device-mapper-libs  |
|  device-mapper-multipath  |
|  device-mapper-multipath-libs  |
|  device-mapper-persistent-data  |
|  dhclient  |
|  dhcp  |
|  dhcp-common  |
|  dhcp-devel  |
|  dialog  |
|  dialog-devel  |
|  diffstat  |
|  diffutils  |
|  directory-naming  |
|  dirmngr  |
|  dirsplit  |
|  dkim-milter  |
|  dkms  |
|  dmidecode  |
|  dmraid  |
|  dmraid-devel  |
|  dmraid-events  |
|  dmraid-events-logwatch  |
|  dnsmasq  |
|  dnsmasq-utils  |
|  docbook-dtds  |
|  docbook-simple  |
|  docbook-slides  |
|  docbook-style-dsssl  |
|  docbook-style-xsl  |
|  docbook-utils  |
|  docbook-utils-pdf  |
|  docbook2X  |
|  docbook5-schemas  |
|  docbook5-style-xsl  |
|  docker  |
|  docker-storage-setup  |
|  dojo  |
|  dos2unix  |
|  dosfstools  |
|  dovecot  |
|  dovecot-devel  |
|  dovecot-mysql  |
|  dovecot-pgsql  |
|  dovecot-pigeonhole  |
|  doxygen  |
|  doxygen-latex  |
|  dracut  |
|  dracut-caps  |
|  dracut-fips  |
|  dracut-fips-aesni  |
|  dracut-generic  |
|  dracut-kernel  |
|  dracut-modules-growroot  |
|  dracut-network  |
|  dracut-tools  |
|  drm-utils  |
|  drpmsync  |
|  dstat  |
|  dump  |
|  dyninst  |
|  dyninst-devel  |
|  dyninst-doc  |
|  dyninst-static  |
|  dyninst-testsuite  |
|  e2fsprogs  |
|  e2fsprogs-devel  |
|  e2fsprogs-libs  |
|  e2fsprogs-static  |
|  ebtables  |
|  ec2-hibinit-agent  |
|  ec2-net-utils  |
|  ec2-utils  |
|  ecj  |
|  ecryptfs-utils  |
|  ecryptfs-utils-devel  |
|  ecryptfs-utils-python  |
|  ecs-init  |
|  ed  |
|  efax  |
|  egl-utils  |
|  elfutils  |
|  elfutils-devel  |
|  elfutils-devel-static  |
|  elfutils-libelf  |
|  elfutils-libelf-devel  |
|  elfutils-libelf-devel-static  |
|  elfutils-libs  |
|  elinks  |
|  emacs  |
|  emacs-a2ps  |
|  emacs-a2ps-el  |
|  emacs-auctex  |
|  emacs-auctex-doc  |
|  emacs-auctex-el  |
|  emacs-auto-complete  |
|  emacs-auto-complete-el  |
|  emacs-common  |
|  emacs-el  |
|  emacs-gettext  |
|  emacs-gettext-el  |
|  emacs-git  |
|  emacs-git-el  |
|  emacs-gnuplot  |
|  emacs-gnuplot-el  |
|  enchant  |
|  enchant-aspell  |
|  enchant-devel  |
|  enscript  |
|  environment-modules  |
|  epel-release  |
|  erlang  |
|  erlang-appmon  |
|  erlang-asn1  |
|  erlang-common\_test  |
|  erlang-compiler  |
|  erlang-cosEvent  |
|  erlang-cosEventDomain  |
|  erlang-cosFileTransfer  |
|  erlang-cosNotification  |
|  erlang-cosProperty  |
|  erlang-cosTime  |
|  erlang-cosTransactions  |
|  erlang-crypto  |
|  erlang-debugger  |
|  erlang-dialyzer  |
|  erlang-diameter  |
|  erlang-doc  |
|  erlang-docbuilder  |
|  erlang-edoc  |
|  erlang-erl\_docgen  |
|  erlang-erl\_interface  |
|  erlang-erts  |
|  erlang-et  |
|  erlang-eunit  |
|  erlang-examples  |
|  erlang-gs  |
|  erlang-hipe  |
|  erlang-ic  |
|  erlang-inets  |
|  erlang-inviso  |
|  erlang-jinterface  |
|  erlang-kernel  |
|  erlang-megaco  |
|  erlang-mnesia  |
|  erlang-observer  |
|  erlang-odbc  |
|  erlang-orber  |
|  erlang-os\_mon  |
|  erlang-otp\_mibs  |
|  erlang-parsetools  |
|  erlang-percept  |
|  erlang-pman  |
|  erlang-public\_key  |
|  erlang-reltool  |
|  erlang-runtime\_tools  |
|  erlang-sasl  |
|  erlang-snmp  |
|  erlang-ssh  |
|  erlang-ssl  |
|  erlang-stdlib  |
|  erlang-syntax\_tools  |
|  erlang-test\_server  |
|  erlang-toolbar  |
|  erlang-tools  |
|  erlang-tv  |
|  erlang-typer  |
|  erlang-webtool  |
|  erlang-xmerl  |
|  ethtool  |
|  exim  |
|  exim-greylist  |
|  exim-mon  |
|  exim-mysql  |
|  exim-pgsql  |
|  expat  |
|  expat-devel  |
|  expect  |
|  expect-devel  |
|  facter  |
|  facter2  |
|  fail2ban  |
|  fakechroot  |
|  fakechroot-libs  |
|  fakeroot  |
|  fakeroot-libs  |
|  fcgi  |
|  fcgi-devel  |
|  fcgi-libs  |
|  fcgi-perl  |
|  fetchmail  |
|  fftw  |
|  fftw-devel  |
|  fftw-static  |
|  figlet  |
|  file  |
|  file-devel  |
|  file-libs  |
|  file-static  |
|  filesystem  |
|  findutils  |
|  finger  |
|  finger-server  |
|  fio  |
|  fipscheck  |
|  fipscheck-devel  |
|  fipscheck-lib  |
|  flac  |
|  flac-devel  |
|  flex  |
|  flex-devel  |
|  flex-doc  |
|  fontconfig  |
|  fontconfig-devel  |
|  fontforge  |
|  fontforge-devel  |
|  fontpackages-devel  |
|  fontpackages-filesystem  |
|  fontpackages-tools  |
|  foomatic  |
|  foomatic-db  |
|  foomatic-db-filesystem  |
|  foomatic-db-ppds  |
|  fop-javadoc  |
|  fortune-mod  |
|  fpart  |
|  fping  |
|  freeglut  |
|  freeglut-devel  |
|  freeradius  |
|  freeradius-krb5  |
|  freeradius-ldap  |
|  freeradius-mysql  |
|  freeradius-perl  |
|  freeradius-postgresql  |
|  freeradius-python  |
|  freeradius-unixODBC  |
|  freeradius-utils  |
|  freetds  |
|  freetds-devel  |
|  freetds-doc  |
|  freetype  |
|  freetype-demos  |
|  freetype-devel  |
|  ftp  |
|  fuse  |
|  fuse-devel  |
|  fuse-libs  |
|  fwsnort  |
|  gamin  |
|  gamin-devel  |
|  gamin-python  |
|  gawk  |
|  gc  |
|  gc-devel  |
|  gcc  |
|  gcc-c\+\+  |
|  gcc-gfortran  |
|  gcc-gnat  |
|  gcc48  |
|  gcc48-c\+\+  |
|  gcc48-gfortran  |
|  gcc48-gnat  |
|  gcc48-plugin-devel  |
|  gcc64  |
|  gcc64-c\+\+  |
|  gcc64-gdb-plugin  |
|  gcc64-gfortran  |
|  gcc64-plugin-devel  |
|  gcc72  |
|  gcc72-c\+\+  |
|  gcc72-gdb-plugin  |
|  gcc72-plugin-devel  |
|  gd  |
|  gd-devel  |
|  gd-progs  |
|  gdb  |
|  gdb-doc  |
|  gdb-gdbserver  |
|  gdbm  |
|  gdbm-devel  |
|  gdisk  |
|  generic-logos  |
|  genisoimage  |
|  GeoIP  |
|  GeoIP-devel  |
|  geos  |
|  geos-devel  |
|  geos-python27  |
|  geronimo-specs  |
|  geronimo-specs-compat  |
|  get\_reference\_source  |
|  gettext  |
|  gettext-common-devel  |
|  gettext-devel  |
|  gettext-libs  |
|  ghostscript  |
|  ghostscript-devel  |
|  ghostscript-doc  |
|  ghostscript-fonts  |
|  giflib  |
|  giflib-devel  |
|  giflib-utils  |
|  git  |
|  git-all  |
|  git-bzr  |
|  git-clang-format  |
|  git-core  |
|  git-core-doc  |
|  git-cvs  |
|  git-daemon  |
|  git-email  |
|  git-hg  |
|  git-instaweb  |
|  git-p4  |
|  git-subtree  |
|  gitolite  |
|  gitolite3  |
|  gitweb  |
|  glew  |
|  glew-devel  |
|  glib2  |
|  glib2-devel  |
|  glib2-doc  |
|  glib2-fam  |
|  glibc  |
|  glibc-common  |
|  glibc-devel  |
|  glibc-headers  |
|  glibc-static  |
|  glibc-utils  |
|  glpk  |
|  glpk-devel  |
|  glpk-doc  |
|  glpk-static  |
|  glpk-utils  |
|  glx-utils  |
|  gmp  |
|  gmp-devel  |
|  gmp-static  |
|  gnome-doc-utils  |
|  gnome-doc-utils-stylesheets  |
|  gnu-efi  |
|  gnupg  |
|  gnupg2  |
|  gnupg2-smime  |
|  gnuplot  |
|  gnuplot-common  |
|  gnuplot-doc  |
|  gnuplot-latex  |
|  gnuplot-minimal  |
|  gnutls  |
|  gnutls-devel  |
|  gnutls-guile  |
|  gnutls-utils  |
|  go-filesystem  |
|  go-rpm-macros  |
|  go-rpm-templates  |
|  go-srpm-macros  |
|  gobject-introspection  |
|  gobject-introspection-devel  |
|  golang  |
|  golang-bin  |
|  golang-docs  |
|  golang-misc  |
|  golang-race  |
|  golang-shared  |
|  golang-src  |
|  golang-tests  |
|  golist  |
|  google-authenticator  |
|  gperf  |
|  gperftools  |
|  gperftools-devel  |
|  gperftools-libs  |
|  gpgme  |
|  gpgme-devel  |
|  gpm  |
|  gpm-devel  |
|  gpm-libs  |
|  gpm-static  |
|  gprolog  |
|  gprolog-docs  |
|  gprolog-examples  |
|  gpxe-bootimgs  |
|  gpxe-roms  |
|  gpxe-roms-qemu  |
|  GraphicsMagick  |
|  GraphicsMagick-c\+\+  |
|  GraphicsMagick-c\+\+-devel  |
|  GraphicsMagick-devel  |
|  GraphicsMagick-doc  |
|  GraphicsMagick-perl  |
|  graphite2  |
|  graphite2-devel  |
|  graphviz  |
|  graphviz-devel  |
|  graphviz-doc  |
|  graphviz-gd  |
|  graphviz-graphs  |
|  graphviz-guile  |
|  graphviz-java  |
|  graphviz-lua  |
|  graphviz-perl  |
|  graphviz-php  |
|  graphviz-python27  |
|  graphviz-R  |
|  graphviz-tcl  |
|  grep  |
|  groff  |
|  groff-base  |
|  groff-doc  |
|  groff-perl  |
|  grub  |
|  grubby  |
|  gsl  |
|  gsl-devel  |
|  gsl-static  |
|  gtest  |
|  gtest-devel  |
|  gtk-doc  |
|  guile  |
|  guile-devel  |
|  gyp  |
|  gzip  |
|  hamcrest  |
|  hamcrest-demo  |
|  hamcrest-javadoc  |
|  haproxy  |
|  hardlink  |
|  harfbuzz  |
|  harfbuzz-devel  |
|  harfbuzz-icu  |
|  hdparm  |
|  heartbeat  |
|  heartbeat-devel  |
|  heartbeat-libs  |
|  help2man  |
|  hesinfo  |
|  hesiod  |
|  hesiod-devel  |
|  hibagent  |
|  hiera1  |
|  hmaccalc  |
|  hsqldb  |
|  hsqldb-demo  |
|  hsqldb-javadoc  |
|  hsqldb-manual  |
|  ht2html  |
|  htdig  |
|  htdig-web  |
|  html2ps  |
|  htmlview  |
|  htop  |
|  http-parser  |
|  http-parser-devel  |
|  httpd  |
|  httpd-devel  |
|  httpd-manual  |
|  httpd-tools  |
|  httpd24  |
|  httpd24-devel  |
|  httpd24-manual  |
|  httpd24-tools  |
|  hunspell  |
|  hunspell-af  |
|  hunspell-ar  |
|  hunspell-as  |
|  hunspell-az  |
|  hunspell-be  |
|  hunspell-ber  |
|  hunspell-bg  |
|  hunspell-bn  |
|  hunspell-br  |
|  hunspell-ca  |
|  hunspell-cop  |
|  hunspell-csb  |
|  hunspell-cy  |
|  hunspell-da  |
|  hunspell-de  |
|  hunspell-devel  |
|  hunspell-el  |
|  hunspell-en  |
|  hunspell-eo  |
|  hunspell-es  |
|  hunspell-et  |
|  hunspell-eu  |
|  hunspell-fa  |
|  hunspell-fj  |
|  hunspell-fo  |
|  hunspell-fr  |
|  hunspell-fur  |
|  hunspell-fy  |
|  hunspell-ga  |
|  hunspell-gd  |
|  hunspell-gl  |
|  hunspell-gu  |
|  hunspell-gv  |
|  hunspell-hi  |
|  hunspell-hil  |
|  hunspell-hr  |
|  hunspell-hsb  |
|  hunspell-hu  |
|  hunspell-hy  |
|  hunspell-ia  |
|  hunspell-id  |
|  hunspell-is  |
|  hunspell-it  |
|  hunspell-kk  |
|  hunspell-km  |
|  hunspell-kn  |
|  hunspell-ku  |
|  hunspell-la  |
|  hunspell-lt  |
|  hunspell-mai  |
|  hunspell-mg  |
|  hunspell-mi  |
|  hunspell-mk  |
|  hunspell-ml  |
|  hunspell-mn  |
|  hunspell-mr  |
|  hunspell-ms  |
|  hunspell-mt  |
|  hunspell-nb  |
|  hunspell-nds  |
|  hunspell-ne  |
|  hunspell-nl  |
|  hunspell-nn  |
|  hunspell-nr  |
|  hunspell-nso  |
|  hunspell-ny  |
|  hunspell-or  |
|  hunspell-pa  |
|  hunspell-pl  |
|  hunspell-pt  |
|  hunspell-ro  |
|  hunspell-ru  |
|  hunspell-rw  |
|  hunspell-si  |
|  hunspell-sk  |
|  hunspell-sl  |
|  hunspell-so  |
|  hunspell-sq  |
|  hunspell-sr  |
|  hunspell-ss  |
|  hunspell-st  |
|  hunspell-sv  |
|  hunspell-sw  |
|  hunspell-ta  |
|  hunspell-te  |
|  hunspell-tet  |
|  hunspell-th  |
|  hunspell-tk  |
|  hunspell-tl  |
|  hunspell-tn  |
|  hunspell-ts  |
|  hunspell-uk  |
|  hunspell-uz  |
|  hunspell-ve  |
|  hunspell-vi  |
|  hunspell-wa  |
|  hunspell-xh  |
|  hunspell-zu  |
|  hwdata  |
|  hwloc  |
|  hwloc-devel  |
|  hwloc-gui  |
|  hwloc-libs  |
|  hyphen  |
|  hyphen-be  |
|  hyphen-devel  |
|  hyphen-en  |
|  hyphen-et  |
|  hyphen-hr  |
|  hyphen-nb  |
|  hyphen-nn  |
|  hyphen-sr  |
|  iasl  |
|  icedax  |
|  icu  |
|  idm-console-framework  |
|  idn2  |
|  ImageMagick  |
|  ImageMagick-c\+\+  |
|  ImageMagick-c\+\+-devel  |
|  ImageMagick-devel  |
|  ImageMagick-doc  |
|  ImageMagick-perl  |
|  imake  |
|  indent  |
|  info  |
|  iniparser  |
|  iniparser-devel  |
|  initscripts  |
|  innotop  |
|  intltool  |
|  iotop  |
|  ipa-gothic-fonts  |
|  ipa-mincho-fonts  |
|  iproute  |
|  iproute-devel  |
|  iproute-doc  |
|  ipsec-tools  |
|  ipset  |
|  ipset-devel  |
|  ipset-libs  |
|  iptables  |
|  iptables-devel  |
|  iptables-utils  |
|  iptraf  |
|  iptstate  |
|  iputils  |
|  iputils-ninfod  |
|  ipvsadm  |
|  ipxe-bootimgs  |
|  ipxe-roms  |
|  ipxe-roms-qemu  |
|  irqbalance  |
|  irssi  |
|  irssi-devel  |
|  iscsi-initiator-utils  |
|  iscsi-initiator-utils-devel  |
|  isl  |
|  isl-devel  |
|  iso-codes  |
|  iso-codes-devel  |
|  isomd5sum  |
|  isomd5sum-devel  |
|  itstool  |
|  jakarta-commons-httpclient  |
|  jakarta-commons-httpclient-demo  |
|  jakarta-commons-httpclient-javadoc  |
|  jakarta-commons-httpclient-manual  |
|  jakarta-oro  |
|  jakarta-oro-javadoc  |
|  jakarta-taglibs-standard  |
|  jakarta-taglibs-standard-javadoc  |
|  jansson  |
|  jansson-devel  |
|  jansson-devel-doc  |
|  jasper  |
|  jasper-devel  |
|  jasper-libs  |
|  jasper-utils  |
|  java\_cup  |
|  java\_cup-javadoc  |
|  java\_cup-manual  |
|  javacc  |
|  javacc-demo  |
|  javacc-manual  |
|  javapackages-tools  |
|  javassist  |
|  javassist-javadoc  |
|  jbigkit  |
|  jbigkit-devel  |
|  jbigkit-libs  |
|  jdepend  |
|  jdepend-demo  |
|  jdepend-javadoc  |
|  jdom  |
|  jdom-demo  |
|  jdom-javadoc  |
|  jemalloc  |
|  jemalloc-devel  |
|  jflex  |
|  jflex-javadoc  |
|  jlex  |
|  jlex-javadoc  |
|  jline  |
|  jna-contrib  |
|  jna-javadoc  |
|  jpackage-utils  |
|  jq  |
|  jq-devel  |
|  jq-libs  |
|  jrefactory  |
|  jsch  |
|  jsch-demo  |
|  jsch-javadoc  |
|  json-c  |
|  json-c-devel  |
|  json-c-doc  |
|  jsoncpp  |
|  jsoncpp-devel  |
|  jsoncpp-doc  |
|  jss-javadoc  |
|  jtidy  |
|  jtidy-javadoc  |
|  jtidy-scripts  |
|  junit  |
|  junit-demo  |
|  junit-javadoc  |
|  junit-manual  |
|  junit4  |
|  junit4-demo  |
|  junit4-javadoc  |
|  junit4-manual  |
|  jwhois  |
|  jython  |
|  jython-demo  |
|  jython-javadoc  |
|  jython-manual  |
|  jzlib  |
|  jzlib-demo  |
|  jzlib-javadoc  |
|  kbd  |
|  kbd-misc  |
|  keepalived  |
|  kernel  |
|  kernel-devel  |
|  kernel-headers  |
|  kernel-tools  |
|  kernel-tools-devel  |
|  kexec-tools  |
|  kexec-tools-eppic  |
|  keyutils  |
|  keyutils-libs  |
|  keyutils-libs-devel  |
|  kmod  |
|  kmod-devel  |
|  kmod-libs  |
|  kpartx  |
|  krb5-devel  |
|  krb5-libs  |
|  krb5-pkinit-openssl  |
|  krb5-server  |
|  krb5-server-ldap  |
|  krb5-workstation  |
|  ksh  |
|  ktune  |
|  lapack  |
|  lapack-devel  |
|  lapack-static  |
|  lapack64  |
|  lapack64-devel  |
|  lapack64-static  |
|  lasso  |
|  lasso-devel  |
|  lasso-python  |
|  latex2html  |
|  latrace  |
|  lcms  |
|  lcms-devel  |
|  lcms-libs  |
|  lcms2  |
|  lcms2-devel  |
|  lcms2-utils  |
|  ldapjdk  |
|  ldapjdk-javadoc  |
|  ldb-tools  |
|  ldirectord  |
|  ldns  |
|  ldns-devel  |
|  ldns-doc  |
|  ldns-python  |
|  lemon  |
|  less  |
|  lftp  |
|  lftp-scripts  |
|  libacl  |
|  libacl-devel  |
|  libaio  |
|  libaio-devel  |
|  libao  |
|  libao-devel  |
|  libapreq2  |
|  libapreq2-devel  |
|  libapreq2-libs  |
|  libarchive  |
|  libarchive-devel  |
|  libart\_lgpl  |
|  libart\_lgpl-devel  |
|  libasan  |
|  libassuan  |
|  libassuan-devel  |
|  libatomic  |
|  libatomic\_ops-devel  |
|  libattr  |
|  libattr-devel  |
|  libbasicobjects  |
|  libbasicobjects-devel  |
|  libblkid  |
|  libblkid-devel  |
|  libbsd  |
|  libbsd-ctor-static  |
|  libbsd-devel  |
|  libc-client  |
|  libc-client-devel  |
|  libcap  |
|  libcap-devel  |
|  libcap-ng  |
|  libcap-ng-devel  |
|  libcap-ng-python  |
|  libcap-ng-utils  |
|  libcap54  |
|  libcap54-devel  |
|  libcap54-static  |
|  libcgroup  |
|  libcgroup-devel  |
|  libcgroup-pam  |
|  libcilkrts  |
|  libcollectdclient  |
|  libcollectdclient-devel  |
|  libcollection  |
|  libcollection-devel  |
|  libcom\_err  |
|  libcom\_err-devel  |
|  libconfig  |
|  libconfig-devel  |
|  libconfuse  |
|  libconfuse-devel  |
|  libcurl  |
|  libcurl-devel  |
|  libdaemon  |
|  libdaemon-devel  |
|  libdbi  |
|  libdbi-dbd-pgsql  |
|  libdbi-dbd-sqlite  |
|  libdbi-devel  |
|  libdbi-drivers  |
|  libdhash  |
|  libdhash-devel  |
|  libdmx  |
|  libdmx-devel  |
|  libdrm  |
|  libdrm-devel  |
|  libdv  |
|  libdv-devel  |
|  libdv-tools  |
|  libdwarf  |
|  libdwarf-devel  |
|  libdwarf-static  |
|  libdwarf-tools  |
|  libecap  |
|  libecap-devel  |
|  libedit  |
|  libedit-devel  |
|  libEMF  |
|  libEMF-devel  |
|  libepoxy  |
|  libepoxy-devel  |
|  liberation-fonts-common  |
|  liberation-mono-fonts  |
|  liberation-sans-fonts  |
|  liberation-serif-fonts  |
|  libesmtp  |
|  libesmtp-devel  |
|  libev  |
|  libev-devel  |
|  libev-libevent-devel  |
|  libev-source  |
|  libevdev  |
|  libevdev-devel  |
|  libevdev-utils  |
|  libevent  |
|  libevent-devel  |
|  libevent-doc  |
|  libexif  |
|  libexif-devel  |
|  libffi  |
|  libffi-devel  |
|  libfontenc  |
|  libfontenc-devel  |
|  libFS  |
|  libFS-devel  |
|  libgcc44  |
|  libgcc48  |
|  libgcc64  |
|  libgcc72  |
|  libgccjit  |
|  libgccjit-devel  |
|  libgcrypt  |
|  libgcrypt-devel  |
|  libgfortran  |
|  libGLEW  |
|  libglvnd  |
|  libglvnd-core-devel  |
|  libglvnd-devel  |
|  libglvnd-egl  |
|  libglvnd-gles  |
|  libglvnd-glx  |
|  libglvnd-opengl  |
|  libgnat  |
|  libgnat44  |
|  libgnat44-devel  |
|  libgnat44-static  |
|  libgnat48  |
|  libgomp  |
|  libgpg-error  |
|  libgpg-error-devel  |
|  libgssglue  |
|  libgssglue-devel  |
|  libgtop2  |
|  libgtop2-devel  |
|  libgudev1  |
|  libgudev1-devel  |
|  libibcommon  |
|  libibcommon-devel  |
|  libibcommon-static  |
|  libibmad  |
|  libibmad-devel  |
|  libibmad-static  |
|  libibumad  |
|  libibumad-devel  |
|  libibumad-static  |
|  libICE  |
|  libICE-devel  |
|  libicu  |
|  libicu-devel  |
|  libicu-doc  |
|  libIDL  |
|  libIDL-devel  |
|  libidn  |
|  libidn-devel  |
|  libidn2  |
|  libidn2-devel  |
|  libini\_config  |
|  libini\_config-devel  |
|  libipa\_hbac  |
|  libipa\_hbac-devel  |
|  libitm  |
|  libjpeg-turbo  |
|  libjpeg-turbo-devel  |
|  libjpeg-turbo-static  |
|  libjpeg-turbo-utils  |
|  libkadm5  |
|  libksba  |
|  libksba-devel  |
|  libldb  |
|  libldb-devel  |
|  libmcpp  |
|  libmcpp-devel  |
|  libmcrypt  |
|  libmcrypt-devel  |
|  libmemcached  |
|  libmemcached-devel  |
|  libmetalink  |
|  libmetalink-devel  |
|  libmicrohttpd  |
|  libmicrohttpd-devel  |
|  libmicrohttpd-doc  |
|  libmnl  |
|  libmnl-devel  |
|  libmnl-static  |
|  libmount  |
|  libmount-devel  |
|  libmpc  |
|  libmpc-devel  |
|  libmpx  |
|  libmudflap  |
|  libmudflap44-static  |
|  libnet  |
|  libnet-devel  |
|  libnetfilter\_conntrack  |
|  libnetfilter\_conntrack-devel  |
|  libnetfilter\_cthelper  |
|  libnetfilter\_cthelper-devel  |
|  libnetfilter\_cttimeout  |
|  libnetfilter\_cttimeout-devel  |
|  libnetfilter\_queue  |
|  libnetfilter\_queue-devel  |
|  libnfnetlink  |
|  libnfnetlink-devel  |
|  libnfsidmap  |
|  libnfsidmap-devel  |
|  libnghttp2  |
|  libnghttp2-devel  |
|  libnih  |
|  libnih-devel  |
|  libnl  |
|  libnl-devel  |
|  libnl3  |
|  libnl3-cli  |
|  libnl3-devel  |
|  libnl3-doc  |
|  libntlm  |
|  libntlm-devel  |
|  libobjc44  |
|  libogg  |
|  libogg-devel  |
|  libogg-devel-docs  |
|  libpagemap  |
|  libpagemap-devel  |
|  libpath\_utils  |
|  libpath\_utils-devel  |
|  libpcap  |
|  libpcap-devel  |
|  libpciaccess  |
|  libpciaccess-devel  |
|  libpipeline  |
|  libpipeline-devel  |
|  libpng  |
|  libpng-devel  |
|  libpng-static  |
|  libproxy  |
|  libproxy-bin  |
|  libproxy-devel  |
|  libproxy-python  |
|  libpsl  |
|  libpsl-devel  |
|  libpuzzle  |
|  libpuzzle-devel  |
|  libpuzzle-utils  |
|  libpwquality  |
|  libpwquality-devel  |
|  libquadmath  |
|  librabbitmq  |
|  librabbitmq-devel  |
|  libreadline-java-javadoc  |
|  libref\_array  |
|  libref\_array-devel  |
|  libreswan  |
|  libRmath  |
|  libRmath-devel  |
|  libRmath-static  |
|  libsanitizer  |
|  libseccomp  |
|  libseccomp-devel  |
|  libseccomp-static  |
|  libselinux  |
|  libselinux-devel  |
|  libselinux-python  |
|  libselinux-ruby  |
|  libselinux-static  |
|  libselinux-utils  |
|  libsemanage  |
|  libsemanage-devel  |
|  libsemanage-python  |
|  libsemanage-static  |
|  libsepol  |
|  libsepol-devel  |
|  libsepol-static  |
|  libserf  |
|  libserf-devel  |
|  libSM  |
|  libSM-devel  |
|  libsmartcols  |
|  libsmartcols-devel  |
|  libsmbclient  |
|  libsmbclient-devel  |
|  libsmi  |
|  libsmi-devel  |
|  libsoup  |
|  libsoup-devel  |
|  libspiro  |
|  libspiro-devel  |
|  libss  |
|  libss-devel  |
|  libssh2  |
|  libssh2-devel  |
|  libssh2-docs  |
|  libsss\_autofs  |
|  libsss\_certmap  |
|  libsss\_certmap-devel  |
|  libsss\_idmap  |
|  libsss\_idmap-devel  |
|  libsss\_nss\_idmap  |
|  libsss\_nss\_idmap-devel  |
|  libsss\_simpleifp  |
|  libsss\_simpleifp-devel  |
|  libsss\_sudo  |
|  libstdc\+\+-docs  |
|  libstdc\+\+44  |
|  libstdc\+\+48  |
|  libstdc\+\+64  |
|  libstdc\+\+72  |
|  libsysfs  |
|  libsysfs-devel  |
|  libtalloc  |
|  libtalloc-devel  |
|  libtasn1  |
|  libtasn1-devel  |
|  libtasn1-tools  |
|  libtdb  |
|  libtdb-devel  |
|  libtevent  |
|  libtevent-devel  |
|  libthai  |
|  libthai-devel  |
|  libtidy  |
|  libtidy-devel  |
|  libtidyp  |
|  libtidyp-devel  |
|  libtiff  |
|  libtiff-devel  |
|  libtiff-static  |
|  libtirpc  |
|  libtirpc-devel  |
|  libtomcrypt  |
|  libtomcrypt-devel  |
|  libtommath  |
|  libtommath-devel  |
|  libtool  |
|  libtool-ltdl  |
|  libtool-ltdl-devel  |
|  libtsan  |
|  libudev  |
|  libudev-devel  |
|  libuninameslist  |
|  libuninameslist-devel  |
|  libunistring  |
|  libunistring-devel  |
|  libunwind  |
|  libunwind-devel  |
|  libusb  |
|  libusb-devel  |
|  libusb-static  |
|  libusb1  |
|  libusb1-devel  |
|  libusb1-static  |
|  libuser  |
|  libuser-devel  |
|  libuser-python  |
|  libutempter  |
|  libutempter-devel  |
|  libuuid  |
|  libuuid-devel  |
|  libverto  |
|  libverto-devel  |
|  libverto-glib  |
|  libverto-glib-devel  |
|  libverto-libevent  |
|  libverto-libevent-devel  |
|  libverto-tevent  |
|  libverto-tevent-devel  |
|  libvorbis  |
|  libvorbis-devel  |
|  libvorbis-devel-docs  |
|  libvpx  |
|  libvpx-devel  |
|  libvpx-utils  |
|  libwbclient  |
|  libwbclient-devel  |
|  libwebp  |
|  libwebp-devel  |
|  libwebp-tools  |
|  libwmf  |
|  libwmf-devel  |
|  libwmf-lite  |
|  libwvstreams  |
|  libwvstreams-devel  |
|  libX11  |
|  libX11-common  |
|  libX11-devel  |
|  libXau  |
|  libXau-devel  |
|  libXaw  |
|  libXaw-devel  |
|  libxcb  |
|  libxcb-devel  |
|  libxcb-doc  |
|  libxcb-python  |
|  libXcomposite  |
|  libXcomposite-devel  |
|  libXcursor  |
|  libXcursor-devel  |
|  libXdamage  |
|  libXdamage-devel  |
|  libXdmcp  |
|  libXdmcp-devel  |
|  libXevie  |
|  libXevie-devel  |
|  libXext  |
|  libXext-devel  |
|  libXfixes  |
|  libXfixes-devel  |
|  libXfont  |
|  libXfont-devel  |
|  libXft  |
|  libXft-devel  |
|  libXi  |
|  libXi-devel  |
|  libXinerama  |
|  libXinerama-devel  |
|  libxkbfile  |
|  libxkbfile-devel  |
|  libxklavier  |
|  libxklavier-devel  |
|  libxml2  |
|  libxml2-devel  |
|  libxml2-python27  |
|  libxml2-static  |
|  libXmu  |
|  libXmu-devel  |
|  libXp  |
|  libXp-devel  |
|  libXpm  |
|  libXpm-devel  |
|  libXrandr  |
|  libXrandr-devel  |
|  libXrender  |
|  libXrender-devel  |
|  libXres  |
|  libXres-devel  |
|  libxshmfence  |
|  libxshmfence-devel  |
|  libxslt  |
|  libxslt-devel  |
|  libxslt-python27  |
|  libXt  |
|  libXt-devel  |
|  libXtst  |
|  libXtst-devel  |
|  libXv  |
|  libXv-devel  |
|  libXvMC  |
|  libXvMC-devel  |
|  libXxf86dga  |
|  libXxf86dga-devel  |
|  libXxf86misc  |
|  libXxf86misc-devel  |
|  libXxf86vm  |
|  libXxf86vm-devel  |
|  libyaml  |
|  libyaml-devel  |
|  libzip  |
|  libzip-devel  |
|  lighttpd  |
|  lighttpd-fastcgi  |
|  lighttpd-mod\_authn\_gssapi  |
|  lighttpd-mod\_authn\_mysql  |
|  lighttpd-mod\_authn\_pam  |
|  lighttpd-mod\_geoip  |
|  lighttpd-mod\_mysql\_vhost  |
|  linuxdoc-tools  |
|  lksctp-tools  |
|  lksctp-tools-devel  |
|  lksctp-tools-doc  |
|  lldb  |
|  lldb-devel  |
|  llvm  |
|  llvm-devel  |
|  llvm-doc  |
|  llvm-libs  |
|  llvm-static  |
|  llvm6.0  |
|  llvm6.0-devel  |
|  llvm6.0-libs  |
|  llvm6.0-static  |
|  lockdev  |
|  lockdev-devel  |
|  log4cplus  |
|  log4cplus-devel  |
|  log4cpp  |
|  log4cpp-devel  |
|  log4j  |
|  log4j-cve-2021-44228-hotpatch  |
|  log4j-javadoc  |
|  log4j-manual  |
|  logrotate  |
|  logwatch  |
|  lolcat  |
|  lslk  |
|  lsof  |
|  lsscsi  |
|  ltrace  |
|  lua  |
|  lua-devel  |
|  lua-filesystem  |
|  lua-static  |
|  luajit  |
|  luajit-devel  |
|  lucene  |
|  lucene-contrib  |
|  lucene-demo  |
|  lucene-javadoc  |
|  lustre-client  |
|  lvm2  |
|  lvm2-devel  |
|  lvm2-libs  |
|  lynis  |
|  lynx  |
|  lz4  |
|  lz4-devel  |
|  lz4-static  |
|  lzo  |
|  lzo-devel  |
|  lzo-minilzo  |
|  lzop  |
|  m17n-contrib  |
|  m17n-contrib-assamese  |
|  m17n-contrib-bengali  |
|  m17n-contrib-chinese  |
|  m17n-contrib-czech  |
|  m17n-contrib-esperanto  |
|  m17n-contrib-gujarati  |
|  m17n-contrib-hindi  |
|  m17n-contrib-kannada  |
|  m17n-contrib-kashmiri  |
|  m17n-contrib-maithili  |
|  m17n-contrib-malayalam  |
|  m17n-contrib-marathi  |
|  m17n-contrib-nepali  |
|  m17n-contrib-oriya  |
|  m17n-contrib-pashto  |
|  m17n-contrib-punjabi  |
|  m17n-contrib-russian  |
|  m17n-contrib-sindhi  |
|  m17n-contrib-sinhala  |
|  m17n-contrib-tai  |
|  m17n-contrib-tamil  |
|  m17n-contrib-telugu  |
|  m17n-contrib-urdu  |
|  m17n-contrib-vietnamese  |
|  m17n-db  |
|  m17n-db-amharic  |
|  m17n-db-arabic  |
|  m17n-db-armenian  |
|  m17n-db-assamese  |
|  m17n-db-bengali  |
|  m17n-db-cham  |
|  m17n-db-chinese  |
|  m17n-db-common-cjk  |
|  m17n-db-croatian  |
|  m17n-db-danish  |
|  m17n-db-datafiles  |
|  m17n-db-devel  |
|  m17n-db-dhivehi  |
|  m17n-db-farsi  |
|  m17n-db-french  |
|  m17n-db-generic  |
|  m17n-db-greek  |
|  m17n-db-gregorian  |
|  m17n-db-gujarati  |
|  m17n-db-hebrew  |
|  m17n-db-hindi  |
|  m17n-db-japanese  |
|  m17n-db-kannada  |
|  m17n-db-kazakh  |
|  m17n-db-khmer  |
|  m17n-db-korean  |
|  m17n-db-lao  |
|  m17n-db-latin  |
|  m17n-db-malayalam  |
|  m17n-db-myanmar  |
|  m17n-db-oriya  |
|  m17n-db-punjabi  |
|  m17n-db-russian  |
|  m17n-db-sanskrit  |
|  m17n-db-serbian  |
|  m17n-db-sinhala  |
|  m17n-db-slovak  |
|  m17n-db-swedish  |
|  m17n-db-syriac  |
|  m17n-db-tamil  |
|  m17n-db-telugu  |
|  m17n-db-thai  |
|  m17n-db-tibetan  |
|  m17n-db-uyghur  |
|  m17n-db-vietnamese  |
|  m17n-lib  |
|  m17n-lib-devel  |
|  m4  |
|  mailcap  |
|  mailman  |
|  mailx  |
|  make  |
|  MAKEDEV  |
|  man-db  |
|  man-pages  |
|  man-pages-fr  |
|  man-pages-ja  |
|  mariadb-connector-java  |
|  mc  |
|  mcpp  |
|  mcpp-doc  |
|  mcstrans  |
|  mdadm  |
|  meanwhile  |
|  meanwhile-devel  |
|  meanwhile-doc  |
|  memcached  |
|  memcached-devel  |
|  mesa-demos  |
|  mesa-dri-drivers  |
|  mesa-filesystem  |
|  mesa-libd3d  |
|  mesa-libd3d-devel  |
|  mesa-libEGL  |
|  mesa-libEGL-devel  |
|  mesa-libgbm  |
|  mesa-libgbm-devel  |
|  mesa-libGL  |
|  mesa-libGL-devel  |
|  mesa-libglapi  |
|  mesa-libGLES  |
|  mesa-libGLES-devel  |
|  mesa-libGLU  |
|  mesa-libGLU-devel  |
|  mesa-libOSMesa  |
|  mesa-libOSMesa-devel  |
|  mesa-libxatracker  |
|  mesa-libxatracker-devel  |
|  meson  |
|  mgetty  |
|  mgetty-sendfax  |
|  mgetty-viewfax  |
|  mgetty-voice  |
|  microcode\_ctl  |
|  mingetty  |
|  minizip  |
|  minizip-devel  |
|  mkbootdisk  |
|  mlocate  |
|  mlogc  |
|  mlogc24  |
|  mod24\_auth\_kerb  |
|  mod24\_auth\_mellon  |
|  mod24\_auth\_mellon-diagnostics  |
|  mod24\_auth\_openidc  |
|  mod24\_dav\_svn  |
|  mod24\_fcgid  |
|  mod24\_geoip  |
|  mod24\_ldap  |
|  mod24\_md  |
|  mod24\_nss  |
|  mod24\_perl  |
|  mod24\_perl-devel  |
|  mod24\_proxy\_html  |
|  mod24\_security  |
|  mod24\_session  |
|  mod24\_ssl  |
|  mod24\_wsgi-python27  |
|  mod\_auth\_kerb  |
|  mod\_auth\_mellon  |
|  mod\_auth\_mysql  |
|  mod\_auth\_pgsql  |
|  mod\_authz\_ldap  |
|  mod\_dav\_svn  |
|  mod\_fcgid  |
|  mod\_geoip  |
|  mod\_nss  |
|  mod\_perl  |
|  mod\_perl-devel  |
|  mod\_proxy\_html  |
|  mod\_python27  |
|  mod\_security  |
|  mod\_security\_crs  |
|  mod\_security\_crs-extras  |
|  mod\_ssl  |
|  mod\_wsgi-python27  |
|  mon  |
|  monit  |
|  mosh  |
|  most  |
|  mozldap  |
|  mozldap-devel  |
|  mozldap-tools  |
|  mpage  |
|  mpfr  |
|  mpfr-devel  |
|  mpich  |
|  mpich-autoload  |
|  mpich-devel  |
|  mpich-doc  |
|  mrtg  |
|  mrtg-libs  |
|  mtdev  |
|  mtdev-devel  |
|  mtools  |
|  mtr  |
|  multilib-rpm-config  |
|  multitail  |
|  munin  |
|  munin-async  |
|  munin-cgi  |
|  munin-common  |
|  munin-java-plugins  |
|  munin-netip-plugins  |
|  munin-nginx  |
|  munin-node  |
|  munin-ruby-plugins  |
|  mutt  |
|  mx4j  |
|  mx4j-javadoc  |
|  mx4j-manual  |
|  mysql  |
|  mysql-bench  |
|  mysql-common  |
|  mysql-config  |
|  mysql-connector-java  |
|  mysql-connector-odbc  |
|  mysql-devel  |
|  mysql-embedded  |
|  mysql-embedded-devel  |
|  mysql-libs  |
|  mysql-server  |
|  mysql-test  |
|  mythes-nb  |
|  mythes-nn  |
|  nagios-common  |
|  nagios-devel  |
|  nagios-plugins  |
|  nagios-plugins-all  |
|  nagios-plugins-apt  |
|  nagios-plugins-breeze  |
|  nagios-plugins-by\_ssh  |
|  nagios-plugins-check-updates  |
|  nagios-plugins-cluster  |
|  nagios-plugins-dhcp  |
|  nagios-plugins-dig  |
|  nagios-plugins-disk  |
|  nagios-plugins-dns  |
|  nagios-plugins-dummy  |
|  nagios-plugins-file\_age  |
|  nagios-plugins-flexlm  |
|  nagios-plugins-fping  |
|  nagios-plugins-hpjd  |
|  nagios-plugins-http  |
|  nagios-plugins-icmp  |
|  nagios-plugins-ide\_smart  |
|  nagios-plugins-ifoperstatus  |
|  nagios-plugins-ifstatus  |
|  nagios-plugins-ircd  |
|  nagios-plugins-ldap  |
|  nagios-plugins-linux\_raid  |
|  nagios-plugins-load  |
|  nagios-plugins-log  |
|  nagios-plugins-mailq  |
|  nagios-plugins-mrtg  |
|  nagios-plugins-mrtgtraf  |
|  nagios-plugins-mysql  |
|  nagios-plugins-nagios  |
|  nagios-plugins-nrpe  |
|  nagios-plugins-nt  |
|  nagios-plugins-ntp  |
|  nagios-plugins-ntp-perl  |
|  nagios-plugins-nwstat  |
|  nagios-plugins-oracle  |
|  nagios-plugins-overcr  |
|  nagios-plugins-perl  |
|  nagios-plugins-pgsql  |
|  nagios-plugins-ping  |
|  nagios-plugins-procs  |
|  nagios-plugins-radius  |
|  nagios-plugins-real  |
|  nagios-plugins-rpc  |
|  nagios-plugins-smtp  |
|  nagios-plugins-snmp  |
|  nagios-plugins-ssh  |
|  nagios-plugins-swap  |
|  nagios-plugins-tcp  |
|  nagios-plugins-time  |
|  nagios-plugins-ups  |
|  nagios-plugins-users  |
|  nagios-plugins-wave  |
|  nano  |
|  nasm  |
|  nasm-doc  |
|  nasm-rdoff  |
|  nc  |
|  ncdu  |
|  ncompress  |
|  ncurses  |
|  ncurses-base  |
|  ncurses-devel  |
|  ncurses-libs  |
|  ncurses-static  |
|  ncurses-term  |
|  neon  |
|  neon-devel  |
|  neon0.25  |
|  net-snmp  |
|  net-snmp-devel  |
|  net-snmp-libs  |
|  net-snmp-perl  |
|  net-snmp-python  |
|  net-snmp-utils  |
|  net-tools  |
|  nethack  |
|  netlabel\_tools  |
|  netpbm  |
|  netpbm-devel  |
|  netperf  |
|  newt  |
|  newt-devel  |
|  newt-python27  |
|  newt-static  |
|  nfs-utils  |
|  nfs4-acl-tools  |
|  nghttp2  |
|  nginx  |
|  nginx-all-modules  |
|  nginx-mod-http-geoip  |
|  nginx-mod-http-image-filter  |
|  nginx-mod-http-perl  |
|  nginx-mod-http-xslt-filter  |
|  nginx-mod-mail  |
|  nginx-mod-stream  |
|  nilfs-utils  |
|  nilfs-utils-devel  |
|  ninja-build  |
|  nmap  |
|  nmap-ncat  |
|  nrpe  |
|  nsca  |
|  nsca-client  |
|  nscd  |
|  nspr  |
|  nspr-devel  |
|  nss  |
|  nss-devel  |
|  nss-pam-ldapd  |
|  nss-pem  |
|  nss-pkcs11-devel  |
|  nss-softokn  |
|  nss-softokn-devel  |
|  nss-softokn-freebl  |
|  nss-softokn-freebl-devel  |
|  nss-sysinit  |
|  nss-tools  |
|  nss-util  |
|  nss-util-devel  |
|  nss\_compat\_ossl  |
|  nss\_compat\_ossl-devel  |
|  nss\_lwres  |
|  ntp  |
|  ntp-doc  |
|  ntp-perl  |
|  ntpdate  |
|  ntsysv  |
|  numactl  |
|  numactl-devel  |
|  nuttcp  |
|  nvme-cli  |
|  oddjob  |
|  oddjob-mkhomedir  |
|  oniguruma  |
|  oniguruma-devel  |
|  openais  |
|  openaislib  |
|  openaislib-devel  |
|  openblas  |
|  openblas-devel  |
|  openblas-openmp  |
|  openblas-openmp64  |
|  openblas-openmp64\_  |
|  openblas-Rblas  |
|  openblas-serial64  |
|  openblas-serial64\_  |
|  openblas-static  |
|  openblas-threads  |
|  openblas-threads64  |
|  openblas-threads64\_  |
|  OpenIPMI  |
|  OpenIPMI-devel  |
|  OpenIPMI-libs  |
|  OpenIPMI-perl  |
|  OpenIPMI-python27  |
|  openjade  |
|  openjpeg  |
|  openjpeg-devel  |
|  openjpeg-libs  |
|  openldap  |
|  openldap-clients  |
|  openldap-devel  |
|  openldap-servers  |
|  openldap-servers-sql  |
|  openmotif  |
|  openmotif-devel  |
|  openmpi  |
|  openmpi-devel  |
|  openscap  |
|  openscap-containers  |
|  openscap-devel  |
|  openscap-engine-sce  |
|  openscap-engine-sce-devel  |
|  openscap-python  |
|  openscap-scanner  |
|  opensp  |
|  opensp-devel  |
|  openssh  |
|  openssh-cavs  |
|  openssh-clients  |
|  openssh-keycat  |
|  openssh-ldap  |
|  openssh-server  |
|  openssl  |
|  openssl-devel  |
|  openssl-perl  |
|  openssl-static  |
|  openswan-doc  |
|  openvpn  |
|  openvpn-auth-ldap  |
|  openvpn-devel  |
|  oprofile  |
|  oprofile-devel  |
|  oprofile-jit  |
|  overpass-fonts  |
|  p11-kit  |
|  p11-kit-devel  |
|  p11-kit-trust  |
|  pam  |
|  pam-devel  |
|  pam\_ccreds  |
|  pam\_krb5  |
|  pam\_ldap  |
|  pam\_passwdqc  |
|  pam\_ssh\_agent\_auth  |
|  pango  |
|  pango-devel  |
|  paps  |
|  paps-devel  |
|  paps-libs  |
|  parallel  |
|  parted  |
|  parted-devel  |
|  passivetex  |
|  passwd  |
|  patch  |
|  patchutils  |
|  pax  |
|  pciutils  |
|  pciutils-devel  |
|  pciutils-devel-static  |
|  pciutils-libs  |
|  pcre  |
|  pcre-devel  |
|  pcre-static  |
|  pcre-tools  |
|  pdf-tools  |
|  perf  |
|  perl  |
|  perl-Algorithm-C3  |
|  perl-Algorithm-Dependency  |
|  perl-Algorithm-Diff  |
|  perl-aliased  |
|  perl-Amazon-SQS-Simple  |
|  perl-Apache2-SOAP  |
|  perl-App-cpanminus  |
|  perl-App-SVN-Bisect  |
|  perl-AppConfig  |
|  perl-Archive-Any  |
|  perl-Archive-Extract  |
|  perl-Archive-Tar  |
|  perl-Archive-Zip  |
|  perl-Array-Diff  |
|  perl-Array-Utils  |
|  perl-Authen-PAM  |
|  perl-Authen-SASL  |
|  perl-autodie  |
|  perl-AutoXS-Header  |
|  perl-B-Compiling  |
|  perl-B-Hooks-EndOfScope  |
|  perl-B-Hooks-OP-Check  |
|  perl-B-Keywords  |
|  perl-B-Lint  |
|  perl-bareword-filehandles  |
|  perl-BerkeleyDB  |
|  perl-Bit-Vector  |
|  perl-boolean  |
|  perl-Browser-Open  |
|  perl-BSD-Resource  |
|  perl-Bundle-LWP  |
|  perl-Business-ISBN  |
|  perl-Business-ISBN-Data  |
|  perl-Cache-Cache  |
|  perl-Cache-Memcached  |
|  perl-Capture-Tiny  |
|  perl-Carp  |
|  perl-Carp-Always  |
|  perl-Carp-Clan  |
|  perl-CGI  |
|  perl-CGI-Session  |
|  perl-Class-Accessor  |
|  perl-Class-Accessor-Chained  |
|  perl-Class-Accessor-Grouped  |
|  perl-Class-Autouse  |
|  perl-Class-C3  |
|  perl-Class-C3-Componentised  |
|  perl-Class-C3-tests  |
|  perl-Class-C3-XS  |
|  perl-Class-Data-Inheritable  |
|  perl-Class-DBI  |
|  perl-Class-DBI-Plugin  |
|  perl-Class-DBI-Plugin-DeepAbstractSearch  |
|  perl-Class-ErrorHandler  |
|  perl-Class-Factory-Util  |
|  perl-Class-Inspector  |
|  perl-Class-ISA  |
|  perl-Class-Load  |
|  perl-Class-Load-XS  |
|  perl-Class-MakeMethods  |
|  perl-Class-Method-Modifiers  |
|  perl-Class-MethodMaker  |
|  perl-Class-Singleton  |
|  perl-Class-Std  |
|  perl-Class-Std-Fast  |
|  perl-Class-Std-Storable  |
|  perl-Class-Trigger  |
|  perl-Class-XSAccessor  |
|  perl-Clone  |
|  perl-Collectd  |
|  perl-common-sense  |
|  perl-Compress-Raw-Bzip2  |
|  perl-Compress-Raw-Lzma  |
|  perl-Compress-Raw-Zlib  |
|  perl-Config-Any  |
|  perl-Config-Any-tests  |
|  perl-Config-Augeas  |
|  perl-Config-General  |
|  perl-Config-Simple  |
|  perl-Config-Tiny  |
|  perl-constant  |
|  perl-Context-Preserve  |
|  perl-Context-Preserve-tests  |
|  perl-Convert-ASCII-Armour  |
|  perl-Convert-ASN1  |
|  perl-Convert-BER  |
|  perl-Convert-BinHex  |
|  perl-Convert-PEM  |
|  perl-Convert-TNEF  |
|  perl-Convert-Units  |
|  perl-Convert-UUlib  |
|  perl-core  |
|  perl-CPAN  |
|  perl-CPAN-Changes  |
|  perl-CPAN-DistnameInfo  |
|  perl-CPAN-Meta  |
|  perl-CPAN-Meta-Check  |
|  perl-CPAN-Meta-Requirements  |
|  perl-CPAN-Meta-YAML  |
|  perl-CPAN-Perl-Releases  |
|  perl-CPANPLUS  |
|  perl-CPANPLUS-Dist-Build  |
|  perl-Crypt-CBC  |
|  perl-Crypt-DES  |
|  perl-Crypt-DES\_EDE3  |
|  perl-Crypt-OpenSSL-Bignum  |
|  perl-Crypt-OpenSSL-Random  |
|  perl-Crypt-OpenSSL-RSA  |
|  perl-Crypt-PasswdMD5  |
|  perl-Crypt-RC4  |
|  perl-Crypt-SmbHash  |
|  perl-Crypt-SSLeay  |
|  perl-CSS-Tiny  |
|  perl-Data-Alias  |
|  perl-Data-Compare  |
|  perl-Data-Dump  |
|  perl-Data-Dumper  |
|  perl-Data-Dumper-Concise  |
|  perl-Data-Dumper-Names  |
|  perl-Data-Flow  |
|  perl-Data-HexDump-XXD  |
|  perl-Data-OptList  |
|  perl-Data-Page  |
|  perl-Data-Peek  |
|  perl-Data-Section  |
|  perl-Data-Section-Simple  |
|  perl-Data-Stream-Bulk  |
|  perl-Data-UUID  |
|  perl-Data-Visitor  |
|  perl-Date-Calc  |
|  perl-Date-Manip  |
|  perl-Date-Simple  |
|  perl-DateTime  |
|  perl-DateTime-Calendar-Mayan  |
|  perl-DateTime-Event-Cron  |
|  perl-DateTime-Event-ICal  |
|  perl-DateTime-Event-Recurrence  |
|  perl-DateTime-Format-Builder  |
|  perl-DateTime-Format-DateParse  |
|  perl-DateTime-Format-Flexible  |
|  perl-DateTime-Format-HTTP  |
|  perl-DateTime-Format-IBeat  |
|  perl-DateTime-Format-ICal  |
|  perl-DateTime-Format-ISO8601  |
|  perl-DateTime-Format-Mail  |
|  perl-DateTime-Format-MySQL  |
|  perl-DateTime-Format-Natural  |
|  perl-DateTime-Format-Natural-Test  |
|  perl-DateTime-Format-Pg  |
|  perl-DateTime-Format-SQLite  |
|  perl-DateTime-Format-SQLite-tests  |
|  perl-DateTime-Format-Strptime  |
|  perl-DateTime-Format-W3CDTF  |
|  perl-DateTime-Locale  |
|  perl-DateTime-Set  |
|  perl-DateTime-TimeZone  |
|  perl-DateTimeX-Easy  |
|  perl-DB\_File  |
|  perl-DBD-CSV  |
|  perl-DBD-Mock  |
|  perl-DBD-Pg  |
|  perl-DBD-Pg-tests  |
|  perl-DBD-SQLite  |
|  perl-DBD-XBase  |
|  perl-DBI  |
|  perl-DBIx-Class  |
|  perl-DBIx-Class-Storage-Debug-PrettyPrint  |
|  perl-DBIx-ContextualFetch  |
|  perl-DBIx-Simple  |
|  perl-DBM-Deep  |
|  perl-Declare-Constraints-Simple  |
|  perl-devel  |
|  perl-Devel-CallChecker  |
|  perl-Devel-CallParser  |
|  perl-Devel-CheckLib  |
|  perl-Devel-Cover  |
|  perl-Devel-Cycle  |
|  perl-Devel-Declare  |
|  perl-Devel-EnforceEncapsulation  |
|  perl-Devel-GlobalDestruction  |
|  perl-Devel-Hide  |
|  perl-Devel-Leak  |
|  perl-Devel-PartialDump  |
|  perl-Devel-PatchPerl  |
|  perl-Devel-StackTrace  |
|  perl-Devel-StringInfo  |
|  perl-Devel-Symdump  |
|  perl-Digest  |
|  perl-Digest-BubbleBabble  |
|  perl-Digest-HMAC  |
|  perl-Digest-MD4  |
|  perl-Digest-MD5  |
|  perl-Digest-MD5-File  |
|  perl-Digest-Perl-MD5  |
|  perl-Digest-SHA  |
|  perl-Digest-SHA1  |
|  perl-Dist-CheckConflicts  |
|  perl-DynaLoader-Functions  |
|  perl-Email-Abstract  |
|  perl-Email-Address  |
|  perl-Email-Date  |
|  perl-Email-Date-Format  |
|  perl-Email-MessageID  |
|  perl-Email-MIME  |
|  perl-Email-MIME-Attachment-Stripper  |
|  perl-Email-MIME-ContentType  |
|  perl-Email-MIME-Encodings  |
|  perl-Email-Reply  |
|  perl-Email-Send  |
|  perl-Email-Simple  |
|  perl-Email-Valid  |
|  perl-Encode  |
|  perl-Encode-Detect  |
|  perl-Encode-devel  |
|  perl-Encode-Locale  |
|  perl-enum  |
|  perl-Env  |
|  perl-Env-Sanctify  |
|  perl-Error  |
|  perl-Eval-Closure  |
|  perl-Event-Lib  |
|  perl-Exception-Class  |
|  perl-Exporter  |
|  perl-Exporter-Lite  |
|  perl-ExtUtils-AutoInstall  |
|  perl-ExtUtils-CBuilder  |
|  perl-ExtUtils-Depends  |
|  perl-ExtUtils-Embed  |
|  perl-ExtUtils-Install  |
|  perl-ExtUtils-MakeMaker  |
|  perl-ExtUtils-MakeMaker-Coverage  |
|  perl-ExtUtils-Manifest  |
|  perl-ExtUtils-ParseXS  |
|  perl-ExtUtils-XSBuilder  |
|  perl-FCGI  |
|  perl-File-chdir  |
|  perl-File-CheckTree  |
|  perl-File-chmod  |
|  perl-File-Copy-Recursive  |
|  perl-File-FcntlLock  |
|  perl-File-Fetch  |
|  perl-File-Find-Rule  |
|  perl-File-Find-Rule-Perl  |
|  perl-File-Flat  |
|  perl-File-HomeDir  |
|  perl-File-Inplace  |
|  perl-File-Listing  |
|  perl-File-MMagic  |
|  perl-File-Next  |
|  perl-File-NFSLock  |
|  perl-File-Path  |
|  perl-File-Path-Tiny  |
|  perl-File-pushd  |
|  perl-File-ReadBackwards  |
|  perl-File-Remove  |
|  perl-File-ShareDir  |
|  perl-File-Slurp  |
|  perl-File-Tail  |
|  perl-File-Temp  |
|  perl-File-Which  |
|  perl-FileHandle-Fmode  |
|  perl-FileHandle-Unget  |
|  perl-Filter  |
|  perl-Font-AFM  |
|  perl-Font-TTF  |
|  perl-FreezeThaw  |
|  perl-Frontier-RPC  |
|  perl-Frontier-RPC-Client  |
|  perl-Frontier-RPC-doc  |
|  perl-GD  |
|  perl-GD-Barcode  |
|  perl-GDGraph  |
|  perl-GDGraph3d  |
|  perl-GDTextUtil  |
|  perl-Geography-Countries  |
|  perl-Getopt-Long  |
|  perl-Getopt-Long-Descriptive  |
|  perl-gettext  |
|  perl-Git  |
|  perl-Git-SVN  |
|  perl-Graph  |
|  perl-GraphViz  |
|  perl-GSSAPI  |
|  perl-GTop  |
|  perl-Hash-Merge  |
|  perl-homedir  |
|  perl-Hook-LexWrap  |
|  perl-HTML-Form  |
|  perl-HTML-Format  |
|  perl-HTML-FormatText-WithLinks  |
|  perl-HTML-FormatText-WithLinks-AndTables  |
|  perl-HTML-Lint  |
|  perl-HTML-Parser  |
|  perl-HTML-Scrubber  |
|  perl-HTML-Tagset  |
|  perl-HTML-Template  |
|  perl-HTML-Tidy  |
|  perl-HTML-Tree  |
|  perl-HTTP-Cookies  |
|  perl-HTTP-Daemon  |
|  perl-HTTP-Date  |
|  perl-HTTP-Message  |
|  perl-HTTP-Negotiate  |
|  perl-HTTP-Tiny  |
|  perl-Ima-DBI  |
|  perl-Image-Base  |
|  perl-Image-ExifTool  |
|  perl-Image-Info  |
|  perl-Image-Size  |
|  perl-Image-Xbm  |
|  perl-Image-Xpm  |
|  perl-Import-Into  |
|  perl-indirect  |
|  perl-Inline  |
|  perl-Inline-Files  |
|  perl-IO-All  |
|  perl-IO-Capture  |
|  perl-IO-CaptureOutput  |
|  perl-IO-Compress  |
|  perl-IO-HTML  |
|  perl-IO-Interactive  |
|  perl-IO-Multiplex  |
|  perl-IO-Socket-INET6  |
|  perl-IO-Socket-IP  |
|  perl-IO-Socket-SSL  |
|  perl-IO-Socket-Timeout  |
|  perl-IO-String  |
|  perl-IO-stringy  |
|  perl-IO-Tty  |
|  perl-IO-Zlib  |
|  perl-IPC-Cmd  |
|  perl-IPC-Run  |
|  perl-IPC-Run3  |
|  perl-IPC-SharedCache  |
|  perl-IPC-ShareLite  |
|  perl-IPC-Signal  |
|  perl-IPTables-Parse  |
|  perl-Jcode  |
|  perl-JSON  |
|  perl-JSON-Any  |
|  perl-JSON-Any-tests  |
|  perl-JSON-PP  |
|  perl-JSON-tests  |
|  perl-JSON-XS  |
|  perl-JSON-XS-tests  |
|  perl-LDAP  |
|  perl-Lexical-SealRequireHints  |
|  perl-Lexical-Var  |
|  perl-libapreq2  |
|  perl-libintl  |
|  perl-libs  |
|  perl-libwww-perl  |
|  perl-libxml-perl  |
|  perl-Lingua-EN-Inflect  |
|  perl-Lingua-EN-Sentence  |
|  perl-Linux-Pid  |
|  perl-List-MoreUtils  |
|  perl-local-lib  |
|  perl-Locale-Codes  |
|  perl-Locale-Maketext  |
|  perl-Locale-Maketext-Gettext  |
|  perl-Locale-Maketext-Lexicon  |
|  perl-Locale-Maketext-Simple  |
|  perl-Locale-PO  |
|  perl-Locale-US  |
|  perl-Log-Dispatch  |
|  perl-Log-Dispatch-FileRotate  |
|  perl-Log-Log4perl  |
|  perl-Log-Message  |
|  perl-Log-Message-Simple  |
|  perl-LWP-MediaTypes  |
|  perl-LWP-Protocol-http10  |
|  perl-LWP-Protocol-https  |
|  perl-LWP-UserAgent-Determined  |
|  perl-macros  |
|  perl-Mail-Box  |
|  perl-Mail-DKIM  |
|  perl-Mail-IMAPClient  |
|  perl-Mail-Mbox-MessageParser  |
|  perl-Mail-MboxParser  |
|  perl-Mail-Sender  |
|  perl-Mail-Sendmail  |
|  perl-Mail-SPF  |
|  perl-Mail-Transport-Dbx  |
|  perl-MailTools  |
|  perl-Makefile-DOM  |
|  perl-Makefile-Parser  |
|  perl-Math-Base36  |
|  perl-Math-Calc-Units  |
|  perl-mime-construct  |
|  perl-MIME-Lite  |
|  perl-MIME-tools  |
|  perl-MIME-Types  |
|  perl-Mixin-Linewise  |
|  perl-MLDBM  |
|  perl-Module-Build  |
|  perl-Module-CoreList  |
|  perl-Module-CPANTS-Analyse  |
|  perl-Module-ExtractUse  |
|  perl-Module-Find  |
|  perl-Module-Implementation  |
|  perl-Module-Info  |
|  perl-Module-Install  |
|  perl-Module-Install-Repository  |
|  perl-Module-Load  |
|  perl-Module-Load-Conditional  |
|  perl-Module-Loaded  |
|  perl-Module-Manifest  |
|  perl-Module-Metadata  |
|  perl-Module-Pluggable  |
|  perl-Module-Refresh  |
|  perl-Module-Runtime  |
|  perl-Module-ScanDeps  |
|  perl-Module-Signature  |
|  perl-Module-Util  |
|  perl-Mon  |
|  perl-Moo  |
|  perl-Moose  |
|  perl-MooseX-ConfigFromFile  |
|  perl-MooseX-Getopt  |
|  perl-MooseX-Role-Parameterized  |
|  perl-MooseX-SimpleConfig  |
|  perl-MooseX-StrictConstructor  |
|  perl-MooseX-Types  |
|  perl-MooseX-Types-DateTime  |
|  perl-MooseX-Types-DateTime-MoreCoercions  |
|  perl-MooseX-Types-JSON  |
|  perl-MooseX-Types-JSON-tests  |
|  perl-MooseX-Types-Path-Class  |
|  perl-Mozilla-CA  |
|  perl-Mozilla-LDAP  |
|  perl-MRO-Compat  |
|  perl-multidimensional  |
|  perl-Nagios-Plugin  |
|  perl-namespace-autoclean  |
|  perl-namespace-clean  |
|  perl-Net-Amazon-EC2  |
|  perl-Net-Amazon-S3  |
|  perl-Net-CIDR  |
|  perl-Net-CIDR-Lite  |
|  perl-Net-Daemon  |
|  perl-Net-DNS  |
|  perl-Net-DNS-Nameserver  |
|  perl-Net-DNS-Resolver-Programmable  |
|  perl-Net-Domain-TLD  |
|  perl-Net-HTTP  |
|  perl-Net-IMAP-Simple-SSL  |
|  perl-Net-IP  |
|  perl-Net-Jabber  |
|  perl-Net-LibIDN  |
|  perl-Net-OAuth  |
|  perl-Net-Server  |
|  perl-Net-SMTP-SSL  |
|  perl-Net-SNMP  |
|  perl-Net-SNPP  |
|  perl-Net-SSLeay  |
|  perl-Net-Telnet  |
|  perl-Net-XMPP  |
|  perl-NetAddr-IP  |
|  perl-Newt  |
|  perl-Number-Compare  |
|  perl-Object-Accessor  |
|  perl-Object-Deadly  |
|  perl-Object-Realize-Later  |
|  perl-OLE-Storage\_Lite  |
|  perl-Package-Constants  |
|  perl-Package-DeprecationManager  |
|  perl-Package-Generator  |
|  perl-Package-Stash  |
|  perl-Package-Stash-XS  |
|  perl-Package-Variant  |
|  perl-PadWalker  |
|  perl-PAR-Dist  |
|  perl-Parallel-Iterator  |
|  perl-Params-Check  |
|  perl-Params-Coerce  |
|  perl-Params-Util  |
|  perl-Params-Validate  |
|  perl-parent  |
|  perl-Parse-CPAN-Meta  |
|  perl-Parse-RecDescent  |
|  perl-Parse-Yapp  |
|  perl-Path-Class  |
|  perl-PathTools  |
|  perl-PDF-Reuse  |
|  perl-Perl-Critic  |
|  perl-Perl-Critic-More  |
|  perl-Perl-Destruct-Level  |
|  perl-Perl-MinimumVersion  |
|  perl-Perl-OSType  |
|  perl-Perl4-CoreLibs  |
|  perl-Perlilog  |
|  perl-PerlIO-via-Timeout  |
|  perl-PlRPC  |
|  perl-Pod-Checker  |
|  perl-Pod-Coverage  |
|  perl-Pod-Coverage-TrustPod  |
|  perl-Pod-Escapes  |
|  perl-Pod-Eventual  |
|  perl-Pod-LaTeX  |
|  perl-Pod-Parser  |
|  perl-Pod-Perldoc  |
|  perl-Pod-Plainer  |
|  perl-Pod-POM  |
|  perl-Pod-Simple  |
|  perl-Pod-Spell  |
|  perl-Pod-Strip  |
|  perl-Pod-Tests  |
|  perl-Pod-Usage  |
|  perl-podlators  |
|  perl-PPI  |
|  perl-PPI-HTML  |
|  perl-PPIx-Regexp  |
|  perl-PPIx-Utilities  |
|  perl-prefork  |
|  perl-Probe-Perl  |
|  perl-Proc-Daemon  |
|  perl-Proc-PID-File  |
|  perl-Proc-ProcessTable  |
|  perl-Proc-WaitStat  |
|  perl-Razor-Agent  |
|  perl-Readonly  |
|  perl-Readonly-XS  |
|  perl-Redis  |
|  perl-Regexp-Common  |
|  perl-Return-Value  |
|  perl-Role-Tiny  |
|  perl-RRD-Simple  |
|  perl-Scalar-List-Utils  |
|  perl-Scalar-Properties  |
|  perl-Scope-Guard  |
|  perl-Scope-Guard-tests  |
|  perl-Set-Crontab  |
|  perl-Set-Infinite  |
|  perl-Set-Scalar  |
|  perl-SGMLSpm  |
|  perl-SNMP\_Session  |
|  perl-SOAP-Lite  |
|  perl-SOAP-Transport-TCP  |
|  perl-SOAP-WSDL  |
|  perl-Socket  |
|  perl-Socket6  |
|  perl-Software-License  |
|  perl-Sort-Versions  |
|  perl-Spiffy  |
|  perl-Spreadsheet-ParseExcel  |
|  perl-Spreadsheet-WriteExcel  |
|  perl-SQL-Abstract  |
|  perl-SQL-Statement  |
|  perl-SQL-Translator  |
|  perl-srpm-macros  |
|  perl-Statistics-Descriptive  |
|  perl-Storable  |
|  perl-strictures  |
|  perl-String-CRC32  |
|  perl-String-Format  |
|  perl-String-ShellQuote  |
|  perl-String-Similarity  |
|  perl-Sub-Exporter  |
|  perl-Sub-Exporter-Progressive  |
|  perl-Sub-Identify  |
|  perl-Sub-Install  |
|  perl-Sub-Name  |
|  perl-Sub-Uplevel  |
|  perl-SUPER  |
|  perl-Switch  |
|  perl-Syntax-Highlight-Engine-Kate  |
|  perl-Sys-CPU  |
|  perl-Sys-MemInfo  |
|  perl-Sys-Statistics-Linux  |
|  perl-Sys-Syslog  |
|  perl-Taint-Runtime  |
|  perl-Task-Weaken  |
|  perl-Template-Toolkit  |
|  perl-Term-ProgressBar  |
|  perl-Term-ProgressBar-Quiet  |
|  perl-Term-ProgressBar-Simple  |
|  perl-Term-UI  |
|  perl-TermReadKey  |
|  perl-Test-Base  |
|  perl-Test-CheckChanges  |
|  perl-Test-CheckDeps  |
|  perl-Test-ClassAPI  |
|  perl-Test-CPAN-Meta  |
|  perl-Test-CPAN-Meta-JSON  |
|  perl-Test-CPAN-Meta-YAML  |
|  perl-Test-Deep  |
|  perl-Test-Differences  |
|  perl-Test-DistManifest  |
|  perl-Test-Distribution  |
|  perl-Test-EOL  |
|  perl-Test-Exception  |
|  perl-Test-Fatal  |
|  perl-Test-Harness  |
|  perl-Test-HasVersion  |
|  perl-Test-Inline  |
|  perl-Test-Inter  |
|  perl-Test-Kwalitee  |
|  perl-Test-LeakTrace  |
|  perl-Test-Manifest  |
|  perl-Test-Memory-Cycle  |
|  perl-Test-MinimumVersion  |
|  perl-Test-MockModule  |
|  perl-Test-MockObject  |
|  perl-Test-MockTime  |
|  perl-Test-Moose  |
|  perl-Test-Most  |
|  perl-Test-NoTabs  |
|  perl-Test-NoWarnings  |
|  perl-Test-Object  |
|  perl-Test-Output  |
|  perl-Test-Perl-Critic  |
|  perl-Test-Perl-Critic-Policy  |
|  perl-Test-Pod  |
|  perl-Test-Pod-Coverage  |
|  perl-Test-Portability-Files  |
|  perl-Test-Prereq  |
|  perl-Test-Requires  |
|  perl-Test-Script  |
|  perl-Test-SharedFork  |
|  perl-Test-Simple  |
|  perl-Test-Spec  |
|  perl-Test-Spelling  |
|  perl-Test-SubCalls  |
|  perl-Test-Synopsis  |
|  perl-Test-Taint  |
|  perl-Test-TCP  |
|  perl-Test-TempDir  |
|  perl-Test-Tester  |
|  perl-Test-Trap  |
|  perl-Test-use-ok  |
|  perl-Test-Valgrind  |
|  perl-Test-Vars  |
|  perl-Test-Warn  |
|  perl-Test-Without-Module  |
|  perl-Test-YAML-Meta  |
|  perl-Test-YAML-Valid  |
|  perl-tests  |
|  perl-TeX-Hyphen  |
|  perl-Text-Autoformat  |
|  perl-Text-CharWidth  |
|  perl-Text-CSV  |
|  perl-Text-CSV\_XS  |
|  perl-Text-Diff  |
|  perl-Text-Glob  |
|  perl-Text-Haml  |
|  perl-Text-Iconv  |
|  perl-Text-Markdown  |
|  perl-Text-ParseWords  |
|  perl-Text-PDF  |
|  perl-Text-RecordParser  |
|  perl-Text-Reform  |
|  perl-Text-Soundex  |
|  perl-Text-TabularDisplay  |
|  perl-Text-Template  |
|  perl-Text-Unidecode  |
|  perl-Text-WrapI18N  |
|  perl-Thread-Queue  |
|  perl-threads  |
|  perl-threads-shared  |
|  perl-Tie-IxHash  |
|  perl-Tie-ToObject  |
|  perl-Time-Duration  |
|  perl-Time-Duration-Parse  |
|  perl-Time-HiRes  |
|  perl-Time-Local  |
|  perl-Time-modules  |
|  perl-Time-Period  |
|  perl-Time-Piece  |
|  perl-Time-Piece-MySQL  |
|  perl-TimeDate  |
|  perl-Tk  |
|  perl-Tk-devel  |
|  perl-Tree-DAG\_Node  |
|  perl-Try-Tiny  |
|  perl-Unicode-Map  |
|  perl-Unicode-Map8  |
|  perl-Unicode-String  |
|  perl-UNIVERSAL-can  |
|  perl-UNIVERSAL-isa  |
|  perl-UNIVERSAL-moniker  |
|  perl-UNIVERSAL-require  |
|  perl-Unix-Syslog  |
|  perl-URI  |
|  perl-User-Identity  |
|  perl-Variable-Magic  |
|  perl-version  |
|  perl-Version-Requirements  |
|  perl-WWW-Curl  |
|  perl-WWW-RobotRules  |
|  perl-X11-Protocol  |
|  perl-XML-Catalog  |
|  perl-XML-DOM  |
|  perl-XML-DOM-XPath  |
|  perl-XML-Dumper  |
|  perl-XML-Filter-BufferText  |
|  perl-XML-Grove  |
|  perl-XML-Handler-YAWriter  |
|  perl-XML-LibXML  |
|  perl-XML-LibXSLT  |
|  perl-XML-NamespaceSupport  |
|  perl-XML-Parser  |
|  perl-XML-RegExp  |
|  perl-XML-RSS  |
|  perl-XML-SAX  |
|  perl-XML-SAX-Base  |
|  perl-XML-SAX-Writer  |
|  perl-XML-Simple  |
|  perl-XML-Stream  |
|  perl-XML-TokeParser  |
|  perl-XML-TreeBuilder  |
|  perl-XML-Twig  |
|  perl-XML-Writer  |
|  perl-XML-XPath  |
|  perl-XML-XPathEngine  |
|  perl-XML-XQL  |
|  perl-YAML  |
|  perl-YAML-LibYAML  |
|  perl-YAML-Syck  |
|  perl-YAML-Tiny  |
|  perlbrew  |
|  perltidy  |
|  php-common  |
|  php56  |
|  php56-bcmath  |
|  php56-cli  |
|  php56-common  |
|  php56-dba  |
|  php56-dbg  |
|  php56-devel  |
|  php56-embedded  |
|  php56-enchant  |
|  php56-fpm  |
|  php56-gd  |
|  php56-gmp  |
|  php56-imap  |
|  php56-intl  |
|  php56-jsonc  |
|  php56-jsonc-devel  |
|  php56-ldap  |
|  php56-mbstring  |
|  php56-mcrypt  |
|  php56-mssql  |
|  php56-mysqlnd  |
|  php56-odbc  |
|  php56-opcache  |
|  php56-pdo  |
|  php56-pecl-apcu  |
|  php56-pecl-apcu-devel  |
|  php56-pecl-http  |
|  php56-pecl-http-devel  |
|  php56-pecl-igbinary  |
|  php56-pecl-igbinary-devel  |
|  php56-pecl-imagick  |
|  php56-pecl-memcache  |
|  php56-pecl-memcached  |
|  php56-pecl-oauth  |
|  php56-pecl-propro  |
|  php56-pecl-propro-devel  |
|  php56-pecl-raphf  |
|  php56-pecl-raphf-devel  |
|  php56-pecl-redis  |
|  php56-pecl-ssh2  |
|  php56-pecl-xdebug  |
|  php56-pgsql  |
|  php56-process  |
|  php56-pspell  |
|  php56-recode  |
|  php56-snmp  |
|  php56-soap  |
|  php56-tidy  |
|  php56-xml  |
|  php56-xmlrpc  |
|  pigz  |
|  pinentry  |
|  pinfo  |
|  pixman  |
|  pixman-devel  |
|  pkcs11-helper  |
|  pkcs11-helper-devel  |
|  pkgconfig  |
|  pl-devel  |
|  pl-static  |
|  plotutils  |
|  plotutils-devel  |
|  plpa  |
|  plpa-devel  |
|  plpa-libs  |
|  pm-utils  |
|  pm-utils-devel  |
|  pngcrush  |
|  policycoreutils  |
|  policycoreutils-newrole  |
|  policycoreutils-python  |
|  policycoreutils-restorecond  |
|  poppler  |
|  poppler-cpp  |
|  poppler-cpp-devel  |
|  poppler-data  |
|  poppler-devel  |
|  poppler-glib  |
|  poppler-glib-devel  |
|  poppler-utils  |
|  popt  |
|  popt-devel  |
|  popt-static  |
|  portreserve  |
|  postfix  |
|  postfix-perl-scripts  |
|  postgresql-jdbc  |
|  postgresql-odbc  |
|  postgresql92  |
|  postgresql92-contrib  |
|  postgresql92-devel  |
|  postgresql92-docs  |
|  postgresql92-libs  |
|  postgresql92-plperl  |
|  postgresql92-plpython26  |
|  postgresql92-plpython27  |
|  postgresql92-pltcl  |
|  postgresql92-server  |
|  postgresql92-server-compat  |
|  postgresql92-test  |
|  postgrey  |
|  ppl-devel  |
|  ppl-docs  |
|  ppl-gprolog-static  |
|  ppl-java-javadoc  |
|  ppl-pwl  |
|  ppl-pwl-devel  |
|  ppl-pwl-docs  |
|  ppl-pwl-static  |
|  ppl-static  |
|  ppl-swiprolog-static  |
|  ppp  |
|  ppp-devel  |
|  pprof  |
|  pptp  |
|  pptp-setup  |
|  prelink  |
|  preupgrade-assistant  |
|  preupgrade-assistant-al1toal2  |
|  preupgrade-assistant-tools  |
|  privoxy  |
|  procmail  |
|  procps  |
|  procps-devel  |
|  protobuf  |
|  protobuf-compiler  |
|  protobuf-devel  |
|  protobuf-lite  |
|  protobuf-lite-devel  |
|  protobuf-lite-static  |
|  protobuf-python27  |
|  protobuf-static  |
|  protobuf-vim  |
|  psacct  |
|  psl  |
|  psmisc  |
|  pssh  |
|  pstoedit  |
|  pstoedit-devel  |
|  psutils  |
|  psutils-perl  |
|  pth  |
|  pth-devel  |
|  publican  |
|  publican-doc  |
|  pv  |
|  pygobject2  |
|  pygobject2-codegen  |
|  pygobject2-devel  |
|  pygobject2-doc  |
|  pykickstart  |
|  pyldb  |
|  pyldb-devel  |
|  pyparted  |
|  pytalloc  |
|  pytalloc-devel  |
|  python-createrepo\_c  |
|  python-deltarpm  |
|  python-dmidecode  |
|  python-formencode-common  |
|  python-lcms  |
|  python-netaddr  |
|  python-pwquality  |
|  python-sphinx-common  |
|  python-twisted-core-zsh  |
|  python27  |
|  python27-babel  |
|  python27-backports  |
|  python27-backports-ssl\_match\_hostname  |
|  python27-beaker  |
|  python27-boto  |
|  python27-boto3  |
|  python27-botocore  |
|  python27-cairosvg  |
|  python27-certifi  |
|  python27-chardet  |
|  python27-cheetah  |
|  python27-clang  |
|  python27-colorama  |
|  python27-configobj  |
|  python27-coverage  |
|  python27-crypto  |
|  python27-Cython  |
|  python27-daemon  |
|  python27-dateutil  |
|  python27-decorator  |
|  python27-decoratortools  |
|  python27-devel  |
|  python27-dns  |
|  python27-docs  |
|  python27-docutils  |
|  python27-dtopt  |
|  python27-ecdsa  |
|  python27-enchant  |
|  python27-epdb  |
|  python27-ethtool  |
|  python27-fastimport  |
|  python27-formencode  |
|  python27-fpconst  |
|  python27-funcsigs  |
|  python27-futures  |
|  python27-genshi  |
|  python27-gevent  |
|  python27-greenlet  |
|  python27-greenlet-devel  |
|  python27-gudev  |
|  python27-httplib2  |
|  python27-httpretty  |
|  python27-hwdata  |
|  python27-imaging  |
|  python27-imaging-devel  |
|  python27-iniparse  |
|  python27-inotify  |
|  python27-inotify-examples  |
|  python27-ipaddr  |
|  python27-IPy  |
|  python27-jinja2  |
|  python27-jmespath  |
|  python27-jsonpatch  |
|  python27-jsonpointer  |
|  python27-kerberos  |
|  python27-kitchen  |
|  python27-kitchen-doc  |
|  python27-krbV  |
|  python27-ldap  |
|  python27-libipa\_hbac  |
|  python27-libs  |
|  python27-libsss\_nss\_idmap  |
|  python27-lit  |
|  python27-lockfile  |
|  python27-lxml  |
|  python27-lxml-docs  |
|  python27-lzo  |
|  python27-m2crypto  |
|  python27-magic  |
|  python27-mako  |
|  python27-markdown  |
|  python27-markupsafe  |
|  python27-memcached  |
|  python27-minimock  |
|  python27-mock  |
|  python27-mock13  |
|  python27-nose  |
|  python27-nose-docs  |
|  python27-nose-exclude  |
|  python27-numpy  |
|  python27-numpy-doc  |
|  python27-numpy-f2py  |
|  python27-oauth2  |
|  python27-paramiko  |
|  python27-paste  |
|  python27-paste-deploy  |
|  python27-paste-script  |
|  python27-pbr  |
|  python27-pep8  |
|  python27-pexpect  |
|  python27-pip  |
|  python27-ply  |
|  python27-prettytable  |
|  python27-psycopg2  |
|  python27-psycopg2-doc  |
|  python27-py  |
|  python27-pyasn1  |
|  python27-pyasn1-modules  |
|  python27-pycairo  |
|  python27-pycairo-devel  |
|  python27-pycurl  |
|  python27-pygments  |
|  python27-pygpgme  |
|  python27-PyGreSQL  |
|  python27-pyliblzma  |
|  python27-pyOpenSSL  |
|  python27-pyparsing  |
|  python27-pyparsing-doc  |
|  python27-pystache  |
|  python27-pytest  |
|  python27-pytz  |
|  python27-pyudev  |
|  python27-pyxattr  |
|  python27-PyYAML  |
|  python27-requests  |
|  python27-rsa  |
|  python27-scipy  |
|  python27-setuptools  |
|  python27-simplejson  |
|  python27-six  |
|  python27-SOAPpy  |
|  python27-sphinx  |
|  python27-sphinx-doc  |
|  python27-sss  |
|  python27-sss-murmur  |
|  python27-sssdconfig  |
|  python27-sure  |
|  python27-tdb  |
|  python27-tempita  |
|  python27-test  |
|  python27-testtools  |
|  python27-testtools-doc  |
|  python27-tevent  |
|  python27-tools  |
|  python27-tornado  |
|  python27-tornado-doc  |
|  python27-tre  |
|  python27-twisted  |
|  python27-twisted-conch  |
|  python27-twisted-core  |
|  python27-twisted-core-doc  |
|  python27-twisted-lore  |
|  python27-twisted-mail  |
|  python27-twisted-names  |
|  python27-twisted-news  |
|  python27-twisted-runner  |
|  python27-twisted-web  |
|  python27-twisted-words  |
|  python27-unittest2  |
|  python27-urlgrabber  |
|  python27-urllib3  |
|  python27-virtualenv  |
|  python27-webob  |
|  python27-webtest  |
|  python27-which  |
|  python27-wsgiproxy  |
|  python27-zope-filesystem  |
|  python27-zope-interface  |
|  qdox  |
|  qdox-javadoc  |
|  qemu-img  |
|  qemu-kvm  |
|  qemu-kvm-common  |
|  qemu-kvm-tools  |
|  qrencode  |
|  qrencode-devel  |
|  qrencode-libs  |
|  quagga  |
|  quagga-contrib  |
|  quagga-devel  |
|  quilt  |
|  quota  |
|  quota-devel  |
|  quota-doc  |
|  quota-nls  |
|  quota-warnquota  |
|  R  |
|  R-core  |
|  R-core-devel  |
|  R-devel  |
|  R-java  |
|  R-java-devel  |
|  radiusclient-ng  |
|  radiusclient-ng-devel  |
|  radiusclient-ng-utils  |
|  rarian  |
|  rarian-devel  |
|  rcs  |
|  rcs-docs  |
|  rdate  |
|  rdist  |
|  re2c  |
|  readahead  |
|  readline  |
|  readline-devel  |
|  readline-static  |
|  realmd  |
|  realmd-devel-docs  |
|  recode  |
|  recode-devel  |
|  redhat-lsb  |
|  redhat-lsb-compat  |
|  redhat-lsb-core  |
|  redhat-lsb-printing  |
|  regexp  |
|  regexp-javadoc  |
|  reptyr  |
|  resource-agents  |
|  rhino  |
|  rhino-demo  |
|  rhino-javadoc  |
|  rkhunter  |
|  rls  |
|  rmt  |
|  rng-tools  |
|  robotfindskitten  |
|  rootfiles  |
|  rpcbind  |
|  rpm  |
|  rpm-apidocs  |
|  rpm-build  |
|  rpm-build-libs  |
|  rpm-cron  |
|  rpm-devel  |
|  rpm-libs  |
|  rpm-python27  |
|  rpm-sign  |
|  rpmdevtools  |
|  rpmlint  |
|  rrdtool  |
|  rrdtool-devel  |
|  rrdtool-doc  |
|  rrdtool-lua  |
|  rrdtool-perl  |
|  rrdtool-python27  |
|  rrdtool-ruby20  |
|  rrdtool-tcl  |
|  rsh  |
|  rsh-server  |
|  rssh  |
|  rsync  |
|  rsyslog  |
|  rsyslog-gnutls  |
|  rsyslog-gssapi  |
|  rsyslog-mysql  |
|  rsyslog-pgsql  |
|  rsyslog-snmp  |
|  ruby  |
|  ruby-devel  |
|  ruby-doc  |
|  ruby-flexmock  |
|  ruby-irb  |
|  ruby-libs  |
|  ruby-mysql  |
|  ruby20  |
|  ruby20-augeas  |
|  ruby20-devel  |
|  ruby20-doc  |
|  ruby20-irb  |
|  ruby20-libs  |
|  ruby20-shadow  |
|  rubygem-bigdecimal  |
|  rubygem-columnize  |
|  rubygem-crack  |
|  rubygem-crack-doc  |
|  rubygem-daemons  |
|  rubygem-flexmock  |
|  rubygem-flexmock-doc  |
|  rubygem-hoe  |
|  rubygem-hoe-doc  |
|  rubygem-httparty  |
|  rubygem-httparty-doc  |
|  rubygem-io-console  |
|  rubygem-jnunemaker-matchy  |
|  rubygem-jnunemaker-matchy-doc  |
|  rubygem-json  |
|  rubygem-json\_pure  |
|  rubygem-json\_pure-doc  |
|  rubygem-linecache-doc  |
|  rubygem-log4r  |
|  rubygem-log4r-doc  |
|  rubygem-madeleine  |
|  rubygem-madeleine-doc  |
|  rubygem-minitest  |
|  rubygem-open4  |
|  rubygem-open4-doc  |
|  rubygem-psych  |
|  rubygem-rake  |
|  rubygem-rake-compiler  |
|  rubygem-rake-compiler-doc  |
|  rubygem-rdoc  |
|  rubygem-ruby-debug  |
|  rubygem-ruby-debug-base  |
|  rubygem-ruby-debug-base-doc  |
|  rubygem-ruby-debug-doc  |
|  rubygem-shoulda  |
|  rubygem-shoulda-doc  |
|  rubygem20-aws-sdk  |
|  rubygem20-aws-sdk-doc  |
|  rubygem20-bigdecimal  |
|  rubygem20-diff-lcs  |
|  rubygem20-diff-lcs-doc  |
|  rubygem20-io-console  |
|  rubygem20-json  |
|  rubygem20-json-doc  |
|  rubygem20-minitest  |
|  rubygem20-minitest-doc  |
|  rubygem20-minitest5  |
|  rubygem20-minitest5-doc  |
|  rubygem20-nokogiri  |
|  rubygem20-nokogiri-doc  |
|  rubygem20-power\_assert  |
|  rubygem20-power\_assert-doc  |
|  rubygem20-psych  |
|  rubygem20-rake  |
|  rubygem20-rake-doc  |
|  rubygem20-rdoc  |
|  rubygem20-rdoc-doc  |
|  rubygem20-rspec  |
|  rubygem20-rspec-core  |
|  rubygem20-rspec-core-doc  |
|  rubygem20-rspec-expectations  |
|  rubygem20-rspec-expectations-doc  |
|  rubygem20-rspec-mocks  |
|  rubygem20-rspec-mocks-doc  |
|  rubygem20-uuidtools  |
|  rubygem20-uuidtools-doc  |
|  rubygems  |
|  rubygems-devel  |
|  rubygems20  |
|  rubygems20-devel  |
|  runc  |
|  rust  |
|  rust-analysis  |
|  rust-debugger-common  |
|  rust-doc  |
|  rust-gdb  |
|  rust-src  |
|  rust-std-static  |
|  rustfmt  |
|  samba  |
|  samba-client  |
|  samba-client-libs  |
|  samba-common  |
|  samba-common-libs  |
|  samba-common-tools  |
|  samba-devel  |
|  samba-krb5-printing  |
|  samba-libs  |
|  samba-pidl  |
|  samba-python  |
|  samba-python-test  |
|  samba-test  |
|  samba-test-libs  |
|  samba-winbind  |
|  samba-winbind-clients  |
|  samba-winbind-krb5-locator  |
|  samba-winbind-modules  |
|  saxon  |
|  saxon-aelfred  |
|  saxon-demo  |
|  saxon-javadoc  |
|  saxon-jdom  |
|  saxon-manual  |
|  saxon-scripts  |
|  scap-security-guide  |
|  scap-security-guide-doc  |
|  scons  |
|  screen  |
|  scrollkeeper  |
|  seabios  |
|  seabios-bin  |
|  seavgabios-bin  |
|  sed  |
|  selinux-policy  |
|  selinux-policy-doc  |
|  selinux-policy-minimum  |
|  selinux-policy-mls  |
|  selinux-policy-targeted  |
|  sendmail  |
|  sendmail-cf  |
|  sendmail-devel  |
|  sendmail-doc  |
|  sendmail-milter  |
|  setools  |
|  setools-console  |
|  setools-devel  |
|  setools-libs  |
|  setools-libs-python  |
|  setools-libs-tcl  |
|  setserial  |
|  setup  |
|  sgabios  |
|  sgabios-bin  |
|  sgml-common  |
|  sgpio  |
|  shadow-utils  |
|  shared-mime-info  |
|  sharutils  |
|  shorewall  |
|  shorewall-core  |
|  shorewall-init  |
|  shorewall-lite  |
|  shorewall6  |
|  shorewall6-lite  |
|  sip  |
|  sip-devel  |
|  sip-macros  |
|  sl  |
|  slang  |
|  slang-devel  |
|  slang-slsh  |
|  slang-static  |
|  slf4j  |
|  slf4j-javadoc  |
|  slf4j-manual  |
|  snappy  |
|  snappy-devel  |
|  socat  |
|  sos  |
|  source-highlight  |
|  source-highlight-devel  |
|  spamassassin  |
|  spawn-fcgi  |
|  speex  |
|  speex-devel  |
|  speex-tools  |
|  splint  |
|  sqlite  |
|  sqlite-devel  |
|  sqlite-doc  |
|  sqlite-tcl  |
|  squashfs-tools  |
|  squid  |
|  squid-migration-script  |
|  sssd  |
|  sssd-ad  |
|  sssd-client  |
|  sssd-common  |
|  sssd-common-pac  |
|  sssd-dbus  |
|  sssd-ipa  |
|  sssd-krb5  |
|  sssd-krb5-common  |
|  sssd-ldap  |
|  sssd-libwbclient  |
|  sssd-libwbclient-devel  |
|  sssd-proxy  |
|  sssd-tools  |
|  sssd-winbind-idmap  |
|  star  |
|  stix-fonts  |
|  stix-math-fonts  |
|  strace  |
|  stress  |
|  stress-ng  |
|  stunnel  |
|  sudo  |
|  sudo-devel  |
|  suitesparse  |
|  suitesparse-devel  |
|  suitesparse-doc  |
|  suitesparse-static  |
|  svn-bisect  |
|  svn2cl  |
|  svrcore  |
|  svrcore-devel  |
|  swig  |
|  swig-doc  |
|  symlinks  |
|  sysctl-defaults  |
|  sysfsutils  |
|  syslinux  |
|  syslinux-devel  |
|  syslinux-extlinux  |
|  syslinux-perl  |
|  syslinux-tftpboot  |
|  sysstat  |
|  system-logos  |
|  system-release  |
|  system-release-gpu  |
|  system-release-obsoletes  |
|  system-rpm-config  |
|  systemtap  |
|  systemtap-client  |
|  systemtap-initscript  |
|  systemtap-runtime  |
|  systemtap-runtime-python2  |
|  systemtap-sdt-devel  |
|  systemtap-server  |
|  sysvinit  |
|  t1lib  |
|  t1lib-apps  |
|  t1lib-devel  |
|  t1lib-static  |
|  t1utils  |
|  talk  |
|  talk-server  |
|  tar  |
|  tbb  |
|  tbb-devel  |
|  tbb-doc  |
|  tcl  |
|  tcl-devel  |
|  tcp\_wrappers  |
|  tcp\_wrappers-devel  |
|  tcp\_wrappers-libs  |
|  tcpdump  |
|  tcsh  |
|  tdb-tools  |
|  teckit  |
|  teckit-devel  |
|  telnet  |
|  telnet-server  |
|  tex-preview  |
|  texi2html  |
|  texinfo  |
|  texinfo-tex  |
|  texlive  |
|  texlive-adjustbox  |
|  texlive-adjustbox-doc  |
|  texlive-ae  |
|  texlive-ae-doc  |
|  texlive-algorithms  |
|  texlive-algorithms-doc  |
|  texlive-amscls  |
|  texlive-amscls-doc  |
|  texlive-amsfonts  |
|  texlive-amsfonts-doc  |
|  texlive-amsmath  |
|  texlive-amsmath-doc  |
|  texlive-anysize  |
|  texlive-anysize-doc  |
|  texlive-appendix  |
|  texlive-appendix-doc  |
|  texlive-arabxetex  |
|  texlive-arabxetex-doc  |
|  texlive-arphic  |
|  texlive-arphic-doc  |
|  texlive-attachfile  |
|  texlive-attachfile-doc  |
|  texlive-avantgar  |
|  texlive-babel  |
|  texlive-babel-doc  |
|  texlive-babelbib  |
|  texlive-babelbib-doc  |
|  texlive-base  |
|  texlive-beamer  |
|  texlive-beamer-doc  |
|  texlive-bera  |
|  texlive-bera-doc  |
|  texlive-beton  |
|  texlive-beton-doc  |
|  texlive-bibtex  |
|  texlive-bibtex-bin  |
|  texlive-bibtex-doc  |
|  texlive-bibtopic  |
|  texlive-bibtopic-doc  |
|  texlive-bidi  |
|  texlive-bidi-doc  |
|  texlive-bigfoot  |
|  texlive-bigfoot-doc  |
|  texlive-bookman  |
|  texlive-booktabs  |
|  texlive-booktabs-doc  |
|  texlive-breakurl  |
|  texlive-breakurl-doc  |
|  texlive-caption  |
|  texlive-caption-doc  |
|  texlive-carlisle  |
|  texlive-carlisle-doc  |
|  texlive-changebar  |
|  texlive-changebar-doc  |
|  texlive-changepage  |
|  texlive-changepage-doc  |
|  texlive-charter  |
|  texlive-charter-doc  |
|  texlive-chngcntr  |
|  texlive-chngcntr-doc  |
|  texlive-cite  |
|  texlive-cite-doc  |
|  texlive-cjk  |
|  texlive-cjk-doc  |
|  texlive-cm  |
|  texlive-cm-doc  |
|  texlive-cm-lgc  |
|  texlive-cm-lgc-doc  |
|  texlive-cm-super  |
|  texlive-cm-super-doc  |
|  texlive-cmap  |
|  texlive-cmap-doc  |
|  texlive-cmextra  |
|  texlive-cns  |
|  texlive-cns-doc  |
|  texlive-collectbox  |
|  texlive-collectbox-doc  |
|  texlive-collection-basic  |
|  texlive-collection-documentation-base  |
|  texlive-collection-fontsrecommended  |
|  texlive-collection-htmlxml  |
|  texlive-collection-latex  |
|  texlive-collection-latexrecommended  |
|  texlive-collection-xetex  |
|  texlive-colortbl  |
|  texlive-colortbl-doc  |
|  texlive-courier  |
|  texlive-crop  |
|  texlive-crop-doc  |
|  texlive-csquotes  |
|  texlive-csquotes-doc  |
|  texlive-ctable  |
|  texlive-ctable-doc  |
|  texlive-currfile  |
|  texlive-currfile-doc  |
|  texlive-datetime  |
|  texlive-datetime-doc  |
|  texlive-dvipdfm  |
|  texlive-dvipdfm-bin  |
|  texlive-dvipdfm-doc  |
|  texlive-dvipdfmx  |
|  texlive-dvipdfmx-bin  |
|  texlive-dvipdfmx-def  |
|  texlive-dvipdfmx-doc  |
|  texlive-dvipng  |
|  texlive-dvipng-bin  |
|  texlive-dvipng-doc  |
|  texlive-dvips  |
|  texlive-dvips-bin  |
|  texlive-dvips-doc  |
|  texlive-ec  |
|  texlive-ec-doc  |
|  texlive-eepic  |
|  texlive-eepic-doc  |
|  texlive-enctex  |
|  texlive-enctex-doc  |
|  texlive-enumitem  |
|  texlive-enumitem-doc  |
|  texlive-epsf  |
|  texlive-epsf-doc  |
|  texlive-epstopdf  |
|  texlive-epstopdf-bin  |
|  texlive-epstopdf-doc  |
|  texlive-eso-pic  |
|  texlive-eso-pic-doc  |
|  texlive-etex  |
|  texlive-etex-doc  |
|  texlive-etex-pkg  |
|  texlive-etex-pkg-doc  |
|  texlive-etoolbox  |
|  texlive-etoolbox-doc  |
|  texlive-euenc  |
|  texlive-euenc-doc  |
|  texlive-euler  |
|  texlive-euler-doc  |
|  texlive-euro  |
|  texlive-euro-doc  |
|  texlive-eurosym  |
|  texlive-eurosym-doc  |
|  texlive-extsizes  |
|  texlive-extsizes-doc  |
|  texlive-fancybox  |
|  texlive-fancybox-doc  |
|  texlive-fancyhdr  |
|  texlive-fancyhdr-doc  |
|  texlive-fancyref  |
|  texlive-fancyref-doc  |
|  texlive-fancyvrb  |
|  texlive-fancyvrb-doc  |
|  texlive-filecontents  |
|  texlive-filecontents-doc  |
|  texlive-filehook  |
|  texlive-filehook-doc  |
|  texlive-fix2col  |
|  texlive-fix2col-doc  |
|  texlive-fixlatvian  |
|  texlive-fixlatvian-doc  |
|  texlive-float  |
|  texlive-float-doc  |
|  texlive-fmtcount  |
|  texlive-fmtcount-doc  |
|  texlive-fncychap  |
|  texlive-fncychap-doc  |
|  texlive-fontbook  |
|  texlive-fontbook-doc  |
|  texlive-fontspec  |
|  texlive-fontspec-doc  |
|  texlive-fontware  |
|  texlive-fontware-bin  |
|  texlive-fontwrap  |
|  texlive-fontwrap-doc  |
|  texlive-footmisc  |
|  texlive-footmisc-doc  |
|  texlive-fp  |
|  texlive-fp-doc  |
|  texlive-fpl  |
|  texlive-fpl-doc  |
|  texlive-framed  |
|  texlive-framed-doc  |
|  texlive-garuda-c90  |
|  texlive-geometry  |
|  texlive-geometry-doc  |
|  texlive-glyphlist  |
|  texlive-graphics  |
|  texlive-graphics-doc  |
|  texlive-gsftopk  |
|  texlive-gsftopk-bin  |
|  texlive-helvetic  |
|  texlive-hyperref  |
|  texlive-hyperref-doc  |
|  texlive-hyph-utf8  |
|  texlive-hyph-utf8-doc  |
|  texlive-hyphen-base  |
|  texlive-hyphenat  |
|  texlive-hyphenat-doc  |
|  texlive-ifetex  |
|  texlive-ifetex-doc  |
|  texlive-ifluatex  |
|  texlive-ifluatex-doc  |
|  texlive-ifmtarg  |
|  texlive-ifmtarg-doc  |
|  texlive-ifoddpage  |
|  texlive-ifoddpage-doc  |
|  texlive-iftex  |
|  texlive-iftex-doc  |
|  texlive-ifxetex  |
|  texlive-ifxetex-doc  |
|  texlive-index  |
|  texlive-index-doc  |
|  texlive-jadetex  |
|  texlive-jadetex-bin  |
|  texlive-jadetex-doc  |
|  texlive-jknapltx  |
|  texlive-jknapltx-doc  |
|  texlive-kastrup  |
|  texlive-kastrup-doc  |
|  texlive-kerkis  |
|  texlive-kerkis-doc  |
|  texlive-koma-script  |
|  texlive-kpathsea  |
|  texlive-kpathsea-bin  |
|  texlive-kpathsea-doc  |
|  texlive-kpathsea-lib  |
|  texlive-kpathsea-lib-devel  |
|  texlive-l3experimental  |
|  texlive-l3experimental-doc  |
|  texlive-l3kernel  |
|  texlive-l3kernel-doc  |
|  texlive-l3packages  |
|  texlive-l3packages-doc  |
|  texlive-lastpage  |
|  texlive-lastpage-doc  |
|  texlive-latex  |
|  texlive-latex-bin  |
|  texlive-latex-bin-bin  |
|  texlive-latex-doc  |
|  texlive-latex-fonts  |
|  texlive-latex-fonts-doc  |
|  texlive-latexconfig  |
|  texlive-lettrine  |
|  texlive-lettrine-doc  |
|  texlive-listings  |
|  texlive-listings-doc  |
|  texlive-lm  |
|  texlive-lm-doc  |
|  texlive-lm-math  |
|  texlive-lm-math-doc  |
|  texlive-ltxmisc  |
|  texlive-lua-alt-getopt  |
|  texlive-lua-alt-getopt-doc  |
|  texlive-lualatex-math  |
|  texlive-lualatex-math-doc  |
|  texlive-luaotfload  |
|  texlive-luaotfload-bin  |
|  texlive-luaotfload-doc  |
|  texlive-luatex  |
|  texlive-luatex-bin  |
|  texlive-luatex-doc  |
|  texlive-luatexbase  |
|  texlive-luatexbase-doc  |
|  texlive-makecmds  |
|  texlive-makecmds-doc  |
|  texlive-makeindex  |
|  texlive-makeindex-bin  |
|  texlive-makeindex-doc  |
|  texlive-marginnote  |
|  texlive-marginnote-doc  |
|  texlive-marvosym  |
|  texlive-marvosym-doc  |
|  texlive-mathpazo  |
|  texlive-mathpazo-doc  |
|  texlive-mathspec  |
|  texlive-mathspec-doc  |
|  texlive-mdwtools  |
|  texlive-mdwtools-doc  |
|  texlive-memoir  |
|  texlive-memoir-doc  |
|  texlive-metafont  |
|  texlive-metafont-bin  |
|  texlive-metalogo  |
|  texlive-metalogo-doc  |
|  texlive-metapost  |
|  texlive-metapost-bin  |
|  texlive-metapost-doc  |
|  texlive-metapost-examples-doc  |
|  texlive-mflogo  |
|  texlive-mflogo-doc  |
|  texlive-mfnfss  |
|  texlive-mfnfss-doc  |
|  texlive-mfware  |
|  texlive-mfware-bin  |
|  texlive-mh  |
|  texlive-mh-doc  |
|  texlive-microtype  |
|  texlive-microtype-doc  |
|  texlive-misc  |
|  texlive-mnsymbol  |
|  texlive-mnsymbol-doc  |
|  texlive-mparhack  |
|  texlive-mparhack-doc  |
|  texlive-mptopdf  |
|  texlive-mptopdf-bin  |
|  texlive-ms  |
|  texlive-ms-doc  |
|  texlive-multido  |
|  texlive-multido-doc  |
|  texlive-multirow  |
|  texlive-multirow-doc  |
|  texlive-natbib  |
|  texlive-natbib-doc  |
|  texlive-ncctools  |
|  texlive-ncctools-doc  |
|  texlive-ncntrsbk  |
|  texlive-norasi-c90  |
|  texlive-ntgclass  |
|  texlive-ntgclass-doc  |
|  texlive-oberdiek  |
|  texlive-oberdiek-doc  |
|  texlive-overpic  |
|  texlive-overpic-doc  |
|  texlive-palatino  |
|  texlive-paralist  |
|  texlive-paralist-doc  |
|  texlive-parallel  |
|  texlive-parallel-doc  |
|  texlive-parskip  |
|  texlive-parskip-doc  |
|  texlive-passivetex  |
|  texlive-pdfpages  |
|  texlive-pdfpages-doc  |
|  texlive-pdftex  |
|  texlive-pdftex-bin  |
|  texlive-pdftex-def  |
|  texlive-pdftex-doc  |
|  texlive-pgf  |
|  texlive-pgf-doc  |
|  texlive-philokalia  |
|  texlive-philokalia-doc  |
|  texlive-placeins  |
|  texlive-placeins-doc  |
|  texlive-plain  |
|  texlive-polyglossia  |
|  texlive-polyglossia-doc  |
|  texlive-powerdot  |
|  texlive-powerdot-doc  |
|  texlive-preprint  |
|  texlive-preprint-doc  |
|  texlive-psfrag  |
|  texlive-psfrag-doc  |
|  texlive-pslatex  |
|  texlive-psnfss  |
|  texlive-psnfss-doc  |
|  texlive-pspicture  |
|  texlive-pspicture-doc  |
|  texlive-pst-3d  |
|  texlive-pst-3d-doc  |
|  texlive-pst-blur  |
|  texlive-pst-blur-doc  |
|  texlive-pst-coil  |
|  texlive-pst-coil-doc  |
|  texlive-pst-eps  |
|  texlive-pst-eps-doc  |
|  texlive-pst-fill  |
|  texlive-pst-fill-doc  |
|  texlive-pst-grad  |
|  texlive-pst-grad-doc  |
|  texlive-pst-math  |
|  texlive-pst-math-doc  |
|  texlive-pst-node  |
|  texlive-pst-node-doc  |
|  texlive-pst-plot  |
|  texlive-pst-plot-doc  |
|  texlive-pst-slpe  |
|  texlive-pst-slpe-doc  |
|  texlive-pst-text  |
|  texlive-pst-text-doc  |
|  texlive-pst-tree  |
|  texlive-pst-tree-doc  |
|  texlive-pstricks  |
|  texlive-pstricks-add  |
|  texlive-pstricks-add-doc  |
|  texlive-pstricks-doc  |
|  texlive-ptext  |
|  texlive-ptext-doc  |
|  texlive-pxfonts  |
|  texlive-pxfonts-doc  |
|  texlive-qstest  |
|  texlive-qstest-doc  |
|  texlive-rcs  |
|  texlive-rcs-doc  |
|  texlive-realscripts  |
|  texlive-realscripts-doc  |
|  texlive-rotating  |
|  texlive-rotating-doc  |
|  texlive-rsfs  |
|  texlive-rsfs-doc  |
|  texlive-sansmath  |
|  texlive-sansmath-doc  |
|  texlive-sauerj  |
|  texlive-sauerj-doc  |
|  texlive-scheme-basic  |
|  texlive-section  |
|  texlive-section-doc  |
|  texlive-sectsty  |
|  texlive-sectsty-doc  |
|  texlive-seminar  |
|  texlive-seminar-doc  |
|  texlive-sepnum  |
|  texlive-sepnum-doc  |
|  texlive-setspace  |
|  texlive-setspace-doc  |
|  texlive-showexpl  |
|  texlive-showexpl-doc  |
|  texlive-soul  |
|  texlive-soul-doc  |
|  texlive-stmaryrd  |
|  texlive-stmaryrd-doc  |
|  texlive-subfig  |
|  texlive-subfig-doc  |
|  texlive-subfigure  |
|  texlive-subfigure-doc  |
|  texlive-svn-prov  |
|  texlive-svn-prov-doc  |
|  texlive-symbol  |
|  texlive-t2  |
|  texlive-t2-doc  |
|  texlive-tetex  |
|  texlive-tetex-bin  |
|  texlive-tetex-doc  |
|  texlive-tex  |
|  texlive-tex-bin  |
|  texlive-tex-gyre  |
|  texlive-tex-gyre-doc  |
|  texlive-tex-gyre-math  |
|  texlive-tex-gyre-math-doc  |
|  texlive-tex4ht  |
|  texlive-tex4ht-bin  |
|  texlive-tex4ht-doc  |
|  texlive-texconfig  |
|  texlive-texconfig-bin  |
|  texlive-texlive.infra  |
|  texlive-texlive.infra-bin  |
|  texlive-texlive.infra-doc  |
|  texlive-textcase  |
|  texlive-textcase-doc  |
|  texlive-textpos  |
|  texlive-textpos-doc  |
|  texlive-thailatex  |
|  texlive-thailatex-doc  |
|  texlive-threeparttable  |
|  texlive-threeparttable-doc  |
|  texlive-thumbpdf  |
|  texlive-thumbpdf-bin  |
|  texlive-thumbpdf-doc  |
|  texlive-times  |
|  texlive-tipa  |
|  texlive-tipa-doc  |
|  texlive-titlesec  |
|  texlive-titlesec-doc  |
|  texlive-titling  |
|  texlive-titling-doc  |
|  texlive-tocloft  |
|  texlive-tocloft-doc  |
|  texlive-tools  |
|  texlive-tools-doc  |
|  texlive-txfonts  |
|  texlive-txfonts-doc  |
|  texlive-type1cm  |
|  texlive-type1cm-doc  |
|  texlive-typehtml  |
|  texlive-typehtml-doc  |
|  texlive-ucharclasses  |
|  texlive-ucharclasses-doc  |
|  texlive-ucs  |
|  texlive-ucs-doc  |
|  texlive-uhc  |
|  texlive-uhc-doc  |
|  texlive-ulem  |
|  texlive-ulem-doc  |
|  texlive-underscore  |
|  texlive-underscore-doc  |
|  texlive-unicode-math  |
|  texlive-unicode-math-doc  |
|  texlive-unisugar  |
|  texlive-unisugar-doc  |
|  texlive-url  |
|  texlive-url-doc  |
|  texlive-utopia  |
|  texlive-utopia-doc  |
|  texlive-varwidth  |
|  texlive-varwidth-doc  |
|  texlive-wadalab  |
|  texlive-wadalab-doc  |
|  texlive-was  |
|  texlive-was-doc  |
|  texlive-wasy  |
|  texlive-wasy-doc  |
|  texlive-wasysym  |
|  texlive-wasysym-doc  |
|  texlive-wrapfig  |
|  texlive-wrapfig-doc  |
|  texlive-xcolor  |
|  texlive-xcolor-doc  |
|  texlive-xdvi  |
|  texlive-xdvi-bin  |
|  texlive-xecjk  |
|  texlive-xecjk-doc  |
|  texlive-xecolor  |
|  texlive-xecolor-doc  |
|  texlive-xecyr  |
|  texlive-xecyr-doc  |
|  texlive-xeindex  |
|  texlive-xeindex-doc  |
|  texlive-xepersian  |
|  texlive-xepersian-doc  |
|  texlive-xesearch  |
|  texlive-xesearch-doc  |
|  texlive-xetex  |
|  texlive-xetex-bin  |
|  texlive-xetex-def  |
|  texlive-xetex-doc  |
|  texlive-xetex-itrans  |
|  texlive-xetex-itrans-doc  |
|  texlive-xetex-pstricks  |
|  texlive-xetex-pstricks-doc  |
|  texlive-xetex-tibetan  |
|  texlive-xetex-tibetan-doc  |
|  texlive-xetexconfig  |
|  texlive-xetexfontinfo  |
|  texlive-xetexfontinfo-doc  |
|  texlive-xifthen  |
|  texlive-xifthen-doc  |
|  texlive-xkeyval  |
|  texlive-xkeyval-doc  |
|  texlive-xltxtra  |
|  texlive-xltxtra-doc  |
|  texlive-xmltex  |
|  texlive-xmltex-bin  |
|  texlive-xmltex-doc  |
|  texlive-xstring  |
|  texlive-xstring-doc  |
|  texlive-xtab  |
|  texlive-xtab-doc  |
|  texlive-xunicode  |
|  texlive-xunicode-doc  |
|  texlive-zapfchan  |
|  texlive-zapfding  |
|  tftp  |
|  tftp-server  |
|  tidy  |
|  tidyp  |
|  tig  |
|  tigervnc  |
|  tigervnc-server  |
|  tigervnc-server-module  |
|  time  |
|  tmpwatch  |
|  tmux  |
|  tokyocabinet  |
|  tokyocabinet-devel  |
|  tomcat-native  |
|  tomcat8  |
|  tomcat8-admin-webapps  |
|  tomcat8-docs-webapp  |
|  tomcat8-el-3.0-api  |
|  tomcat8-javadoc  |
|  tomcat8-jsp-2.3-api  |
|  tomcat8-lib  |
|  tomcat8-log4j  |
|  tomcat8-servlet-3.1-api  |
|  tomcat8-webapps  |
|  traceroute  |
|  transfig  |
|  tre  |
|  tre-common  |
|  tre-devel  |
|  tree  |
|  trousers  |
|  trousers-devel  |
|  trousers-static  |
|  ttmkfdir  |
|  tunctl  |
|  turbojpeg  |
|  turbojpeg-devel  |
|  tzdata  |
|  tzdata-java  |
|  uClibc-devel  |
|  udev  |
|  udftools  |
|  unbound  |
|  unbound-devel  |
|  unbound-libs  |
|  unbound-python  |
|  unicode-ucd  |
|  unifdef  |
|  units  |
|  unix2dos  |
|  unixODBC  |
|  unixODBC-devel  |
|  unzip  |
|  update-motd  |
|  upstart  |
|  urlview  |
|  urw-fonts  |
|  usbutils  |
|  usermode  |
|  ustr  |
|  ustr-debug  |
|  ustr-debug-static  |
|  ustr-devel  |
|  ustr-static  |
|  util-linux  |
|  uuid  |
|  uuid-c\+\+  |
|  uuid-c\+\+-devel  |
|  uuid-dce  |
|  uuid-dce-devel  |
|  uuid-devel  |
|  uuid-perl  |
|  uuid-php  |
|  uuid-php56  |
|  uuidd  |
|  valgrind  |
|  valgrind-devel  |
|  valgrind-openmpi  |
|  varnish  |
|  varnish-docs  |
|  varnish-libs  |
|  varnish-libs-devel  |
|  vconfig  |
|  velocity  |
|  velocity-demo  |
|  velocity-javadoc  |
|  velocity-manual  |
|  veritysetup  |
|  vim-common  |
|  vim-data  |
|  vim-enhanced  |
|  vim-filesystem  |
|  vim-minimal  |
|  virt-what  |
|  VirtualGL  |
|  VirtualGL-devel  |
|  vlgothic-fonts  |
|  vlgothic-fonts-common  |
|  vlgothic-p-fonts  |
|  vlock  |
|  vorbis-tools  |
|  vpnc  |
|  vpnc-consoleuser  |
|  vsftpd  |
|  w3m  |
|  watchdog  |
|  werken-xpath  |
|  werken-xpath-javadoc  |
|  wget  |
|  which  |
|  wireshark  |
|  wireshark-devel  |
|  wodim  |
|  words  |
|  wqy-zenhei-fonts  |
|  wqy-zenhei-fonts-common  |
|  ws-commons-util  |
|  ws-commons-util-javadoc  |
|  wsdl4j  |
|  wsdl4j-javadoc  |
|  x86info  |
|  xalan-j2  |
|  xalan-j2-demo  |
|  xalan-j2-javadoc  |
|  xalan-j2-manual  |
|  xalan-j2-xsltc  |
|  Xaw3d  |
|  Xaw3d-devel  |
|  xcache-admin  |
|  xcb-proto  |
|  xcb-util  |
|  xcb-util-devel  |
|  xcb-util-image  |
|  xcb-util-image-devel  |
|  xcb-util-keysyms  |
|  xcb-util-keysyms-devel  |
|  xcb-util-wm  |
|  xcb-util-wm-devel  |
|  xdelta  |
|  xdelta-devel  |
|  xdoclet  |
|  xdoclet-javadoc  |
|  xdoclet-manual  |
|  xerces-j2  |
|  xerces-j2-demo  |
|  xerces-j2-javadoc-apis  |
|  xerces-j2-javadoc-impl  |
|  xerces-j2-javadoc-other  |
|  xerces-j2-javadoc-xni  |
|  xerces-j2-scripts  |
|  xferstats  |
|  xfsdump  |
|  xfsprogs  |
|  xfsprogs-devel  |
|  xhtml1-dtds  |
|  xhtml2fo-style-xsl  |
|  xinetd  |
|  xjavadoc  |
|  xjavadoc-javadoc  |
|  xkeyboard-config  |
|  xkeyboard-config-devel  |
|  xml-common  |
|  xml-commons-apis  |
|  xml-commons-apis-javadoc  |
|  xml-commons-apis-manual  |
|  xml-commons-resolver  |
|  xml-commons-resolver-javadoc  |
|  xml-stylebook  |
|  xml-stylebook-demo  |
|  xml-stylebook-javadoc  |
|  xmlgraphics-commons  |
|  xmlgraphics-commons-javadoc  |
|  xmlrpc-c  |
|  xmlrpc-c-apps  |
|  xmlrpc-c-c\+\+  |
|  xmlrpc-c-client  |
|  xmlrpc-c-client\+\+  |
|  xmlrpc-c-devel  |
|  xmlsec1  |
|  xmlsec1-devel  |
|  xmlsec1-gcrypt  |
|  xmlsec1-gcrypt-devel  |
|  xmlsec1-gnutls  |
|  xmlsec1-gnutls-devel  |
|  xmlsec1-nss  |
|  xmlsec1-nss-devel  |
|  xmlsec1-openssl  |
|  xmlsec1-openssl-devel  |
|  xmlstarlet  |
|  xmltex  |
|  xmlto  |
|  xmlto-tex  |
|  xmlto-xhtml  |
|  xmltoman  |
|  xorg-x11-apps  |
|  xorg-x11-drv-evdev  |
|  xorg-x11-drv-evdev-devel  |
|  xorg-x11-drv-vesa  |
|  xorg-x11-drv-void  |
|  xorg-x11-font-utils  |
|  xorg-x11-fonts-100dpi  |
|  xorg-x11-fonts-75dpi  |
|  xorg-x11-fonts-cyrillic  |
|  xorg-x11-fonts-ethiopic  |
|  xorg-x11-fonts-ISO8859-1-100dpi  |
|  xorg-x11-fonts-ISO8859-1-75dpi  |
|  xorg-x11-fonts-ISO8859-14-100dpi  |
|  xorg-x11-fonts-ISO8859-14-75dpi  |
|  xorg-x11-fonts-ISO8859-15-100dpi  |
|  xorg-x11-fonts-ISO8859-15-75dpi  |
|  xorg-x11-fonts-ISO8859-2-100dpi  |
|  xorg-x11-fonts-ISO8859-2-75dpi  |
|  xorg-x11-fonts-ISO8859-9-100dpi  |
|  xorg-x11-fonts-ISO8859-9-75dpi  |
|  xorg-x11-fonts-misc  |
|  xorg-x11-fonts-Type1  |
|  xorg-x11-proto-devel  |
|  xorg-x11-server-common  |
|  xorg-x11-server-devel  |
|  xorg-x11-server-source  |
|  xorg-x11-server-utils  |
|  xorg-x11-server-Xdmx  |
|  xorg-x11-server-Xephyr  |
|  xorg-x11-server-Xnest  |
|  xorg-x11-server-Xorg  |
|  xorg-x11-server-Xvfb  |
|  xorg-x11-util-macros  |
|  xorg-x11-utils  |
|  xorg-x11-xauth  |
|  xorg-x11-xbitmaps  |
|  xorg-x11-xdm  |
|  xorg-x11-xinit  |
|  xorg-x11-xkb-extras  |
|  xorg-x11-xkb-utils  |
|  xorg-x11-xkb-utils-devel  |
|  xorg-x11-xtrans-devel  |
|  xrestop  |
|  xterm  |
|  xz  |
|  xz-devel  |
|  xz-libs  |
|  xz-lzma-compat  |
|  yap  |
|  yap-devel  |
|  yap-docs  |
|  yasm  |
|  yasm-devel  |
|  yelp-tools  |
|  yelp-xsl  |
|  yelp-xsl-devel  |
|  yp-tools  |
|  ypbind  |
|  ypserv  |
|  yum  |
|  yum-cron  |
|  yum-cron-daily  |
|  yum-cron-hourly  |
|  yum-cron-security  |
|  yum-metadata-parser  |
|  yum-NetworkManager-dispatcher  |
|  yum-plugin-aliases  |
|  yum-plugin-auto-update-debug-info  |
|  yum-plugin-changelog  |
|  yum-plugin-copr  |
|  yum-plugin-dkms-build-requires  |
|  yum-plugin-fastestmirror  |
|  yum-plugin-filter-data  |
|  yum-plugin-fs-snapshot  |
|  yum-plugin-keys  |
|  yum-plugin-list-data  |
|  yum-plugin-local  |
|  yum-plugin-merge-conf  |
|  yum-plugin-ovl  |
|  yum-plugin-post-transaction-actions  |
|  yum-plugin-pre-transaction-actions  |
|  yum-plugin-priorities  |
|  yum-plugin-protectbase  |
|  yum-plugin-ps  |
|  yum-plugin-puppetverify  |
|  yum-plugin-refresh-updatesd  |
|  yum-plugin-remove-with-leaves  |
|  yum-plugin-rpm-warm-cache  |
|  yum-plugin-show-leaves  |
|  yum-plugin-tmprepo  |
|  yum-plugin-tsflags  |
|  yum-plugin-upgrade-helper  |
|  yum-plugin-verify  |
|  yum-plugin-versionlock  |
|  yum-updateonboot  |
|  yum-updatesd  |
|  yum-utils  |
|  zbar  |
|  zbar-devel  |
|  zerofree  |
|  zip  |
|  zisofs-tools  |
|  zlib  |
|  zlib-devel  |
|  zlib-static  |
|  zsh  |
|  zsh-html  |
|  zziplib  |
|  zziplib-devel  |
|  zziplib-utils  |

## aws-apitools-\* packages deprecated March 1, 2017
<a name="support-info-by-support-statement-eol_aws-apitools-common"></a>
+ Start Date: 2017-03-01
+ End Date:

The following packages were superseded by the AWS CLI.

### Packages
<a name="support-info-by-support-statement-packages-eol_aws-apitools-common"></a>

| Package | Note |
| --- | --- |
|  aws-apitools-as  | Upstream EOL for aws-apitools-\* (aws-apitools-common) is 2017-03-01 |
|  aws-apitools-cfn  | Upstream EOL for aws-apitools-\* (aws-apitools-common) is 2017-03-01 |
|  aws-apitools-common  | Upstream EOL for aws-apitools-\* (aws-apitools-common) is 2017-03-01 |
|  aws-apitools-ec2  | Upstream EOL for aws-apitools-\* (aws-apitools-common) is 2017-03-01 |
|  aws-apitools-elb  | Upstream EOL for aws-apitools-\* (aws-apitools-common) is 2017-03-01 |
|  aws-apitools-iam  | Upstream EOL for aws-apitools-\* (aws-apitools-common) is 2017-03-01 |
|  aws-apitools-mon  | Upstream EOL for aws-apitools-\* (aws-apitools-common) is 2017-03-01 |
|  aws-apitools-rds  | Upstream EOL for aws-apitools-\* (aws-apitools-common) is 2017-03-01 |

## Backwards compatibility packages
<a name="support-info-by-support-statement-compat"></a>
+ Start Date:
+ End Date:

 The following packages are provided only for binary compatibility with previous Amazon Linux versions and do not receive security updates. For more information, see [Amazon Linux AMI FAQs](https://aws.amazon.com/amazon-linux-ami/faqs/).

### Packages
<a name="support-info-by-support-statement-packages-compat"></a>

| Package |
| --- |
|  boost141-graph  |
|  boost141-graph-mpich2  |
|  boost141-graph-openmpi  |
|  boost141-mpich2  |
|  boost141-mpich2-python  |
|  boost141-openmpi  |
|  boost141-openmpi-python  |
|  boost141-regex  |
|  cloog-ppl  |
|  compat-audit  |
|  compat-boost  |
|  compat-boost-date-time  |
|  compat-boost-filesystem  |
|  compat-boost-graph  |
|  compat-boost-iostreams  |
|  compat-boost-mpich2  |
|  compat-boost-openmpi  |
|  compat-boost-program-options  |
|  compat-boost-python  |
|  compat-boost-regex  |
|  compat-boost-serialization  |
|  compat-boost-signals  |
|  compat-boost-system  |
|  compat-boost-test  |
|  compat-boost-thread  |
|  compat-boost-wave  |
|  compat-expat1  |
|  compat-gmp4  |
|  compat-ImageMagick  |
|  compat-iptables  |
|  compat-libcap1  |
|  compat-libevent  |
|  compat-libffi5  |
|  compat-libicu4  |
|  compat-libmpc0  |
|  compat-libstdc\+\+-33  |
|  compat-libtermcap  |
|  compat-libtiff3  |
|  compat-mpfr2  |
|  compat-mpich-devel  |
|  compat-mpich-doc  |
|  compat-openldap  |
|  compat-openmpi  |
|  compat-openmpi-devel  |
|  compat-openmpi-psm  |
|  compat-openmpi-psm-devel  |
|  compat-openmpi16  |
|  compat-openmpi16-devel  |
|  compat-protobuf  |
|  compat-readline5  |
|  compat-readline5-devel  |
|  compat-readline5-static  |
|  netpbm-progs  |
|  openssl098e  |
|  openswan  |
|  pl  |
|  ppl  |
|  ppl-gprolog  |
|  ppl-swiprolog  |
|  ppl-utils  |
|  ppl-yap  |
|  xz-compat-libs  |

## Packages that are EOL as of January 1, 2020
<a name="support-info-by-support-statement-eol202001"></a>
+ Start Date: 2020-01-20
+ End Date:

 The following packages will no longer receive updates, as announced with AL1 maintenance support. This matches their upstream EOL. For more information, see [Amazon Linux AMI FAQs](https://aws.amazon.com/amazon-linux-ami/faqs/).

### Packages
<a name="support-info-by-support-statement-packages-eol202001"></a>

| Package | Note |
| --- | --- |
|  apcu71-panel  | Part of upstream EOL for php71 |
|  bzr-common  | Part of upstream EOL for bzr-python27 |
|  bzr-doc-python27  | Part of upstream EOL for bzr-python27 |
|  bzr-fastimport-python27  | Part of upstream EOL for bzr-python27 |
|  bzr-python27  | Part of upstream EOL for bzr-python27 |
|  collectd-gmond  | Part of upstream EOL for ganglia |
|  emacs-mercurial  | AL1 EOL for mercurial-python27 |
|  emacs-mercurial-el  | AL1 EOL for mercurial-python27 |
|  ganglia  | Part of upstream EOL for ganglia |
|  ganglia-devel  | Part of upstream EOL for ganglia |
|  ganglia-gmetad  | Part of upstream EOL for ganglia |
|  ganglia-gmond  | Part of upstream EOL for ganglia |
|  ganglia-gmond-python  | Part of upstream EOL for ganglia |
|  ganglia-web  | Part of upstream EOL for PHP 5.3 |
|  git-svn  | Part of upstream EOL for Subversion 1.9 |
|  liblibdbi-dbd-mysql  | The AL1 libdbi-dbd-mysql package links to old MySQL libraries, and as such will no longer receive security updates beyond end 2020. |
|  mercurial-common  | AL1 EOL for mercurial-python27 |
|  mercurial-python27  | AL1 EOL for mercurial-python27 |
|  mod24\_wsgi-python34  | Part of upstream EOL for python34 |
|  mod24\_wsgi-python35  | Part of upstream EOL for python35 |
|  nagios  | Part of upstream EOL for PHP 5.3 |
|  php  | Part of upstream EOL for PHP 5.3 |
|  php-amazon-sdk  | Part of upstream EOL for PHP 5.3 |
|  php-amazon-sdk2  | Part of upstream EOL for PHP 5.3 |
|  php-bcmath  | Part of upstream EOL for PHP 5.3 |
|  php-channel-amazon  | Part of upstream EOL for PHP 5.3 |
|  php-channel-doctrine  | Part of upstream EOL for PHP 5.3 |
|  php-channel-ezc  | Part of upstream EOL for PHP 5.3 |
|  php-channel-guzzle  | Part of upstream EOL for PHP 5.3 |
|  php-channel-pearhub  | Part of upstream EOL for PHP 5.3 |
|  php-channel-phpunit  | Part of upstream EOL for PHP 5.3 |
|  php-channel-swift  | Part of upstream EOL for PHP 5.3 |
|  php-channel-symfony  | Part of upstream EOL for PHP 5.3 |
|  php-channel-symfony2  | Part of upstream EOL for PHP 5.3 |
|  php-cli  | Part of upstream EOL for PHP 5.3 |
|  php-dba  | Part of upstream EOL for PHP 5.3 |
|  php-devel  | Part of upstream EOL for PHP 5.3 |
|  php-doctrine-Doctrine  | Part of upstream EOL for PHP 5.3 |
|  php-embedded  | Part of upstream EOL for PHP 5.3 |
|  php-enchant  | Part of upstream EOL for PHP 5.3 |
|  php-ezc-Base  | Part of upstream EOL for PHP 5.3 |
|  php-ezc-ConsoleTools  | Part of upstream EOL for PHP 5.3 |
|  php-fpm  | Part of upstream EOL for PHP 5.3 |
|  php-gd  | Part of upstream EOL for PHP 5.3 |
|  php-guzzle-Guzzle  | Part of upstream EOL for PHP 5.3 |
|  php-imap  | Part of upstream EOL for PHP 5.3 |
|  php-intl  | Part of upstream EOL for PHP 5.3 |
|  php-ldap  | Part of upstream EOL for PHP 5.3 |
|  php-libpuzzle  | Part of upstream EOL for PHP 5.3 |
|  php-mbstring  | Part of upstream EOL for PHP 5.3 |
|  php-mcrypt  | Part of upstream EOL for PHP 5.3 |
|  php-Monolog  | Part of upstream EOL for PHP 5.3 |
|  php-Monolog-amqp  | Part of upstream EOL for PHP 5.3 |
|  php-Monolog-raven  | Part of upstream EOL for PHP 5.3 |
|  php-mssql  | Part of upstream EOL for PHP 5.3 |
|  php-mysql  | Part of upstream EOL for PHP 5.3 |
|  php-mysqlnd  | Part of upstream EOL for PHP 5.3 |
|  php-odbc  | Part of upstream EOL for PHP 5.3 |
|  php-pdo  | Part of upstream EOL for PHP 5.3 |
|  php-pear  | Part of upstream EOL for PHP 5.3 |
|  php-pear-Auth-SASL  | Part of upstream EOL for PHP 5.3 |
|  php-pear-Cache-Lite  | Part of upstream EOL for PHP 5.3 |
|  php-pear-DB  | Part of upstream EOL for PHP 5.3 |
|  php-pear-HTTP-OAuth  | Part of upstream EOL for PHP 5.3 |
|  php-pear-HTTP-Request2  | Part of upstream EOL for PHP 5.3 |
|  php-pear-Log  | Part of upstream EOL for PHP 5.3 |
|  php-pear-Mail  | Part of upstream EOL for PHP 5.3 |
|  php-pear-MDB2  | Part of upstream EOL for PHP 5.3 |
|  php-pear-Net-SMTP  | Part of upstream EOL for PHP 5.3 |
|  php-pear-Net-Socket  | Part of upstream EOL for PHP 5.3 |
|  php-pear-Net-URL2  | Part of upstream EOL for PHP 5.3 |
|  php-pear-XML-RPC2  | Part of upstream EOL for PHP 5.3 |
|  php-pearhub-Monolog  | Part of upstream EOL for PHP 5.3 |
|  php-pecl-amqp  | Part of upstream EOL for PHP 5.3 |
|  php-pecl-apc  | Part of upstream EOL for PHP 5.3 |
|  php-pecl-apc-devel  | Part of upstream EOL for PHP 5.3 |
|  php-pecl-igbinary  | Part of upstream EOL for PHP 5.3 |
|  php-pecl-igbinary-devel  | Part of upstream EOL for PHP 5.3 |
|  php-pecl-imagick  | Part of upstream EOL for PHP 5.3 |
|  php-pecl-memcache  | Part of upstream EOL for PHP 5.3 |
|  php-pecl-memcached  | Part of upstream EOL for PHP 5.3 |
|  php-pecl-oauth  | Part of upstream EOL for PHP 5.3 |
|  php-pecl-ssh2  | Part of upstream EOL for PHP 5.3 |
|  php-pecl-xdebug  | Part of upstream EOL for PHP 5.3 |
|  php-pgsql  | Part of upstream EOL for PHP 5.3 |
|  php-phpunit-DbUnit  | Part of upstream EOL for PHP 5.3 |
|  php-phpunit-File-Iterator  | Part of upstream EOL for PHP 5.3 |
|  php-phpunit-PHP-CodeCoverage  | Part of upstream EOL for PHP 5.3 |
|  php-phpunit-PHP-Invoker  | Part of upstream EOL for PHP 5.3 |
|  php-phpunit-PHP-Timer  | Part of upstream EOL for PHP 5.3 |
|  php-phpunit-PHP-TokenStream  | Part of upstream EOL for PHP 5.3 |
|  php-phpunit-PHPUnit  | Part of upstream EOL for PHP 5.3 |
|  php-phpunit-PHPUnit-MockObject  | Part of upstream EOL for PHP 5.3 |
|  php-phpunit-PHPUnit-Selenium  | Part of upstream EOL for PHP 5.3 |
|  php-phpunit-Text-Template  | Part of upstream EOL for PHP 5.3 |
|  php-process  | Part of upstream EOL for PHP 5.3 |
|  php-pspell  | Part of upstream EOL for PHP 5.3 |
|  php-PsrLog  | Part of upstream EOL for PHP 5.3 |
|  php-Raven  | Part of upstream EOL for PHP 5.3 |
|  php-Raven-tests  | Part of upstream EOL for PHP 5.3 |
|  php-recode  | Part of upstream EOL for PHP 5.3 |
|  php-snmp  | Part of upstream EOL for PHP 5.3 |
|  php-soap  | Part of upstream EOL for PHP 5.3 |
|  php-swift-Swift  | Part of upstream EOL for PHP 5.3 |
|  php-symfony-YAML  | Part of upstream EOL for PHP 5.3 |
|  php-symfony2-Config  | Part of upstream EOL for PHP 5.3 |
|  php-symfony2-DependencyInjection  | Part of upstream EOL for PHP 5.3 |
|  php-symfony2-EventDispatcher  | Part of upstream EOL for PHP 5.3 |
|  php-symfony2-Yaml  | Part of upstream EOL for PHP 5.3 |
|  php-tidy  | Part of upstream EOL for PHP 5.3 |
|  php-xcache  | Part of upstream EOL for PHP 5.3 |
|  php-xml  | Part of upstream EOL for PHP 5.3 |
|  php-xmlrpc  | Part of upstream EOL for PHP 5.3 |
|  php-ZendFramework  | Part of upstream EOL for PHP 5.3 |
|  php-ZendFramework-Auth-Adapter-Ldap  | Part of upstream EOL for PHP 5.3 |
|  php-ZendFramework-Cache-Backend-Apc  | Part of upstream EOL for PHP 5.3 |
|  php-ZendFramework-Cache-Backend-Libmemcached  | Part of upstream EOL for PHP 5.3 |
|  php-ZendFramework-Cache-Backend-Memcached  | Part of upstream EOL for PHP 5.3 |
|  php-ZendFramework-Captcha  | Part of upstream EOL for PHP 5.3 |
|  php-ZendFramework-Db-Adapter-Mysqli  | Part of upstream EOL for PHP 5.3 |
|  php-ZendFramework-Db-Adapter-Pdo  | Part of upstream EOL for PHP 5.3 |
|  php-ZendFramework-Db-Adapter-Pdo-Mssql  | Part of upstream EOL for PHP 5.3 |
|  php-ZendFramework-Db-Adapter-Pdo-Mysql  | Part of upstream EOL for PHP 5.3 |
|  php-ZendFramework-Db-Adapter-Pdo-Pgsql  | Part of upstream EOL for PHP 5.3 |
|  php-ZendFramework-demos  | Part of upstream EOL for PHP 5.3 |
|  php-ZendFramework-Dojo  | Part of upstream EOL for PHP 5.3 |
|  php-ZendFramework-extras  | Part of upstream EOL for PHP 5.3 |
|  php-ZendFramework-Feed  | Part of upstream EOL for PHP 5.3 |
|  php-ZendFramework-full  | Part of upstream EOL for PHP 5.3 |
|  php-ZendFramework-Ldap  | Part of upstream EOL for PHP 5.3 |
|  php-ZendFramework-Pdf  | Part of upstream EOL for PHP 5.3 |
|  php-ZendFramework-Search-Lucene  | Part of upstream EOL for PHP 5.3 |
|  php-ZendFramework-Serializer-Adapter-Igbinary  | Part of upstream EOL for PHP 5.3 |
|  php-ZendFramework-Services  | Part of upstream EOL for PHP 5.3 |
|  php-ZendFramework-Soap  | Part of upstream EOL for PHP 5.3 |
|  php55  | Part of upstream EOL for php55 |
|  php55-bcmath  | Part of upstream EOL for php55 |
|  php55-cli  | Part of upstream EOL for php55 |
|  php55-common  | Part of upstream EOL for php55 |
|  php55-dba  | Part of upstream EOL for php55 |
|  php55-devel  | Part of upstream EOL for php55 |
|  php55-embedded  | Part of upstream EOL for php55 |
|  php55-enchant  | Part of upstream EOL for php55 |
|  php55-fpm  | Part of upstream EOL for php55 |
|  php55-gd  | Part of upstream EOL for php55 |
|  php55-gmp  | Part of upstream EOL for php55 |
|  php55-imap  | Part of upstream EOL for php55 |
|  php55-intl  | Part of upstream EOL for php55 |
|  php55-ldap  | Part of upstream EOL for php55 |
|  php55-mbstring  | Part of upstream EOL for php55 |
|  php55-mcrypt  | Part of upstream EOL for php55 |
|  php55-mssql  | Part of upstream EOL for php55 |
|  php55-mysqlnd  | Part of upstream EOL for php55 |
|  php55-odbc  | Part of upstream EOL for php55 |
|  php55-opcache  | Part of upstream EOL for php55 |
|  php55-pdo  | Part of upstream EOL for php55 |
|  php55-pecl-apc  | Part of upstream EOL for php55 |
|  php55-pecl-apc-devel  | Part of upstream EOL for php55 |
|  php55-pecl-apcu  | Part of upstream EOL for php55 |
|  php55-pecl-apcu-devel  | Part of upstream EOL for php55 |
|  php55-pecl-http  | Part of upstream EOL for php55 |
|  php55-pecl-http-devel  | Part of upstream EOL for php55 |
|  php55-pecl-igbinary  | Part of upstream EOL for php55 |
|  php55-pecl-igbinary-devel  | Part of upstream EOL for php55 |
|  php55-pecl-imagick  | Part of upstream EOL for php55 |
|  php55-pecl-jsonc  | Part of upstream EOL for php55 |
|  php55-pecl-jsonc-devel  | Part of upstream EOL for php55 |
|  php55-pecl-memcache  | Part of upstream EOL for php55 |
|  php55-pecl-memcached  | Part of upstream EOL for php55 |
|  php55-pecl-oauth  | Part of upstream EOL for php55 |
|  php55-pecl-propro  | Part of upstream EOL for php55 |
|  php55-pecl-propro-devel  | Part of upstream EOL for php55 |
|  php55-pecl-raphf  | Part of upstream EOL for php55 |
|  php55-pecl-raphf-devel  | Part of upstream EOL for php55 |
|  php55-pecl-redis  | Part of upstream EOL for php55 |
|  php55-pecl-ssh2  | Part of upstream EOL for php55 |
|  php55-pecl-xdebug  | Part of upstream EOL for php55 |
|  php55-pgsql  | Part of upstream EOL for php55 |
|  php55-process  | Part of upstream EOL for php55 |
|  php55-pspell  | Part of upstream EOL for php55 |
|  php55-recode  | Part of upstream EOL for php55 |
|  php55-snmp  | Part of upstream EOL for php55 |
|  php55-soap  | Part of upstream EOL for php55 |
|  php55-tidy  | Part of upstream EOL for php55 |
|  php55-xml  | Part of upstream EOL for php55 |
|  php55-xmlrpc  | Part of upstream EOL for php55 |
|  php71  | Part of upstream EOL for php71 |
|  php71-bcmath  | Part of upstream EOL for php71 |
|  php71-cli  | Part of upstream EOL for php71 |
|  php71-common  | Part of upstream EOL for php71 |
|  php71-dba  | Part of upstream EOL for php71 |
|  php71-dbg  | Part of upstream EOL for php71 |
|  php71-devel  | Part of upstream EOL for php71 |
|  php71-embedded  | Part of upstream EOL for php71 |
|  php71-enchant  | Part of upstream EOL for php71 |
|  php71-fpm  | Part of upstream EOL for php71 |
|  php71-gd  | Part of upstream EOL for php71 |
|  php71-gmp  | Part of upstream EOL for php71 |
|  php71-imap  | Part of upstream EOL for php71 |
|  php71-intl  | Part of upstream EOL for php71 |
|  php71-json  | Part of upstream EOL for php71 |
|  php71-ldap  | Part of upstream EOL for php71 |
|  php71-mbstring  | Part of upstream EOL for php71 |
|  php71-mcrypt  | Part of upstream EOL for php71 |
|  php71-mysqlnd  | Part of upstream EOL for php71 |
|  php71-odbc  | Part of upstream EOL for php71 |
|  php71-opcache  | Part of upstream EOL for php71 |
|  php71-pdo  | Part of upstream EOL for php71 |
|  php71-pdo-dblib  | Part of upstream EOL for php71 |
|  php71-pecl-apcu  | Part of upstream EOL for php71 |
|  php71-pecl-apcu-devel  | Part of upstream EOL for php71 |
|  php71-pecl-http  | Part of upstream EOL for php71 |
|  php71-pecl-http-devel  | Part of upstream EOL for php71 |
|  php71-pecl-igbinary  | Part of upstream EOL for php71 |
|  php71-pecl-igbinary-devel  | Part of upstream EOL for php71 |
|  php71-pecl-imagick  | Part of upstream EOL for php71 |
|  php71-pecl-imagick-devel  | Part of upstream EOL for php71 |
|  php71-pecl-memcache  | Part of upstream EOL for php71 |
|  php71-pecl-memcached  | Part of upstream EOL for php71 |
|  php71-pecl-oauth  | Part of upstream EOL for php71 |
|  php71-pecl-propro  | Part of upstream EOL for php71 |
|  php71-pecl-propro-devel  | Part of upstream EOL for php71 |
|  php71-pecl-raphf  | Part of upstream EOL for php71 |
|  php71-pecl-raphf-devel  | Part of upstream EOL for php71 |
|  php71-pecl-redis  | Part of upstream EOL for php71 |
|  php71-pecl-ssh2  | Part of upstream EOL for php71 |
|  php71-pecl-xdebug  | Part of upstream EOL for php71 |
|  php71-pgsql  | Part of upstream EOL for php71 |
|  php71-process  | Part of upstream EOL for php71 |
|  php71-pspell  | Part of upstream EOL for php71 |
|  php71-recode  | Part of upstream EOL for php71 |
|  php71-snmp  | Part of upstream EOL for php71 |
|  php71-soap  | Part of upstream EOL for php71 |
|  php71-tidy  | Part of upstream EOL for php71 |
|  php71-xml  | Part of upstream EOL for php71 |
|  php71-xmlrpc  | Part of upstream EOL for php71 |
|  postgresql93  | Part of upstream EOL for postgresql93 |
|  postgresql93-contrib  | Part of upstream EOL for postgresql93 |
|  postgresql93-devel  | Part of upstream EOL for postgresql93 |
|  postgresql93-docs  | Part of upstream EOL for postgresql93 |
|  postgresql93-libs  | Part of upstream EOL for postgresql93 |
|  postgresql93-plperl  | Part of upstream EOL for postgresql93 |
|  postgresql93-plpython26  | Part of upstream EOL for postgresql93 |
|  postgresql93-plpython27  | Part of upstream EOL for postgresql93 |
|  postgresql93-pltcl  | Part of upstream EOL for postgresql93 |
|  postgresql93-server  | Part of upstream EOL for postgresql93 |
|  postgresql93-test  | Part of upstream EOL for postgresql93 |
|  puppet  | Part of upstream EOL for Puppet 2.7 |
|  puppet-server  | Part of upstream EOL for Puppet 2.7 |
|  puppet3  | Part of upstream EOL for puppet3 |
|  puppet3-server  | Part of upstream EOL for puppet3 |
|  python34  | Part of upstream EOL for python34 |
|  python34-devel  | Part of upstream EOL for python34 |
|  python34-docs  | Part of upstream EOL for python34 |
|  python34-libs  | Part of upstream EOL for python34 |
|  python34-pip  | Part of upstream EOL for python34 |
|  python34-setuptools  | Part of upstream EOL for python34 |
|  python34-test  | Part of upstream EOL for python34 |
|  python34-tools  | Part of upstream EOL for python34 |
|  python34-virtualenv  | Part of upstream EOL for python34 |
|  python35  | Part of upstream EOL for python35 |
|  python35-devel  | Part of upstream EOL for python35 |
|  python35-libs  | Part of upstream EOL for python35 |
|  python35-pip  | Part of upstream EOL for python35 |
|  python35-setuptools  | Part of upstream EOL for python35 |
|  python35-test  | Part of upstream EOL for python35 |
|  python35-tools  | Part of upstream EOL for python35 |
|  python35-virtualenv  | Part of upstream EOL for python35 |
|  ruby23  | Part of upstream EOL for ruby23 |
|  ruby23-devel  | Part of upstream EOL for ruby23 |
|  ruby23-doc  | Part of upstream EOL for ruby23 |
|  ruby23-irb  | Part of upstream EOL for ruby23 |
|  ruby23-libs  | Part of upstream EOL for ruby23 |
|  rubygem23-bigdecimal  | Part of upstream EOL for ruby23 |
|  rubygem23-did\_you\_mean  | Part of upstream EOL for ruby23 |
|  rubygem23-io-console  | Part of upstream EOL for ruby23 |
|  rubygem23-json  | Part of upstream EOL for ruby23 |
|  rubygem23-json-doc  | Part of upstream EOL for ruby23 |
|  rubygem23-minitest5  | Part of upstream EOL for ruby23 |
|  rubygem23-minitest5-doc  | Part of upstream EOL for ruby23 |
|  rubygem23-power\_assert  | Part of upstream EOL for ruby23 |
|  rubygem23-power\_assert-doc  | Part of upstream EOL for ruby23 |
|  rubygem23-psych  | Part of upstream EOL for ruby23 |
|  rubygem23-rake  | Part of upstream EOL for ruby23 |
|  rubygem23-rake-doc  | Part of upstream EOL for ruby23 |
|  rubygem23-rdoc  | Part of upstream EOL for ruby23 |
|  rubygem23-rdoc-doc  | Part of upstream EOL for ruby23 |
|  rubygems23  | Part of upstream EOL for ruby23 |
|  rubygems23-devel  | Part of upstream EOL for ruby23 |
|  subversion  | Part of upstream EOL for Subversion 1.9 |
|  subversion-devel  | Part of upstream EOL for Subversion 1.9 |
|  subversion-javahl  | Part of upstream EOL for Subversion 1.9 |
|  subversion-libs  | Part of upstream EOL for Subversion 1.9 |
|  subversion-perl  | Part of upstream EOL for Subversion 1.9 |
|  subversion-python27  | Part of upstream EOL for Subversion 1.9 |
|  subversion-ruby  | Part of upstream EOL for Subversion 1.9 |
|  tomcat7  | Part of upstream EOL for tomcat7 |
|  tomcat7-admin-webapps  | Part of upstream EOL for tomcat7 |
|  tomcat7-docs-webapp  | Part of upstream EOL for tomcat7 |
|  tomcat7-el-2.2-api  | Part of upstream EOL for tomcat7 |
|  tomcat7-javadoc  | Part of upstream EOL for tomcat7 |
|  tomcat7-jsp-2.2-api  | Part of upstream EOL for tomcat7 |
|  tomcat7-lib  | Part of upstream EOL for tomcat7 |
|  tomcat7-log4j  | Part of upstream EOL for tomcat7 |
|  tomcat7-servlet-3.0-api  | Part of upstream EOL for tomcat7 |
|  tomcat7-webapps  | Part of upstream EOL for tomcat7 |
|  tomcat80  | Part of upstream EOL for tomcat80 |
|  tomcat80-admin-webapps  | Part of upstream EOL for tomcat80 |
|  tomcat80-docs-webapp  | Part of upstream EOL for tomcat80 |
|  tomcat80-el-3.0-api  | Part of upstream EOL for tomcat80 |
|  tomcat80-javadoc  | Part of upstream EOL for tomcat80 |
|  tomcat80-jsp-2.3-api  | Part of upstream EOL for tomcat80 |
|  tomcat80-lib  | Part of upstream EOL for tomcat80 |
|  tomcat80-log4j  | Part of upstream EOL for tomcat80 |
|  tomcat80-servlet-3.1-api  | Part of upstream EOL for tomcat80 |
|  tomcat80-webapps  | Part of upstream EOL for tomcat80 |
|  transmission  | AL1 EOL for transmission |
|  transmission-cli  | AL1 EOL for transmission |
|  transmission-common  | AL1 EOL for transmission |
|  transmission-daemon  | AL1 EOL for transmission |
|  uuid-php55  | Part of upstream EOL for php55 |

## MySQL 5.5 EOL December 3, 2018
<a name="support-info-by-support-statement-eol_mysql55"></a>
+ Start Date: 2018-12-03
+ End Date:

Following upstream sources, MySQL 5.5 reached EOL December 3,2018. For more information, see [Amazon Linux AMI FAQs](https://aws.amazon.com/amazon-linux-ami/faqs/).

### Packages
<a name="support-info-by-support-statement-packages-eol_mysql55"></a>

| Package | Note |
| --- | --- |
|  libdbi-dbd-mysql  | Upstream EOL for MySQL 5.5 (mysql55) is 2018-12-03 |
|  MySQL-python27  | Upstream EOL for MySQL 5.5 (mysql55) is 2018-12-03 |
|  mysql55  | Upstream EOL for MySQL 5.5 (mysql55) is 2018-12-03 |
|  mysql55-bench  | Upstream EOL for MySQL 5.5 (mysql55) is 2018-12-03 |
|  mysql55-devel  | Upstream EOL for MySQL 5.5 (mysql55) is 2018-12-03 |
|  mysql55-embedded  | Upstream EOL for MySQL 5.5 (mysql55) is 2018-12-03 |
|  mysql55-embedded-devel  | Upstream EOL for MySQL 5.5 (mysql55) is 2018-12-03 |
|  mysql55-libs  | Upstream EOL for MySQL 5.5 (mysql55) is 2018-12-03 |
|  mysql55-server  | Upstream EOL for MySQL 5.5 (mysql55) is 2018-12-03 |
|  mysql55-test  | Upstream EOL for MySQL 5.5 (mysql55) is 2018-12-03 |
|  perl-DBD-MySQL  | Upstream EOL for MySQL 5.5 (mysql55) is 2018-12-03 |
|  perl-DBD-MySQL55  | Upstream EOL for MySQL 5.5 (mysql55) is 2018-12-03 |

## MySQL 5.6 EOL February 5, 2021
<a name="support-info-by-support-statement-eol_mysql56"></a>
+ Start Date: 2021-02-05
+ End Date:

MySQL 5.6, as part of AL1, reached EOL on February 5, 2021. For more information, see [Amazon Linux AMI FAQs](https://aws.amazon.com/amazon-linux-ami/faqs/).

### Packages
<a name="support-info-by-support-statement-packages-eol_mysql56"></a>

| Package | Note |
| --- | --- |
|  mysql56  | Upstream EOL for MySQL 5.6 (mysql56) is 2021-02-05 |
|  mysql56-bench  | Upstream EOL for MySQL 5.6 (mysql56) is 2021-02-05 |
|  mysql56-common  | Upstream EOL for MySQL 5.6 (mysql56) is 2021-02-05 |
|  mysql56-devel  | Upstream EOL for MySQL 5.6 (mysql56) is 2021-02-05 |
|  mysql56-embedded  | Upstream EOL for MySQL 5.6 (mysql56) is 2021-02-05 |
|  mysql56-embedded-devel  | Upstream EOL for MySQL 5.6 (mysql56) is 2021-02-05 |
|  mysql56-errmsg  | Upstream EOL for MySQL 5.6 (mysql56) is 2021-02-05 |
|  mysql56-libs  | Upstream EOL for MySQL 5.6 (mysql56) is 2021-02-05 |
|  mysql56-server  | Upstream EOL for MySQL 5.6 (mysql56) is 2021-02-05 |
|  mysql56-test  | Upstream EOL for MySQL 5.6 (mysql56) is 2021-02-05 |
|  perl-DBD-MySQL56  | Upstream EOL for MySQL 5.6 (mysql56) is 2021-02-05 |

## MySQL 5.7 EOL October 21, 2023
<a name="support-info-by-support-statement-eol_mysql57"></a>
+ Start Date: 2023-10-21
+ End Date:

Upstream MySQL 5.7 reached EOL on October 21, 2023. For more information, see [Amazon Linux AMI FAQs](https://aws.amazon.com/amazon-linux-ami/faqs/).

### Packages
<a name="support-info-by-support-statement-packages-eol_mysql57"></a>

| Package | Note |
| --- | --- |
|  mysql57  | Upstream EOL for MySQL 5.7 (mysql57) is 2023-10-21 |
|  mysql57-common  | Upstream EOL for MySQL 5.7 (mysql57) is 2023-10-21 |
|  mysql57-devel  | Upstream EOL for MySQL 5.7 (mysql57) is 2023-10-21 |
|  mysql57-embedded  | Upstream EOL for MySQL 5.7 (mysql57) is 2023-10-21 |
|  mysql57-embedded-devel  | Upstream EOL for MySQL 5.7 (mysql57) is 2023-10-21 |
|  mysql57-errmsg  | Upstream EOL for MySQL 5.7 (mysql57) is 2023-10-21 |
|  mysql57-libs  | Upstream EOL for MySQL 5.7 (mysql57) is 2023-10-21 |
|  mysql57-server  | Upstream EOL for MySQL 5.7 (mysql57) is 2023-10-21 |
|  mysql57-test  | Upstream EOL for MySQL 5.7 (mysql57) is 2023-10-21 |

## OpenJDK 1.7.0 EOL June 30, 2020
<a name="support-info-by-support-statement-eol_java-1.7.0-openjdk"></a>
+ Start Date: 2020-06-30
+ End Date:

OpenJDK 1.7.0 reached EOL June 30, 2020. For more information, see [Amazon Linux AMI FAQs](https://aws.amazon.com/amazon-linux-ami/faqs/)

### Packages
<a name="support-info-by-support-statement-packages-eol_java-1.7.0-openjdk"></a>

| Package | Note |
| --- | --- |
|  java-1.7.0-openjdk  | Upstream EOL for OpenJDK 1.7.0 (java-1.7.0-openjdk) is 2020-06-30 |
|  java-1.7.0-openjdk-demo  | Upstream EOL for OpenJDK 1.7.0 (java-1.7.0-openjdk) is 2020-06-30 |
|  java-1.7.0-openjdk-devel  | Upstream EOL for OpenJDK 1.7.0 (java-1.7.0-openjdk) is 2020-06-30 |
|  java-1.7.0-openjdk-javadoc  | Upstream EOL for OpenJDK 1.7.0 (java-1.7.0-openjdk) is 2020-06-30 |
|  java-1.7.0-openjdk-src  | Upstream EOL for OpenJDK 1.7.0 (java-1.7.0-openjdk) is 2020-06-30 |

## OpenJDK 1.8.0 EOL December 31, 2023
<a name="support-info-by-support-statement-eol_java-1.8.0-openjdk"></a>
+ Start Date: 2023-12-31
+ End Date:

OpenJDK 1.8.0 reached EOL December 31, 2023. For more information, see [Amazon Linux AMI FAQs](https://aws.amazon.com/amazon-linux-ami/faqs/).

### Packages
<a name="support-info-by-support-statement-packages-eol_java-1.8.0-openjdk"></a>

| Package | Note |
| --- | --- |
|  java-1.8.0-openjdk  | Upstream EOL for OpenJDK 1.8.0 (java-1.8.0-openjdk) is 2023-12-31 |
|  java-1.8.0-openjdk-demo  | Upstream EOL for OpenJDK 1.8.0 (java-1.8.0-openjdk) is 2023-12-31 |
|  java-1.8.0-openjdk-devel  | Upstream EOL for OpenJDK 1.8.0 (java-1.8.0-openjdk) is 2023-12-31 |
|  java-1.8.0-openjdk-headless  | Upstream EOL for OpenJDK 1.8.0 (java-1.8.0-openjdk) is 2023-12-31 |
|  java-1.8.0-openjdk-javadoc  | Upstream EOL for OpenJDK 1.8.0 (java-1.8.0-openjdk) is 2023-12-31 |
|  java-1.8.0-openjdk-javadoc-zip  | Upstream EOL for OpenJDK 1.8.0 (java-1.8.0-openjdk) is 2023-12-31 |
|  java-1.8.0-openjdk-src  | Upstream EOL for OpenJDK 1.8.0 (java-1.8.0-openjdk) is 2023-12-31 |

## PHP 7.2 upstream EOL November 30, 2020
<a name="support-info-by-support-statement-eol_php72-common"></a>
+ Start Date: 2020-11-30
+ End Date:

As previously announced, AL1 is following the upstream PHP 7.2 EOL date. Upstream PHP 7.2 reached EOL on November 30, 2020. For more information about upstream PHP EOL, see [Unsupported branches](https://www.php.net/eol.php).

### Packages
<a name="support-info-by-support-statement-packages-eol_php72-common"></a>

| Package | Note |
| --- | --- |
|  apcu72-panel  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-bcmath  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-cli  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-common  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-dba  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-dbg  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-devel  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-embedded  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-enchant  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-fpm  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-gd  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-gmp  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-imap  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-intl  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-json  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-ldap  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-mbstring  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-mysqlnd  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-odbc  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-opcache  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-pdo  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-pdo-dblib  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-pecl-apcu  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-pecl-apcu-devel  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-pecl-igbinary  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-pecl-igbinary-devel  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-pecl-imagick  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-pecl-imagick-devel  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-pecl-mcrypt  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-pecl-memcache  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-pecl-memcached  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-pecl-oauth  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-pecl-redis  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-pecl-ssh2  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-pecl-uuid  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-pecl-xdebug  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-pgsql  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-process  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-pspell  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-recode  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-snmp  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-soap  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-tidy  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-xml  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |
|  php72-xmlrpc  | Upstream EOL for PHP 7.2 (php72-common) is 2020-11-30 |

## PHP 7.3 upstream EOL December 6, 2021
<a name="support-info-by-support-statement-eol_php73-common"></a>
+ Start Date: 2021-12-06
+ End Date:

As previously announced, AL1 is following the upstream PHP 7.3 EOL dates. Upstream PHP 7.3 reached EOL on December 6, 2021. For more information about upstream PHP EOL, see [Supported versions](https://www.php.net/supported-versions).

### Packages
<a name="support-info-by-support-statement-packages-eol_php73-common"></a>

| Package | Note |
| --- | --- |
|  php7-pear  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |
|  php73  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |
|  php73-bcmath  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |
|  php73-cli  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |
|  php73-common  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |
|  php73-dba  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |
|  php73-dbg  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |
|  php73-devel  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |
|  php73-embedded  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |
|  php73-enchant  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |
|  php73-fpm  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |
|  php73-gd  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |
|  php73-gmp  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |
|  php73-imap  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |
|  php73-intl  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |
|  php73-json  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |
|  php73-ldap  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |
|  php73-mbstring  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |
|  php73-mysqlnd  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |
|  php73-odbc  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |
|  php73-opcache  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |
|  php73-pdo  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |
|  php73-pdo-dblib  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |
|  php73-pgsql  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |
|  php73-process  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |
|  php73-pspell  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |
|  php73-recode  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |
|  php73-snmp  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |
|  php73-soap  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |
|  php73-tidy  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |
|  php73-xml  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |
|  php73-xmlrpc  | Upstream EOL for PHP 7.3 (php73-common) is 2021-12-06 |

## PostgreSQL 9.4 upstream EOL February 13, 2020
<a name="support-info-by-support-statement-eol_postgresql94"></a>
+ Start Date: 2020-02-13
+ End Date:

As previously announced, AL1 is following upstream PostgreSQL 9.4 EOL. Upstream PostgreSQL 9.4 reached EOL on February 13, 2020. For more information, see [Releases](https://www.postgresql.org/support/versioning/).

### Packages
<a name="support-info-by-support-statement-packages-eol_postgresql94"></a>

| Package | Note |
| --- | --- |
|  postgresql94  | Upstream EOL for PostgreSQL 9.4 (postgresql94) is 2020-02-13 |
|  postgresql94-contrib  | Upstream EOL for PostgreSQL 9.4 (postgresql94) is 2020-02-13 |
|  postgresql94-devel  | Upstream EOL for PostgreSQL 9.4 (postgresql94) is 2020-02-13 |
|  postgresql94-docs  | Upstream EOL for PostgreSQL 9.4 (postgresql94) is 2020-02-13 |
|  postgresql94-libs  | Upstream EOL for PostgreSQL 9.4 (postgresql94) is 2020-02-13 |
|  postgresql94-plperl  | Upstream EOL for PostgreSQL 9.4 (postgresql94) is 2020-02-13 |
|  postgresql94-plpython26  | Upstream EOL for PostgreSQL 9.4 (postgresql94) is 2020-02-13 |
|  postgresql94-plpython27  | Upstream EOL for PostgreSQL 9.4 (postgresql94) is 2020-02-13 |
|  postgresql94-server  | Upstream EOL for PostgreSQL 9.4 (postgresql94) is 2020-02-13 |
|  postgresql94-test  | Upstream EOL for PostgreSQL 9.4 (postgresql94) is 2020-02-13 |

## PostgreSQL 9.5 upstream EOL February 11, 2021
<a name="support-info-by-support-statement-eol_postgresql95"></a>
+ Start Date: 2021-02-11
+ End Date:

As previously announced, AL1 is following upstream PostgreSQL 9.5 EOL. Upstream PostgreSQL 9.5 reached EOL on February 11, 2021. For more information, see [Versioning policy](https://www.postgresql.org/support/versioning/).

### Packages
<a name="support-info-by-support-statement-packages-eol_postgresql95"></a>

| Package | Note |
| --- | --- |
|  postgresql95  | Upstream EOL for PostgreSQL 9.5 (postgresql95) is 2021-02-11 |
|  postgresql95-contrib  | Upstream EOL for PostgreSQL 9.5 (postgresql95) is 2021-02-11 |
|  postgresql95-devel  | Upstream EOL for PostgreSQL 9.5 (postgresql95) is 2021-02-11 |
|  postgresql95-docs  | Upstream EOL for PostgreSQL 9.5 (postgresql95) is 2021-02-11 |
|  postgresql95-libs  | Upstream EOL for PostgreSQL 9.5 (postgresql95) is 2021-02-11 |
|  postgresql95-plperl  | Upstream EOL for PostgreSQL 9.5 (postgresql95) is 2021-02-11 |
|  postgresql95-plpython26  | Upstream EOL for PostgreSQL 9.5 (postgresql95) is 2021-02-11 |
|  postgresql95-plpython27  | Upstream EOL for PostgreSQL 9.5 (postgresql95) is 2021-02-11 |
|  postgresql95-server  | Upstream EOL for PostgreSQL 9.5 (postgresql95) is 2021-02-11 |
|  postgresql95-static  | Upstream EOL for PostgreSQL 9.5 (postgresql95) is 2021-02-11 |
|  postgresql95-test  | Upstream EOL for PostgreSQL 9.5 (postgresql95) is 2021-02-11 |

## PostgreSQL 9.6 upstream EOL November 11, 2021
<a name="support-info-by-support-statement-eol_postgresql96"></a>
+ Start Date: 2021-11-11
+ End Date:

 As previously announced, AL1 is following upstream PostgreSQL 9.6 EOL. Upstream PostgreSQL 9.6 reached EOL on November 11, 2021. For more information, see [Versioning policy](https://www.postgresql.org/support/versioning/).

### Packages
<a name="support-info-by-support-statement-packages-eol_postgresql96"></a>

| Package | Note |
| --- | --- |
|  postgresql96  | Upstream EOL for PostgreSQL 9.6 (postgresql96) is 2021-11-11 |
|  postgresql96-contrib  | Upstream EOL for PostgreSQL 9.6 (postgresql96) is 2021-11-11 |
|  postgresql96-devel  | Upstream EOL for PostgreSQL 9.6 (postgresql96) is 2021-11-11 |
|  postgresql96-docs  | Upstream EOL for PostgreSQL 9.6 (postgresql96) is 2021-11-11 |
|  postgresql96-libs  | Upstream EOL for PostgreSQL 9.6 (postgresql96) is 2021-11-11 |
|  postgresql96-plperl  | Upstream EOL for PostgreSQL 9.6 (postgresql96) is 2021-11-11 |
|  postgresql96-plpython26  | Upstream EOL for PostgreSQL 9.6 (postgresql96) is 2021-11-11 |
|  postgresql96-plpython27  | Upstream EOL for PostgreSQL 9.6 (postgresql96) is 2021-11-11 |
|  postgresql96-server  | Upstream EOL for PostgreSQL 9.6 (postgresql96) is 2021-11-11 |
|  postgresql96-static  | Upstream EOL for PostgreSQL 9.6 (postgresql96) is 2021-11-11 |
|  postgresql96-test  | Upstream EOL for PostgreSQL 9.6 (postgresql96) is 2021-11-11 |

## Python 3.6 upstream EOL December 31, 2021
<a name="support-info-by-support-statement-eol_python36"></a>
+ Start Date: 2021-12-31
+ End Date:

 As previously announced, AL1 will follow the upstream Python 3.6 EOL. Python 3.6 reached EOL on December 31, 2021. For more information, see [Python 3.6 release schedule](https://www.python.org/dev/peps/pep-0494/).

### Packages
<a name="support-info-by-support-statement-packages-eol_python36"></a>

| Package | Note |
| --- | --- |
|  bcc-tools  | Upstream EOL for Python 3.6 (python36) is 2021-12-31 |
|  mod24\_wsgi-python36  | Upstream EOL for Python 3.6 (python36) is 2021-12-31 |
|  python36  | Upstream EOL for Python 3.6 (python36) is 2021-12-31 |
|  python36-bcc  | Upstream EOL for Python 3.6 (python36) is 2021-12-31 |
|  python36-debug  | Upstream EOL for Python 3.6 (python36) is 2021-12-31 |
|  python36-devel  | Upstream EOL for Python 3.6 (python36) is 2021-12-31 |
|  python36-libs  | Upstream EOL for Python 3.6 (python36) is 2021-12-31 |
|  python36-lit  | Upstream EOL for Python 3.6 (python36) is 2021-12-31 |
|  python36-pip  | Upstream EOL for Python 3.6 (python36) is 2021-12-31 |
|  python36-setuptools  | Upstream EOL for Python 3.6 (python36) is 2021-12-31 |
|  python36-test  | Upstream EOL for Python 3.6 (python36) is 2021-12-31 |
|  python36-tools  | Upstream EOL for Python 3.6 (python36) is 2021-12-31 |
|  python36-virtualenv  | Upstream EOL for Python 3.6 (python36) is 2021-12-31 |

## Python 3.8 upstream EOL is after AL1 EOL
<a name="support-info-by-support-statement-eol_python38"></a>
+ Start Date: 2024-10-14
+ End Date:

 The estimated upstream Python 3.8 EOL date is October 2024. Because this date is after the AL1 EOL date, the earlier EOL date of AL1 applies. For more information, see [Python 3.8 Release Schedule](https://peps.python.org/pep-0569/).

### Packages
<a name="support-info-by-support-statement-packages-eol_python38"></a>

| Package | Note |
| --- | --- |
|  python38  | Upstream EOL for Python 3.8 (python38) is 2024-10-14 |
|  python38-debug  | Upstream EOL for Python 3.8 (python38) is 2024-10-14 |
|  python38-devel  | Upstream EOL for Python 3.8 (python38) is 2024-10-14 |
|  python38-libs  | Upstream EOL for Python 3.8 (python38) is 2024-10-14 |
|  python38-pip  | Upstream EOL for Python 3.8 (python38) is 2024-10-14 |
|  python38-setuptools  | Upstream EOL for Python 3.8 (python38) is 2024-10-14 |
|  python38-test  | Upstream EOL for Python 3.8 (python38) is 2024-10-14 |
|  python38-tools  | Upstream EOL for Python 3.8 (python38) is 2024-10-14 |

## Ruby 2.4 upstream EOL March 31, 2020
<a name="support-info-by-support-statement-eol_ruby24"></a>
+ Start Date: 2020-03-31
+ End Date:

As previously announced, AL1 is following upstream Ruby 2.4 EOL. Upstream Ruby 2.4 reached EOL March 31, 2020. For more information, see [Support of Ruby 2.4 has ended](https://www.ruby-lang.org/en/news/2020/04/05/support-of-ruby-2-4-has-ended/).

### Packages
<a name="support-info-by-support-statement-packages-eol_ruby24"></a>

| Package | Note |
| --- | --- |
|  ruby24  | Upstream EOL for Ruby 2.4 (ruby24) is 2020-03-31 |
|  ruby24-devel  | Upstream EOL for Ruby 2.4 (ruby24) is 2020-03-31 |
|  ruby24-doc  | Upstream EOL for Ruby 2.4 (ruby24) is 2020-03-31 |
|  ruby24-irb  | Upstream EOL for Ruby 2.4 (ruby24) is 2020-03-31 |
|  ruby24-libs  | Upstream EOL for Ruby 2.4 (ruby24) is 2020-03-31 |
|  rubygem24-bigdecimal  | Upstream EOL for Ruby 2.4 (ruby24) is 2020-03-31 |
|  rubygem24-did\_you\_mean  | Upstream EOL for Ruby 2.4 (ruby24) is 2020-03-31 |
|  rubygem24-io-console  | Upstream EOL for Ruby 2.4 (ruby24) is 2020-03-31 |
|  rubygem24-json  | Upstream EOL for Ruby 2.4 (ruby24) is 2020-03-31 |
|  rubygem24-json-doc  | Upstream EOL for Ruby 2.4 (ruby24) is 2020-03-31 |
|  rubygem24-minitest5  | Upstream EOL for Ruby 2.4 (ruby24) is 2020-03-31 |
|  rubygem24-minitest5-doc  | Upstream EOL for Ruby 2.4 (ruby24) is 2020-03-31 |
|  rubygem24-net-telnet  | Upstream EOL for Ruby 2.4 (ruby24) is 2020-03-31 |
|  rubygem24-power\_assert  | Upstream EOL for Ruby 2.4 (ruby24) is 2020-03-31 |
|  rubygem24-power\_assert-doc  | Upstream EOL for Ruby 2.4 (ruby24) is 2020-03-31 |
|  rubygem24-psych  | Upstream EOL for Ruby 2.4 (ruby24) is 2020-03-31 |
|  rubygem24-rake  | Upstream EOL for Ruby 2.4 (ruby24) is 2020-03-31 |
|  rubygem24-rake-doc  | Upstream EOL for Ruby 2.4 (ruby24) is 2020-03-31 |
|  rubygem24-rdoc  | Upstream EOL for Ruby 2.4 (ruby24) is 2020-03-31 |
|  rubygem24-rdoc-doc  | Upstream EOL for Ruby 2.4 (ruby24) is 2020-03-31 |
|  rubygem24-test-unit  | Upstream EOL for Ruby 2.4 (ruby24) is 2020-03-31 |
|  rubygem24-xmlrpc  | Upstream EOL for Ruby 2.4 (ruby24) is 2020-03-31 |
|  rubygems24  | Upstream EOL for Ruby 2.4 (ruby24) is 2020-03-31 |
|  rubygems24-devel  | Upstream EOL for Ruby 2.4 (ruby24) is 2020-03-31 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
