---
source_url: https://docs.aws.amazon.com/PRM/latest/aws-prm-onboarding-guide/included-aws-services-marketplace-metering.html
---

# Included AWS Services
<a name="included-aws-services-marketplace-metering"></a>

Partner Revenue Measurement automatically measures service consumption for Amazon Machine Image (AMI) and Machine Learning (ML) products listed on AWS Marketplace. The following services are supported:

**AWS Marketplace Metering Included Services**

| Service Name | Product Service Code | Notes |
| --- | --- | --- |
| Amazon EC2 | AmazonEC2 | Amazon Machine Image (AMI) products |
| Amazon SageMaker AI | AmazonSageMaker | Machine Learning (ML) products |

**Note**
Partner Revenue Measurement intends to support all AWS services. We recommend that you instrument PRM on all AWS services and resources that your partner solution interacts with to avoid on-going operational changes as service coverage expands. At this time, revenue attribution data is surfaced for the services listed above. Any partial spend captured on services not listed above is aggregated as "Other".

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Revenue Measurement. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query PRM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
