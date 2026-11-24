---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/security-iam-apiportal.html
---

# Identity and access management for API Portal

API Portal is a feature of API Gateway with its own IAM service prefix, `apiportal`. Use identity-based policies to control which principals can enable discovery, view the API inventory, promote APIs to managed APIs, and create products and documentation portals. API Portal doesn't support resource-based policies.

## API Portal actions and resources
<a name="security-iam-apiportal-actions"></a>

Policy actions for API Portal use the `apiportal:` prefix, for example `apiportal:PutDiscoveryConfiguration`, `apiportal:ListApiInventoryItems`, `apiportal:CreateManagedApi`, `apiportal:CreateProduct`, and `apiportal:CreatePortal`. API Portal resources have the following ARN formats.

| Resource | ARN format |
| --- | --- |
| Discovery configuration (account scope) | arn:aws:apiportal:{{region}}:{{account-id}}:discoveryconfiguration |
| Organization discovery configuration | arn:aws:apiportal:{{region}}:{{management-account-id}}:orgdiscoveryconfiguration |
| Managed API | arn:aws:apiportal:{{region}}:{{account-id}}:managedapis/{{managed-api-id}} |
| Product | arn:aws:apiportal:{{region}}:{{account-id}}:products/{{product-id}} |
| Product page | arn:aws:apiportal:{{region}}:{{account-id}}:products/{{product-id}}/productpages/{{product-page-id}} |
| Product API page | arn:aws:apiportal:{{region}}:{{account-id}}:products/{{product-id}}/apipages/{{api-page-id}} |
| Product sharing policy | arn:aws:apiportal:{{region}}:{{account-id}}:products/{{product-id}}/sharingpolicy |
| Documentation portal | arn:aws:apiportal:{{region}}:{{account-id}}:portals/{{portal-id}} |

All API Portal resources support tags, so you can also control access with the `aws:ResourceTag`, `aws:RequestTag`, and `aws:TagKeys` condition keys. For the full list of actions, resources, and condition keys, see [Actions, resources, and condition keys for API Portal](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonapigatewayapiportal.html) in the *Service Authorization Reference*.

## API Portal identity-based policy examples
<a name="security-iam-apiportal-examples"></a>

The following policy lets a principal view the API inventory and managed APIs in one Region without changing anything.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ViewApiInventory",
      "Effect": "Allow",
      "Action": [
        "apiportal:GetDiscoveryConfiguration",
        "apiportal:ListDiscoveryStatuses",
        "apiportal:ListApiInventoryItems",
        "apiportal:GetApiInventoryItem",
        "apiportal:ListManagedApis",
        "apiportal:GetManagedApi"
      ],
      "Resource": [
        "arn:aws:apiportal:us-east-1:{{111122223333}}:discoveryconfiguration",
        "arn:aws:apiportal:us-east-1:{{111122223333}}:managedapis/*"
      ]
    }
  ]
}
```

The following policy lets a principal manage the products and documentation portals that are tagged `team=payments`, and create new ones only with that tag.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ManageTaggedPortalsAndProducts",
      "Effect": "Allow",
      "Action": [
        "apiportal:GetPortal",
        "apiportal:UpdatePortal",
        "apiportal:UpdatePortalPublishStatus",
        "apiportal:GetProduct",
        "apiportal:UpdateProduct",
        "apiportal:AssociateManagedApis",
        "apiportal:DisassociateManagedApis"
      ],
      "Resource": [
        "arn:aws:apiportal:us-east-1:{{111122223333}}:portals/*",
        "arn:aws:apiportal:us-east-1:{{111122223333}}:products/*"
      ],
      "Condition": {
        "StringEquals": { "aws:ResourceTag/team": "payments" }
      }
    },
    {
      "Sid": "CreateWithTeamTag",
      "Effect": "Allow",
      "Action": [
        "apiportal:CreatePortal",
        "apiportal:CreateProduct"
      ],
      "Resource": [
        "arn:aws:apiportal:us-east-1:{{111122223333}}:portals/*",
        "arn:aws:apiportal:us-east-1:{{111122223333}}:products/*"
      ],
      "Condition": {
        "StringEquals": { "aws:RequestTag/team": "payments" },
        "ForAllValues:StringEquals": { "aws:TagKeys": ["team"] }
      }
    }
  ]
}
```

The following policy lets a principal in a delegated administrator account manage organization-wide discovery. Replace the account ID with your organization's management account.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ManageOrganizationDiscovery",
      "Effect": "Allow",
      "Action": [
        "apiportal:GetOrganizationDiscoveryConfiguration",
        "apiportal:PutOrganizationDiscoveryConfiguration",
        "apiportal:StartDiscovery",
        "apiportal:StopDiscovery",
        "apiportal:ListDiscoveryStatuses"
      ],
      "Resource": "arn:aws:apiportal:us-east-1:{{999999999999}}:orgdiscoveryconfiguration"
    }
  ]
}
```

Only the management account can enable trusted access and register delegated administrators. Those actions are authorized through AWS Organizations, not API Portal. For more information, see [Enable discovery for your AWS Organization](apiportal-enable-discovery.md#apiportal-enable-discovery-organization).

## Service-linked role for API Portal
<a name="security-iam-apiportal-slr"></a>

API Portal uses the service-linked role **AWSServiceRoleForAPIPortal** to read your AWS Organizations organization and to manage the AWS Config configuration recorder that discovery uses. API Portal creates the role in your account when you enable discovery, and in each member account when you enable organization-wide discovery. For organization-wide discovery, the role must exist in the management account.

The role trusts the `apiportal.amazonaws.com` service principal to assume it. Its permissions policy allows the following actions.
+ `organizations:DescribeAccount`, `organizations:DescribeOrganization`, `organizations:DescribeOrganizationalUnit`, `organizations:ListAccounts`, `organizations:ListParents`, `organizations:ListChildren`, `organizations:ListDelegatedAdministrators`, and `organizations:ListAWSServiceAccessForOrganization` on all resources, to resolve the accounts and organizational units in scope for discovery and to confirm trusted access and delegated administrators.
+ `config:PutServiceLinkedConfigurationRecorder`, `config:DescribeConfigurationRecorders`, `config:DescribeConfigurationRecorderStatus`, `config:DeleteServiceLinkedConfigurationRecorder`, `config:AssociateResourceTypes`, and `config:DisassociateResourceTypes` on configuration recorders whose name contains `ConfigurationRecorderForAPIPortal`, to record only the resource types that discovery needs.
+ `iam:CreateServiceLinkedRole` for `config.amazonaws.com`, so that AWS Config can create its own service-linked role if it doesn't exist.
+ `wafv2:ListEvents` on all resources, to retrieve the AWS WAF API Security events shown for your managed APIs.

You can't edit the role's permissions. To delete the role, first delete your discovery configuration and documentation portals, and then delete the role in the IAM console. In the management account, you must also disable trusted access for API Portal in AWS Organizations before you can delete the role. If API Portal is still using the role, the deletion fails. For general information about service-linked roles, see [Using service-linked roles for API Gateway](using-service-linked-roles.md).
