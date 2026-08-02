---
source_url: https://docs.aws.amazon.com/agent-toolkit/latest/userguide/oauth-authentication.html
---

# OAuth 2.1 authentication for AWS MCP Server
<a name="oauth-authentication"></a>

AWS MCP Server supports OAuth 2.1 authorization through AWS Sign-in. OAuth-compatible MCP clients — including Claude Code, Cursor, Gemini CLI, Kiro, and GitHub Copilot — can connect directly to AWS MCP Server. No local proxy software is required. For an overview of how OAuth works with AWS Sign-in, see [OAuth with AWS Sign-in overview](https://docs.aws.amazon.com/signin/latest/userguide/oauth-sign-in-overview.html) and [AWS MCP Server](https://docs.aws.amazon.com/signin/latest/userguide/aws-mcp-server.html) in the *AWS Sign-in User Guide*.

With OAuth, your MCP client authenticates using standard OAuth authorization flows while continuing to rely on existing IAM identities, permissions, and organizational controls. AWS Sign-in acts as the OAuth authorization server, issuing scoped access tokens that AWS MCP Server accepts as bearer tokens.

## Prerequisites
<a name="oauth-prerequisites"></a>

Before using OAuth with AWS MCP Server, ensure the following:
+ **IAM permissions** — The IAM principal must have `signin:AuthorizeOAuth2Access` and `signin:CreateOAuth2Token` actions allowed. You can use the AWS managed policy `AWSMCPSignInOAuthAccessPolicy`, or create a custom policy.
+ **Supported MCP client** — An OAuth-compatible MCP client such as Claude Code, Cursor, Cline, Gemini CLI, Kiro, or GitHub Copilot.

**Attach the managed policy**

```
aws iam attach-role-policy \
  --role-name MyRole \
  --policy-arn arn:aws:iam::aws:policy/AWSMCPSignInOAuthAccessPolicy
```

**Or use a custom IAM policy**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "signin:AuthorizeOAuth2Access",
        "signin:CreateOAuth2Token"
      ],
      "Resource": "arn:aws:signin:*:*:service-principal/aws-mcp.amazonaws.com"
    }
  ]
}
```

## Configure your MCP client for OAuth
<a name="oauth-configure-client"></a>

Add the AWS MCP Server endpoint directly to your MCP client. Unlike the SigV4 proxy method, OAuth-compatible clients connect to the server URL without requiring `mcp-proxy-for-aws` or `uvx`.

------
#### [ Kiro CLI (2.11 or later) ]

```
kiro-cli mcp add --name aws-mcp --url https://aws-mcp.us-east-1.api.aws/mcp
```

------
#### [ Claude Code ]

```
claude mcp add aws-mcp https://aws-mcp.us-east-1.api.aws/mcp --transport http
```

------
#### [ Claude Desktop ]

Add as a remote MCP server with URL: `https://aws-mcp.us-east-1.api.aws/mcp?oauth=initialize`

------
#### [ Cursor ]

Add as a remote MCP server with URL: `https://aws-mcp.us-east-1.api.aws/mcp?oauth=initialize`

------
#### [ Codex ]

```
codex mcp add aws-mcp --url https://aws-mcp.us-east-1.api.aws/mcp?oauth=initialize
```

------
#### [ Gemini CLI ]

```
gemini mcp add aws-mcp https://aws-mcp.us-east-1.api.aws/mcp?oauth=initialize --transport http
```

------

For other clients, see your MCP client documentation for instructions on adding a remote MCP server. Use the endpoint URL `https://aws-mcp.us-east-1.api.aws/mcp` (or the endpoint for your preferred Region).

**Legacy MCP clients**
Some MCP clients might not fully support the latest MCP specification for OAuth discovery. If your client does not automatically initiate the OAuth flow, append the `?oauth=initialize` query parameter to the endpoint URL:

```
https://aws-mcp.us-east-1.api.aws/mcp?oauth=initialize
```
This instructs the server to explicitly trigger the OAuth authorization flow for clients that do not handle it natively.

## Authenticate with OAuth
<a name="oauth-authenticate"></a>

