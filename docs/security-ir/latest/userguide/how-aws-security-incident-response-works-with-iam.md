---
source_url: https://docs.aws.amazon.com/security-ir/latest/userguide/how-aws-security-incident-response-works-with-iam.html
---

# How AWS Security Incident Response Works with IAM
<a name="how-aws-security-incident-response-works-with-iam"></a>

 AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources. IAM administrators control who can be *authenticated* (signed in) and *authorized* (have permissions) to use AWS Security Incident Response resources. IAM is an AWS service that you can use with no additional charge.

|  IAM features that you can use with AWS Security Incident Response  |   |
| --- | --- |
| *IAM feature* | *Service alignment* |
| Identity-based policies | Yes |
| Resource-based policies | No |
| Policy actions | Yes |
| Policy resources | Yes |
| Policy conditions keys | Yes (global) |
| ACLs | No |
| ABAC (tags in policies) | Yes |
| Temporary credentials | Yes |
| Forward access sessions (FAS) | Yes |
| Service roles | No |
| Service-linked roles | Yes |

**Topics**
+ [Identity-based policies for AWS Security Incident Response](identity-based-policies.md)
+ [Policy condition keys for AWS Security Incident Response](policy-condition-keys-for-aws-security-incident-response.md)
+ [Access control lists (ACLs) in AWS Security Incident Response](access-control-lists-acls-in-aws-security-incident-response.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Incident Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-ir` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
