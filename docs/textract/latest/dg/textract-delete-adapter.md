---
source_url: https://docs.aws.amazon.com/textract/latest/dg/textract-delete-adapter.html
---

# Delete an Adapter
<a name="textract-delete-adapter"></a>

You can delete a custom Amazon Textract adapter at any time by calling the [DeleteAdapter](https://docs.aws.amazon.com/textract/latest/APIReference/API_DeleteAdapter.html) API operation. You can delete an adapter by providing the DeleteAdapter operation with the AdapterId of the adapter that you want to delete. Invoke DeleteAdapter will delete all Adapter Versions associated with the Adapter ARN.

To delete an adapter with the console:
+ Sign in to the Amazon Textract console.
+ Select **Custom Queries** from the left navigation panel.
+ From the list of your adapters, select the adapter to delete.
+ Select **Delete** and follow the instructions to delete your adapter.

To create an adapter with the AWS CLI or AWS SDK:
+ If you haven't already done so, install and configure the AWS CLI and the AWS SDKs. For more information, see [Step 2: Set Up the AWS CLI and AWS SDKs](setup-awscli-sdk.md).
+ Use the following code to create an adapter:

------
#### [ CLI ]

```
aws textract delete-adapter \
--adapter-id 'abcdef123456'
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Textract. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query textract` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
