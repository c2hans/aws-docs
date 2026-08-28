---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/ca-regions.html
---

# Call analytics service quotas for the Amazon Chime SDK
<a name="ca-regions"></a>

The tables in this section list the service quotas for Amazon Chime SDK call analytics.

For more information about the call analytics Regions, refer to [Available AWS Regions for the Amazon Chime SDK](sdk-available-regions.md), earlier in this guide.

Amazon Chime SDK call analytics and voice analytics have the following service quotas.

| Resource | Default limit | Adjustable |
| --- | --- | --- |
| Media Insights Pipeline Configurations per region | 100 | Yes |
| Active Media Insights Pipelines per region | 20 | Yes |
| Voice profile domains per region | 3 | Yes |
| Voice profiles per voice profile domain | 20 | Yes |
| Active speaker search tasks per region | 25 | Yes |
| Active voice tone analysis tasks per region | 25 | Yes |
| Active Voice Connector calls with voice analytics per region | 25 | Yes |
| Active speaker search tasks per Voice Connector call per transaction ID | 1 | No |
| Active voice tone analysis task per Voice Connector call per transaction ID | 1 | No |
| Maximum concurrent API calls per voice profile domain | 1 | Yes |
| Maximum concurrent API calls per voice profile | 1 | Yes |
| Maximum concurrent API calls per speaker search task | 1 | Yes |
| Maximum concurrent API calls per voice tone analysis task | 1 | Yes |

For more information about API rates and quotas, refer to [Amazon Chime SDK endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/chime-sdk.html) in the *AWS General Reference*.

**Note**
If you exceed the quota for any Region, you receive a **Resource Limit Exceeded** exception. You can use the **Service Quotas** page in the AWS console to request an increase, or you can contact your [customer support representative](https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html).
Several of the call analytics APIs create resources and API requests for other AWS services. Those additional count against your account's quotas. If you request a quota or transactions-per-second increase from call analytics, you must also request increases for those other AWS services. Otherwise, your requests may be throttled and fail.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
