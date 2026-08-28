---
source_url: https://docs.aws.amazon.com/whitepapers/latest/patterns-for-ingesting-saas-data-into-aws-data-lakes/purpose-built-integration-service.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Purpose-built integration service
<a name="purpose-built-integration-service"></a>

## Amazon AppFlow: Introduction
<a name="amazon-appflow"></a>

 [Amazon AppFlow](https://aws.amazon.com/appflow/) is a fully-managed integration service that enables you to securely transfer data between SaaS applications (such as Salesforce, Marketo, Slack, and ServiceNow) and AWS services (such as Amazon S3 and [Amazon Redshift](https://aws.amazon.com/redshift)*)*. With Amazon AppFlow, you can run data flows at nearly any scale and frequency (on a schedule, in response to a business event in real time, or on demand). You can configure data transformations such as data masking and concatenation of fields, as well as validate and filter data (omitting records that don’t fit a criteria) to generate rich, ready-to-use data as part of the flow itself, without additional steps.

 Amazon AppFlow automatically encrypts data in motion, and optionally allows you to restrict data from flowing over the public internet for SaaS applications that are integrated with [AWS PrivateLink](https://aws.amazon.com/privatelink/), reducing exposure to security threats. For a complete list of all the SaaS applications that can be integrated with Amazon AppFlow, refer to [*Amazon AppFlow integrations*](https://aws.amazon.com/appflow/integrations/).

### Architecture overview
<a name="architecture-overview"></a>

 The following diagram depicts the architecture of the solution where data from Salesforce is ingested into Amazon S3 using Amazon AppFlow. Once the data is ingested in Amazon S3, you can use an [AWS Glue crawler](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html) to populate the [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/components-overview.html#data-catalog-intro) with tables and start consuming this data using SQL in [Amazon Athena](https://aws.amazon.com/athena).

![This is a diagram that shows how Amazon AppFlow does data ingestion.](http://docs.aws.amazon.com/whitepapers/latest/patterns-for-ingesting-saas-data-into-aws-data-lakes/images/appflow-based-data-ingestion-pattern.png)

### Usage patterns
<a name="usage-patterns"></a>

 Because Amazon AppFlow can connect to many SaaS applications and is a low-code/no-code approach, this makes it very appealing for those who would want a quick and easy mechanism to ingest data from these SaaS applications.

 Some use cases are as follows:
+  Create a copy of a Salesforce object (for example, opportunity, case, campaign) in Amazon S3.
+  Send case tickets from Zendesk to Amazon S3.
+  Hydrate an Amazon S3 data lake with transactional data from SAP S/4HANA enterprise resource planning (ERP).
+  Send logs, metrics, and dashboards from Datadog to Amazon S3, to create monthly reports or perform other analyses automatically, instead of doing this manually.
+  Send Marketo data, like new leads or email responses, in Amazon S3.

### Considerations
<a name="considerations"></a>

 If a SaaS application you want to get data from is not supported out of the box, you can now build your own connector using the Amazon AppFlow custom connector SDK. AWS has released the [python custom connector SDK](https://github.com/awslabs/aws-appflow-custom-connector-python) as well as [java custom connector SDK](https://github.com/awslabs/aws-appflow-custom-connector-java) for AppFlow. The AppFlow Custom Connector SDK enables customers and third-party developers to build custom source and/or destination connectors for the AppFlow service. With the SDK, you can connect to private APIs, on-premise proprietary systems, and other cloud services by adding to AppFlow's library of connectors.

 If any of the following scenarios apply, other ingestion patterns discussed in this paper may be a better fit for your type of ingestion:
+  A supported application is heavily customized.
+  Your use case exceeds any of the application-specific limitations.

 For every SaaS application that Amazon AppFlow supports, there are a set of limitations included. For example, if you are transferring more than one million Salesforce records, you cannot choose any Salesforce compound field. Before using Amazon AppFlow, look for the limitations for the application that you are planning to connect, evaluate your use case against those limitations, and see if the service is still a good fit for what you are trying to do.

 SaaS applications are sometimes heavily customized, so it’s always good to make sure the edge cases can be solved with Amazon AppFlow. You can find the list of known limitations and considerations in the notes section of the Amazon AppFlow documentation. For example, the known limitations for Salesforce as a source are listed [here](https://docs.aws.amazon.com/appflow/latest/userguide/salesforce.html#salesforce-notes).

 Also, consider the Amazon AppFlow service [quotas](https://docs.aws.amazon.com/appflow/latest/userguide/service-quotas.html) to ensure your use case fits well within those limitations.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
