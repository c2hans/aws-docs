---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-portal-quotas.html
---

# Quotas for configuring portals in API Gateway
<a name="api-gateway-portal-quotas"></a>

The following quotas apply to creating portals in API Gateway. For more information, see [API Gateway portals](apigateway-portals.md).

| Resource or operation | Default quota | Can be increased |
| --- | --- | --- |
| Portals per account | 15 | Yes |
| Portal products per portal | 200 | No |
| Portal products per account | 500 | No |
| Product REST endpoint pages per portal product | 40 | Yes |
| Product pages per portal product | 40 | Yes |
| Logo size | 200 KB | No |
| Documentation page size per product REST endpoint page | 32,000 characters | No |
| Custom page size for product pages | 32,000 characters | No |
| Custom domain names per portal | 1 | No |
| Authorizers per portal | 1 | No |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
