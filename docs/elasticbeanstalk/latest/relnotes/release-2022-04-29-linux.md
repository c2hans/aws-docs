---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2022-04-29-linux.html
---

# Release: Elastic Beanstalk Amazon Linux platform updates on April 29, 2022
<a name="release-2022-04-29-linux"></a>

This release provides new versions for AWS Elastic Beanstalk platforms based on Amazon Linux. The release includes security updates. It also provides updates for AMI, Docker, Go, .NET Core, Node.js, and Ruby.

**Release date:** April 29, 2022

## Changes
<a name="release-2022-04-29-linux.changes"></a>

The following table lists the changes included in this release.

**Notes**
These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated) platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html) in the *AWS Elastic Beanstalk Platforms* guide.
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category** | **Description** |
| --- | --- |
| **Component** | **Update** |
| --- | --- |
| **Platform** | **Update** |
| --- | --- |
| **Security updates** | Applied all security updates published in the [Amazon Linux Security Center](https://alas.aws.amazon.com/) on or before **April 20, 2022** to released Amazon Linux 2 platforms. <br />Some CVEs were missed from this release’s Ruby update. They were added in the next [Ruby release of May 4, 2020](release-2022-05-04-ruby.md). For more information, see the Ruby platform in this table's **Platform-specific updates**.<br /> Some of the platform updates are security releases. For more information, see **Platform-specific updates** in this table. |
| **Cross-platform updates** | Made these cross-platform updates:[See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2022-04-29-linux.html) |
| **Platform-specific updates** | Made these platform-specific updates:[See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2022-04-29-linux.html) |
| **Base AMI** | Updated the base AMI to version **2.0.20220419**. |
| **Docker** | Updated Amazon ECS to version **1.61.0** on the *ECS running on Amazon Linux 2* platform branch. |
| **Go** | Updated Go to release **1.18.1**. For details, see [go1.18](https://golang.org/doc/devel/release.html#go1.18) in *The Go Programming Language Release History*. |
| **.NET Core** | Updated .NET Core to releases [6.0.4](https://github.com/dotnet/core/blob/main/release-notes/6.0/6.0.4/6.0.4.md) , [5.0.16](https://github.com/dotnet/core/blob/main/release-notes/5.0/5.0.16/5.0.16.md) , and [3.1.24](https://github.com/dotnet/core/blob/main/release-notes/3.1/3.1.24/3.1.24.md)  |
| **Node.js** | Updated Node.js 12 to add support for Node version [12.22.12](https://nodejs.org/en/blog/release/v12.22.12/). |
| **Ruby** | Updated Ruby 2.7 and 2.6 to releases [2.7.6](https://www.ruby-lang.org/en/news/2022/04/12/ruby-2-7-6-released/) and [2.6.10](https://www.ruby-lang.org/en/news/2022/04/12/ruby-2-6-10-released/), respectively.<br />Updated RubyGems to release [3.3.12](https://blog.rubygems.org/2022/04/20/3.3.12-released.html).<br />Updated Puma to version [5.6.4](https://github.com/puma/puma/releases/tag/v5.6.4).<br />The new Puma version is a security release.<br />The Ruby updates are security releases.  These CVEs were missed from today's Ruby update. They were added in the next [Ruby release of May 4, 2020](release-2022-05-04-ruby.md).   [ALAS-2022-1580](https://alas.aws.amazon.com/ALAS-2022-1580.html): [CVE-2022-0070](https://alas.aws.amazon.com/cve/html/CVE-2022-0070.html)    [ALAS-2022-1581](https://alas.aws.amazon.com/ALAS-2022-1581.html): [CVE-2022-26490](https://alas.aws.amazon.com/cve/html/CVE-2022-26490.html) [CVE-2022-27666](https://alas.aws.amazon.com/cve/html/CVE-2022-27666.html) [CVE-2022-28356](https://alas.aws.amazon.com/cve/html/CVE-2022-28356.html)     |

## New platform versions
<a name="release-2022-04-29-linux.platforms"></a>

**Topics**
+ [Docker](#release-2022-04-29-linux.platforms.docker)
+ [Go](#release-2022-04-29-linux.platforms.go)
+ [Java SE](#release-2022-04-29-linux.platforms.javase)
+ [Tomcat](#release-2022-04-29-linux.platforms.java)
+ [.NET Core on Linux](#release-2022-04-29-linux.platforms.dotnetlinux)
+ [Node.js](#release-2022-04-29-linux.platforms.nodejs)
+ [PHP](#release-2022-04-29-linux.platforms.PHP)
+ [Python](#release-2022-04-29-linux.platforms.python)
+ [Ruby](#release-2022-04-29-linux.platforms.ruby)

### Docker
<a name="release-2022-04-29-linux.platforms.docker"></a>

**Note**
*ECS Amazon Linux 2 v3.1.1* is running ECS Agent 1.61.0.

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Docker  |  Docker Compose  |  Proxy Server  |
| --- | --- | --- | --- | --- |
|  ** Docker AL2 version 3.4.14** <br /> * 64bit Amazon Linux 2 v3.4.14 running Docker *  | 2.0.20220419 | 20.10.7-5 | 1.29.2 | nginx 1.20.0 |
|  ** ECS AL2 version 3.1.1** <br /> * 64bit Amazon Linux 2 v3.1.1 running ECS *  | 2.0.20220419 |  |  |  |

### Go
<a name="release-2022-04-29-linux.platforms.go"></a>

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  AWS X-Ray  |  Proxy Server  |
| --- | --- | --- | --- | --- |
|  ** Go 1 AL2 version 3.5.1** <br /> * 64bit Amazon Linux 2 v3.5.1 running Go 1 *  | 2.0.20220419 | Go 1.18.1 | 3.2.0 | nginx 1.20.0 |

### Java SE
<a name="release-2022-04-29-linux.platforms.javase"></a>

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Tools  |  AWS X-Ray  |  Proxy Server  |
| --- | --- | --- | --- | --- | --- |
|  ** Corretto 11 version 3.2.14** <br /> * 64bit Amazon Linux 2 v3.2.14 running Corretto 11 *  | 2.0.20220419 | Corretto 11.0.14.10.1 | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0 | nginx 1.20.0 |
|  ** Corretto 8 version 3.2.14** <br /> * 64bit Amazon Linux 2 v3.2.14 running Corretto 8 *  | 2.0.20220419 | Corretto 8.322.06.3 | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0 | nginx 1.20.0 |

### Tomcat
<a name="release-2022-04-29-linux.platforms.java"></a>

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  AWS X-Ray  |  Application Server  |  Proxy Server  |
| --- | --- | --- | --- | --- | --- |
|  ** Corretto 11 with Tomcat 8.5 AL2 version 4.2.14** <br /> * 64bit Amazon Linux 2 v4.2.14 running Tomcat 8.5 Corretto 11 *  | 2.0.20220419 | Corretto 11.0.14.10.1 | 3.2.0 | Tomcat 8.5.75 | nginx 1.20.0 (default), Apache 2.4.52 |
|  ** Corretto 8 with Tomcat 8.5 AL2 version 4.2.14** <br /> * 64bit Amazon Linux 2 v4.2.14 running Tomcat 8.5 Corretto 8 *  | 2.0.20220419 | Corretto 8.322.06.3 | 3.2.0 | Tomcat 8.5.75 | nginx 1.20.0 (default), Apache 2.4.52 |

### .NET Core on Linux
<a name="release-2022-04-29-linux.platforms.dotnetlinux"></a>

****

|  Platform Version and *Solution Stack Name*   |  Framework  |  Proxy Server  |  AMI  |  AWS X-Ray  |
| --- | --- | --- | --- | --- |
|  ** .NET Core on AL2 version 2.3.1** <br /> * 64bit Amazon Linux 2 v2.3.1 running .NET Core *  | .NET 6.0.4, supports 6.0.4, 5.0.16, 3.1.24 | nginx 1.20.0 | 2.0.20220419 | 3.2.0 |

### Node.js
<a name="release-2022-04-29-linux.platforms.nodejs"></a>

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Node.js versions (npm versions)  |  Proxy Server  |  Git  |  AWS X-Ray  |
| --- | --- | --- | --- | --- | --- |
|  ** Node.js 16 AL2 version 5.5.2** <br /> * 64bit Amazon Linux 2 v5.5.2 running Node.js 16 *  | 2.0.20220419 | 16.14.2 (8.5.0), 16.14.1 (8.5.0), 16.14.0 (8.3.1), 16.13.2 (8.1.2), 16.13.1 (8.1.2), 16.13.0 (8.1.0), 16.12.0 (8.1.0), 16.11.1 (8.0.0), 16.11.0 (8.0.0), 16.10.0 (7.24.0), 16.9.1 (7.21.1), 16.9.0 (7.21.1), 16.8.0 (7.21.0), 16.7.0 (7.20.3), 16.6.2 (7.20.3), 16.6.1 (7.20.3), 16.6.0 (7.19.1), 16.5.0 (7.19.1), 16.4.2 (7.18.1), 16.4.1 (7.18.1), 16.4.0 (7.18.1), 16.3.0 (7.15.1), 16.2.0 (7.13.0), 16.1.0 (7.11.2), 16.0.0 (7.10.0)<br /> Default version: 16.14.2 | nginx 1.20.0 (default), Apache 2.4.52 | 2.32.0 | 3.2.0 |
|  ** Node.js 14 AL2 version 5.5.2** <br /> * 64bit Amazon Linux 2 v5.5.2 running Node.js 14 *  | 2.0.20220419 | 14.19.1 (6.14.16), 14.19.0 (6.14.16), 14.18.3 (6.14.15), 14.18.2 (6.14.15), 14.18.1 (6.14.15), 14.18.0 (6.14.15), 14.17.6 (6.14.15), 14.17.5 (6.14.14), 14.17.4 (6.14.14), 14.17.3 (6.14.13), 14.17.2 (6.14.13), 14.17.1 (6.14.13), 14.17.0 (6.14.13), 14.16.1 (6.14.12), 14.16.0 (6.14.11), 14.15.5 (6.14.11), 14.15.4 (6.14.10), 14.15.3 (6.14.9), 14.15.2 (6.14.9), 14.15.1 (6.14.8), 14.15.0 (6.14.8), 14.14.0 (6.14.8), 14.13.1 (6.14.8), 14.13.0 (6.14.8), 14.12.0 (6.14.8), 14.11.0 (6.14.8), 14.10.1 (6.14.8), 14.10.0 (6.14.8), 14.9.0 (6.14.8), 14.8.0 (6.14.7), 14.7.0 (6.14.7), 14.6.0 (6.14.6), 14.5.0 (6.14.5), 14.4.0 (6.14.5), 14.3.0 (6.14.5), 14.2.0 (6.14.4), 14.1.0 (6.14.4), 14.0.0 (6.14.4)<br /> Default version: 14.19.1 | nginx 1.20.0 (default), Apache 2.4.52 | 2.32.0 | 3.2.0 |

### PHP
<a name="release-2022-04-29-linux.platforms.PHP"></a>

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Composer  |  Proxy Server  |
| --- | --- | --- | --- | --- |
|  ** PHP 8.0 AL2 version 3.3.13** <br /> * 64bit Amazon Linux 2 v3.3.13 running PHP 8.0 *  | 2.0.20220419 | PHP 8.0.16 | 2.0.13 | nginx 1.20.0 (default), Apache 2.4.52 |

### Python
<a name="release-2022-04-29-linux.platforms.python"></a>

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Packager  |  meld3  |  AWS X-Ray  |  Proxy Server  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  ** Python 3.8 AL2 version 3.3.13** <br /> * 64bit Amazon Linux 2 v3.3.13 running Python 3.8 *  | 2.0.20220419 | Python 3.8.5 | pipenv 2021.11.9 |  |  | 3.2.0 | nginx 1.20.0 (default), Apache 2.4.52 |
|  ** Python 3.7 AL2 version 3.3.13** <br /> * 64bit Amazon Linux 2 v3.3.13 running Python 3.7 *  | 2.0.20220419 | Python 3.7.10 | pipenv 2021.11.9 |  |  | 3.2.0 | nginx 1.20.0 (default), Apache 2.4.52 |

### Ruby
<a name="release-2022-04-29-linux.platforms.ruby"></a>

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Application Server  |  AWS X-Ray  |  Proxy Server  |
| --- | --- | --- | --- | --- | --- | --- |
|  ** Ruby 3.0 AL2 version 3.4.5** <br /> * 64bit Amazon Linux 2 v3.4.5 running Ruby 3.0 *  | 2.0.20220419 | Ruby 3.0.3-p157 | RubyGems 3.3.12 | Puma 5.6.4 | 3.2.0 | nginx 1.20.0 |
|  ** Ruby 2.7 AL2 version 3.4.5** <br /> * 64bit Amazon Linux 2 v3.4.5 running Ruby 2.7 *  | 2.0.20220419 | Ruby 2.7.6-p219 | RubyGems 3.3.12 | Puma 5.6.4 | 3.2.0 | nginx 1.20.0 |
