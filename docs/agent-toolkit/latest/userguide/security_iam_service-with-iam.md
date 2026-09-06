---
source_url: https://docs.aws.amazon.com/agent-toolkit/latest/userguide/security_iam_service-with-iam.html
---

# How AWS MCP Server works with IAM
<a name="security_iam_service-with-iam"></a>

AWS MCP Server uses a simplified authorization model that works like the AWS Command Line Interface (AWS CLI) and AWS SDKs. The server does not define its own IAM actions, resources, or service-specific condition keys. Instead, it authenticates your request using [SigV4](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html), adds standardized condition context keys, and forwards the request to the downstream AWS service. The downstream service performs the authorization check using your existing IAM policies. This means your AI agents work with your existing AWS credentials and service-level permissions, and you do not need to configure separate MCP-specific IAM actions.

## Authorization flow
<a name="security_iam_service-with-iam-authorization-flow"></a>

When an AI agent calls the AWS MCP Server, the following authorization flow occurs:

1. Your agent's request is authenticated with your AWS credentials using [SigV4](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html). The [MCP Proxy for AWS](https://github.com/aws/mcp-proxy-for-aws) handles this signing automatically between your host application and the server.

1. AWS MCP Server authenticates the request and adds the MCP condition context keys (`aws:ViaAWSMCPService` and `aws:CalledViaAWSMCP`).

1. AWS MCP Server forwards the request to the target AWS service.

1. The target AWS service authorizes the request using your existing IAM policies, which can reference the MCP condition context keys for fine-grained control.

## MCP condition context keys
<a name="security_iam_service-with-iam-id-based-policies-conditionkeys"></a>

AWS MCP Server automatically adds the following global condition context keys to all requests it forwards to downstream AWS services. You can use these keys in IAM policies and service control policies (SCPs) to differentiate between requests made through an AWS managed MCP server and direct API calls.

`aws:ViaAWSMCPService`
A Boolean key set to `true` for any request that passes through an AWS managed MCP server. Use this key to allow or deny all actions initiated through any AWS managed MCP server.
Type: Boolean

`aws:CalledViaAWSMCP`
A single-valued string key containing the service principal of the specific AWS managed MCP server that initiated the request. Use this key to apply controls for a specific MCP server.
Type: String
Example values:
+ `aws-mcp.amazonaws.com` – AWS MCP Server
+ `eks-mcp.amazonaws.com` – Amazon EKS MCP Server
+ `ecs-mcp.amazonaws.com` – Amazon ECS MCP Server

For more information about global condition context keys, see [IAM condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

## OAuth condition keys for AWS Sign-in
<a name="security_iam_service-with-iam-oauth-conditionkeys"></a>

When you use OAuth authentication with AWS MCP Server through AWS Sign-in, the following service-specific condition keys are available in the `signin:` namespace. Use these keys in IAM policies and SCPs to govern how OAuth is used within your organization.

`signin:OAuthClientId`
The ARN of the OAuth client making the request. Use this key to allow only approved OAuth clients to access AWS MCP Server.
Type: String (ARN)
Applies to: `signin:AuthorizeOAuth2Access`, `signin:CreateOAuth2Token`

`signin:OAuthRedirectUri`
The redirect URI used in the authorization request. Use this key to restrict token delivery to trusted redirect URIs such as localhost or corporate domains.
Type: String
Applies to: `signin:AuthorizeOAuth2Access`

`signin:OAuthGrantType`
The OAuth grant type being used. Use this key to control which OAuth authorization flows are permitted.
Type: String
Example values: `authorization_code`, `refresh_token`, `client_credentials`
Applies to: `signin:CreateOAuth2Token`

`signin:OAuthClientAuthentication`
The client authentication method used. Use this key to require specific authentication methods.
Type: String
Example values: `none`, `client_secret_basic`, `client_secret_post`
Applies to: `signin:CreateOAuth2Token`

OAuth access tokens carry the `aws:SignInSessionArn` global condition key. This key contains the unique ARN of the AWS Sign-in session.

For more information about OAuth condition keys, see [OAuth condition keys reference](https://docs.aws.amazon.com/signin/latest/userguide/reference-signin-condition-keys.html) in the *AWS Sign-in User Guide*. For OAuth authentication setup and governance examples, see [OAuth 2.1 authentication for AWS MCP Server](oauth-authentication.md).

## Identity-based policies
<a name="security_iam_service-with-iam-id-based-policies"></a>

**Supports identity-based policies:** Yes

Because AWS MCP Server forwards requests to downstream AWS services using your credentials, the IAM policies attached to your IAM user or role determine what actions the MCP server can perform on your behalf. No additional IAM configuration is required to use AWS MCP Server beyond the permissions you already grant for direct API access.

You can use the MCP condition context keys in your existing policies to apply different permissions when actions are initiated through an MCP server. For examples, see [Identity-based policy examples for AWS MCP Server](security_iam_id-based-policy-examples.md).

## Using temporary credentials with AWS MCP Server
<a name="security_iam_service-with-iam-roles-tempcreds"></a>

**Supports temporary credentials:** Yes

AWS MCP Server works with temporary credentials obtained through AWS STS. When you authenticate with AWS MCP Server, you can use temporary credentials from IAM roles, federated identities, or assumed roles. The server forwards these credentials to downstream AWS services, which honor the same session policies and permission boundaries as direct API calls.

## Deprecated MCP-specific IAM actions
<a name="security_iam_service-with-iam-deprecated-actions"></a>

During the preview period, AWS MCP Server required the following service-specific IAM actions:
+ `aws-mcp:InvokeMcp`
+ `aws-mcp:CallReadOnlyTool`
+ `aws-mcp:CallReadWriteTool`

These actions are no longer required and have no effect. If you previously configured IAM permissions using these actions, we recommend that you remove them from your policies. If you used these actions in Deny statements to block access to AWS MCP Server, you must update your policies to use the `aws:ViaAWSMCPService` or `aws:CalledViaAWSMCP` condition context keys instead.
