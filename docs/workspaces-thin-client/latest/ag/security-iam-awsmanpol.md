---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/security-iam-awsmanpol.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/workspacesthinclient-end-of-support.html).

# AWS managed policies for Amazon WorkSpaces Thin Client
<a name="security-iam-awsmanpol"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

## AWS managed policy: AmazonWorkSpacesThinClientReadOnlyAccess
<a name="security-iam-awsmanpol-AmazonWorkSpacesThinClientReadOnlyAccess"></a>

You can attach the `AmazonWorkSpacesThinClientReadOnlyAccess` policy to your IAM identities. This policy grants full access permissions to the WorkSpaces Thin Client service and its dependencies. For more information on this managed policy, see [ AmazonWorkSpacesThinClientReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonWorkSpacesThinClientReadOnlyAccess.html) in the *AWS Managed Policy Reference guide*.

**Permissions details**

This policy includes the following permissions.
+ `thinclient` (WorkSpaces Thin Client) – Allows read-only access to all WorkSpaces Thin Client actions.
+ `workspaces` (WorkSpaces) – Allows permissions to describe WorkSpaces directories and connection aliases. This is used to check that your WorkSpaces resources are compatible with WorkSpaces Thin Client. It is also used to show these resources in the WorkSpaces Thin Client AWS console.
+ `workspaces-web` (WorkSpaces Secure Browser) – Allows permissions to describe WorkSpaces Secure Browser portals and user settings. This is used to check that your WorkSpaces Secure Browser resources are compatible with WorkSpaces Thin Client. It is also used to show these resources in the WorkSpaces Thin Client AWS console.
+ `appstream` (WorkSpaces Applications) – Allows permissions to describe WorkSpaces Applications stacks. This is used to check that your WorkSpaces Applications resources are compatible with WorkSpaces Thin Client. It is also used to show these resources in the WorkSpaces Thin Client AWS console.

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid": "AllowThinClientReadAccess",
      "Effect": "Allow",
      "Action": [
        "thinclient:GetDevice",
        "thinclient:GetDeviceDetails",
        "thinclient:GetEnvironment",
        "thinclient:GetSoftwareSet",
        "thinclient:ListDevices",
        "thinclient:ListDeviceSessions",
        "thinclient:ListEnvironments",
        "thinclient:ListSoftwareSets",
        "thinclient:ListTagsForResource"
      ],
      "Resource": "*"
    },
    {
      "Sid": "AllowWorkSpacesAccess",
      "Effect": "Allow",
      "Action": [
        "workspaces:DescribeConnectionAliases",
        "workspaces:DescribeWorkspaceDirectories"
      ],
      "Resource": "*"
    },
    {
      "Sid": "AllowWorkSpacesSecureBrowserAccess",
      "Effect": "Allow",
      "Action": [
        "workspaces-web:GetPortal",
        "workspaces-web:GetUserSettings",
        "workspaces-web:ListPortals"
      ],
      "Resource": "*"
    },
    {
      "Sid": "AllowAppStreamAccess",
      "Effect": "Allow",
      "Action": [
        "appstream:DescribeStacks"
      ],
      "Resource": "*"
    }
  ]
}
```

------

## AWS managed policy: AmazonWorkSpacesThinClientFullAccess
<a name="security-iam-awsmanpol-AmazonWorkSpacesThinClientFullAccess"></a>

You can attach the `AmazonWorkSpacesThinClientFullAccess` policy to your IAM identities. This policy grants full access permissions to the WorkSpaces Thin Client service and its dependencies. For more information on this managed policy, see [ AmazonWorkSpacesThinClientFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonWorkSpacesThinClientFullAccess.html) in the *AWS Managed Policy Reference Guide*.

**Permissions details**

This policy includes the following permissions:
+ `thinclient` (WorkSpaces Thin Client) – Allows full access to all WorkSpaces Thin Client actions.
+ `workspaces` (WorkSpaces) – Allows permissions to describe WorkSpaces directories and connection aliases. This is used to check that your WorkSpaces resources are compatible with WorkSpaces Thin Client. It is also used to show these resources in the WorkSpaces Thin Client AWS console.
+ `workspaces-web` (WorkSpaces Secure Browser) – Allows permissions to describe WorkSpaces Secure Browser portals and user settings. This is used to check that your WorkSpaces Secure Browser resources are compatible with WorkSpaces Thin Client. It is also used to show these resources in the WorkSpaces Thin Client AWS console.
+ `appstream` (WorkSpaces Applications) – Allows permissions to describe WorkSpaces Applications stacks. This is used to check that your WorkSpaces Applications resources are compatible with WorkSpaces Thin Client. It is also used to show these resources in the WorkSpaces Thin Client AWS console.
+ `iam` – Allows WorkSpaces Thin Client to create a service-linked role in your account. This role enables WorkSpaces Thin Client to publish metrics to CloudWatch on your behalf.

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid": "AllowThinClientFullAccess",
      "Effect": "Allow",
      "Action": [
        "thinclient:*"
      ],
      "Resource": "*"
    },
    {
      "Sid": "AllowWorkSpacesAccess",
      "Effect": "Allow",
      "Action": [
        "workspaces:DescribeConnectionAliases",
        "workspaces:DescribeWorkspaceDirectories"
      ],
      "Resource": "*"
    },
    {
      "Sid": "AllowWorkSpacesSecureBrowserAccess",
      "Effect": "Allow",
      "Action": [
        "workspaces-web:GetPortal",
        "workspaces-web:GetUserSettings",
        "workspaces-web:ListPortals"
      ],
      "Resource": "*"
    },
    {
      "Sid": "AllowAppStreamAccess",
      "Effect": "Allow",
      "Action": [
        "appstream:DescribeStacks"
      ],
      "Resource": "*"
    },
    {
      "Sid": "AllowCreateServiceLinkedRole",
      "Effect": "Allow",
      "Action": "iam:CreateServiceLinkedRole",
      "Resource": "arn:aws:iam::*:role/aws-service-role/monitoring.thinclient.amazonaws.com/AWSServiceRoleForAmazonWorkSpacesThinClientMonitoring",
      "Condition": {
        "StringEquals": {
          "iam:AWSServiceName": "monitoring.thinclient.amazonaws.com"
        }
      }
    }
  ]
}
```

