---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/apireference/custom-endpoints.html
---

# Getting Started with AWS Elemental MediaConvert Using the AWS SDKs or the AWS CLI
<a name="custom-endpoints"></a>

To get started with AWS Elemental MediaConvert using one of the AWS SDKS or the AWS Command Line Interface (AWS CLI), follow this general procedure.

1. Set up AWS Identity and Access Management (IAM) permissions for both yourself and for the MediaConvert service to access your resources on your behalf:
   + For information about setting up permissions for yourself, see [Overview of Identity Management: Users](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_identity-management.html) in the *IAM User Guide*.
   + For information about setting up permissions for the service to access your resources, see [Set Up IAM Permissions](https://docs.aws.amazon.com/mediaconvert/latest/ug/iam-role.html) in the *MediaConvert User Guide*.

1. In your client configuration, specify your authentication credentials and your AWS Region. For instructions that are specific to the programming language that you use, choose from this list of links to open the relevant topics in the AWS CLI or SDK guides:
   +  [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)
   + C\+\+: [credentials](https://docs.aws.amazon.com/sdk-for-cpp/latest/developer-guide/credentials.html) and [Region](https://docs.aws.amazon.com/sdk-for-cpp/latest/developer-guide/client-config.html)
   +  [ Go ](https://docs.aws.amazon.com/sdk-for-go/latest/developer-guide/configuring-sdk.html)
   + [Java](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/setup-credentials.html)
   + [JavaScript](https://docs.aws.amazon.com/sdk-for-javascript/latest/developer-guide/setting-credentials.html)
   + [.NET](https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/net-dg-config.html)
   + [PHP](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_configuration.html)
   + Python: [credentials](https://docs.aws.amazon.com/boto3/latest/guide/configuration.html) and [Region](https://docs.aws.amazon.com/boto3/latest/guide/configuration.html#environment-variable-configuration)
   + [Ruby](https://docs.aws.amazon.com/sdk-for-ruby/latest/developer-guide/setup-config.html)
   + [Tools for PowerShell](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-getting-started.html)

1. To prevent duplicate jobs from being created, use client request tokens. For more information see [Preventing duplicate jobs](idempotency.md).

**Choosing the correct case for requests**
When you send requests, use camelCase or PascalCase as appropriate for the language you are using. All examples in this guide use PascalCase, which is the correct casing for the AWS CLI and AWS SDK for Python (Boto3). The MediaConvert console JSON export function also generates JSON job specifications in PascalCase.

When you use a language that specifies camelCase, such as JavaScript, you must convert the casing of your properties before you submit your requests. For example, if you use the properties "Settings" and "TimecodeConfig" in your call through the AWS CLI, you must change those to "settings" and "timecodeConfig" for your call through the AWS SDK for JavaScript.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
