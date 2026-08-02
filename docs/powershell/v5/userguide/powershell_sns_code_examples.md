---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/powershell_sns_code_examples.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# Amazon SNS examples using Tools for PowerShell V5
<a name="powershell_sns_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V5 with Amazon SNS.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Publish-SNSMessage`
<a name="sns_Publish_powershell_topic"></a>

The following code example shows how to use `Publish-SNSMessage`.

**Tools for PowerShell V5**
**Example 1: This example shows publishing a message with a single MessageAttribute declared inline.**

```
Publish-SNSMessage -TopicArn "arn:aws:sns:us-west-2:123456789012:my-topic" -Message "Hello" -MessageAttribute @{'City'=[Amazon.SimpleNotificationService.Model.MessageAttributeValue]@{DataType='String'; StringValue ='AnyCity'}}
```
**Example 2: This example shows publishing a message with multiple MessageAttributes declared in advance.**

```
$cityAttributeValue = New-Object Amazon.SimpleNotificationService.Model.MessageAttributeValue
$cityAttributeValue.DataType = "String"
$cityAttributeValue.StringValue = "AnyCity"

$populationAttributeValue = New-Object Amazon.SimpleNotificationService.Model.MessageAttributeValue
$populationAttributeValue.DataType = "Number"
$populationAttributeValue.StringValue = "1250800"

$messageAttributes = New-Object System.Collections.Hashtable
$messageAttributes.Add("City", $cityAttributeValue)
$messageAttributes.Add("Population", $populationAttributeValue)

Publish-SNSMessage -TopicArn "arn:aws:sns:us-west-2:123456789012:my-topic" -Message "Hello" -MessageAttribute $messageAttributes
```
+  For API details, see [Publish](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.
