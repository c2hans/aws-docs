---
source_url: https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/create-new-lambda.html
---

# Creating an AWS Lambda function by using the AWS Toolkit for JetBrains
<a name="create-new-lambda"></a>

You can use the AWS Toolkit for JetBrains to create an AWS Lambda function that is part of an AWS serverless application. Or you can create a standalone Lambda function.

To create a Lambda function that is part of an AWS serverless application, skip the rest of this topic and see [Creating an application](deploy-serverless-app.md) instead.

To create a standalone Lambda function, you must first install the AWS Toolkit for JetBrains and, if you haven't yet, connect to an AWS account for the first time. Then, with IntelliJ IDEA, PyCharm, WebStorm, or JetBrains Rider already running, do one of the following:
+ Open AWS Explorer, if it isn't already open. If you need to switch to a different AWS Region to create the function in, do that now. Then right-click **Lambda**, and choose **Create new AWS Lambda**.
![Creating an AWS Lambda function by starting from AWS Explorer](http://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/images/lambda-create-aws-explorer.png)

  Complete the [Create Function](create-function-dialog.md) dialog box, and then choose **Create Function**. The AWS Toolkit for JetBrains creates a corresponding AWS CloudFormation stack for the deployment, and adds the function name to the **Lambda** list in **AWS Explorer**. If the deployment fails, you can try to determine why by viewing event logs for the stack.
+ Create a code file that implements a function handler for [Java](https://docs.aws.amazon.com/lambda/latest/dg/java-programming-model-handler-types.html), [Python](https://docs.aws.amazon.com/lambda/latest/dg/python-programming-model-handler-types.html), [Node.js](https://docs.aws.amazon.com/lambda/latest/dg/nodejs-prog-model-handler.html), or [C\#](https://docs.aws.amazon.com/lambda/latest/dg/dotnet-programming-model-handler-types.html).

  If you need to switch to a different AWS Region to create the remote function to be run (invoked), do that now. Then in the code file, choose the **Lambda** icon in the gutter next to the function handler, and then choose **Create new AWS Lambda**. Complete the [Create Function](create-function-dialog.md) dialog box, and then choose **Create Function**.
![Creating an AWS Lambda function by starting from an existing function handler in a code file](http://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/images/lambda-create-code-file.png)
**Note**
If the **Lambda** icon isn't displayed in the gutter next to the function handler, try displaying it for the current project by selecting the following box in **Settings**/**Preferences**: **Tools**, **AWS**, **Project settings**, **Show gutter icons for all potential AWS Lambda handlers**. Also, if the function handler is already defined in the corresponding AWS SAM template, the **Create new AWS Lambda** command won't appear.

  After you choose **Create Function**, the AWS Toolkit for JetBrains creates a corresponding function in the Lambda service for the connected AWS account. If the operation succeeds, after you refresh **AWS Explorer**, the **Lambda** list displays the name of the new function.
+ If you already have a project that contains an AWS Lambda function, and if you need to first switch to a different AWS Region to create the function in, do that now. Then in the code file that contains the function handler for [Java](https://docs.aws.amazon.com/lambda/latest/dg/java-programming-model-handler-types.html), [Python](https://docs.aws.amazon.com/lambda/latest/dg/python-programming-model-handler-types.html), [Node.js](https://docs.aws.amazon.com/lambda/latest/dg/nodejs-prog-model-handler.html), or [C\#](https://docs.aws.amazon.com/lambda/latest/dg/dotnet-programming-model-handler-types.html), choose the **Lambda** icon in the gutter next to the function handler. Choose **Create new AWS Lambda**, complete the [Create Function](create-function-dialog.md) dialog box, and then choose **Create Function**.
![Creating an AWS Lambda function by starting from an existing function handler in a code file](http://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/images/lambda-create-code-file.png)
**Note**
If the **Lambda** icon isn't displayed in the gutter next to the function handler, try displaying it for the current project by selecting the following box in **Settings**/**Preferences**: **Tools**, **AWS**, **Project settings**, **Show gutter icons for all potential AWS Lambda handlers**. Also, the **Create new AWS Lambda** command won't be displayed if the function handler is already defined in the corresponding AWS SAM template.

  After you choose **Create Function**, the AWS Toolkit for JetBrains creates a corresponding function in the Lambda service for the connected AWS account. If the operation succeeds, after you refresh **AWS Explorer**, the new function's name appears in the **Lambda** list.

After you create the function, you can run (invoke) or debug the local version of the function or run (invoke) the remote version.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for JetBrains. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-jetbrains` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
