---
source_url: https://docs.aws.amazon.com/apprunner/latest/relnotes/release-2022-02-22-java.html
---

AWS App Runner will no longer be open to new customers starting April 30, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Release: App Runner adds a Java platform and a Node.js 14 runtime on February 22, 2022
<a name="release-2022-02-22-java"></a>

AWS App Runner added a new platform for building and running Java web applications, and a new Node.js runtime.

**Release date:** February 22, 2022

## Changes
<a name="release-2022-02-22-java.changes"></a>

AWS App Runner added support for building and running Java web applications with the new Java platform. The Java platform launched with two runtimes. They are Corretto 11 and Corretto 8. Both runtimes add the Maven and Gradle tools to your application's container in addition to the respective Corretto runtime version. For more information, see [Using the Java platform](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-java.html) in the *AWS App Runner Developer Guide*.

App Runner also added a new runtime, Node.js 14, to the existing Node.js platform. For more information, see [Node.js runtime release information](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-nodejs-releases.html) in the *AWS App Runner Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for App Runner. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apprunner` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
