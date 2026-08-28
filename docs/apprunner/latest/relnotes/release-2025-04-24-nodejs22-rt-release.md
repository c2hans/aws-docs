---
source_url: https://docs.aws.amazon.com/apprunner/latest/relnotes/release-2025-04-24-nodejs22-rt-release.html
---

AWS App Runner will no longer be open to new customers starting April 30, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Release: App Runner adds support for Node.js 22 on April 24, 2025
<a name="release-2025-04-24-nodejs22-rt-release"></a>

AWS App Runner adds support for Node.js 22.

**Release date:** April 24, 2025

## App Runner managed platforms
<a name="release-2025-04-24-nodejs22-rt-release.managed-platforms"></a>

App Runner provides convenient platform-specific managed runtimes. When you use a managed runtime, App Runner starts with a managed runtime base image to build a container image from your source code. For more information, see [ App Runner managed platforms](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code.html#service-source-code.managed-platforms) in the *AWS App Runner Developer Guide*.

## Changes
<a name="release-2025-04-24-nodejs22-rt-release.changes"></a>

App Runner now supports Node.js 22 as part of its managed runtime service.

This release provides the following versions and packages:
+ Major version release: Node.js 22.14.0
+ Packages: npm 10.9.2, yarn 1.22.22

For details, see [ Node.js supported runtimes](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-nodejs-releases.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for App Runner. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apprunner` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
