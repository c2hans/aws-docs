---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Remove_service_from_Cross_Service_Dashboard.html
---

# Removing a service from appearing in the CloudWatch cross-service dashboard
<a name="Remove_service_from_Cross_Service_Dashboard"></a>

You can prevent a service's metrics from appearing in the cross-service dashboard. This helps you focus your cross-service dashboard on the services you most want to monitor.

If you remove a service from the cross-service dashboard, the alarms for that service still appear in the views of your alarms.

**To remove a service's metrics from the cross-service dashboard**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

   The home page appears.

1. At the top of the page, under **Overview**, choose the service you want to remove.

   The view changes to show metrics from only that service.

1. Choose **Actions**, then clear the check box next to **Show on cross service dashboard**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
