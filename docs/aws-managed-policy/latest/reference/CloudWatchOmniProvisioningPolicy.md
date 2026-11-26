---
source_url: https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchOmniProvisioningPolicy.html
---

# CloudWatchOmniProvisioningPolicy

**Description**: Provides permissions to set up CloudWatch Omni in an AWS Organizations member account on behalf of the organization's administrator.

`CloudWatchOmniProvisioningPolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="CloudWatchOmniProvisioningPolicy-how-to-use"></a>

You can attach `CloudWatchOmniProvisioningPolicy` to your users, groups, and roles.

## Policy details
<a name="CloudWatchOmniProvisioningPolicy-details"></a>
+ **Type**: AWS managed policy
+ **Creation time**: November 23, 2026, 22:27 UTC
+ **Edited time:** November 23, 2026, 22:27 UTC
+ **ARN**: `arn:aws:iam::aws:policy/CloudWatchOmniProvisioningPolicy`

## Policy version
<a name="CloudWatchOmniProvisioningPolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request.

## JSON policy document
<a name="CloudWatchOmniProvisioningPolicy-json"></a>

```json
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "CreateAndListSpaces",
      "Effect" : "Allow",
      "Action" : [
        "cloudwatch:CreateSpace",
        "cloudwatch:ListSpaces"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "ReadAndDeleteSpaces",
      "Effect" : "Allow",
      "Action" : [
        "cloudwatch:GetSpace",
        "cloudwatch:DeleteSpace"
      ],
      "Resource" : "arn:aws:cloudwatch:*:*:space/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "ManageDatasetIntegrations",
      "Effect" : "Allow",
      "Action" : [
        "observabilityadmin:CreateDatasetIntegration",
        "observabilityadmin:GetDatasetIntegration",
        "observabilityadmin:DeleteDatasetIntegration"
      ],
      "Resource" : "arn:aws:observabilityadmin:*:*:dataset-integration/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "ListDatasetIntegrations",
      "Effect" : "Allow",
      "Action" : "observabilityadmin:ListDatasetIntegrations",
      "Resource" : "*"
    },
    {
      "Sid" : "ReadDatasetEncryption",
      "Effect" : "Allow",
      "Action" : "cloudwatch:GetDataset",
      "Resource" : "arn:aws:cloudwatch:*:*:dataset/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "PassSpaceRoles",
      "Effect" : "Allow",
      "Action" : "iam:PassRole",
      "Resource" : [
        "arn:aws:iam::*:role/service-role/CloudWatchOmniSpaceDataAccessRole-Org*",
        "arn:aws:iam::*:role/service-role/AgentCoreEvaluationRole-Org*"
      ],
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}",
          "iam:PassedToService" : "cloudwatch.amazonaws.com"
        }
      }
    },
    {
      "Sid" : "PassDatasetIntegrationRole",
      "Effect" : "Allow",
      "Action" : "iam:PassRole",
      "Resource" : "arn:aws:iam::*:role/service-role/CloudWatchOmniDatasetIntegrationRole-Org*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}",
          "iam:PassedToService" : "logs.amazonaws.com"
        }
      }
    },
    {
      "Sid" : "ValidateIdentityCenterRegion",
      "Effect" : "Allow",
      "Action" : "sso:ListRegions",
      "Resource" : "arn:aws:sso:::instance/*"
    },
    {
      "Sid" : "DecryptIdentityCenterCmkForRegionCheck",
      "Effect" : "Allow",
      "Action" : "kms:Decrypt",
      "Resource" : "arn:aws:kms:*:*:key/*",
      "Condition" : {
        "StringLike" : {
          "kms:EncryptionContext:aws:sso:instance-arn" : "arn:aws:sso:::instance/*",
          "kms:ViaService" : "sso.*.amazonaws.com"
        },
        "StringEquals" : {
          "aws:ResourceOrgID" : "${aws:PrincipalOrgID}"
        }
      }
    }
  ]
}
```

## Learn more
<a name="CloudWatchOmniProvisioningPolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html)
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html)
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)
