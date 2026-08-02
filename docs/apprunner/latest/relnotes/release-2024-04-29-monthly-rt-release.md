---
source_url: https://docs.aws.amazon.com/apprunner/latest/relnotes/release-2024-04-29-monthly-rt-release.html
---

AWS App Runner will no longer be open to new customers starting April 30, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Release: App Runner runtime updates on April 29, 2024
<a name="release-2024-04-29-monthly-rt-release"></a>

This release provides minor version updates for the Python, Node.js Corretto (Java SE), .NET Core, and PHP language runtimes. It also provides package updates to the Python, Node.js, .NET Core, and Ruby platforms.

**Release date:** April 29, 2024

## App Runner managed platforms
<a name="release-2024-04-29-monthly-rt-release.managed-platforms"></a>

App Runner provides convenient platform-specific managed runtimes. When you use a managed runtime, App Runner starts with a managed runtime base image to build a container image from your source code. For more information, see [ App Runner managed platforms](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code.html#service-source-code.managed-platforms) in the *AWS App Runner Developer Guide*.

## Changes
<a name="release-2024-04-29-monthly-rt-release.changes"></a>

The following table lists the changes included in this release.

| **Category** | **Description** |
| --- | --- |
| **Component** | **Update** |
| --- | --- |
| **Platform** | **Update** |
| --- | --- |
| **Base container image updates** | Made the following updates to the base container images: [See the AWS documentation website for more details](http://docs.aws.amazon.com/apprunner/latest/relnotes/release-2024-04-29-monthly-rt-release.html)<br /> To view the Amazon Linux container image on the *Amazon ECR Public Gallery,* see the *Image tags* tab on [Amazon ECR Public Gallery - amazonlinux](https://gallery.ecr.aws/amazonlinux/amazonlinux). <br /> |
| **Platform-specific updates** | Made these platform-specific updates:[See the AWS documentation website for more details](http://docs.aws.amazon.com/apprunner/latest/relnotes/release-2024-04-29-monthly-rt-release.html) |
| Base container image for AL2023  | Updated base container image to version **2023.4.20240416.0**. This image only applies to Node.js 18 and Python 3.11 runtimes.  |
| Base container image for AL2 | Updated base container image to version **2.0.20240412.0**. This image applies to all runtimes, except for Node.js 18 and Python 3.11.  |
| **Corretto** | Language runtime updates:[See the AWS documentation website for more details](http://docs.aws.amazon.com/apprunner/latest/relnotes/release-2024-04-29-monthly-rt-release.html) |
| **.NET Core**<br />[Supported runtimes ](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-net6-releases.html) | Updated **.NET Core 6.0** to version [6.0.29](https://github.com/dotnet/core/blob/main/release-notes/6.0/6.0.29/6.0.29.md).<br />Package updates:[See the AWS documentation website for more details](http://docs.aws.amazon.com/apprunner/latest/relnotes/release-2024-04-29-monthly-rt-release.html) |
| **Node.js**<br />[Supported runtimes ](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-nodejs-releases.html) | Updated Node.js 18 to version [18.20.2](https://nodejs.org/en/blog/release/v18.20.2)<br />Tools Updates:[See the AWS documentation website for more details](http://docs.aws.amazon.com/apprunner/latest/relnotes/release-2024-04-29-monthly-rt-release.html) |
| **PHP**<br />[Supported runtimes ](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-php-releases.html) | Updated **PHP 8.1** to version [8.1.28](https://www.php.net/releases/8_1_28.php).<br />No package updates. |
| **Python**<br />[Supported runtimes](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-python-releases.html) | Updated Python 3.11 from version 3.11.8 to [Python 3.11.9](https://docs.python.org/release/3.11.9/whatsnew/changelog.html#changelog).<br />No updates to language versions.<br />Package updates:[See the AWS documentation website for more details](http://docs.aws.amazon.com/apprunner/latest/relnotes/release-2024-04-29-monthly-rt-release.html) |
| **Ruby**<br />[Supported runtimes ](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-ruby-releases.html) | No updates to language versions.<br />Package updates:[See the AWS documentation website for more details](http://docs.aws.amazon.com/apprunner/latest/relnotes/release-2024-04-29-monthly-rt-release.html) |
