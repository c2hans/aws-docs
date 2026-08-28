---
source_url: https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/net-dg-config.html
---

The AWS SDK for .NET V3 has reached end-of-support.

We recommend that you migrate to [AWS SDK for .NET V4](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/welcome.html). For additional details and information on how to migrate, please refer to our [end-of-support announcement](https://aws.amazon.com/blogs/developer/aws-sdk-for-net-v3-end-of-support-announcement/).

# Get started with the AWS SDK for .NET
<a name="net-dg-config"></a>

To use the AWS SDK for .NET, you need to install your toolchain and configure a number of essential things that your application needs to access AWS services. These include:
+ An appropriate user account or role
+ Authentication information for that user account or to assume that role
+ Specification of the AWS Region
+ AWSSDK packages or assemblies

Some of the topics in this section provide information about how to configure these essential things.

Other topics in this section and other sections provide information about more advanced ways that you can configure your project.

**Topics**
+ [Install and configure your toolchain](net-dg-dev-env.md)
+ [Configure SDK authentication](creds-idc.md)
+ [Take a quick tour](quick-start.md)
+ [Start a new project](net-dg-start-new-project.md)
+ [Configure the AWS Region](net-dg-region-selection.md)
+ [Install AWSSDK packages with NuGet](net-dg-install-assemblies.md)
+ [Install AWSSDK assemblies without NuGet](net-dg-install-without-nuget.md)
+ [Credential and profile resolution](creds-assign.md)
+ [Users and roles](net-dg-users-roles.md)
+ [Advanced configuration](net-dg-advanced-config.md)
+ [Using legacy credentials](net-dg-legacy-creds.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for .NET. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-net` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
