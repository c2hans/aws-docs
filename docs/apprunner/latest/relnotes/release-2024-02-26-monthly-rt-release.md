---
source_url: https://docs.aws.amazon.com/apprunner/latest/relnotes/release-2024-02-26-monthly-rt-release.html
---

AWS App Runner will no longer be open to new customers starting April 30, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Release: App Runner runtime updates on February 26, 2024
<a name="release-2024-02-26-monthly-rt-release"></a>

This release provides minor version updates for the Python and Corretto (Java SE) language runtimes. It also provides package updates to the Python and Ruby platforms.

**Release date:** February 26, 2024

## App Runner managed platforms
<a name="release-2024-02-26-monthly-rt-release.managed-platforms"></a>

App Runner provides convenient platform-specific managed runtimes. When you use a managed runtime, App Runner starts with a managed runtime base image to build a container image from your source code. For more information, see [ App Runner managed platforms](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code.html#service-source-code.managed-platforms) in the *AWS App Runner Developer Guide*.

## Changes
<a name="release-2024-02-26-monthly-rt-release.changes"></a>

The following table lists the changes included in this release.

| **Category** | **Description** |
| --- | --- |
| **Component** | **Update** |
| --- | --- |
| **Platform** | **Update** |
| --- | --- |
| **Base container image updates** | Made the following updates to the base container images: [See the AWS documentation website for more details](http://docs.aws.amazon.com/apprunner/latest/relnotes/release-2024-02-26-monthly-rt-release.html)<br />To view the Amazon Linux container image on the *Amazon ECR Public Gallery,* see the *Image tags* tab on [Amazon ECR Public Gallery - amazonlinux](https://gallery.ecr.aws/amazonlinux/amazonlinux). <br /> |
| **Platform-specific updates** | Made these platform-specific updates:[See the AWS documentation website for more details](http://docs.aws.amazon.com/apprunner/latest/relnotes/release-2024-02-26-monthly-rt-release.html) |
| Base container image for AL2023 | Updated base container image to version **2023.3.20240205.2.** This image only applies to Node.js 18 and Python 3.11 runtimes.  |
| Base container image for AL2 | Updated base container image to version **2.0.20240131.0**. This image applies to all runtimes, except for Node.js 18 and Python 3.11.  |
| **Python**<br /> [Supported runtimes](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-python-releases.html)  | Language runtime updates:[See the AWS documentation website for more details](http://docs.aws.amazon.com/apprunner/latest/relnotes/release-2024-02-26-monthly-rt-release.html)<br />Package updates:[See the AWS documentation website for more details](http://docs.aws.amazon.com/apprunner/latest/relnotes/release-2024-02-26-monthly-rt-release.html) |
| **Corretto**<br />[Supported runtimes](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-java-releases.html) | Language runtime updates:[See the AWS documentation website for more details](http://docs.aws.amazon.com/apprunner/latest/relnotes/release-2024-02-26-monthly-rt-release.html)<br />No package updates. |
| **Ruby**<br />[Supported runtimes ](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-ruby-releases.html) | No updates to language versions.<br />Package updates:[See the AWS documentation website for more details](http://docs.aws.amazon.com/apprunner/latest/relnotes/release-2024-02-26-monthly-rt-release.html) |
