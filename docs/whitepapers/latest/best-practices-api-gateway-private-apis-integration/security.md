---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-api-gateway-private-apis-integration/security.html
---

# Security
<a name="security"></a>

 Private APIs and private integration offer an extra layer of security from a network standpoint, because communications are limited within a private network. However, malicious users can potentially gain access to private networks, so it’s a best practice to implement an authorizer for APIs. REST and WebSocket offer the same set of authorizers, such as IAM, Amazon Cognito, and Lambda authorizers. HTTP APIs support IAM, Lambda authorizers, and JSON Web Token (JWT) authorizers. Amazon Cognito can also be used with HTTP APIs through the JWT authorizer. [Serverless Application Lens](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html) covers [identity and access management](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/identity-and-access-management.html) in serverless API in depth.

 *Table 3 – Authorizations *

|  Authorization type  |  Available API type  |  Use case  |
| --- | --- | --- |
|  IAM  |  REST, WebSocket, HTTP  |  If clients have IAM user or role credentials, they can sign the request with IAM credentials.  |
|  Amazon Cognito  |  REST, WebSocket  |  This is commonly used for web and mobile applications where end users log in through Amazon Cognito user pools or federated identity providers.  |
|  Lambda  |  REST, WebSocket, HTTP  |  A Lambda authorizer enables developers to design a business logic around authorization. This can act as a JWT. authorizer, or validate other types of tokens.  |
|  JWT  |  HTTP  |  The JWT authorizer is available only for HTTP APIs, and allows clients to pass a JWT token, including tokens from Amazon Cognito.  |

 Enable [API Gateway Access Logs](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html) and selectively choose data you need as logs might contain sensitive data.

 It is recommended to setup basic API Gateway request validation as a first step to ensure that the request adheres to the configured JSON-schema, and has the required parameter query strings and headers.

 Learn more in the Security pillar of the [Serverless Well-Architected Whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/security-pillar.html).

## TLS considerations
<a name="tls-considerations"></a>
+  Private REST APIs support TLS 1.2 only. Earlier TLS versions are not supported. If you make a request using HTTP/2 protocol, the request is enforced to use HTTP/1.1 protocol.
+  Private custom domain names use the TLS-1-2 security policy. You cannot configure a different security policy for private custom domain names.
+  Public custom domain names support enhanced TLS 1.3 security policies (announced October 2023). These policies provide improved performance and security for public-facing APIs. TLS 1.3 enhanced policies do not apply to private custom domain names. For more information, see [Security policies for custom domain names in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-custom-domain-tls-version.html).
