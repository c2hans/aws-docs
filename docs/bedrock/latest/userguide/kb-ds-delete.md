---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-ds-delete.html
---

# Delete a data source from your Amazon Bedrock knowledge base
<a name="kb-ds-delete"></a>

**Important**
For optimized retrieval accuracy and a managed experience, we recommend [Amazon Bedrock Managed Knowledge Base](kb-build-managed.md).

You can delete or remove a data source that you no longer need or use for your knowledge base.

Choose the tab for your preferred method, and then follow the steps:

------
#### [ Console ]

**To delete a data source**

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock).

1. In the left navigation pane, choose **Knowledge bases**.

1. In the **Data source** section, select the radio button next to the data source that you want to delete.

1. Choose **Delete**.

1. A green banner appears when the data source is successfully deleted.
**Note**
Your data deletion policy for your data source is set to either "Delete" (deletes all data when you delete your data source, but **doesn't delete the vector store itself**) or "Retain" (retains all data when you delete your data source). If you delete a data source or knowledge base, the **vector store itself is not deleted**. If the data source data deletion policy is set to "Delete", it's possible for the data source to unsuccessfully complete the process of deletion due to issues with the configuration or access to the vector store. You can check the "DELETE\_UNSUCCESSFUL" status to see the reason why the data source could not successfully delete.

------
#### [ API ]

To delete a data source from a knowledge base, send a [DeleteDataSource](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_DeletDataSource.html) request, specifying the `dataSourceId` and `knowledgeBaseId`.

**Note**
Your data deletion policy for your data source is set to either `DELETE` (deletes all data when you delete your data source, but **doesn't delete the vector store itself**) or `RETAIN` (retains all data when you delete your data source). If you delete a data source or knowledge base, the **vector store itself is not deleted**. If the data source data deletion policy is set to `DELETE`, it's possible for the data source to unsuccessfully complete the process of deletion due to issues with the configuration or access to the vector store. You can view `failureReasons` if the data source status is `DELETE_UNSUCCESSFUL` to see the reason why the data source could not successfully delete.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
