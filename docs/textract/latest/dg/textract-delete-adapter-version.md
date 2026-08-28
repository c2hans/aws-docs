---
source_url: https://docs.aws.amazon.com/textract/latest/dg/textract-delete-adapter-version.html
---

# Delete adapter version
<a name="textract-delete-adapter-version"></a>

You can delete an adapter version you’re no longer using by calling [DeleteAdapterVersion](https://docs.aws.amazon.com/textract/latest/APIReference/API_DeleteAdapterVersion.html). To delete an adapter version you provide the DeleteAdapterVersion operation with both the adapter’s AdapterId and the specific AdapterVersion that you want to delete. Note that you cannot delete adapter versions with an "IN\_PROGRESS" status.

To delete an adapter version with the console:
+ Sign in to the Amazon Textract console.
+ Select **Custom Queries** from the left navigation panel.
+ From the list of your adapters, select the adapter.
+ Select **Delete** and follow the instructions.
+ Select the adapter version that you want to delete from the list of versions in the **Adapter** versions box.
+ Select **Delete** and follow the instructions to delete your adapter.

To delete an adapter with the AWS CLI or AWS SDK:
+ If you haven't already done so, install and configure the AWS CLI and the AWS SDKs. For more information, see [Step 2: Set Up the AWS CLI and AWS SDKs](setup-awscli-sdk.md).
+ Use the following code to create an adapter:

------
#### [ CLI ]

```
aws textract delete-adapter-version \
--adapter-id "abcdef123456" \
--adapter-version "1"
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Textract. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query textract` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
