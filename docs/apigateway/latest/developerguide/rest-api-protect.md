---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-protect.html
---

# Protect your REST APIs in API Gateway
<a name="rest-api-protect"></a>

API Gateway provides a number of ways to protect your API from certain threats, like malicious users or spikes in traffic. You can protect your API using strategies like generating SSL certificates, configuring a web application firewall, setting throttling targets, and only allowing access to your API from a Virtual Private Cloud (VPC). In this section you can learn how to enable these capabilities using API Gateway.

**Topics**
+ [Require client certificates for your API with mutual TLS authentication in API Gateway](rest-api-mutual-tls.md)
+ [Present client certificates to backend services with mutual TLS in API Gateway](rest-api-backend-authentication.md)
+ [Use AWS WAF to protect your REST APIs in API Gateway](apigateway-control-access-aws-waf.md)
+ [Throttle requests to your REST APIs for better throughput in API Gateway](api-gateway-request-throttling.md)
+ [Private REST APIs in API Gateway](apigateway-private-apis.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
