---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/setup.html
---

# Setting up the AWS SDK for Java 2.x
<a name="setup"></a>

This section provides information about how to set up your development environment and projects to use the AWS SDK for Java 2.x.

## Setup overview
<a name="setup-overview"></a>

To successfully develop applications that access AWS services using the AWS SDK for Java, the following conditions are required:
+ The Java SDK must have access to credentials to [authenticate requests](get-started-auth.md#setup-auth) on your behalf.
+ The [permissions of the IAM role](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetsconcept.html) configured for the SDK must allow access to the AWS services that your application requires. The permissions associated with the **PowerUserAccess** AWS managed policy are sufficient for most development needs.
+ A development environment with the following elements:
  + [Shared configuration files](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html) that are set up in at least one of the following ways:
    + The `config` file contains [IAM Identity Center single sign-on settings](get-started-auth.md#setup-credentials) so that the SDK can get AWS credentials.
    + The `credentials` file contains temporary credentials.
  + An [installation of Java 8](setup-java-buildtool.md) or later.
  + A [build automation tool ](setup-java-buildtool.md)such as [Maven](https://maven.apache.org/download.cgi) or [Gradle](https://gradle.org/install/).
  + A text editor to work with code.
  + (Optional, but recommended) An IDE (integrated development environment) such as [IntelliJ IDEA](https://www.jetbrains.com/idea/download/#section=windows), [Eclipse](https://www.eclipse.org/ide/), or [NetBeans](https://netbeans.apache.org/front/main/download/index.html).

    If you use IntelliJ IDEA, you can also add the [AWS Toolkit for IntelliJ IDEA](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html) to integrate AWS services directly into the IDE to help you streamline development.
+ An active AWS access portal session when you are ready to run your application. You use the AWS Command Line Interface to [initiate the sign-in process](get-started-auth.md#setup-login-sso) to IAM Identity Center's AWS access portal.

**Important**
The instructions in this setup section assume that you or organization uses IAM Identity Center. If your organization uses an external identity provider that works independently of IAM Identity Center, find out how you can get temporary credentials for the SDK for Java to use. Follow [these instructions](credentials-temporary.md#credentials-temporary-from-portal) to add temporary credentials to the `~/.aws/credentials` file.
If your identity provider adds temporary credentials automatically to the `~/.aws/credentials` file, make sure that the profile name is `[default]` so that you do not need to provide a profile name to the SDK or AWS CLI.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
