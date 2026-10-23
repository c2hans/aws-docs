---
source_url: https://docs.aws.amazon.com/agent-toolkit/latest/userguide/security-iam-awsmanpol.html
---

# AWS managed policies for AWS MCP Server
<a name="security-iam-awsmanpol"></a>

To add permissions to users, groups, and roles, it is easier to use AWS managed policies than to write policies yourself. It takes time and expertise to [create IAM customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) that provide your team with only the permissions they need. To get started quickly, you can use our AWS managed policies. These policies cover common use cases and are available in your AWS account. For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

AWS services maintain and update AWS managed policies. You can't change the permissions in AWS managed policies. Services occasionally add additional permissions to an AWS managed policy to support new features. This type of update affects all identities (users, groups, and roles) where the policy is attached. Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available. Services do not remove permissions from an AWS managed policy, so policy updates won't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple services. For example, the **ReadOnlyAccess** AWS managed policy provides read-only access to all AWS services and resources. When a service launches a new feature, AWS adds read-only permissions for new operations and resources. For a list and descriptions of job function policies, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.

## AWSMCPSignInOAuthAccessPolicy
<a name="security-iam-awsmanpol-oauth"></a>

The `AWSMCPSignInOAuthAccessPolicy` managed policy grants the permissions required to use OAuth authentication with AWS MCP Server through AWS Sign-in. Attach this policy to the IAM roles that need to connect to AWS MCP Server using OAuth-compatible MCP clients.

This policy includes the following permissions:
+ `signin:AuthorizeOAuth2Access` — Grants the IAM principal permission to complete the OAuth authorization flow.
+ `signin:CreateOAuth2Token` — Grants the IAM principal permission to obtain OAuth tokens.

The policy allows these actions only on the AWS MCP Server service principal resource. The following policy document shows this restriction.

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AllowOAuthForAWSMCP",
      "Effect" : "Allow",
      "Action" : [
        "signin:AuthorizeOAuth2Access",
        "signin:CreateOAuth2Token"
      ],
      "Resource" : "arn:aws:signin:*:*:service-principal/aws-mcp.amazonaws.com"
    }
  ]
}
```

For more information about OAuth authentication setup, see [OAuth 2.1 authentication for AWS MCP Server](oauth-authentication.md).

## AWS MCP Server updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for AWS MCP Server since this service began tracking these changes.

| Change | Description | Date |
| --- | --- | --- |
| `AWSMCPSignInOAuthAccessPolicy` — New policy | AWS MCP Server added a managed policy for OAuth authentication through AWS Sign-in, granting signin:AuthorizeOAuth2Access and signin:CreateOAuth2Token permissions. | July 8, 2026 |
| AWS MCP Server started tracking changes | AWS MCP Server started tracking changes for its AWS managed policies. | November 30, 2025 |