------

## WorkSpaces Thin Client updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

| Change | Description | Date |
| --- | --- | --- |
| AmazonWorkSpacesThinClientMonitoringServiceRolePolicy – Removed policy | WorkSpaces Thin Client removed the AmazonWorkSpacesThinClientMonitoringServiceRolePolicy section. | November 12, 2025 |
| [AmazonWorkSpacesThinClientFullAccess](#security-iam-awsmanpol-AmazonWorkSpacesThinClientFullAccess) – Updated policy<br />AmazonWorkSpacesThinClientMonitoringServiceRolePolicy – New policy | WorkSpaces Thin Client updated the policy to include service linked roles. | August 26th 2025 |
| [AmazonWorkSpacesThinClientReadOnlyAccess](#security-iam-awsmanpol-AmazonWorkSpacesThinClientReadOnlyAccess) – Updated policy | WorkSpaces Thin Client updated the policy to include limited read permissions for device details and WorkSpaces connection aliases. | January 9th 2025 |
| [AmazonWorkSpacesThinClientFullAccess](#security-iam-awsmanpol-AmazonWorkSpacesThinClientFullAccess) – Updated policy | WorkSpaces Thin Client updated the policy to include limited read permissions for WorkSpaces connection aliases. | January 9th 2025 |
| [AmazonWorkSpacesThinClientReadOnlyAccess](#security-iam-awsmanpol-AmazonWorkSpacesThinClientReadOnlyAccess) – Updated policy | WorkSpaces Thin Client updated the policy to include limited read permissions for WorkSpaces Applications, WorkSpaces Web and WorkSpaces. | August 9th 2024 |
| [AmazonWorkSpacesThinClientFullAccess](#security-iam-awsmanpol-AmazonWorkSpacesThinClientFullAccess) – New policy | Provides full access to Amazon WorkSpaces Thin Client as well as limited access to required related services. | August 9th 2024 |
| [AmazonWorkSpacesThinClientReadOnlyAccess](#security-iam-awsmanpol-AmazonWorkSpacesThinClientReadOnlyAccess) – New policy | Provides read-only access to Amazon WorkSpaces Thin Client and its dependencies. | July 19th 2024 |
| WorkSpaces Thin Client started tracking changes | WorkSpaces Thin Client started tracking changes for its AWS managed policies. | July 19th 2024 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Thin Client. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-thin-client` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
