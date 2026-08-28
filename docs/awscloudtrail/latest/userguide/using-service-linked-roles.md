---
source_url: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/using-service-linked-roles.html
---

# Using service-linked roles for CloudTrail
<a name="using-service-linked-roles"></a>

AWS CloudTrail uses AWS Identity and Access Management (IAM) [ service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to CloudTrail. Service-linked roles are predefined by CloudTrail and include all the permissions that the service requires to call other AWS services on your behalf.

**Topics**
+ [Using roles for creating and managing CloudTrail organization trails and CloudTrail Lake organization event data stores in CloudTrail](using-service-linked-roles-create-slr-for-org-trails.md)
+ [Supported Regions for CloudTrail service-linked roles](#slr-regions-create-slr-for-org-trails)
+ [Using roles for creating and managing CloudTrail event context in CloudTrail](using-service-linked-roles-create-slr-for-context-management.md)
+ [Supported Regions for CloudTrail service-linked roles](#slr-regions-create-slr-for-context-management)

## Supported Regions for CloudTrail service-linked roles
<a name="slr-regions-create-slr-for-org-trails"></a>

CloudTrail supports using service-linked roles in all of the AWS Regions where CloudTrail and Organizations are both available. For more information, see [AWS Regions and endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html) in the *AWS General Reference*.

## Supported Regions for CloudTrail service-linked roles
<a name="slr-regions-create-slr-for-context-management"></a>

CloudTrail supports using service-linked roles in all of the Regions where CloudTrail and EventBridge are available. For more information, see [AWS Regions and endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudTrail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awscloudtrail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
