---
source_url: https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/lambda-runtimes.html
---

# AWS Lambda runtimes and support in the AWS Toolkit for JetBrains
<a name="lambda-runtimes"></a>

AWS Lambda supports multiple languages through the use of runtimes. A runtime provides a language-specific environment that relays invocation events, context information, and responses between Lambda and the function. For detailed information about the Lambda service and supported runtimes, see the [Lambda runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-support-policy) topic in the *AWS Lambda User Guide*.

The following describes runtime environments currently supported for use with the AWS Toolkit for JetBrains.

| Name | Identifier | Operating System | Architecture |
| --- | --- | --- | --- |
| Node.js 18 | nodejs18.x | Amazon Linux 2 | x86\_64, arm64 |
| Node.js 16 | nodejs16.x | Amazon Linux 2 | x86\_64, arm64 |
| Node.js 14 | nodejs14.x | Amazon Linux 2 | x86\_64, arm64 |
| Python 3.11 | python3.11 | Amazon Linux 2 | x86\_64, arm64 |
| Python 3.10 | python3.10 | Amazon Linux 2 | x86\_64, arm64 |
| Python 3.9 | python3.9 | Amazon Linux 2 | x86\_64, arm64 |
| Python 3.8 | python3.8 | Amazon Linux 2 | x86\_64, arm64 |
| Python 3.7 | python3.7 | Amazon Linux 2 | x86\_64 |
| Java 17 | java17 | Amazon Linux 2 | x86\_64, arm64 |
| Java 11 | java11 | Amazon Linux 2 | x86\_64, arm64 |
| Java 8 | java8.al2 | Amazon Linux 2 | x86\_64, arm64 |
| Java 8 | java8 | Amazon Linux 2 | x86\_64 |
| .NET 6 | dotnet6 | Amazon Linux 2 | x86\_64, arm64 |
| Go 1.x | go1.x | Amazon Linux 2 | x86\_64 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for JetBrains. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-jetbrains` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
