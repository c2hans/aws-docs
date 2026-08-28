---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/iam-access-analyzer.html
---

# AWS IAM Access Analyzer
<a name="iam-access-analyzer"></a>

You can run [AWS Identity and Access Management (IAM) Access Analyzer](https://aws.amazon.com/iam/access-analyzer/) policy checks on your IAM policies authored in CloudFormation templates, Terraform plans, and JSON policy documents, using the IAM Access Analyzer in the AWS Toolkit for Visual Studio Code.

IAM Access Analyzer policy checks include policy validation and custom policy checks. Policy validation helps validate your IAM policies according to the standards detailed in the [Grammar of the IAM JSON policy language](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_grammar.html) and AWS [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) topics, located in the *AWS Identity and Access Management* User Guide. Your policy validation findings include security warnings, errors, general warnings, and policy suggestions.

You can also run custom policy checks for new access, based on your security standards. A charge is associated with each custom policy check for new access. For detailed information about pricing, see the [AWS IAM Access Analyzer pricing](https://aws.amazon.com/iam/access-analyzer/pricing/) site. For details about IAM Access Analyzer policy checks, see the [Checks for validating policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-checks-validating-policies.html) topic in the *AWS Identity and Access Management* User Guide.

The following topics describe how to work with IAM Access Analyzer policy checks in the AWS Toolkit for Visual Studio Code.

**Topics**
+ [Working with AWS IAM Access Analyzer](iam-access-analyzer-overview.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for Visual Studio Code. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-vscode` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
