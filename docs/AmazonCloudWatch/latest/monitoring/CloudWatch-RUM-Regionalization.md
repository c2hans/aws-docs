---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-Regionalization.html
---

# Regionalization
<a name="CloudWatch-RUM-Regionalization"></a>

This section illustrates strategies for using CloudWatch RUM with applications in different Regions.

## My application is deployed in multiple AWS Regions
<a name="CloudWatch-RUM-Regionalization-multiple"></a>

If your application is deployed in multiple AWS Regions, you have three options:
+ Deploy one app monitor in one Region, in one account, serving all Regions.
+ Deploy separate app monitors for each Region, in unique accounts.
+ Deploy separate app monitors for each Region, all in one account.

The advantage of using one app monitor is that all data will be centralized into one visualization, and all logs are written to the same log group in CloudWatch Logs. With a single app monitor there is a small amount of extra latency for requests, and a single point of failure.

Using multiple app monitors removes the single point of failure, but prevents all data from being combined into one visualization.

### CloudWatch RUM hasn't launched in some Regions that my application is deployed in
<a name="CloudWatch-RUM-Regionalization-notavailable"></a>

CloudWatch RUM is launched into many Regions and has wide geographical coverage. By setting up CloudWatch RUM in the Regions where it is available, you can get the benefits. End users can be anywhere and still have their sessions included if you have set up an app monitor in the Region that they are connecting to.

However, CloudWatch RUM is not yet launched in any Regions in China. You are not able to send data to CloudWatch RUM from these Regions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
