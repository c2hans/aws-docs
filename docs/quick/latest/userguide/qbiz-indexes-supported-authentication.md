---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/qbiz-indexes-supported-authentication.html
---

# Supported authentication methods
<a name="qbiz-indexes-supported-authentication"></a>

The authentication methods supported depend on your implementation type:

## IDC Implementation
<a name="qbiz-indexes-auth-idc"></a>
+ Amazon Quick: AWS Identity Center authentication only
+ Amazon Q Business: `AWS_IAM_IDC`

## Non-IDC Implementation
<a name="qbiz-indexes-auth-qbiz"></a>
+ Amazon Quick:
  + Native identities (username/password)
  + AWS Managed Microsoft AD
  + IAM federation
+ Amazon Q Business: `AWS_QUICKSIGHT_IDP`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
