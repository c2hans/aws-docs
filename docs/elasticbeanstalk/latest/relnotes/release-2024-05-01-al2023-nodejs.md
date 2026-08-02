---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2024-05-01-al2023-nodejs.html
---

# Release: Elastic Beanstalk Amazon Linux 2023 Node.js platform updates on May 01, 2024
<a name="release-2024-05-01-al2023-nodejs"></a>

This release is an emergent AWS Elastic Beanstalk Node.js platform update for Amazon Linux 2023. It addresses a security vulnerability and also updates Apache HTTP server on the Node.js AL2023 platforms.

**Release date:** May 01, 2024

## Changes
<a name="release-2024-05-01-al2023-nodejs.changes"></a>

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
| **Security updates** | Applied all security updates published in the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html) on or before **April 25, 2024** to all AL2023 platforms.<br />Applied security updates that address [CVE-2024-27983](https://explore.alas.aws.amazon.com/CVE-2024-27983.html) to the Node.js AL2023 platform branches.<br />  |
| **Cross-platform updates** | Made these cross-platform updates:[See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2024-05-01-al2023-nodejs.html) |
| **Platform-specific updates** | Made these platform-specific updates:[See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2024-05-01-al2023-nodejs.html) |
| **AMI** | Updated the base AMI to version 2023.4.20240429. |
| **Node.js** | **Language runtime updates**[See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2024-05-01-al2023-nodejs.html)<br />This Node.js update is a security release.<br />**Apache HTTP Server**[See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2024-05-01-al2023-nodejs.html)<br />This Apache update is security release. |

## New platform versions
<a name="release-2024-05-01-al2023-nodejs.platforms"></a>

**Topics**
+ [Node.js](#release-2024-05-01-nodejs-al2023.platforms.nodejs)

### Node.js
<a name="release-2024-05-01-nodejs-al2023.platforms.nodejs"></a>

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Node.js versions (npm versions)  |  Proxy Server  |  Git  |  AWS X-Ray  |
| --- | --- | --- | --- | --- | --- |
|  ** Node.js 20 AL2023 version 6.1.4** <br /> * 64bit Amazon Linux 2023 v6.1.4 running Node.js 20 *  | 2023.4.20240429 | 20.12.2 (10.5.0)<br /> Default version: 20.12.2 | nginx 1.24.0 (default), Apache 2.4.59 | 2.40.1 | 3.2.0 |
|  ** Node.js 18 AL2023 version 6.1.4** <br /> * 64bit Amazon Linux 2023 v6.1.4 running Node.js 18 *  | 2023.4.20240429 | 18.18.2 (9.8.1)<br /> Default version: 18.18.2 | nginx 1.24.0 (default), Apache 2.4.59 | 2.40.1 | 3.2.0 |
