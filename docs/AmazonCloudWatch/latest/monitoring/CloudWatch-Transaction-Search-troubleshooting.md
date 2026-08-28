---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search-troubleshooting.html
---

# Troubleshooting application issues
<a name="CloudWatch-Transaction-Search-troubleshooting"></a>

 With Application Signals, you can troubleshoot rarely occurring latency spikes in your applications. After you enable Transaction Search and configure a head sampling rate capturing 100% of spans, you get complete visibility into any application issue. The following scenario describes how Application Signals can be used with transaction spans to monitor your services and identify service quality issues.

## Example troubleshooting scenario
<a name="w2aac25c21c25b5"></a>

 This scenario focuses on a pet clinic application composed of several micro-services calling third-party payment APIs. These calls have been intermittently slow, thus impacting revenue.

 Jane opens the CloudWatch Application Signals console and notices a customer-service application responsible for registering customers is healthy and not breaching any SLOs.

![CloudWatch Application Signals console.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/troubleshooting1.png)

 She opens the service to investigate any patterns of rarely occurring failures and notices the registration API experienced intermittent p99 latency spikes.

![Intermittent latency spikes.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/troubleshooting2.png)

 Jane chooses a datapoint in the latency chart to view correlated spans. She groups the spans by customer ID to view all the customers who are impacted by the latency spikes.

![Customers impacted by latency spikes.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/troubleshooting3.png)

 Jane selects one of the correlated spans with a fault status, which opens the trace detail page for the selected trace. She scrolls to the segments timeline section to follow the call path, where she notices that calls to the payment gateway have been failing and preventing customers from registering.

![Failing call payments.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/troubleshooting4.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
