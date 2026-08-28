---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/call-analytics.html
---

# Generating insights from calls using call analytics for the Amazon Chime SDK
<a name="call-analytics"></a>

The topics in this section explain how to use Amazon Chime SDK call analytics to generate insights from your call data.

Amazon Chime SDK call analytics gives developers low-code solutions for generating cost-effective insights from real-time audio, including audio ingestion, analysis, alerting, and data lake integration. Call analytics enables you to generate insights through integration with Amazon Transcribe and Transcribe Call Analytics (TCA), and natively through Amazon Chime SDK voice analytics. Call analytics can also record calls to your Amazon S3 Bucket.

You can use the following methods to configure and run call analytics.
+ Use the Amazon Chime SDK console to create a call analytics configuration and associate it with an Amazon Chime SDK Voice Connector. During that process, you can enable call recording and analytics. You don't need to write code to complete the process.
+ Use a set of Amazon Chime SDK APIs [Amazon Chime SDK](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/welcome.html) APIs to programmatically create and run a configuration.

For more information, refer to [Creating call analytics configurations for the Amazon Chime SDK](creating-ca-configuration.md) and [Using call analytics configurations for the Amazon Chime SDK](using-call-analytics-configurations.md), later in this section.

**Topics**
+ [What is Amazon Chime SDK call analytics](what-is-amazon-chime-sdk-call-analytics.md)
+ [Understanding call analytics terminology for the Amazon Chime SDK](ca-terms-concepts.md)
+ [Creating call analytics configurations for the Amazon Chime SDK](creating-ca-configuration.md)
+ [Using call analytics configurations for the Amazon Chime SDK](using-call-analytics-configurations.md)
+ [Managing call analytics pipelines for the Amazon Chime SDK](managing-call-analytics-pipelines.md)
+ [Pausing and resuming call analytics pipelines for the Amazon Chime SDK](pausing-and-resuming-call-analytics-pipelines.md)
+ [Using the call analytics resource access role for the Amazon Chime SDK](call-analytics-resource-access-role.md)
+ [Understanding the call analytics statuses for the Amazon Chime SDK](call-analytics-statuses.md)
+ [Monitoring call analytics pipelines for the Amazon Chime SDK with Amazon CloudWatch](monitoring-with-cloudwatch.md)
+ [Call analytics processor and output destinations for the Amazon Chime SDK](call-analytics-processor-and-output-destinations.md)
+ [Call analytics data model for the Amazon Chime SDK](ca-data-model.md)
+ [Using Amazon Chime SDK voice analytics](voice-analytics.md)
+ [Call analytics service quotas for the Amazon Chime SDK](ca-regions.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
