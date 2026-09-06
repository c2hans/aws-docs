---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/troubleshooting-states-in-aws-step-functions.html
---

# Troubleshoot states in AWS Step Functions by using Amazon Bedrock
<a name="troubleshooting-states-in-aws-step-functions"></a>

*Aniket Kurzadkar and Sangam Kushwaha, Amazon Web Services*

## Summary
<a name="troubleshooting-states-in-aws-step-functions-summary"></a>

AWS Step Functions error handling capabilities can help you see an error that occurs during a state in a [workflow](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-statemachines.html), but it can still be a challenge to find the root cause of an error and debug it. This pattern addresses that challenge and shows how Amazon Bedrock can help you resolve errors that occur during states in Step Functions.

Step Functions provides workflow orchestration, making it easier for developers to automate processes. Step Functions also provides error handling functionality that provides the following benefits:
+ Developers can create more resilient applications that don't fail completely when something goes wrong.
+ Workflows can include conditional logic to handle different types of errors differently.
+ The system can automatically retry failed operations, perhaps with exponential backoff.
+ Alternative execution paths can be defined for error scenarios, allowing the workflow to adapt and continue processing.

When an error occurs in a Step Functions workflow, this pattern shows how the error message and context can be sent to a foundation model (FM) like Claude 3 that’s supported by Step Functions. The FM can analyze the error, categorize it, and suggest potential remediation steps.

## Prerequisites and limitations
<a name="troubleshooting-states-in-aws-step-functions-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ Basic understanding of [AWS Step Functions and workflows](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-statemachines.html)
+ Amazon Bedrock [API connectivity](https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started-api.html)

**Limitations**
+ You can use this pattern’s approach for various AWS services. However, the results might vary according to the prompt created by AWS Lambda that’s subsequently evaluated by Amazon Bedrock.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

## Architecture
<a name="troubleshooting-states-in-aws-step-functions-architecture"></a>

The following diagram shows the workflow and architecture components for this pattern.

![Workflow for error handling and notification using Step Functions, Amazon Bedrock, and Amazon SNS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/78f86c74-c9de-4562-adcc-105b87a77a54/images/d8eda499-ea1d-45e5-8a36-e04a44ad5c4b.png)

The diagram shows the automated workflow for error handling and notification in a Step Functions state machine:

1. The developer starts a state machine’s execution.

1. The Step Functions state machine begins processing its states. There are two possible outcomes:
   + (a) If all states execute successfully, the workflow proceeds directly to Amazon SNS for an email success notification.
   + (b) If any state fails, the workflow moves to the error handling Lambda function.

1. In case of an error, the following occurs:
   + (a) The Lambda function (error handler) is triggered. The Lambda function extracts the error message from the event data that the Step Functions state machine passed to it. Then the Lambda function prepares a prompt based on this error message and sends the prompt to Amazon Bedrock. The prompt requests solutions and suggestions related to the specific error encountered.
   + (b) Amazon Bedrock, which hosts the generative AI model, processes the input prompt. (This pattern uses the Anthropic Claude 3 foundation model (FM), which is one of many FMs that Amazon Bedrock supports.) The AI model analyses the error context. Then the model generates a response that can include explanations of why the error occurred, potential solutions to resolve the error, and suggestions to avoid making the same mistakes in the future.

     Amazon Bedrock returns its AI-generated response to the Lambda function. The Lambda function processes the response, potentially formatting it or extracting key information. Then the Lambda function sends the response to the state machine output.

1. After error handling or successful execution, the workflow concludes by triggering Amazon SNS to send an email notification.

## Tools
<a name="troubleshooting-states-in-aws-step-functions-tools"></a>

**AWS services**
+ [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) is a fully managed service that makes high-performing foundation models (FMs) from leading AI startups and Amazon available for your use through a unified API.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) helps you coordinate and manage the exchange of messages between publishers and clients, including web servers and email addresses.
+ [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) is a serverless orchestration service that helps you combine AWS Lambda functions and other AWS services to build business-critical applications.

## Best practices
<a name="troubleshooting-states-in-aws-step-functions-best-practices"></a>
+ Given that Amazon Bedrock is a generative AI model that learns from trained data, it also uses that data to train and generate context. As a best practice, conceal any private information that might lead to data leak problems.
+ Although generative AI can provide valuable insights, critical error-handling decisions should still involve human oversight, especially in production environments.

## Epics
<a name="troubleshooting-states-in-aws-step-functions-epics"></a>

