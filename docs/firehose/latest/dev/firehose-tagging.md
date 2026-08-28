---
source_url: https://docs.aws.amazon.com/firehose/latest/dev/firehose-tagging.html
---

# Tag a Firehose stream
<a name="firehose-tagging"></a>

You can assign your own metadata to Firehose streams that you create in Amazon Data Firehose in the form of *tags*. A tag is a key-value pair that you define for a stream. Using tags is a simple yet powerful way to manage AWS resources and organize data, including billing data.

You can specify tags when you invoke [CreateDeliveryStream](https://docs.aws.amazon.com/firehose/latest/APIReference/API_CreateDeliveryStream.html) to create a new Firehose stream. For existing Firehose streams, you can add, list, and remove tags using the following three operations:
+ [TagDeliveryStream](https://docs.aws.amazon.com/firehose/latest/APIReference/API_TagDeliveryStream.html)
+ [ListTagsForDeliveryStream](https://docs.aws.amazon.com/firehose/latest/APIReference/API_ListTagsForDeliveryStream.html)
+ [UntagDeliveryStream](https://docs.aws.amazon.com/firehose/latest/APIReference/API_UntagDeliveryStream.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
