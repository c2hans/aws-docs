---
source_url: https://docs.aws.amazon.com/sap/latest/general/extensions-rise.html
---

# Extensions
<a name="extensions-rise"></a>

You can extend RISE with SAP by using AWS services to improve performance, security, agility, and reduce costs. The following table provides recommended AWS services based on use case.

| Category | Use case |  AWS services |
| --- | --- | --- |
|  [Performance](rise-performance.md)  | SAP Fiori and SAP GUI access with proactive observability |  [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html), [Accelerated Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/accelerated-vpn.html), [AWS Internet Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html)  |
|  [Application integration](application-integration.md)  | Application Integration |  [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) and [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)  |
|  [Archiving and Document Management](document-management.md)  | Archiving and Document Management |  [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html), [AWS S3 File Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/what-is-file-s3.html), [Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)  |
|  [Development and Extension](development-extension.md)  | Development, Compatibility packs and alternatives |  [AWS SDK for SAP ABAP](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/home.html), [AWS Marketplace](https://docs.aws.amazon.com/marketplace/)  |
|  [Security Extension](security-extension.md)  | Single Sign On, Zero Trust Access |  [mTLS Authentication through Amazon ALB](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/mutual-authentication.html), [AWS Verified Access for SAP](https://docs.aws.amazon.com/verified-access/latest/ug/what-is-verified-access.html)  |
|  [Artificial Intelligence](artificial-intelligence.md)  | Generative AI |  [Amazon Q for Business](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/what-is.html), [Amazon QuickSight](https://docs.aws.amazon.com/quicksuite/latest/userguide/quicksight-gen-bi.html), [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for SAP on AWS Technical Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
