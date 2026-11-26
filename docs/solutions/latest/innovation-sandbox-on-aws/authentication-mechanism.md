---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/authentication-mechanism.html
---

# Authentication mechanism

Innovation Sandbox on AWS authenticates web UI users with [Amazon Cognito](https://aws.amazon.com/cognito/), which federates to the [Single Sign-On service](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) from [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/) using the [SAML 2.0](https://aws.amazon.com/identity/saml/) protocol. You register a SAML 2.0 application in IAM Identity Center and provide its metadata URL to the solution; Amazon Cognito acts as the SAML service provider.

When a user signs in, Amazon Cognito completes the SAML flow with IAM Identity Center and issues an ID token. A Cognito Pre Token Generation trigger resolves your IAM Identity Center group memberships and adds the corresponding solution roles (Admin, Manager, or User) to the token. A Cognito identity pool then exchanges the ID token for temporary IAM credentials mapped to one of three role tiers.

The web UI signs every API request with those temporary credentials using AWS Signature Version 4 (SigV4). It also includes the Cognito ID token in a signed `x-isb-identity` header. API Gateway authorizes requests natively using IAM authorization and does not require a custom Lambda authorizer. Handler-side middleware verifies the `x-isb-identity` token and enforces role-based access control.

The solution API can also be called from other custom clients; see [Machine-to-machine (M2M) access](m2m-access.md) and [Remote MCP server](mcp-server.md).

Sandbox Spaces chat uses a WebSocket connection instead of REST requests. The web UI opens the connection with a SigV4 presigned URL that expires after 60 seconds.

The MCP server uses a separate public Amazon Cognito app client. The app client signs users in with the authorization code flow and Proof Key for Code Exchange (PKCE) through the same SAML federation. A client on the user’s computer exchanges the resulting ID token for the same temporary IAM credentials that the web UI uses. For more information, see [MCP server](mcp-server-architecture.md).

You sign in to sandbox accounts from the Applications tab on the [AWS access portal](https://docs.aws.amazon.com/singlesignon/latest/userguide/using-the-portal.html).
