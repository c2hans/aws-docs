---
source_url: https://docs.aws.amazon.com/healthimaging/latest/devguide/security-iam-service-linked-roles.html
---

# Using service-linked roles for HealthImaging
<a name="security-iam-service-linked-roles"></a>

AWS HealthImaging uses AWS Identity and Access Management (IAM) [service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role) that are predefined by the service and include all the permissions that the service requires to call other AWS services on your behalf. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the IAM User Guide.

## Service-linked role permissions for HealthImaging
<a name="slr-permissions"></a>

HealthImaging uses the service-linked role named `AWSServiceRoleForHealthImaging` to perform operations in your AWS account. You need to create this service-linked role if you want HealthImaging to publish metrics about your data stores to CloudWatch.

 The role permissions policy named `AWSHealthImagingServiceRolePolicy` grants permissions for HealthImaging to manage service operations and publish service metrics.

For managed policy updates, see [HealthImaging managed policies](https://docs.aws.amazon.com/healthimaging/latest/devguide/security-iam-awsmanpol.html#security-iam-awsmanpol-updates).

## Creating a service-linked role for HealthImaging
<a name="create-slr"></a>

**Create a service-linked role with the IAM Console**

You can create a service-linked role using the IAM Console by Selecting `AWS Service` as the Trusted entity type, and then `HealthImaging` in the Use case drop down menu.

**Create a service-linked role with the AWS CLI**

In the AWS CLI, run `aws iam create-service-linked-role —aws-service-name medical-imaging.amazonaws.com`

## Deleting a service-linked role for HealthImaging
<a name="delete-slr"></a>

You can delete a service-linked role at any time, but doing so will block HealthImaging from performing actions in your AWS account, such as publishing data store metrics to CloudWatch.

**To manually delete the service-linked role using IAM**

You can use the IAM console, the AWS CLI, or the AWS API to delete the `AWSServiceRoleForHealthImaging` service-linked role. For more information, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*. If you deleted a service-linked role, you can use the role creation process to create a new one.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthImaging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthimaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
