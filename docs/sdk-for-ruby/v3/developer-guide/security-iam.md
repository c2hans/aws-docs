---
source_url: https://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/security-iam.html
---

# Identity and Access Management for AWS SDK for Ruby
<a name="security-iam"></a>

AWS Identity and Access Management (IAM) is an Amazon Web Services (AWS) service that helps an administrator securely control access to AWS resources. IAM administrators control who can be *authenticated* (signed in) and *authorized* (have permissions) to use resources AWS services. IAM is an AWS service that you can use with no additional charge.

To use AWS SDK for Ruby to access AWS, you need an AWS account and AWS credentials. To increase the security of your AWS account, we recommend that you use an *IAM user* to provide access credentials instead of using your AWS account credentials.

For details about working with IAM, see [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/).

For an overview of IAM users and why they are important for the security of your account, see [AWS Security Credentials](https://docs.aws.amazon.com/general/latest/gr/aws-security-credentials.html) in the [Amazon Web Services General Reference](https://docs.aws.amazon.com/general/latest/gr/).

AWS SDK for Ruby follows the [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model) through the specific Amazon Web Services (AWS) services it supports. For AWS service security information, see the [AWS service security documentation page](https://aws.amazon.com/security/?id=docs_gateway#aws-security) and [AWS services that are in scope of AWS compliance efforts by compliance program](https://aws.amazon.com/compliance/services-in-scope/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Ruby. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-ruby` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