### Create a state machine for your workflow
<a name="create-a-state-machine-for-your-workflow"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a state machine. | To create a state machine that’s appropriate for your workflow, do the following:1. Sign in to the AWS Management Console, and open the AWS Step Functions [console](https://console.aws.amazon.com/states/home). <br />2. From the left navigation pane, choose **State machines**.<br />3. Choose **Create state machine**.<br />4. Choose a template according to your use case, or choose **Blank **to create a template according to your requirements. | AWS DevOps |

### Create a Lambda function
<a name="create-a-lam-function"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a Lambda function.  | To create a Lambda function, do the following:1. In the AWS Management Console, navigate to the AWS Lambda console. <br />2. In the left navigation pane, choose **Functions** and then choose **Create function**.<br />3. On the **Create function** page, choose from the options to create a function. Then, enter a name in **Function name** and choose the appropriate language from the dropdown list in **Runtime**.<br />4. Choose **Create function**. | AWS DevOps |
| Set up the required logic in the Lambda code. | + To connect to the Amazon Bedrock API by using the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/pythonsdk/), use the following code.<br />This code sets up a client for Amazon Bedrock, prepares the necessary parameters, and then sends a request to the Claude 3 model with a specified prompt.<br />This pattern invokes the Claude 3 model. For more information about all the supported foundation models including related model IDs, see [Supported foundation models in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html) in the Amazon Bedrock documentation.<pre>client = boto3.client(<br />        service_name="bedrock-runtime", region_name="selected-region"<br />    )<br /><br />    # Invoke Claude 3 with the text prompt<br />    model_id = "your-model-id" # Select your Model ID, Based on the Model Id, Change the body format<br /><br />    try:<br />        response = client.invoke_model(<br />            modelId=model_id,<br />            body=json.dumps(<br />                {<br />                    "anthropic_version": "bedrock-2023-05-31",<br />                    "max_tokens": 1024,<br />                    "messages": [<br />                        {<br />                            "role": "user",<br />                            "content": [{"type": "text", "text": prompt}],<br />                        }<br />                    ],<br />                }<br />            ),<br />        )<br /></pre>+ (Optional) Replace the AWS account IDs with placeholder account IDs. For security purposes, this approach can be useful for sanitizing logs, error messages, or other output that might contain sensitive account information.<br />The following code will find any occurrence of a 12-digit number enclosed in colons (which is the format of AWS account IDs in Amazon Resource Names (ARNs) and some other AWS identifiers) and replace it with the placeholder account ID `":123456789012:"`.<pre>def replace_account_id(input_string):<br />   <br />    # Use a regular expression to find the AWS account ID pattern<br />    account_id_pattern = r'(:\d{12}:)'<br />    <br />    # Replace the matched pattern with ":123456789012:"<br />    modified_string = re.sub(account_id_pattern, ":123456789012:", input_string)<br />    <br />    return modified_string</pre> | AWS DevOps |

### Integrate Step Functions with Lambda
<a name="integrate-sfn-with-lam"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up Lambda to handle errors in Step Functions. | To set up Step Functions to handle errors without disrupting the workflow, do the following:1. In the Step Functions console, navigate to the state machine that you created earlier.<br />2. Choose **Edit**, and then choose the service that you want to set up error handling for and choose **Error Handling**.<br />3. Choose **Add new catcher**, and for **Fallback state**, choose **Lambda **and then choose the Lambda function that you created earlier. For more information, see [Catch errors](https://docs.aws.amazon.com/step-functions/latest/dg/workflow-studio-process-error.html#workflow-studio-process-error-catch) in the Step Functions documentation. | AWS DevOps |

## Troubleshooting
<a name="troubleshooting-states-in-aws-step-functions-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Lambda cannot access the Amazon Bedrock API (Not authorized to perform) | This error occurs when the Lambda role doesn’t have permission to access the Amazon Bedrock API. To resolve this issue, add the `AmazonBedrockFullAccess` policy for the Lambda role. For more information, see [AmazonBedrockFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonBedrockFullAccess.html) in the *AWS Managed Policy Reference Guide*. |
| Lambda timeout error | Sometimes it might take more than 30 seconds to generate a response and send it back, depending on the prompt. To resolve this issue, increase the configuration time. For more information, see [Configure Lambda function timeout](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonBedrockFullAccess.html) in the *AWS Lambda Developer Guide*. |

## Related resources
<a name="troubleshooting-states-in-aws-step-functions-resources"></a>
+ [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)
+ [Amazon Bedrock API access](https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started-api.html)
+ [Create your first Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)
+ [Developing workflows with Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/developing-workflows.html#development-run-debug)
+ [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
