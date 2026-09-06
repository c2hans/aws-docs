---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/powershell_4_sqs_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Amazon SQS examples using Tools for PowerShell V4
<a name="powershell_4_sqs_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V4 with Amazon SQS.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Add-SQSPermission`
<a name="sqs_AddPermission_powershell_4_topic"></a>

The following code example shows how to use `Add-SQSPermission`.

**Tools for PowerShell V4**
**Example 1: This example allows the specified AWS account to send messages from the specified queue.**

```
Add-SQSPermission -Action SendMessage -AWSAccountId 80398EXAMPLE -Label SendMessagesFromMyQueue -QueueUrl https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue
```
+  For API details, see [AddPermission](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Clear-SQSQueue`
<a name="sqs_PurgeQueue_powershell_4_topic"></a>

The following code example shows how to use `Clear-SQSQueue`.

**Tools for PowerShell V4**
**Example 1: This example deletes all messages from the specified queue.**

```
Clear-SQSQueue -QueueUrl https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue
```
+  For API details, see [PurgeQueue](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Edit-SQSMessageVisibility`
<a name="sqs_ChangeMessageVisibility_powershell_4_topic"></a>

The following code example shows how to use `Edit-SQSMessageVisibility`.

**Tools for PowerShell V4**
**Example 1: This example changes the visibility timeout for the message with the specified receipt handle in the specified queue to 10 hours (10 hours \* 60 minutes \* 60 seconds = 36000 seconds).**

```
Edit-SQSMessageVisibility -QueueUrl https://sqs.us-east-1.amazonaws.com/8039EXAMPLE/MyQueue -ReceiptHandle AQEBgGDh...J/Iqww== -VisibilityTimeout 36000
```
+  For API details, see [ChangeMessageVisibility](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Edit-SQSMessageVisibilityBatch`
<a name="sqs_ChangeMessageVisibilityBatch_powershell_4_topic"></a>

The following code example shows how to use `Edit-SQSMessageVisibilityBatch`.

**Tools for PowerShell V4**
**Example 1: This example changes the visibility timeout for 2 messages with the specified receipt handles in the specified queue. The first message's visibility timeout is changed to 10 hours (10 hours \* 60 minutes \* 60 seconds = 36000 seconds). The second message's visibility timeout is changed to 5 hours (5 hours \* 60 minutes \* 60 seconds = 18000 seconds).**

```
$changeVisibilityRequest1 = New-Object Amazon.SQS.Model.ChangeMessageVisibilityBatchRequestEntry
$changeVisibilityRequest1.Id = "Request1"
$changeVisibilityRequest1.ReceiptHandle = "AQEBd329...v6gl8Q=="
$changeVisibilityRequest1.VisibilityTimeout = 36000

$changeVisibilityRequest2 = New-Object Amazon.SQS.Model.ChangeMessageVisibilityBatchRequestEntry
$changeVisibilityRequest2.Id = "Request2"
$changeVisibilityRequest2.ReceiptHandle = "AQEBgGDh...J/Iqww=="
$changeVisibilityRequest2.VisibilityTimeout = 18000

Edit-SQSMessageVisibilityBatch -QueueUrl https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue -Entry $changeVisibilityRequest1, $changeVisibilityRequest2
```
**Output:**

```
Failed    Successful
------    ----------
{}        {Request2, Request1}
```
+  For API details, see [ChangeMessageVisibilityBatch](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SQSDeadLetterSourceQueue`
<a name="sqs_ListDeadLetterSourceQueues_powershell_4_topic"></a>

The following code example shows how to use `Get-SQSDeadLetterSourceQueue`.

**Tools for PowerShell V4**
**Example 1: This example lists the URLs of any queues that rely on the specified queue as their dead letter queue.**

```
Get-SQSDeadLetterSourceQueue -QueueUrl https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyDeadLetterQueue
```
**Output:**

```
https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue
https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyOtherQueue
```
+  For API details, see [ListDeadLetterSourceQueues](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SQSQueue`
<a name="sqs_ListQueues_powershell_4_topic"></a>

The following code example shows how to use `Get-SQSQueue`.

**Tools for PowerShell V4**
**Example 1: This example lists all queues.**

```
Get-SQSQueue
```
**Output:**

```
https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue
https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/AnotherQueue
https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/DeadLetterQueue
https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyOtherQueue
https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyDeadLetterQueue
```
**Example 2: This example lists any queues that start with the specified name.**

```
Get-SQSQueue -QueueNamePrefix My
```
**Output:**

```
https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue
https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyOtherQueue
https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyDeadLetterQueue
```
+  For API details, see [ListQueues](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SQSQueueAttribute`
<a name="sqs_GetQueueAttributes_powershell_4_topic"></a>

The following code example shows how to use `Get-SQSQueueAttribute`.

**Tools for PowerShell V4**
**Example 1: This example lists all attributes for the specified queue.**

```
Get-SQSQueueAttribute -AttributeName All -QueueUrl https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue
```
**Output:**

```
VisibilityTimeout                     : 30
DelaySeconds                          : 0
MaximumMessageSize                    : 262144
MessageRetentionPeriod                : 345600
ApproximateNumberOfMessages           : 0
ApproximateNumberOfMessagesNotVisible : 0
ApproximateNumberOfMessagesDelayed    : 0
CreatedTimestamp                      : 2/11/2015 5:53:35 PM
LastModifiedTimestamp                 : 12/29/2015 2:23:17 PM
QueueARN                              : arn:aws:sqs:us-east-1:80398EXAMPLE:MyQueue
Policy                                : {"Version":"2012-10-17",		 	 	 "Id":"arn:aws:sqs:us-east-1:80398EXAMPLE:MyQueue/SQSDefaultPolicy","Statement":[{"Sid":"Sid14
                                        495134224EX","Effect":"Allow","Principal":{"AWS":"*"},"Action":"SQS:SendMessage","Resource":"arn:aws:sqs:us-east-1:80
                                        398EXAMPLE:MyQueue","Condition":{"ArnEquals":{"aws:SourceArn":"arn:aws:sns:us-east-1:80398EXAMPLE:MyTopic"}}},{"Sid":
                                        "SendMessagesFromMyQueue","Effect":"Allow","Principal":{"AWS":"80398EXAMPLE"},"Action":"SQS:SendMessage","Resource":"
                                        arn:aws:sqs:us-east-1:80398EXAMPLE:MyQueue"}]}
Attributes                            : {[QueueArn, arn:aws:sqs:us-east-1:80398EXAMPLE:MyQueue], [ApproximateNumberOfMessages, 0],
                                        [ApproximateNumberOfMessagesNotVisible, 0], [ApproximateNumberOfMessagesDelayed, 0]...}
```
**Example 2: This example lists separately only the specified attributes for the specified queue.**

```
Get-SQSQueueAttribute -AttributeName MaximumMessageSize, VisibilityTimeout -QueueUrl https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue
```
**Output:**

```
VisibilityTimeout                     : 30
DelaySeconds                          : 0
MaximumMessageSize                    : 262144
MessageRetentionPeriod                : 345600
ApproximateNumberOfMessages           : 0
ApproximateNumberOfMessagesNotVisible : 0
ApproximateNumberOfMessagesDelayed    : 0
CreatedTimestamp                      : 2/11/2015 5:53:35 PM
LastModifiedTimestamp                 : 12/29/2015 2:23:17 PM
QueueARN                              : arn:aws:sqs:us-east-1:80398EXAMPLE:MyQueue
Policy                                : {"Version":"2012-10-17",		 	 	 "Id":"arn:aws:sqs:us-east-1:80398EXAMPLE:MyQueue/SQSDefaultPolicy","Statement":[{"Sid":"Sid14
                                        495134224EX","Effect":"Allow","Principal":{"AWS":"*"},"Action":"SQS:SendMessage","Resource":"arn:aws:sqs:us-east-1:80
                                        398EXAMPLE:MyQueue","Condition":{"ArnEquals":{"aws:SourceArn":"arn:aws:sns:us-east-1:80398EXAMPLE:MyTopic"}}},{"Sid":
                                        "SendMessagesFromMyQueue","Effect":"Allow","Principal":{"AWS":"80398EXAMPLE"},"Action":"SQS:SendMessage","Resource":"
                                        arn:aws:sqs:us-east-1:80398EXAMPLE:MyQueue"}]}
Attributes                            : {[MaximumMessageSize, 262144], [VisibilityTimeout, 30]}
```
+  For API details, see [GetQueueAttributes](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SQSQueueUrl`
<a name="sqs_GetQueueUrl_powershell_4_topic"></a>

The following code example shows how to use `Get-SQSQueueUrl`.

**Tools for PowerShell V4**
**Example 1: This example lists the URL of the queue with the specified name.**

```
Get-SQSQueueUrl -QueueName MyQueue
```
**Output:**

```
https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue
```
+  For API details, see [GetQueueUrl](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-SQSQueue`
<a name="sqs_CreateQueue_powershell_4_topic"></a>

The following code example shows how to use `New-SQSQueue`.

**Tools for PowerShell V4**
**Example 1: This example creates a queue with the specified name.**

```
New-SQSQueue -QueueName MyQueue
```
**Output:**

```
https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue
```
+  For API details, see [CreateQueue](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Receive-SQSMessage`
<a name="sqs_ReceiveMessage_powershell_4_topic"></a>

The following code example shows how to use `Receive-SQSMessage`.

**Tools for PowerShell V4**
**Example 1: This example lists information for up to the next 10 messages to be received for the specified queue. The information will contain values for the specified message attributes, if they exist.**

```
Receive-SQSMessage -AttributeName SenderId, SentTimestamp -MessageAttributeName StudentName, StudentGrade -MessageCount 10 -QueueUrl https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue
```
**Output:**

```
Attributes             : {[SenderId, AIDAIAZKMSNQ7TEXAMPLE], [SentTimestamp, 1451495923744]}
Body                   : Information about John Doe's grade.
MD5OfBody              : ea572796e3c231f974fe75d89EXAMPLE
MD5OfMessageAttributes : 48c1ee811f0fe7c4e88fbe0f5EXAMPLE
MessageAttributes      : {[StudentGrade, Amazon.SQS.Model.MessageAttributeValue], [StudentName, Amazon.SQS.Model.MessageAttributeValue]}
MessageId              : 53828c4b-631b-469b-8833-c093cEXAMPLE
ReceiptHandle          : AQEBpfGp...20Q5cg==
```
+  For API details, see [ReceiveMessage](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-SQSMessage`
<a name="sqs_DeleteMessage_powershell_4_topic"></a>

The following code example shows how to use `Remove-SQSMessage`.

**Tools for PowerShell V4**
**Example 1: This example deletes the message with the specified receipt handle from the specified queue.**

```
Remove-SQSMessage -QueueUrl https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue -ReceiptHandle AQEBd329...v6gl8Q==
```
+  For API details, see [DeleteMessage](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-SQSMessageBatch`
<a name="sqs_DeleteMessageBatch_powershell_4_topic"></a>

The following code example shows how to use `Remove-SQSMessageBatch`.

**Tools for PowerShell V4**
**Example 1: This example deletes 2 messages with the specified receipt handles from the specified queue.**

```
$deleteMessageRequest1 = New-Object Amazon.SQS.Model.DeleteMessageBatchRequestEntry
$deleteMessageRequest1.Id = "Request1"
$deleteMessageRequest1.ReceiptHandle = "AQEBX2g4...wtJSQg=="

$deleteMessageRequest2 = New-Object Amazon.SQS.Model.DeleteMessageBatchRequestEntry
$deleteMessageRequest2.Id = "Request2"
$deleteMessageRequest2.ReceiptHandle = "AQEBqOVY...KTsLYg=="

Remove-SQSMessageBatch -QueueUrl https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue -Entry $deleteMessageRequest1, $deleteMessageRequest2
```
**Output:**

```
Failed    Successful
------    ----------
{}        {Request1, Request2}
```
+  For API details, see [DeleteMessageBatch](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-SQSPermission`
<a name="sqs_RemovePermission_powershell_4_topic"></a>

The following code example shows how to use `Remove-SQSPermission`.

**Tools for PowerShell V4**
**Example 1: This example removes the permission settings with the specified label from the specified queue.**

```
Remove-SQSPermission -Label SendMessagesFromMyQueue -QueueUrl https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue
```
+  For API details, see [RemovePermission](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-SQSQueue`
<a name="sqs_DeleteQueue_powershell_4_topic"></a>

The following code example shows how to use `Remove-SQSQueue`.

**Tools for PowerShell V4**
**Example 1: This example deletes the specified queue.**

```
Remove-SQSQueue -QueueUrl https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue
```
+  For API details, see [DeleteQueue](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Send-SQSMessage`
<a name="sqs_SendMessage_powershell_4_topic"></a>

The following code example shows how to use `Send-SQSMessage`.

**Tools for PowerShell V4**
**Example 1: This example sends a message with the specified attributes and message body to the specified queue with message delivery delayed for 10 seconds.**

```
$cityAttributeValue = New-Object Amazon.SQS.Model.MessageAttributeValue
$cityAttributeValue.DataType = "String"
$cityAttributeValue.StringValue = "AnyCity"

$populationAttributeValue = New-Object Amazon.SQS.Model.MessageAttributeValue
$populationAttributeValue.DataType = "Number"
$populationAttributeValue.StringValue = "1250800"

$messageAttributes = New-Object System.Collections.Hashtable
$messageAttributes.Add("City", $cityAttributeValue)
$messageAttributes.Add("Population", $populationAttributeValue)

Send-SQSMessage -DelayInSeconds 10 -MessageAttributes $messageAttributes -MessageBody "Information about the largest city in Any Region." -QueueUrl https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue
```
**Output:**

```
MD5OfMessageAttributes              MD5OfMessageBody                    MessageId
----------------------              ----------------                    ---------
1d3e51347bc042efbdf6dda31EXAMPLE    51b0a3256d59467f973009b73EXAMPLE    c35fed8f-c739-4d0c-818b-1820eEXAMPLE
```
+  For API details, see [SendMessage](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Send-SQSMessageBatch`
<a name="sqs_SendMessageBatch_powershell_4_topic"></a>

The following code example shows how to use `Send-SQSMessageBatch`.

**Tools for PowerShell V4**
**Example 1: This example sends 2 messages with the specified attributes and message bodies to the specified queue. Delivery is delayed for 15 seconds for the first message and 10 seconds for the second message.**

```
$student1NameAttributeValue = New-Object Amazon.SQS.Model.MessageAttributeValue
$student1NameAttributeValue.DataType = "String"
$student1NameAttributeValue.StringValue = "John Doe"

$student1GradeAttributeValue = New-Object Amazon.SQS.Model.MessageAttributeValue
$student1GradeAttributeValue.DataType = "Number"
$student1GradeAttributeValue.StringValue = "89"

$student2NameAttributeValue = New-Object Amazon.SQS.Model.MessageAttributeValue
$student2NameAttributeValue.DataType = "String"
$student2NameAttributeValue.StringValue = "Jane Doe"

$student2GradeAttributeValue = New-Object Amazon.SQS.Model.MessageAttributeValue
$student2GradeAttributeValue.DataType = "Number"
$student2GradeAttributeValue.StringValue = "93"

$message1 = New-Object Amazon.SQS.Model.SendMessageBatchRequestEntry
$message1.DelaySeconds = 15
$message1.Id = "FirstMessage"
$message1.MessageAttributes.Add("StudentName", $student1NameAttributeValue)
$message1.MessageAttributes.Add("StudentGrade", $student1GradeAttributeValue)
$message1.MessageBody = "Information about John Doe's grade."

$message2 = New-Object Amazon.SQS.Model.SendMessageBatchRequestEntry
$message2.DelaySeconds = 10
$message2.Id = "SecondMessage"
$message2.MessageAttributes.Add("StudentName", $student2NameAttributeValue)
$message2.MessageAttributes.Add("StudentGrade", $student2GradeAttributeValue)
$message2.MessageBody = "Information about Jane Doe's grade."

Send-SQSMessageBatch -QueueUrl https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue -Entry $message1, $message2
```
**Output:**

```
Failed    Successful
------    ----------
{}        {FirstMessage, SecondMessage}
```
+  For API details, see [SendMessageBatch](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Set-SQSQueueAttribute`
<a name="sqs_SetQueueAttributes_powershell_4_topic"></a>

The following code example shows how to use `Set-SQSQueueAttribute`.

**Tools for PowerShell V4**
**Example 1: This example shows how to set a policy subscribing a queue to an SNS topic. When a message is published to the topic, a message is sent to the subscribed queue.**

```
# create the queue and topic to be associated
$qurl = New-SQSQueue -QueueName "myQueue"
$topicarn = New-SNSTopic -Name "myTopic"

# get the queue ARN to inject into the policy; it will be returned
# in the output's QueueARN member but we need to put it into a variable
# so text expansion in the policy string takes effect
$qarn = (Get-SQSQueueAttribute -QueueUrl $qurl -AttributeName "QueueArn").QueueARN

# construct the policy and inject arns
$policy = @"
{
  "Version":"2012-10-17",
  "Id": "$qarn/SQSPOLICY",
  "Statement": [
      {
      "Sid": "1",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "SQS:SendMessage",
      "Resource": "$qarn",
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "$topicarn"
          }
      }
    }
  ]
}
"@

# set the policy
Set-SQSQueueAttribute -QueueUrl $qurl -Attribute @{ Policy=$policy }
```
**Example 2: This example sets the specified attributes for the specified queue.**

```
Set-SQSQueueAttribute -Attribute @{"DelaySeconds" = "10"; "MaximumMessageSize" = "131072"} -QueueUrl https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue
```
+  For API details, see [SetQueueAttributes](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.
