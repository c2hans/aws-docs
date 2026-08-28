---
source_url: https://docs.aws.amazon.com/healthimaging/latest/devguide/managing-data-stores.html
---

# Managing data stores with AWS HealthImaging
<a name="managing-data-stores"></a>

With AWS HealthImaging, you create and manage [data stores](getting-started-concepts.md#concept-data-store) for medical image resources. The following topics describe how to use HealthImaging cloud native actions to create, describe, list, and delete data stores using the AWS Management Console, AWS CLI, and AWS SDKs.

**Note**
The last topic in this chapter is about [cost optimization](cost-optimization.md). After you import your medical imaging data into a HealthImaging data store, it automatically moves between two storage tiers based on time and usage. The storage tiers have different pricing levels, so it's important to understand the tier movement process and the HealthImaging resources that are recognized for billing purposes.

**Topics**
+ [Creating a data store](create-data-store.md)
+ [Getting data store properties](get-data-store.md)
+ [Listing data stores](list-data-stores.md)
+ [Deleting a data store](delete-data-store.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthImaging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthimaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
