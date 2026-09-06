---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/python_3_cognito-identity_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Amazon Cognito Identity examples using SDK for Python (Boto3)
<a name="python_3_cognito-identity_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Python (Boto3) with Amazon Cognito Identity.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Scenarios](#scenarios)

## Scenarios
<a name="scenarios"></a>

### Create an Amazon Textract explorer application
<a name="cross_TextractExplorer_python_3_topic"></a>

The following code example shows how to explore Amazon Textract output through an interactive application.

**SDK for Python (Boto3)**
 Shows how to use the AWS SDK for Python (Boto3) with Amazon Textract to detect text, form, and table elements in a document image. The input image and Amazon Textract output are shown in a Tkinter application that lets you explore the detected elements.
+ Submit a document image to Amazon Textract and explore the output of detected elements.
+ Submit images directly to Amazon Textract or through an Amazon Simple Storage Service (Amazon S3) bucket.
+ Use asynchronous APIs to start a job that publishes a notification to an Amazon Simple Notification Service (Amazon SNS) topic when the job completes.
+ Poll an Amazon Simple Queue Service (Amazon SQS) queue for a job completion message and display the results.
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/cross_service/textract_explorer).

**Services used in this example**
+ Amazon Cognito Identity
+ Amazon S3
+ Amazon SNS
+ Amazon SQS
+ Amazon Textract
