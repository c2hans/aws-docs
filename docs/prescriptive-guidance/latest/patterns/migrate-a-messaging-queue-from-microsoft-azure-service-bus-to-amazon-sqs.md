---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-a-messaging-queue-from-microsoft-azure-service-bus-to-amazon-sqs.html
---

# Migrate a messaging queue from Microsoft Azure Service Bus to Amazon SQS
<a name="migrate-a-messaging-queue-from-microsoft-azure-service-bus-to-amazon-sqs"></a>

*Nisha Gambhir, Amazon Web Services*

## Summary
<a name="migrate-a-messaging-queue-from-microsoft-azure-service-bus-to-amazon-sqs-summary"></a>

This pattern describes how to migrate a .NET Framework or .NET Core web or console application from using the Microsoft Azure Service Bus queue messaging platform to Amazon Simple Queue Service (Amazon SQS).

Applications use messaging services to send data to, and receive data from, other applications. These services help build decoupled, highly scalable microservices, distributed systems, and serverless applications in the cloud.

Azure Service Bus queues are part of a broader Azure messaging infrastructure that supports queuing and publish/subscribe messaging.

Amazon SQS is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. Amazon SQS eliminates the complexity and overhead associated with managing and operating message-oriented middleware, and enables developers to focus on differentiating work. Using Amazon SQS, you can send, store, and receive messages between software components at any volume, without losing messages or requiring other services to be available.

## Prerequisites and limitations
<a name="migrate-a-messaging-queue-from-microsoft-azure-service-bus-to-amazon-sqs-prerequisites-and-limitations"></a>

**Prerequisites**
+ An active AWS account
+ A .NET Framework or .NET Core web or console application that uses Azure Service Bus queues (sample code attached)

**Product versions**
+ .NET Framework 3.5 or later, or .NET Core 1.0.1, 2.0.0, or later

## Architecture
<a name="migrate-a-messaging-queue-from-microsoft-azure-service-bus-to-amazon-sqs-architecture"></a>

**Source technology stack  **
+ A .NET (Core or Framework) web or console application that uses an Azure Service Bus queue to send messages

**Target technology stack  **
+ Amazon SQS

## Tools
<a name="migrate-a-messaging-queue-from-microsoft-azure-service-bus-to-amazon-sqs-tools"></a>

**Tools**
+ Microsoft Visual Studio

**Code**

To create an AWS Identity and Access management (IAM) policy for Amazon SQS:

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

2. In the navigation pane on the left, choose **Policies**, and then choose **Create policy**.

3. Choose the **JSON** tab, and paste the following code:

```
{
   "Version": "2012-10-17",
   "Statement": [
      {
         "Sid": "VisualEditor0",
         "Effect": "Allow",
         "Action": [
            "sqs:DeleteMessage",
            "sqs:GetQueueUrl",
            "sqs:ChangeMessageVisibility",
            "sqs:SendMessageBatch",
            "sqs:ReceiveMessage",
            "sqs:SendMessage",
            "sqs:GetQueueAttributes",
            "sqs:ListQueueTags",
            "sqs:ListDeadLetterSourceQueues",
            "sqs:DeleteMessageBatch",
            "sqs:PurgeQueue",
            "sqs:DeleteQueue",
            "sqs:CreateQueue",
            "sqs:ChangeMessageVisibilityBatch",
            "sqs:SetQueueAttributes"
         ],
         "Resource": "arn:aws:sqs:*:<AccountId>:*"
      },
      {
         "Sid": "VisualEditor1",
         "Effect": "Allow",
         "Action": "sqs:ListQueues",
         "Resource": "*"
      }
   ]
}
```

4. Choose **Review policy**, type a name, and then choose **Create policy**.

5. Attach the newly created policy to your existing IAM role or create a new role.

## Epics
<a name="migrate-a-messaging-queue-from-microsoft-azure-service-bus-to-amazon-sqs-epics"></a>

