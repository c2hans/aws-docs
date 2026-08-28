---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-backend-authentication.html
---

# Present client certificates to backend services with mutual TLS in API Gateway
<a name="rest-api-backend-authentication"></a>

API Gateway can present a client certificate to your backend during the TLS handshake. Your backend can then verify that requests come from API Gateway. This creates a mutual TLS connection between API Gateway and your backend service.

You can choose from two approaches:
+ **AWS Certificate Manager (ACM) certificates** – Import your own CA-signed certificate from ACM and attach it to your API stage. With this approach, you get full certificate chains, automatic renewal, and integration with your existing PKI infrastructure.
+ **API Gateway-generated certificates** – Generate a self-signed certificate in API Gateway. This approach requires no external certificate infrastructure. The certificate expires after 365 days and must be rotated manually.

**Topics**
+ [How backend client certificate authentication works](rest-api-backend-auth-overview.md)
+ [Use your own ACM certificate for backend mutual TLS in API Gateway](rest-api-acm-client-certificates.md)
+ [Use an API Gateway-generated certificate for backend authentication in API Gateway](getting-started-client-side-ssl-authentication.md)
+ [API Gateway-supported certificate authorities for HTTP and HTTP proxy integrations in API Gateway](api-gateway-supported-certificate-authorities-for-http-endpoints.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
