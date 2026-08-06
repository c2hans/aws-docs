---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2019-04-02-linux.html
---

# Release: Elastic Beanstalk Linux-based platform updates on April 2, 2019
<a name="release-2019-04-02-linux"></a>

This release provides new Linux-based platform versions for AWS Elastic Beanstalk. The release includes security updates. It also includes Multicontainer Docker, Go, Node.js, and Ruby updates, an Apache update, and support for additional Amazon EC2 instance types in certain AWS Regions.

**Release date:** April 2, 2019

## Changes
<a name="release-2019-04-02-linux.changes"></a>

| **Category** | **Description** |
| --- | --- |
| **Component** | **Update** |
| --- | --- |
| **Platform** | **Update** |
| --- | --- |
| **Instance types** | **Regions** |
| --- | --- |
| **Security updates** | Applied all security updates published in the [Amazon Linux Security Center](https://alas.aws.amazon.com/) on or before March 11, 2019 to all Linux-based platforms.<br />See also the **Node.js** and **Ruby** entries in **Platform-specific updates** for platform-specific security updates. |
| **Cross-platform updates** | Made these cross-platform updates:[See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2019-04-02-linux.html) |
| **Platform-specific updates** | Made these platform-specific updates:[See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2019-04-02-linux.html) |
| **Instance types** | Added support for more Amazon EC2 instance types in some AWS Regions. In particular, we added support for the new Amazon EC2 Bare Metal instances, which provide your applications with direct access to processor and memory resources of the underlying server. For more information, see [Introducing Five New Amazon EC2 Bare Metal Instances](https://aws.amazon.com/about-aws/whats-new/2019/02/introducing-five-new-amazon-ec2-bare-metal-instances/).<br />The added instance types are listed in the following table.[See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2019-04-02-linux.html) |
| **Apache** | Updated platforms supporting the Apache HTTP Server 2.4 to version 2.4.38. For details, see [Changes with Apache 2.4.x](https://downloads.apache.org/httpd/CHANGES_2.4) on the *Apache Software Foundation* website. |
| **Go** | Updated to minor revision 1.12.1. For details, see [go1.12](https://golang.org/doc/devel/release.html#go1.12) in *The Go Programming Language Release History*. |
| **Multicontainer Docker** |  +  Updated the ECS agent to version 1.26.0. <br />+  Added ECS support in these AWS Regions:  China (Ningxia) – cn-northwest-1 AWS GovCloud (US-East) – us-gov-east-1 AWS GovCloud (US-West) – us-gov-west-1    |
| **Node.js** |  +  Updated the Node.js platform to add support for Node versions [10.15.3](https://nodejs.org/en/blog/release/v10.15.3/), [8.15.1](https://nodejs.org/en/blog/release/v8.15.1/), and [6.17.0](https://nodejs.org/en/blog/release/v6.17.0/). <br />+  These versions include the Node.js [February 2019 Security Releases](https://nodejs.org/en/blog/vulnerability/february-2019-security-releases/).   |
| **Ruby** |  +  Updated the Ruby 2.6 and 2.5 configurations to Ruby releases [2.6.2](https://www.ruby-lang.org/en/news/2019/03/13/ruby-2-6-2-released/), and [2.5.5](https://www.ruby-lang.org/en/news/2019/03/15/ruby-2-5-5-released/), respectively. <br />+  These versions include fixes to [Multiple vulnerabilities in RubyGems](https://www.ruby-lang.org/en/news/2019/03/05/multiple-vulnerabilities-in-rubygems/).   |
| **m5.metal** |  + US East (Ohio) – us-east-2<br />+ US East (N. Virginia) – us-east-1<br />+ US West (N. California) – us-west-1<br />+ US West (Oregon) – us-west-2<br />+ Asia Pacific (Mumbai) – ap-south-1<br />+ Asia Pacific (Seoul) – ap-northeast-2<br />+ Asia Pacific (Singapore) – ap-southeast-1<br />+ Asia Pacific (Sydney) – ap-southeast-2<br />+ Asia Pacific (Tokyo) – ap-northeast-1<br />+ Europe (Frankfurt) – eu-central-1<br />+ Europe (Ireland) – eu-west-1<br />+ Europe (London) – eu-west-2<br />+ Europe (Paris) – eu-west-3<br />+ Europe (Stockholm) – eu-north-1  |
| **m5d.metal** |  + US East (Ohio) – us-east-2<br />+ US East (N. Virginia) – us-east-1<br />+ US West (Oregon) – us-west-2<br />+ Asia Pacific (Mumbai) – ap-south-1<br />+ Asia Pacific (Seoul) – ap-northeast-2<br />+ Asia Pacific (Singapore) – ap-southeast-1<br />+ Asia Pacific (Sydney) – ap-southeast-2<br />+ Europe (Frankfurt) – eu-central-1<br />+ Europe (Ireland) – eu-west-1<br />+ Europe (Paris) – eu-west-3<br />+ Europe (Stockholm) – eu-north-1  |
| **r5.metal** |  + US East (Ohio) – us-east-2<br />+ US East (N. Virginia) – us-east-1<br />+ US West (N. California) – us-west-1<br />+ US West (Oregon) – us-west-2<br />+ Asia Pacific (Mumbai) – ap-south-1<br />+ Asia Pacific (Seoul) – ap-northeast-2<br />+ Asia Pacific (Singapore) – ap-southeast-1<br />+ Europe (Frankfurt) – eu-central-1<br />+ Europe (Ireland) – eu-west-1<br />+ Europe (Paris) – eu-west-3<br />+ Europe (Stockholm) – eu-north-1<br />+ AWS GovCloud (US-West) – us-gov-west-1  |
| **r5d.metal** |  + US East (Ohio) – us-east-2<br />+ US East (N. Virginia) – us-east-1<br />+ US West (N. California) – us-west-1<br />+ Asia Pacific (Mumbai) – ap-south-1<br />+ Asia Pacific (Seoul) – ap-northeast-2<br />+ Asia Pacific (Singapore) – ap-southeast-1<br />+ Europe (Frankfurt) – eu-central-1<br />+ Europe (Paris) – eu-west-3<br />+ Europe (Stockholm) – eu-north-1<br />+ AWS GovCloud (US-West) – us-gov-west-1  |
| **z1d.metal** |  + US East (N. Virginia) – us-east-1<br />+ US West (N. California) – us-west-1<br />+ US West (Oregon) – us-west-2<br />+ Asia Pacific (Singapore) – ap-southeast-1<br />+ Asia Pacific (Tokyo) – ap-northeast-1<br />+ Europe (Ireland) – eu-west-1  |
| **c5, c5d, r5, r5d** |  + China (Beijing) – cn-north-1<br />+ China (Ningxia) – cn-northwest-1  |

## New platform versions
<a name="release-2019-04-02-linux.platforms"></a>

**Topics**
+ [Packer Builder](#release-2019-04-02-linux.platforms.packer)
+ [Single Container Docker](#release-2019-04-02-linux.platforms.docker)
+ [Multicontainer Docker](#release-2019-04-02-linux.platforms.mcdocker)
+ [Preconfigured Docker](#release-2019-04-02-linux.platforms.dockerpreconfig)
+ [Go](#release-2019-04-02-linux.platforms.go)
+ [Java SE](#release-2019-04-02-linux.platforms.javase)
+ [Java with Tomcat](#release-2019-04-02-linux.platforms.java)
+ [Node.js](#release-2019-04-02-linux.platforms.nodejs)
+ [PHP](#release-2019-04-02-linux.platforms.PHP)
+ [Python](#release-2019-04-02-linux.platforms.python)
+ [Ruby](#release-2019-04-02-linux.platforms.ruby)

### Packer Builder
<a name="release-2019-04-02-linux.platforms.packer"></a>

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Packer Version  |
| --- | --- | --- |
|  **Elastic Beanstalk Packer Builder version 2.6.8** <br /> * 64bit Amazon Linux 2018.03 v2.6.8 running Packer 1.0.3 *  | 2018.03.0 | 1.0.3 |

### Single Container Docker
<a name="release-2019-04-02-linux.platforms.docker"></a>

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Docker Version  |  Proxy Server  |
| --- | --- | --- | --- |
|  **Single Container Docker 18.06 version 2.12.10** <br /> * 64bit Amazon Linux 2018.03 v2.12.10 running Docker 18.06.1-ce *  | 2018.03.0 | 18.06.1-ce | nginx 1.14.1 |

### Multicontainer Docker
<a name="release-2019-04-02-linux.platforms.mcdocker"></a>

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Docker Version  |  ECS Agent  |
| --- | --- | --- | --- |
|  **Multicontainer Docker 18.06 version 2.12.0** <br /> * 64bit Amazon Linux 2018.03 v2.12.0 running Multi-container Docker 18.06.1-ce (Generic) *  | 2018.03.0 | 18.06.1-ce | 1.26.0 |

### Preconfigured Docker
<a name="release-2019-04-02-linux.platforms.dockerpreconfig"></a>

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Platform  |  Container OS  |  Language  |  Proxy Server  |  Application Server  |  Docker Image  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  **Glassfish 5.0 (Docker) version 2.12.10** <br /> * 64bit Amazon Linux v2.12.10 running GlassFish 5.0 Java 8 (Preconfigured - Docker) *  | 2018.03.0 | Docker 18.06.1-ce | Amazon Linux 2018.03 | Java 8 | nginx 1.14.1 | Glassfish 5.0 | amazon/aws-eb-glassfish:5.0-al-onbuild-2.11.1 |
|  **Go 1.4 (Docker) version 2.12.10** <br /> * 64bit Debian jessie v2.12.10 running Go 1.4 (Preconfigured - Docker) *  | 2018.03.0 | Docker 18.06.1-ce | Debian Jessie | Go 1.4.2 | nginx 1.14.1 | none | golang:1.4.2-onbuild |
|  **Go 1.3 (Docker) version 2.12.10** <br /> * 64bit Debian jessie v2.12.10 running Go 1.3 (Preconfigured - Docker) *  | 2018.03.0 | Docker 18.06.1-ce | Debian Jessie | Go 1.3.3 | nginx 1.14.1 | none | golang:1.3.3-onbuild |
|  **Python 3.4 with uWSGI 2 (Docker) version 2.12.10** <br /> * 64bit Debian jessie v2.12.10 running Python 3.4 (Preconfigured - Docker) *  | 2018.03.0 | Docker 18.06.1-ce | Debian Jessie | Python 3.4 | nginx 1.14.1 | uWSGI 2.0.8 | amazon/aws-eb-python:3.4.2-onbuild-3.5.1 |

### Go
<a name="release-2019-04-02-linux.platforms.go"></a>

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  AWS X‑Ray  |  Proxy Server  |
| --- | --- | --- | --- | --- |
|  **Go 1.12 version 2.11.0** <br /> * 64bit Amazon Linux 2018.03 v2.11.0 running Go 1.12.1 *  | 2018.03.0 | Go 1.12.1 | 3.0.0 | nginx 1.14.1 |

### Java SE
<a name="release-2019-04-02-linux.platforms.javase"></a>

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Tools  |  AWS X‑Ray  |  Proxy Server  |
| --- | --- | --- | --- | --- | --- |
|  **Java 8 version 2.8.2** <br /> * 64bit Amazon Linux 2018.03 v2.8.2 running Java 8 *  | 2018.03.0 | Java 1.8.0\_201 | Ant 1.9.6, Gradle 2.7, Maven 3.3.3 | 3.0.0 | nginx 1.14.1 |
|  **Java 7 version 2.8.2** <br /> * 64bit Amazon Linux 2018.03 v2.8.2 running Java 7 *  | 2018.03.0 | Java 1.7.0\_211 | Ant 1.9.6, Gradle 2.7, Maven 3.3.3 | 3.0.0 | nginx 1.14.1 |

### Java with Tomcat
<a name="release-2019-04-02-linux.platforms.java"></a>

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  AWS X‑Ray  |  Application Server  |  Proxy Server  |
| --- | --- | --- | --- | --- | --- |
|  **Java 8 with Tomcat 8.5 version 3.1.2** <br /> * 64bit Amazon Linux 2018.03 v3.1.2 running Tomcat 8.5 Java 8 *  | 2018.03.0 | Java 1.8.0\_191 | 3.0.0 | Tomcat 8.5.32 | Apache 2.4.38 (default), Apache 2.2.34, Nginx 1.14.1 |
|  **Java 8 with Tomcat 8 version 3.1.2** <br /> * 64bit Amazon Linux 2018.03 v3.1.2 running Tomcat 8 Java 8 *  | 2018.03.0 | Java 1.8.0\_191 | 3.0.0 | Tomcat 8.0.53 | Apache 2.4.38 (default), Apache 2.2.34, Nginx 1.14.1 |
|  **Java 7 with Tomcat 7 version 3.1.2** <br /> * 64bit Amazon Linux 2018.03 v3.1.2 running Tomcat 7 Java 7 *  | 2018.03.0 | Java 1.7.0\_201 | 3.0.0 | Tomcat 7.0.91 | Apache 2.4.38 (default), Apache 2.2.34, Nginx 1.14.1 |
|  **Java 6 with Tomcat 7 version 3.1.2** <br /> * 64bit Amazon Linux 2018.03 v3.1.2 running Tomcat 7 Java 6 *  | 2018.03.0 | Java 1.6.0\_41 | 3.0.0 | Tomcat 7.0.91 | Apache 2.4.38 (default), Apache 2.2.34, Nginx 1.14.1 |

### Node.js
<a name="release-2019-04-02-linux.platforms.nodejs"></a>

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Node.js versions (npm versions)  |  Proxy Server  |  Git  |  AWS X‑Ray  |
| --- | --- | --- | --- | --- | --- |
|  **Node.js version 4.8.2** <br /> * 64bit Amazon Linux 2018.03 v4.8.2 running Node.js *  | 2018.03.0 | 10.15.3 (6.4.1), 10.15.1 (6.4.1), 10.15.0 (6.4.1), 10.14.1 (6.4.1), 8.15.1 (6.4.1), 8.15.0 (6.4.1), 8.14.0 (6.4.1), 7.10.1 (4.2.0), 6.17.0 (3.10.10), 6.16.0 (3.10.10), 6.15.1 (3.10.10), 5.12.0 (3.8.6), 4.9.1 (2.15.11), 4.8.7 (2.15.11)<br /> Default platform: 10.15.3 | nginx 1.14.1, Apache 2.4.38 | 2.14.5 | 3.0.0 |

### PHP
<a name="release-2019-04-02-linux.platforms.PHP"></a>

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Composer  |  Proxy Server  |
| --- | --- | --- | --- | --- |
|  **PHP 7.2 version 2.8.8** <br /> * 64bit Amazon Linux 2018.03 v2.8.8 running PHP 7.2 *  | 2018.03.0 | PHP 7.2.13 | 1.4.2 | Apache 2.4.38 |
|  **PHP 7.1 version 2.8.8** <br /> * 64bit Amazon Linux 2018.03 v2.8.8 running PHP 7.1 *  | 2018.03.0 | PHP 7.1.25 | 1.4.2 | Apache 2.4.38 |
|  **PHP 7.0 version 2.8.8** <br /> * 64bit Amazon Linux 2018.03 v2.8.8 running PHP 7.0 *  | 2018.03.0 | PHP 7.0.33 | 1.4.2 | Apache 2.4.38 |
|  **PHP 5.6 version 2.8.8** <br /> * 64bit Amazon Linux 2018.03 v2.8.8 running PHP 5.6 *  | 2018.03.0 | PHP 5.6.39 | 1.4.2 | Apache 2.4.38 |
|  **PHP 5.5 version 2.8.8** <br /> * 64bit Amazon Linux 2018.03 v2.8.8 running PHP 5.5 *  | 2018.03.0 | PHP 5.5.38 | 1.4.2 | Apache 2.4.38 |
|  **PHP 5.4 version 2.8.8** <br /> * 64bit Amazon Linux 2018.03 v2.8.8 running PHP 5.4 *  | 2018.03.0 | PHP 5.4.45 | 1.4.2 | Apache 2.4.38 |

### Python
<a name="release-2019-04-02-linux.platforms.python"></a>

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Packager  |  meld3  |  AWS X‑Ray  |  Proxy Server  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  **Python 3.6 version 2.8.2** <br /> * 64bit Amazon Linux 2018.03 v2.8.2 running Python 3.6 *  | 2018.03.0 | Python 3.6.7 | pip 9.0.3 | setuptools 28.8.0 | meld3 1.0.2 | 3.0.0 | Apache 2.4.38 with mod\_wsgi 3.5 |
|  **Python 3.4 version 2.8.2** <br /> * 64bit Amazon Linux 2018.03 v2.8.2 running Python 3.4 *  | 2018.03.0 | Python 3.4.9 | pip 9.0.3 | setuptools 28.8.0 | meld3 1.0.2 | 3.0.0 | Apache 2.4.38 with mod\_wsgi 3.5 |
|  **Python 2.7 version 2.8.2** <br /> * 64bit Amazon Linux 2018.03 v2.8.2 running Python 2.7 *  | 2018.03.0 | Python 2.7.15 | pip 9.0.3 | setuptools 28.8.0 | meld3 1.0.2 | 3.0.0 | Apache 2.4.38 with mod\_wsgi 3.5 |
|  **Python 2.6 version 2.8.2** <br /> * 64bit Amazon Linux 2018.03 v2.8.2 running Python 2.6 *  | 2018.03.0 | Python 2.6.9 | pip 9.0.3 | setuptools 28.8.0 | meld3 1.0.2 | 3.0.0 | Apache 2.4.38 with mod\_wsgi 3.5 |

### Ruby
<a name="release-2019-04-02-linux.platforms.ruby"></a>

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Application Server  |  AWS X‑Ray  |  Proxy Server  |
| --- | --- | --- | --- | --- | --- | --- |
|  **Ruby 2.6 with Puma version 2.9.2** <br /> * 64bit Amazon Linux 2018.03 v2.9.2 running Ruby 2.6 (Puma) *  | 2018.03.0 | Ruby 2.6.2-p47 | RubyGems 2.7.9 | Puma 2.16.0 | 3.0.0 | nginx 1.14.1 |
|  **Ruby 2.6 with Passenger version 2.9.2** <br /> * 64bit Amazon Linux 2018.03 v2.9.2 running Ruby 2.6 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.6.2-p47 | RubyGems 2.7.9 | Passenger 4.0.60 | 3.0.0 | nginx 1.14.1 |
|  **Ruby 2.5 with Puma version 2.9.2** <br /> * 64bit Amazon Linux 2018.03 v2.9.2 running Ruby 2.5 (Puma) *  | 2018.03.0 | Ruby 2.5.5-p157 | RubyGems 2.7.9 | Puma 2.16.0 | 3.0.0 | nginx 1.14.1 |
|  **Ruby 2.5 with Passenger version 2.9.2** <br /> * 64bit Amazon Linux 2018.03 v2.9.2 running Ruby 2.5 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.5.5-p157 | RubyGems 2.7.9 | Passenger 4.0.60 | 3.0.0 | nginx 1.14.1 |
|  **Ruby 2.4 with Puma version 2.9.2** <br /> * 64bit Amazon Linux 2018.03 v2.9.2 running Ruby 2.4 (Puma) *  | 2018.03.0 | Ruby 2.4.5-p335 | RubyGems 2.7.7 | Puma 2.16.0 | 3.0.0 | nginx 1.14.1 |
|  **Ruby 2.4 with Passenger version 2.9.2** <br /> * 64bit Amazon Linux 2018.03 v2.9.2 running Ruby 2.4 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.4.5-p335 | RubyGems 2.7.7 | Passenger 4.0.60 | 3.0.0 | nginx 1.14.1 |
|  **Ruby 2.3 with Puma version 2.9.2** <br /> * 64bit Amazon Linux 2018.03 v2.9.2 running Ruby 2.3 (Puma) *  | 2018.03.0 | Ruby 2.3.8-p459 | RubyGems 2.7.7 | Puma 2.16.0 | 3.0.0 | nginx 1.14.1 |
|  **Ruby 2.3 with Passenger version 2.9.2** <br /> * 64bit Amazon Linux 2018.03 v2.9.2 running Ruby 2.3 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.3.8-p459 | RubyGems 2.7.7 | Passenger 4.0.60 | 3.0.0 | nginx 1.14.1 |
|  **Ruby 2.2 with Puma version 2.9.2** <br /> * 64bit Amazon Linux 2018.03 v2.9.2 running Ruby 2.2 (Puma) *  | 2018.03.0 | Ruby 2.2.10-p489 | RubyGems 2.7.6 | Puma 2.16.0 | 3.0.0 | nginx 1.14.1 |
|  **Ruby 2.2 with Passenger version 2.9.2** <br /> * 64bit Amazon Linux 2018.03 v2.9.2 running Ruby 2.2 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.2.10-p489 | RubyGems 2.7.6 | Passenger 4.0.60 | 3.0.0 | nginx 1.14.1 |
|  **Ruby 2.1 with Puma version 2.9.2** <br /> * 64bit Amazon Linux 2018.03 v2.9.2 running Ruby 2.1 (Puma) *  | 2018.03.0 | Ruby 2.1.10-p492 | RubyGems 2.6.13 | Puma 2.16.0 | 3.0.0 | nginx 1.14.1 |
|  **Ruby 2.1 with Passenger version 2.9.2** <br /> * 64bit Amazon Linux 2018.03 v2.9.2 running Ruby 2.1 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.1.10-p492 | RubyGems 2.6.13 | Passenger 4.0.60 | 3.0.0 | nginx 1.14.1 |
|  **Ruby 2.0 with Puma version 2.9.2** <br /> * 64bit Amazon Linux 2018.03 v2.9.2 running Ruby 2.0 (Puma) *  | 2018.03.0 | Ruby 2.0.0-p648 | RubyGems 2.6.13 | Puma 2.16.0 | 3.0.0 | nginx 1.14.1 |
|  **Ruby 2.0 with Passenger version 2.9.2** <br /> * 64bit Amazon Linux 2018.03 v2.9.2 running Ruby 2.0 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.0.0-p648 | RubyGems 2.6.13 | Passenger 4.0.60 | 3.0.0 | nginx 1.14.1 |
|  **Ruby 1.9 with Passenger version 2.9.2** <br /> * 64bit Amazon Linux 2018.03 v2.9.2 running Ruby 1.9.3 *  | 2018.03.0 | Ruby 1.9.3-p551 | RubyGems 2.6.13 | Passenger 4.0.60 | 3.0.0 | nginx 1.14.1 |
