---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/specifying-lambda-hook-functions.html
---

# Specifying Lambda hook functions
<a name="specifying-lambda-hook-functions"></a>

The guidance’s content designer allows you to dynamically generate answers by specifying your own Lambda hook function for any item. When you specify the name, or ARN, of a Lambda function in the **Lambda hook** field for an item, QnABot on AWS will call your function any time that item is matched to an end user’s question. Your Lambda function can run code to integrate with other services, perform actions, and generate dynamic answers.

QnABot on AWS comes with a simple Lambda hook function example that you can customize:

1. From the content designer, choose **Import** from the tools menu (☰).

1. Select **Examples/Extensions**, and then choose **LOAD** from the **GreetingHook** example.

1. After the import job has completed, return to the edit page, and examine the item **GreetingHookExample**. The Lambda hook field is populated with a Lambda function name.

1. Use the web UI to say, ` "What are Lambda hooks?" `. Note that the answer is prepended with a dynamic greeting based on the current time of day - in this case ` good afternoon `.

    **Example Lambda hook function.**
![image18](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/image18.jpeg)

1. Inspect the `ExampleJSLambdahook` Lambda function using the [AWS Lambda console](https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions/qna-QnABot-hello?tab=graph).

1. Choose **Lambda Hooks** from the content designer tools menu (**☰**) to display additional information to help you create your own Lambda hook functions.

For more information about how you can package Lambda hooks, see the [Extending QnABot with Lambda hook functions](https://github.com/aws-solutions/qnabot-on-aws/blob/main/source/docs/lambda_hooks/README.md) section in the GitHub repository.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for QnABot on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
