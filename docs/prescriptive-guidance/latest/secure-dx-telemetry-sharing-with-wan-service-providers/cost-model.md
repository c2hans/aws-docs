---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-dx-telemetry-sharing-with-wan-service-providers/cost-model.html
---

# Cost Model

The framework is designed to be cost-negligible. The primary AWS services used — IAM, STS, and CloudFormation — incur no charges. CloudWatch and CloudTrail usage may incur costs depending on query frequency and logging configuration. If governance validation is implemented (for example, via AWS Config custom rules or scheduled audits), additional costs may apply depending on the chosen mechanism. The following table provides estimated monthly costs for a typical deployment.

|
|
| Service | Cost Driver | Estimated Monthly Cost |
| --- |--- |--- |
| IAM | Roles and policies | $0 |
| STS | AssumeRole API calls | $0 |
| CloudTrail | Management events | First copy of management events to S3 per Region at no charge |
| AWS Config (optional) | If governance validation implemented | Varies by mechanism |
| CloudWatch | GetMetricData API calls | \~$0.01 per 1,000 metrics |
| CloudFormation | Stack management | $0 |

The base cost of the stack is less than $5 per month (CloudWatch API calls and CloudTrail management events). If governance validation is implemented (for example, via AWS Config custom rules or scheduled audits), additional costs may apply based on the chosen mechanism. This cost is negligible compared to the operational savings from reduced MTTR.
