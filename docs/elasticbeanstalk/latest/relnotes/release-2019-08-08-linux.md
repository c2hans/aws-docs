---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2019-08-08-linux.html
---

# Release: Elastic Beanstalk Linux-based platform updates on August 8, 2019
<a name="release-2019-08-08-linux"></a>

This release provides new Linux-based platform versions for AWS Elastic Beanstalk. The release includes security updates. It also includes Go and Java 8 updates and an AWS X-Ray update.

**Release date:** August 8, 2019

## Changes
<a name="release-2019-08-08-linux.changes"></a>

| **Category** | **Description** |
| --- | --- |
| **Component** | **Update** |
| --- | --- |
| **Platform** | **Update** |
| --- | --- |
| **Instance type** | **Regions** |
| --- | --- |
| **Security updates** | Applied all security updates published in the [Amazon Linux Security Center](https://alas.aws.amazon.com/) on or before **July 25, 2019** to all Linux-based platforms. |
| **Cross-platform updates** | Made these cross-platform updates:[See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2019-08-08-linux.html) |
| **Platform-specific updates** | Made these platform-specific updates:[See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2019-08-08-linux.html) |
| **Instance types** | Added support for more Amazon EC2 instance types in some AWS Regions, as follows:[See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2019-08-08-linux.html) |
| **AWS X-Ray** | Updated platforms that support X-Ray to [X-Ray Daemon version 3.1.0](https://aws.amazon.com/releasenotes/aws-x-ray-daemon-version-3-1-0/?tag=releasenotes%23keywords%23aws-x-ray). |
| **Multicontainer Docker** | Updated the ECS agent to version 1.29.1. |
| **Go** | Updated to minor revision 1.12.7. For details, see [go1.12](https://golang.org/doc/devel/release.html#go1.12) in *The Go Programming Language Release History*. |
| **Java with Tomcat** | Updated Tomcat 8.5 to [Tomcat 8.5.42](https://tomcat.apache.org/tomcat-8.5-doc/changelog.html#Tomcat_8.5.42_(markt)).<br />Updated Tomcat 7 to [Tomcat 7.0.94](https://tomcat.apache.org/tomcat-7.0-doc/changelog.html#Tomcat_7.0.94_(markt)). |
| **PHP** | Updated PHP 7.2 to [7.2.19](https://www.php.net/releases/7_2_19.php). This is a security release which also contains several minor bug fixes. |
| **m5.8xlarge, m5.16xlarge, m5d.8xlarge, m5d.16xlarge, r5.8xlarge,**<br />**r5.16xlarge, r5d.8xlarge, r5d.16xlarge, m5a.8xlarge, m5a.16xlarge,**<br />**r5a.8xlarge, r5a.16xlarge, T3a** |  + US East (Ohio) – us-east-2  |
| **m5.8xlarge, m5.16xlarge, m5d.8xlarge, m5d.16xlarge, r5.8xlarge,**<br />**r5.16xlarge, r5d.8xlarge, r5d.16xlarge, M5a, R5a, T3a** |  + US West (N. California) – us-west-1  |
| **m5.8xlarge, m5.16xlarge, m5d.8xlarge, r5.8xlarge, r5.16xlarge,**<br />**r5d.8xlarge, r5d.16xlarge, m5a.8xlarge, m5a.16xlarge, r5a.8xlarge** |  + US West (Oregon) – us-west-2  |
| **m5.8xlarge, m5.16xlarge, m5d.8xlarge, m5d.16xlarge, r5.8xlarge,**<br />**r5.16xlarge** |  + Asia Pacific (Hong Kong) – ap-east-1  |
| **m5.8xlarge, m5.16xlarge, m5d.8xlarge, m5d.16xlarge, r5.8xlarge,**<br />**r5.16xlarge, r5d.8xlarge, r5d.16xlarge** |  + Asia Pacific (Mumbai) – ap-south-1<br />+ Asia Pacific (Seoul) – ap-northeast-2<br />+ Canada (Central) – ca-central-1<br />+ Europe (London) – eu-west-2<br />+ Europe (Paris) – eu-west-3<br />+ Europe (Stockholm) – eu-north-1  |
| **M5, M5d, R5, R5d** |  + Asia Pacific (Osaka) – ap-northeast-3  |
| **m5.8xlarge, m5.16xlarge, m5d.8xlarge, m5d.16xlarge, r5.8xlarge,**<br />**r5.16xlarge, r5d.8xlarge, r5d.16xlarge, m5a.8xlarge, m5a.16xlarge,**<br />**r5a.8xlarge, r5a.16xlarge** |  + Asia Pacific (Singapore) – ap-southeast-1  |
| **m5.8xlarge, m5.16xlarge, m5d.8xlarge, m5d.16xlarge, r5.8xlarge,**<br />**r5.metal, r5d.8xlarge, r5d.16xlarge, r5d.metal** |  + Asia Pacific (Tokyo) – ap-northeast-1  |
| **r5.8xlarge, r5.16xlarge, r5d.8xlarge, M5, M5d, T3a** |  + China (Beijing) – cn-north-1  |
| **r5d.8xlarge, r5d.16xlarge, M5, M5d, T3a** |  + China (Ningxia) – cn-northwest-1  |
| **m5.8xlarge, m5.16xlarge, m5d.8xlarge, r5.8xlarge, r5.16xlarge,**<br />**r5d.8xlarge, r5d.16xlarge, m5a.large, m5a.xlarge, m5a.2xlarge,**<br />**m5a.4xlarge, m5a.8xlarge, m5a.12xlarge, m5a.24xlarge, r5a.large,**<br />**r5a.xlarge, r5a.2xlarge, r5a.4xlarge, r5a.8xlarge, r5a.12xlarge,**<br />**r5a.24xlarge** |  + Europe (Frankfurt) – eu-central-1  |
| **m5.8xlarge, m5.16xlarge, m5d.8xlarge, m5d.16xlarge, r5.8xlarge,**<br />**r5.16xlarge, r5d.8xlarge, r5d.16xlarge, m5a.8xlarge, r5a.8xlarge,**<br />**T3a** |  + Europe (Ireland) – eu-west-1  |
| **m5.8xlarge, m5.16xlarge** |  + South America (São Paulo) – sa-east-1  |
| **m5.8xlarge, m5.16xlarge, m5d.8xlarge, m5d.16xlarge, r5.8xlarge,**<br />**r5.16xlarge, r5d.8xlarge, r5d.16xlarge, T3a** |  + AWS GovCloud (US-East) – us-gov-east-1<br />+ AWS GovCloud (US-West) – us-gov-west-1  |
| **g3.4xlarge, g3.8xlarge, g3.16xlarge** |  + China (Beijing) – cn-north-1<br />+ Europe (London) – eu-west-2  |
| **g3s.xlarge** |  + Europe (London) – eu-west-2  |

## New platform versions
<a name="release-2019-08-08-linux.platforms"></a>

**Topics**
+ [Packer Builder](#release-2019-08-07-linux.platforms.packer)
+ [Single Container Docker](#release-2019-08-07-linux.platforms.docker)
+ [Multicontainer Docker](#release-2019-08-07-linux.platforms.mcdocker)
+ [Preconfigured Docker](#release-2019-08-07-linux.platforms.dockerpreconfig)
+ [Go](#release-2019-08-07-linux.platforms.go)
+ [Java SE](#release-2019-08-07-linux.platforms.javase)
+ [Java with Tomcat](#release-2019-08-07-linux.platforms.java)
+ [Node.js](#release-2019-08-07-linux.platforms.nodejs)
+ [PHP](#release-2019-08-07-linux.platforms.PHP)
+ [Python](#release-2019-08-07-linux.platforms.python)
+ [Ruby](#release-2019-08-07-linux.platforms.ruby)

### Packer Builder
<a name="release-2019-08-07-linux.platforms.packer"></a>

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Packer Version  |
| --- | --- | --- |
|  **Elastic Beanstalk Packer Builder version 2.6.14** <br /> * 64bit Amazon Linux 2018.03 v2.6.14 running Packer 1.0.3 *  | 2018.03.0 | 1.0.3 |

### Single Container Docker
<a name="release-2019-08-07-linux.platforms.docker"></a>

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Docker Version  |  Proxy Server  |
| --- | --- | --- | --- |
|  **Single Container Docker 18.06 version 2.12.16** <br /> * 64bit Amazon Linux 2018.03 v2.12.16 running Docker 18.06.1-ce *  | 2018.03.0 | 18.06.1-ce | nginx 1.14.1 |

### Multicontainer Docker
<a name="release-2019-08-07-linux.platforms.mcdocker"></a>

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Docker Version  |  ECS Agent  |
| --- | --- | --- | --- |
|  **Multicontainer Docker 18.06 version 2.15.2** <br /> * 64bit Amazon Linux 2018.03 v2.15.2 running Multi-container Docker 18.06.1-ce (Generic) *  | 2018.03.0 | 18.06.1-ce | 1.29.1 |

### Preconfigured Docker
<a name="release-2019-08-07-linux.platforms.dockerpreconfig"></a>

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Platform  |  Container OS  |  Language  |  Proxy Server  |  Application Server  |  Docker Image  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  **Glassfish 5.0 (Docker) version 2.12.16** <br /> * 64bit Amazon Linux v2.12.16 running GlassFish 5.0 Java 8 (Preconfigured - Docker) *  | 2018.03.0 | Docker 18.06.1-ce | Amazon Linux 2018.03 | Java 8 | nginx 1.14.1 | Glassfish 5.0 | amazon/aws-eb-glassfish:5.0-al-onbuild-2.11.1 |

### Go
<a name="release-2019-08-07-linux.platforms.go"></a>

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  AWS X‑Ray  |  Proxy Server  |
| --- | --- | --- | --- | --- |
|  **Go 1.12 version 2.12.1** <br /> * 64bit Amazon Linux 2018.03 v2.12.1 running Go 1.12.7 *  | 2018.03.0 | Go 1.12.7 | 3.1.0 | nginx 1.14.1 |

### Java SE
<a name="release-2019-08-07-linux.platforms.javase"></a>

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Tools  |  AWS X‑Ray  |  Proxy Server  |
| --- | --- | --- | --- | --- | --- |
|  **Java 8 version 2.9.1** <br /> * 64bit Amazon Linux 2018.03 v2.9.1 running Java 8 *  | 2018.03.0 | Java 1.8.0\_201 | Ant 1.9.6, Gradle 2.7, Maven 3.3.3 | 3.1.0 | nginx 1.14.1 |
|  **Java 7 version 2.9.1** <br /> * 64bit Amazon Linux 2018.03 v2.9.1 running Java 7 *  | 2018.03.0 | Java 1.7.0\_211 | Ant 1.9.6, Gradle 2.7, Maven 3.3.3 | 3.1.0 | nginx 1.14.1 |

### Java with Tomcat
<a name="release-2019-08-07-linux.platforms.java"></a>

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  AWS X‑Ray  |  Application Server  |  Proxy Server  |
| --- | --- | --- | --- | --- | --- |
|  **Java 8 with Tomcat 8.5 version 3.2.1** <br /> * 64bit Amazon Linux 2018.03 v3.2.1 running Tomcat 8.5 Java 8 *  | 2018.03.0 | Java 1.8.0\_201 | 3.1.0 | Tomcat 8.5.42 | Apache 2.4.39 (default), Apache 2.2.34, Nginx 1.14.1 |
|  **Java 7 with Tomcat 7 version 3.2.1** <br /> * 64bit Amazon Linux 2018.03 v3.2.1 running Tomcat 7 Java 7 *  | 2018.03.0 | Java 1.7.0\_211 | 3.1.0 | Tomcat 7.0.94 | Apache 2.4.39 (default), Apache 2.2.34, Nginx 1.14.1 |

### Node.js
<a name="release-2019-08-07-linux.platforms.nodejs"></a>

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Node.js versions (npm versions)  |  Proxy Server  |  Git  |  AWS X‑Ray  |
| --- | --- | --- | --- | --- | --- |
|  **Node.js version 4.10.1** <br /> * 64bit Amazon Linux 2018.03 v4.10.1 running Node.js *  | 2018.03.0 | 10.16.0 (6.9.0), 10.15.3 (6.4.1), 10.15.1 (6.4.1), 10.15.0 (6.4.1), 10.14.1 (6.4.1), 8.16.0 (6.4.1), 8.15.1 (6.4.1), 8.15.0 (6.4.1), 8.14.0 (6.4.1), 7.10.1 (4.2.0), 6.17.1 (3.10.10), 6.17.0 (3.10.10), 6.16.0 (3.10.10), 6.15.1 (3.10.10), 5.12.0 (3.8.6), 4.9.1 (2.15.11), 4.8.7 (2.15.11)<br /> Default version: 10.16.0 | nginx 1.14.1, Apache 2.4.39 | 2.14.5 | 3.1.0 |

### PHP
<a name="release-2019-08-07-linux.platforms.PHP"></a>

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Composer  |  Proxy Server  |
| --- | --- | --- | --- | --- |
|  **PHP 7.2 version 2.8.14** <br /> * 64bit Amazon Linux 2018.03 v2.8.14 running PHP 7.2 *  | 2018.03.0 | PHP 7.2.19 | 1.4.2 | Apache 2.4.39 |

### Python
<a name="release-2019-08-07-linux.platforms.python"></a>

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Packager  |  meld3  |  AWS X‑Ray  |  Proxy Server  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  **Python 3.6 version 2.9.1** <br /> * 64bit Amazon Linux 2018.03 v2.9.1 running Python 3.6 *  | 2018.03.0 | Python 3.6.8 | pip 9.0.3 | setuptools 28.8.0 | meld3 1.0.2 | 3.1.0 | Apache 2.4.39 with mod\_wsgi 3.5 |

### Ruby
<a name="release-2019-08-07-linux.platforms.ruby"></a>

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Application Server  |  AWS X‑Ray  |  Proxy Server  |
| --- | --- | --- | --- | --- | --- | --- |
|  **Ruby 2.6 with Puma version 2.10.1** <br /> * 64bit Amazon Linux 2018.03 v2.10.1 running Ruby 2.6 (Puma) *  | 2018.03.0 | Ruby 2.6.3-p62 | RubyGems 2.7.9 | Puma 2.16.0 | 3.1.0 | nginx 1.14.1 |
|  **Ruby 2.6 with Passenger version 2.10.1** <br /> * 64bit Amazon Linux 2018.03 v2.10.1 running Ruby 2.6 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.6.3-p62 | RubyGems 2.7.9 | Passenger 4.0.60 | 3.1.0 | nginx 1.14.1 |
|  **Ruby 2.5 with Puma version 2.10.1** <br /> * 64bit Amazon Linux 2018.03 v2.10.1 running Ruby 2.5 (Puma) *  | 2018.03.0 | Ruby 2.5.5-p157 | RubyGems 2.7.9 | Puma 2.16.0 | 3.1.0 | nginx 1.14.1 |
|  **Ruby 2.5 with Passenger version 2.10.1** <br /> * 64bit Amazon Linux 2018.03 v2.10.1 running Ruby 2.5 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.5.5-p157 | RubyGems 2.7.9 | Passenger 4.0.60 | 3.1.0 | nginx 1.14.1 |
|  **Ruby 2.4 with Puma version 2.10.1** <br /> * 64bit Amazon Linux 2018.03 v2.10.1 running Ruby 2.4 (Puma) *  | 2018.03.0 | Ruby 2.4.6-p354 | RubyGems 2.7.9 | Puma 2.16.0 | 3.1.0 | nginx 1.14.1 |
|  **Ruby 2.4 with Passenger version 2.10.1** <br /> * 64bit Amazon Linux 2018.03 v2.10.1 running Ruby 2.4 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.4.6-p354 | RubyGems 2.7.9 | Passenger 4.0.60 | 3.1.0 | nginx 1.14.1 |
