---
source_url: https://docs.aws.amazon.com/textract/latest/dg/textract-create-adapter.html
---

# Create an Adapter
<a name="textract-create-adapter"></a>

To customize the Amazon Textract base model, create an adapter. To do so, use the [CreateAdapter](https://docs.aws.amazon.com/textract/latest/APIReference/API_CreateAdapter.html) operation. When calling `CreateAdapter,` you provide an AdapterName and FeatureType as an input. Currently Queries is the only feature type supported.

When creating an adapter you can also provide a Description, Tags, and a ClientRequestToken. Finally, you can choose whether the adapter should be auto-updated with the AutoUpdate argument. After creating an adapter, you can start training it on your own sample documents by using the [CreateAdapterVersion](https://docs.aws.amazon.com/textract/latest/APIReference/API_CreateAdapterVersion.html) operation.

To create an adapter with the Amazon Textract console:
+ Sign in to the Amazon Textract console.
+ Select **Custom Queries** from the left navigation panel.
+ Select **Create adapter**.

To create an adapter with the AWS CLI or AWS SDK:
+ If you haven't already done so, install and configure the AWS CLI and the AWS SDKs. For more information, see [Step 2: Set Up the AWS CLI and AWS SDKs](setup-awscli-sdk.md).
+ Use the following code to create an adapter:

------
#### [ CLI ]

```
aws textract create-adapter \
--adapter-name "test-w2" \
--feature-types '["QUERIES"]' \
--description 'demo'
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Textract. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query textract` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
