---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/writes-producer-new.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Producer actions for new datashares in Amazon Redshift
<a name="writes-producer-new"></a>

With Amazon Redshift, you can share live data across Amazon Redshift clusters or AWS accounts using datashares. A datashare is a consumer-producer object that allows you to share live data from your Amazon Redshift cluster with other clusters or AWS accounts. Creating datashares enables secure data sharing while maintaining control over access and ensuring data remains up-to-date. The following sections provide details on creating datashares and adding database objects such as schemas, tables, and views to share live data securely.

**Topics**
+ [Creating a datashare in Amazon Redshift](writes-creating-datashare.md)
+ [Adding objects to a datashare in Amazon Redshift](writes-adding-datashare.md)
+ [Adding data consumers to a datashare in Amazon Redshift](writes-adding-data-consumer.md)
+ [Authorizing a datashare in Amazon Redshift](writes-authorizing.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
