---
source_url: https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/dynamodb-overview.html
---

# Working with Amazon DynamoDB from the AWS Toolkit for JetBrains
<a name="dynamodb-overview"></a>

The AWS Toolkit for JetBrains allows you to view, copy Amazon Resource Names (ARNs), and delete your Amazon DynamoDB resources, directly from your JetBrains IDE.

The following sections describe how to work with these service features from the AWS Toolkit for JetBrains.

## Viewing DynamoDB resources
<a name="dynamodb-overview-view-resources"></a>

At this time, DynamoDB resources can't be created directly from the toolkit, but your resources are visible. To view your DynamoDB resources, complete the following steps:

1. Navigate to the **Explorer** tab in the AWS Toolkit for JetBrains.

1. Expand the **DynamoDB** node.

1. Your DynamoDB resources are displayed under the DynamoDB node.

## Copying DynamoDB resources ARNs
<a name="dynamodb-overview-copy-arn"></a>

An Amazon Resource Name (ARN) is a unique ID that gets assigned to every AWS resource, which include DynamoDB tables. To copy the `ARN` ID for a DynamoDB resource, complete the following steps:

1. Navigate to the **Explorer** tab in the AWS Toolkit for JetBrains.

1. Expand the **DynamoDB** node.

1. Open the context menu for (right-click) the DynamoDB resource you want to copy the `ARN` ID for.

1. Choose **Copy ARN** to copy the resource `ARN` ID to your OS clipboard.

## Deleting DynamoDB resources
<a name="dynamodb-overview-delete"></a>

To delete a DynamoDB resource, complete the following steps:

1. Navigate to the **Explorer** tab in the AWS Toolkit for JetBrains.

1. Expand the **DynamoDB** node.

1. Open the context menu for (right-click) the DynamoDB resource you want to delete.

1. Choose **Delete table...** to open the **Delete table...** confirmation dialog.

1. Complete the confirmation instructions to delete your DynamoDB table.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for JetBrains. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-jetbrains` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
