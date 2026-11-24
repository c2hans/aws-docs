---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apiportal-inventory.html
---

# The API inventory in API Portal

The **API inventory** page lists the APIs that discovery has found. The summary at the top shows **Discovery status**, **Discovery source** (single account or AWS Organization), and **Scanned services** with the current scan state of each.

Each inventory item has the following columns.

| Column | Description |
| --- | --- |
| API | The HTTP method and path, for example GET /v1/payments. |
| Host | The hostname that serves the endpoint. When ten or more hosts differ only in one label, they're shown as one row with <\*> in place of that label. |
| Source service | The service that fronts the API: API Gateway (REST APIs), Application Load Balancer (ALB), or CloudFront. |
| Account ID | The AWS account that owns the resource. |
| Visibility | Public or Private. |
| WAF status | Whether an AWS WAF web ACL is associated with the resource. |
| Workloads | AI protocols seen in the API's traffic (MCP, A2A, LLM), when AI endpoint identification is enabled. |
| Classification | Shadow, Managed, Managed (zombie), or Managed (orphaned). For a managed API, also whether it's managed by your account or by another account in your organization. |

The resource ARN identifies the front-door resource that serves the API. For Application Load Balancer, it's the listener ARN; for CloudFront, the distribution ARN; for API Gateway, it's the stage ARN combined with the method ARN, because an API is discovered per deployed stage.

**Note**
If an API Gateway REST API is also fronted by CloudFront or an Application Load Balancer, the inventory shows a separate row for each front door. These aren't duplicates: each row is the API as seen through that entry point.

Choose an API to open its detail page, which shows its method, path, host, port, resource ARN, source service, visibility, AWS WAF status, and when it was first and last seen. Security posture findings are available only after you promote the API. See [Managed APIs in API Portal](apiportal-managed-apis.md).
