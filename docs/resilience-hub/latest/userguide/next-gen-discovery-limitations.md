---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-discovery-limitations.html
---

# Coverage and known limitations
<a name="next-gen-discovery-limitations"></a>

Dependency discovery covers all DNS queries made through Route 53 resolvers in your VPC, including both IPv4 and IPv6 queries, and queries from Amazon EC2, Amazon ECS, Amazon EKS, and VPC-connected Lambda. The following known limitations apply:

| Limitation | Impact | Workaround |
| --- | --- | --- |
| Non-VPC Lambda | Lambda functions without VPC connectivity are not covered | Connect Lambda functions to VPC |
| Direct IP connections | Connections made by IP address (not DNS) are not discovered | No workaround |
| Infrequent dependencies | Dependencies called less than once per hour may be missed in initial discovery | 35-day lookback catches most; very rare calls may not appear |
| Kubernetes shared tenancy | Multi-tenant Amazon EKS clusters may attribute dependencies to the wrong service | Verify compute resource attribution is correctly mapping resources to services |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