When you first invoke an AWS MCP Server tool, your MCP client opens a browser to AWS Sign-in. Sign in with your existing AWS credentials, review the consent page showing the application requesting access, and authorize access.

After you grant consent, AWS Sign-in issues short-lived OAuth tokens. Your MCP client uses these tokens to interact with AWS MCP Server on your behalf. Access tokens remain valid for 1 hour. AWS Sign-in automatically refreshes them using refresh tokens (valid for up to 12 hours), so you do not need to sign in again during your session.

If you already have an active AWS Sign-in session, AWS Sign-in can reuse that session to complete the authorization flow without requiring you to sign in again.

## OAuth authorization flows
<a name="oauth-flows"></a>

AWS Sign-in supports two authorization flows for accessing AWS MCP Server:

### Interactive user access (Authorization Code flow)
<a name="oauth-interactive-flow"></a>

If you use an MCP client on your local machine, AWS uses the OAuth authorization code flow with Proof Key for Code Exchange (PKCE). This flow supports:
+ Individual developers using IAM users or root users
+ Enterprise users signing in through IAM Identity Center
+ Organizations federating through third-party identity providers such as Okta or Ping

The flow works as follows:

1. The MCP client discovers the authorization server from the AWS MCP Server endpoint and redirects you to AWS Sign-in.

1. You authenticate with your AWS identity (IAM user, Identity Center, or federated identity).

1. You review and approve the consent page showing the permissions requested.

1. AWS Sign-in returns an authorization code to your MCP client.

1. The MCP client exchanges the authorization code for an access token (1-hour validity) and a refresh token.

### Programmatic and agentic access (Client Credentials flow)
<a name="oauth-programmatic-flow"></a>

AI agents and automated applications can access AWS MCP Server without interactive browser sign-in by using the OAuth client credentials flow. The application authenticates using its existing AWS credentials (SigV4) to obtain a short-lived OAuth access token.

This flow is designed for:
+ Headless terminals and developer desktops
+ AWS-managed compute environments that already have credentials
+ AI agents running automated workflows

**Obtain an access token**

Run the following AWS CLI command to request a token:

```
aws signin create-oauth2-token-with-iam \
    --grant-type client_credentials \
    --resource aws-mcp.amazonaws.com \
    --region us-east-1
```

The response includes an access token:

```
{
    "accessToken": "<token>",
    "tokenType": "Bearer",
    "expiresIn": 3597
}
```

Include the value of `accessToken` as an `Authorization: Bearer <token>` header in your MCP client configuration. Check your client's documentation for how to include this header.

