---
source_url: https://docs.aws.amazon.com/marketplace/latest/developerguide/metering-service-quotas.html
---

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Service quotas for AWS Marketplace Metering API
<a name="metering-service-quotas"></a>

 Your AWS account has the following quotas related to the AWS Marketplace Metering service.

**Request quotas**

|  **API action**  | **Request rate (per AWS account)** |  **Description**  |
| --- | --- | --- |
| BatchMeterUsage | 10 per second | The maximum number of BatchMeterUsage requests that you can make, per second, in this account in the current region. |
| MeterUsage | 10 per second | The maximum number of MeterUsage requests that you can make, per second, in this account in the current region. |
| RegisterUsage | 5 per second | The maximum number of RegisterUsage requests that you can make, per second, in this account in the current region. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
