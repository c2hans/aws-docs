---
source_url: https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AgentRegistryFullAccess.html
---

# AgentRegistryFullAccess
<a name="AgentRegistryFullAccess"></a>

**Description**: Provides full access to AWS Agent Registry

`AgentRegistryFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AgentRegistryFullAccess-how-to-use"></a>

You can attach `AgentRegistryFullAccess` to your users, groups, and roles.

## Policy details
<a name="AgentRegistryFullAccess-details"></a>
+ **Type**: AWS managed policy
+ **Creation time**: August 06, 2026, 18:12 UTC
+ **Edited time:** August 06, 2026, 18:12 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AgentRegistryFullAccess`

## Policy version
<a name="AgentRegistryFullAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request.

## JSON policy document
<a name="AgentRegistryFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AgentRegistryFullAccess",
      "Effect" : "Allow",
      "Action" : "agent-registry:*",
      "Resource" : "arn:aws:agent-registry:*:*:*"
    },
    {
      "Sid" : "AgentRegistryPassRoleAccess",
      "Effect" : "Allow",
      "Action" : "iam:PassRole",
      "Resource" : "arn:aws:iam::*:role/*",
      "Condition" : {
        "StringEquals" : {
          "iam:PassedToService" : "agent-registry.amazonaws.com"
        }
      }
    },
    {
      "Sid" : "AgentRegistryWorkloadIdentityAccess",
      "Effect" : "Allow",
      "Action" : [
        "bedrock-agentcore:CreateWorkloadIdentity",
        "bedrock-agentcore:DeleteWorkloadIdentity",
        "bedrock-agentcore:GetWorkloadAccessToken",
        "bedrock-agentcore:GetWorkloadIdentity"
      ],
      "Resource" : "arn:aws:bedrock-agentcore:*:*:workload-identity-directory/*"
    },
    {
      "Sid" : "AllowGetResourceOauth2TokenForOauthBasedSynchronization",
      "Effect" : "Allow",
      "Action" : [
        "bedrock-agentcore:GetResourceOauth2Token"
      ],
      "Resource" : "arn:aws:bedrock-agentcore:*:*:credential-provider/*"
    },
    {
      "Sid" : "AllowListOauth2CredentialsProvidersForConsolePicker",
      "Effect" : "Allow",
      "Action" : [
        "bedrock-agentcore:ListOauth2CredentialProviders"
      ],
      "Resource" : "arn:aws:bedrock-agentcore:*:*:*"
    },
    {
      "Sid" : "IAMListAccess",
      "Effect" : "Allow",
      "Action" : [
        "iam:ListRoles"
      ],
      "Resource" : "arn:aws:iam::*:role/*"
    },
    {
      "Sid" : "AgentRegistryKMSAccess",
      "Effect" : "Allow",
      "Action" : [
        "kms:Decrypt"
      ],
      "Resource" : "arn:aws:kms:*:*:key/*",
      "Condition" : {
        "StringLike" : {
          "kms:ViaService" : "agent-registry.*.amazonaws.com"
        }
      }
    },
    {
      "Sid" : "AgentRegistrySecretsManagerAccess",
      "Effect" : "Allow",
      "Action" : [
        "secretsmanager:GetSecretValue"
      ],
      "Resource" : "arn:aws:secretsmanager:*:*:secret:*"
    },
    {
      "Sid" : "AgentRegistryServiceLinkedRoleAccess",
      "Effect" : "Allow",
      "Action" : "iam:CreateServiceLinkedRole",
      "Resource" : "arn:aws:iam::*:role/aws-service-role/agent-registry.amazonaws.com/AWSServiceRoleForAgentRegistry",
      "Condition" : {
        "StringLike" : {
          "iam:AWSServiceName" : "agent-registry.amazonaws.com"
        }
      }
    }
  ]
}
```

## Learn more
<a name="AgentRegistryFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html)
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html)
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com//IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com//IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)
