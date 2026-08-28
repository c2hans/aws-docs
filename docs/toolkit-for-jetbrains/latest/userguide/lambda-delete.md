---
source_url: https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/lambda-delete.html
---

# Deleting an AWS Lambda function by using the AWS Toolkit for JetBrains
<a name="lambda-delete"></a>

You can use the AWS Toolkit to delete an AWS Lambda function that is part of an AWS serverless application, or you can delete a standalone Lambda function.

**Note**
The deleted Lambda function cannot be recovered. You must be diligent with the resource name, such as the Lambda function and version you intend on deleting.

To delete a Lambda function that is part of an AWS serverless application, skip the rest of this topic and see [Deleting an application](sam-delete.md) instead.

To delete a standalone Lambda function, do the following.

1. Open AWS Explorer, if it isn't already open. If you need to switch to a different AWS Region that contains the function, do that now.

1. Expand **Lambda**.

1. Right-click the name of the function to delete, and then choose **Delete Function**.
![Choosing the Delete Function command](http://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/images/lambda-delete.png)

1. Enter the function's name to confirm the deletion, and then choose **OK**. If the function deletion succeeds, the AWS Toolkit for JetBrains removes the function name from the **Lambda** list.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for JetBrains. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-jetbrains` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
