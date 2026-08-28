---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Database-Insights-Troubleshooting.html
---

# Troubleshooting for CloudWatch Database Insights
<a name="Database-Insights-Troubleshooting"></a>

Use the following information to troubleshoot issues for CloudWatch Database Insights.

## Applying tags to Amazon RDS resources
<a name="Database-Insights-Troubleshooting-tags"></a>

To apply tags to your databases, use the Amazon RDS API, AWS CLI, or Amazon RDS console. For more information, see the following topics.
+ [AddTagsToResource](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_AddTagsToResource.html) in the *Amazon RDS API Reference*
+ [add-tags-to-resource](https://docs.aws.amazon.com/cli/latest/reference/rds/add-tags-to-resource.html) in the *Amazon RDS Command Line Reference*
+ [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*

## Maximum DB instances for fleets
<a name="Database-Insights-Troubleshooting-fleet-limit"></a>

You can't monitor more than 500 DB instances in a database fleet. You can use filters to create a fleet health view with less than 500 DB instances.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
