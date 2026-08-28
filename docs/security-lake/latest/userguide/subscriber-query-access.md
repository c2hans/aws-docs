---
source_url: https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-query-access.html
---

# Managing query access for Security Lake subscribers
<a name="subscriber-query-access"></a>

Subscribers with query access can query data that Security Lake collects. These subscribers directly query AWS Lake Formation tables in your S3 bucket with services like Amazon Athena. Although the primary query engine for Security Lake is Athena you can also use other services, such as [Amazon Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/c-getting-started-using-spectrum.html) and Spark SQL, that integrate with the AWS Glue Data Catalog.

Subscribers query source data from AWS Lake Formation tables in your S3 bucket by using services like Amazon Athena. This subscription type is identified as `LAKEFORMATION` in the `accessTypes` parameter of the [CreateSubscriber](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateSubscriber.html) API.

**Note**
This section explains how to grant query access to a third-party subscriber. For information about running queries against your own data lake, see [Step 4: View and query your own data](get-started-console.md#explore-data-lake).

**Topics**
+ [Prerequisites](prereqs-query-subscriber.md)
+ [Creating a subscriber with query access](create-query-subscriber-procedures.md)
+ [Editing a subscriber with query access](editing-query-access-subscriber.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Security Lake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-lake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