AWS Sign-in does not issue a refresh token for the client credentials flow. Access tokens remain valid for 1 hour. For more information, see [AWS MCP Server](https://docs.aws.amazon.com/signin/latest/userguide/aws-mcp-server.html) in the *AWS Sign-in User Guide*.

## Access control for OAuth
<a name="oauth-access-control"></a>

OAuth authorization does not grant additional AWS permissions to the MCP client. The MCP client can only act within the permissions already granted to you. IAM policies, SCPs, RCPs, permission boundaries, and data perimeter controls still determine what actions are allowed.

OAuth access uses short-lived tokens. The same IAM permissions and organizational controls that apply to other forms of AWS access also govern OAuth access.

**Important**
Multi-profile switching for cross-account workflows is not supported with OAuth authentication. If you need to work with multiple AWS accounts in a single session, use SigV4 authentication with the MCP Proxy for AWS. See [Multi-profile support](multi-account-access.md) for setup instructions.

## Governing OAuth access
<a name="oauth-governance"></a>

AWS Sign-in provides condition keys that you can use to control how OAuth is used within your organization. For a complete reference, see [OAuth condition keys reference](https://docs.aws.amazon.com/signin/latest/userguide/reference-signin-condition-keys.html) in the *AWS Sign-in User Guide*.

`signin:OAuthClientId`
Allow only approved OAuth clients by restricting to specific client ARNs.

`signin:OAuthRedirectUri`
Restrict token delivery to trusted redirect URIs, such as localhost or corporate domains.

`signin:OAuthGrantType`
Control which OAuth authorization flows are permitted, such as allowing the authorization code flow while blocking the client credentials flow. Values: `authorization_code`, `refresh_token`, `client_credentials`.

`signin:OAuthClientAuthentication`
Require specific client authentication methods. Values: `none`, `client_secret_basic`, `client_secret_post`.

For example, the following policy restricts OAuth access to localhost redirects only:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "signin:AuthorizeOAuth2Access",
      "Resource": "arn:aws:signin:*:*:service-principal/aws-mcp.amazonaws.com",
      "Condition": {
        "StringLike": {
          "signin:OAuthRedirectUri": [
            "http://localhost:*/*",
            "http://127.0.0.1:*/*"
          ]
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": "signin:CreateOAuth2Token",
      "Resource": "arn:aws:signin:*:*:service-principal/aws-mcp.amazonaws.com"
    }
  ]
}
```

## Token management
<a name="oauth-token-management"></a>

### Token lifecycle
<a name="oauth-token-lifecycle"></a>
+ **Access tokens** — Valid for 1 hour. Bound to the MCP client, MCP server, and user session. Contain encrypted IAM credentials (not exposed to the MCP client).
+ **Refresh tokens** — Valid up to 12 hours. Single-use: each refresh returns a new access token and new refresh token. Re-use of a refresh token invalidates all tokens for that session.

### Token revocation
<a name="oauth-token-revocation"></a>

AWS Sign-in automatically revokes refresh tokens in the following situations:
+ An IAM policy attached to the principal changes
+ The user's password is changed (IAM users, root)
+ The Sign-in session is explicitly revoked

AWS Sign-in also provides token introspection (`signin:IntrospectOAuth2Token`) and token revocation (`signin:RevokeOAuth2Token`) APIs. You can use these APIs to validate the status of individual OAuth tokens and revoke specific refresh tokens without affecting other active sessions.

For example, if a refresh token is accidentally exposed in a source code repository, administrators can revoke only the affected refresh token without requiring users to reauthorize unrelated applications.

## Monitoring OAuth activity
<a name="oauth-monitoring"></a>

AWS CloudTrail records OAuth-related activities, including authorization requests, token issuance, token revocation, and token introspection events. CloudTrail logs capture details such as the OAuth client, target AWS MCP Server, redirect URI, authorization flow, and associated sign-in session.

When you make API calls using OAuth access tokens, AWS includes the `aws:SignInSessionArn` context key. Use this context key to correlate API activity with the originating OAuth sign-in session.

The following example shows a CloudTrail log entry for an `AuthorizeOAuth2Access` event:

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAEXAMPLE:testuser",
        "arn": "arn:aws:sts::111111111111:assumed-role/Admin/testuser",
        "accountId": "111111111111"
    },
    "eventTime": "2026-07-08T05:09:00Z",
    "eventSource": "signin.amazonaws.com",
    "eventName": "AuthorizeOAuth2Access",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "203.0.113.1",
    "requestParameters": {
        "resource": "https://aws-mcp.us-west-2.api.aws/mcp",
        "redirect_uri": "http://127.0.0.1:60432/oauth/callback",
        "code_challenge_method": "S256",
        "client_id": "arn:aws:signin:us-west-2::external-client/dcr/609544da-example"
    },
    "additionalEventData": {
        "success": "true"
    },
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111111111111"
}
```

The following example shows a CloudTrail log entry for a `CreateOAuth2Token` event:

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAEXAMPLE:testuser",
        "arn": "arn:aws:sts::111111111111:assumed-role/Admin/testuser",
        "accountId": "111111111111"
    },
    "eventTime": "2026-07-08T05:10:04Z",
    "eventSource": "signin.amazonaws.com",
    "eventName": "CreateOAuth2Token",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "203.0.113.2",
    "requestParameters": {
        "resource": "https://aws-mcp.us-west-2.api.aws/mcp",
        "client_id": "arn:aws:signin:us-west-2::external-client/dcr/609544da-example"
    },
    "additionalEventData": {
        "signInSessionArn": "arn:aws:signin:us-west-2:111111111111:session/example-uuid",
        "success": "true"
    },
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111111111111"
}
```
