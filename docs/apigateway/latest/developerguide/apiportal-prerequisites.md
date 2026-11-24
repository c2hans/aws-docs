---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apiportal-prerequisites.html
---

# Prerequisites for API Portal

Before you enable discovery, make sure you have the following.
+ An AWS account and IAM permissions for API Portal (the `apiportal` service prefix). For the actions, resources, and example policies, see [Identity and access management for API Portal](security-iam-apiportal.md). You don't need to have APIs running before you enable discovery; the inventory fills in as APIs are found.
+ For organization-wide discovery only: you're signed in to the management account of your AWS Organizations organization, or to a registered delegated administrator account, and trusted access for API Portal is enabled. See [Enable discovery for your AWS Organization](apiportal-enable-discovery.md#apiportal-enable-discovery-organization).
+ For a documentation portal that requires sign-in: an Amazon Cognito user pool with an app client and a user pool domain. To also control which products each reader can see (fine-grained access control), an identity pool. See [Control access to a documentation portal with Amazon Cognito](apiportal-portals-access.md).
+ For a documentation portal with a custom domain name: an ACM certificate for the domain in the us-east-1 Region. See [Use a custom domain name for a documentation portal](apiportal-portals-domain.md).

## Service-linked role and AWS Config recorder
<a name="apiportal-prerequisites-service-role"></a>

API Portal uses a service-linked role, `AWSServiceRoleForAPIPortal`, to read your AWS Organizations hierarchy and to manage the AWS Config configuration recorder that discovery uses. API Portal creates the role in your account when you enable discovery. For organization-wide discovery, the role must exist in the management account.

**Note**
Discovery creates a service-linked AWS Config configuration recorder for API Portal in each account and Region where discovery runs. It records only the resource types that discovery needs, and there is no AWS Config charge for it.
