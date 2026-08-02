---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2018-12-14-golang.html
---

# Release: AWS Elastic Beanstalk Go platform update on December 14, 2018
<a name="release-2018-12-14-golang"></a>

This release applies security updates to the Go platform for AWS Elastic Beanstalk, and updates platform configuration. The release also includes a Go runtime update, bug fixes, and, for certain AWS Regions, support for additional Amazon EC2 instance types.

**Release date:** December 14, 2018

## Changes
<a name="release-2018-12-14-golang.changes"></a>

Here is a list of the key changes in this release.

| **Category** | **Description** |
| --- | --- |
| **Instance type** | **Regions** |
| --- | --- |
| **Security updates** | Applied all security updates published in the [Amazon Linux Security Center](https://alas.aws.amazon.com/) on or before December 7, 2018 to the Go platform.<br />See also the **Go updates** entry. |
| **Go updates** | Applied minor revision 1.11.3. For details, see [go1.11](https://golang.org/doc/devel/release.html#go1.11) in *The Go Programming Language Release History*.<br />Revision 1.11.3 addresses three recently reported security issues. For details, see [[security] Go 1.11.3 and Go 1.10.6 are released](https://groups.google.com/forum/#!topic/golang-announce/Kw31K8G7Fi0). |
| **Instance types** | Added support for more Amazon EC2 instance types in some AWS Regions, for the Go platform, as follows:[See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2018-12-14-golang.html) |
| **T3** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2018-12-14-golang.html)  |
| **C5n** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2018-12-14-golang.html)  |

## Updated platform configurations
<a name="release-2018-12-14-golang.platforms"></a>

### Go
<a name="release-2018-12-14-golang.platforms.go"></a>

****

|  Configuration and *Solution Stack Name*   |  AMI  |  Language  |  AWS X‑Ray  |  Proxy Server  |
| --- | --- | --- | --- | --- |
|  **Go 1.11 version 2.9.3** <br /> * 64bit Amazon Linux 2018.03 v2.9.3 running Go 1.11.3 *  | 2018.03.0 | Go 1.11.3 | 2.0.0 | nginx 1.12.1 |
