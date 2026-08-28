---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/setup.html
---

# Set up the AWS SDK for Kotlin
<a name="setup"></a>

To make requests to AWS services using the AWS SDK for Kotlin, you need the following:
+ The ability to sign-in to the AWS access portal
+ Permission to use the AWS resources your application needs
+ A development environment with the following elements:
  +  [Shared configuration files](/sdkref/latest/guide/file-format.html) that are setup with at least one of the following ways:
    + The `config` file contains IAM Identity Center credentials settings so that the SDK can obtain AWS credentials
    + The `credentials` file contains temporary credentials
  + A build automation tool such as [Gradle](https://gradle.org/install/) or [Maven](https://maven.apache.org/download.cgi)
+ An active AWS access portal session when you are ready to run your application

**Topics**
+ [Basic set up](setup-basic-onetime-setup.md)
+ [Create project build files](setup-create-project-file.md)
+ [Code your Kotlin project using the SDK for Kotlin](code-project.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Kotlin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-kotlin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
