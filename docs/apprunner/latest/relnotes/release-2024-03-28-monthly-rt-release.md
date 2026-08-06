---
source_url: https://docs.aws.amazon.com/apprunner/latest/relnotes/release-2024-03-28-monthly-rt-release.html
---

AWS App Runner will no longer be open to new customers starting April 30, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Release: App Runner runtime updates on March 28, 2024
<a name="release-2024-03-28-monthly-rt-release"></a>

This release provides minor version updates for the Node.js and .NET Core language runtimes. It also provides package updates to the Python, Node.js, .NET Core, and Ruby platforms.

**Release date:** March 28, 2024

## App Runner managed platforms
<a name="release-2024-03-28-monthly-rt-release.managed-platforms"></a>

App Runner provides convenient platform-specific managed runtimes. When you use a managed runtime, App Runner starts with a managed runtime base image to build a container image from your source code. For more information, see [ App Runner managed platforms](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code.html#service-source-code.managed-platforms) in the *AWS App Runner Developer Guide*.

## Changes
<a name="release-2024-03-28-monthly-rt-release.changes"></a>

The following table lists the changes included in this release.

| **Category** | **Description** |
| --- | --- |
| **Component** | **Update** |
| --- | --- |
| **Platform** | **Update** |
| --- | --- |
| **Base container image updates** | Made the following updates to the base container images: [See the AWS documentation website for more details](http://docs.aws.amazon.com/apprunner/latest/relnotes/release-2024-03-28-monthly-rt-release.html)<br /> To view the Amazon Linux container image on the *Amazon ECR Public Gallery,* see the *Image tags* tab on [Amazon ECR Public Gallery - amazonlinux](https://gallery.ecr.aws/amazonlinux/amazonlinux). <br /> |
| **Platform-specific updates** | Made these platform-specific updates:[See the AWS documentation website for more details](http://docs.aws.amazon.com/apprunner/latest/relnotes/release-2024-03-28-monthly-rt-release.html) |
| Base container image for AL2023  | Updated base container image to version **2023.3.20240312.0**. This image only applies to Node.js 18 and Python 3.11 runtimes.  |
| Base container image for AL2 | Updated base container image to version **2.0.20240306.2**. This image applies to all runtimes, except for Node.js 18 and Python 3.11.  |
| **.NET Core**<br />[Supported runtimes ](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-net6-releases.html) | Updated **.NET Core 6.0** to version [6.0.28](https://github.com/dotnet/core/blob/main/release-notes/6.0/6.0.28/6.0.28.md).<br />Package updates:+  Updated **dotnet6-sdk** package to version **6.0.420**. For more information see [6.0.28](https://github.com/dotnet/core/blob/main/release-notes/6.0/6.0.28/6.0.28.md) Release Notes.  |
| **Node.js**<br />[Supported runtimes ](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-nodejs-releases.html) | Updated Node.js 18 to version [18.19.1](https://nodejs.org/en/blog/release/v18.19.1) |
| **Python**<br />[Supported runtimes](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-python-releases.html) | No updates to language versions.<br />Package updates:+  Updated **SQLite **package to version **3.45.2** for **Python 3.7**, **Python 3.8**, and **Python 3.11**. For more information see [SQLite Release History](https://www.sqlite.org/chronology.html).  |
| **Ruby**<br />[Supported runtimes ](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-ruby-releases.html) | No updates to language versions.<br />Package updates:+  Updated **SQLite **package to version **3.45.2** for **Ruby 3.1**. For more information see [SQLite Release History](https://www.sqlite.org/chronology.html).  |
