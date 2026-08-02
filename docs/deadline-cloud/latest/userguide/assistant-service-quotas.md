---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/userguide/assistant-service-quotas.html
---

# Service quotas and throttling
<a name="assistant-service-quotas"></a>

The assistant uses on-demand inference, which is subject to your account's service quotas. The two primary constraints are:
+ **Requests per minute (RPM)** – The number of model invocation requests allowed per minute.
+ **Tokens per minute (TPM)** – The total number of input and output tokens processed per minute.

Default quotas vary by Region. Some Regions have lower default limits (as low as 20 RPM), which might result in throttling during heavy assistant usage.

## Requesting a quota increase
<a name="assistant-quota-increase"></a>

If you experience throttling errors when using the assistant, you can request a service quota increase:

**To request a quota increase**

1. Open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/).

1. In the navigation pane, choose **AWS services**, then choose ****.

1. Find the quota for the model used by the assistant (look for quotas related to `InvokeModelWithResponseStream` for the relevant model).

1. Choose the quota name, then choose **Request increase at account level**.

1. Enter your desired quota value and submit the request.

For more information, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*.

**Note**
If your Region uses cross-region inference, the service quotas in the destination Regions also apply. Cross-region inference profiles support a minimum of 200 RPM, which can help alleviate throttling in Regions with lower single-Region limits.

## Monitoring quota usage
<a name="assistant-quota-monitoring"></a>

You can monitor your quota usage through CloudWatch metrics. Set up CloudWatch alarms on throttling metrics to proactively identify when you are approaching your quota limits. For more information, see [Monitoring ](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-overview.html) in the * User Guide*.