### Set up Amazon SQS in AWS
<a name="set-up-amazon-sqs-in-aws"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an IAM policy for Amazon SQS. | Create the IAM policy that will provide access to Amazon SQS. See the Code section for a sample policy. | System engineer |
| Create an AWS profile. | Create a new profile by running the AWS Tools for PowerShell command Set-AWSCredential. This command stores your access key and secret key in your default credentials file under the profile name you specify. Link the Amazon SQS policy you created earlier with this account. Keep the AWS access key ID and secret access key. These will be required in the next steps. | System engineer |
| Create an SQS queue. | You can create a standard queue or a first in, first out (FIFO) queue. For instructions, see the link in the References section. | System engineer |

### Revise your .NET application code
<a name="revise-your-net-application-code"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install AWS Toolkit for Visual Studio. | This toolkit is an extension for Microsoft Visual Studio and makes it easier for you to build and deploy .NET applications in AWS. For installation and usage instructions, see the link in the References section. | Application developer |
| Install the AWSSDK.SQS NuGet package. | You can install AWSSDK.SQS by choosing "Manage NuGet Package" in Visual Studio or by running the command "Install-Package AWSSDK.SQS". | Application developer |
| Create an AWSCredentials object in your .NET application. | The sample application in the attachment shows how to create a BasicAWSCredentials object, which inherits from AWSCredentials. You can use the access key ID and secret access key from earlier, or let the object pick these from the .aws folder as part of the user profile at run time. | Application developer |
| Create an SQS client object. | Create an SQS client object (AmazonSQSClient) for .NET Framework. This is part of the Amazon.SQS namespace. This object is required instead of IQueueClient, which is part of the Microsoft.Azure.ServiceBus namespace. | Application developer |
| Call the SendMessageAsync method to send messages to the SQS queue. | Change the code that sends the message to the queue to use the amazonSqsClient.SendMessageAsync method. For details, see the attached code sample. | Application developer |
| Call the ReceiveMessageAsync method to receive messages from the SQS queue. | Change the code that receives the message to use the amazonSqsClient.ReceiveMessageAsync method. For details, see the attached code sample. | Application developer |
| Call the DeleteMessageAsync method to delete messages from the SQS queue. | To delete messages, change the code from the queueClient.CompleteAsync method to the amazonSqsClient.DeleteMessageAsync method. For details, see the attached code sample. | Application developer |

## Related resources
<a name="migrate-a-messaging-queue-from-microsoft-azure-service-bus-to-amazon-sqs-related-resources"></a>
+ [AWS SDK for .NET Developer Guide](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/welcome.html)
+ [Messaging Using Amazon SQS](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/sqs-apis-intro.html)
+ [Creating and Using an Amazon SQS Queue with the AWS SDK for .NET](https://docs.aws.amazon.com/sdk-for-net/v2/developer-guide/how-to-sqs.html)
+ [Send an Amazon SQS Message](https://docs.aws.amazon.com/sdk-for-net/v2/developer-guide/SendMessage.html)
+ [Receive a Message from an Amazon SQS Queue](https://docs.aws.amazon.com/sdk-for-net/v2/developer-guide/ReceiveMessage.html)
+ [Delete a Message from an Amazon SQS Queue](https://docs.aws.amazon.com/sdk-for-net/v2/developer-guide/DeleteMessage.html)
+ [AWS Toolkit for Visual Studio](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/welcome.html)

## Additional information
<a name="migrate-a-messaging-queue-from-microsoft-azure-service-bus-to-amazon-sqs-additional-information"></a>

This pattern includes two sample applications (see the attachments section):
+ **AzureSbTestApp** includes code that uses the Azure Service Bus queue.
+ **AmazonSqsTestApp** uses Amazon SQS. This is a console application that uses .NET Core 2.2 and includes examples for sending and receiving messages.

Notes:
+ queueClient is an object of IQueueClient, which is part of the Microsoft.Azure.ServiceBus namespace (included in the Microsoft.Azure.ServiceBus NuGet package).
+ amazonSqsClient is an object of AmazonSQSClient, which is part of the Amazon.SQS namespace (included in the AWSSDK.SQS NuGet package).
+ Depending upon where the code is running, say if its running on EC2, the role needs to have permission to write into the SQS Queue.

## Attachments
<a name="attachments-25334709-7000-4f60-87ed-ea41acb41a99"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/25334709-7000-4f60-87ed-ea41acb41a99/attachments/attachment.zip)
