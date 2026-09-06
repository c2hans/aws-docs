---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DeleteSubscriber.html
---

# DeleteSubscriber
<a name="API_budgets_DeleteSubscriber"></a>

Deletes a subscriber.

**Important**
Deleting the last subscriber to a notification also deletes the notification.

## Request Syntax
<a name="API_budgets_DeleteSubscriber_RequestSyntax"></a>

```
{
   "AccountId": "{{string}}",
   "BudgetName": "{{string}}",
   "Notification": {
      "ComparisonOperator": "{{string}}",
      "NotificationState": "{{string}}",
      "NotificationType": "{{string}}",
      "Threshold": {{number}},
      "ThresholdType": "{{string}}"
   },
   "Subscriber": {
      "Address": "{{string}}",
      "SubscriptionType": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_budgets_DeleteSubscriber_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountId](#API_budgets_DeleteSubscriber_RequestSyntax) **   <a name="awscostmanagement-budgets_DeleteSubscriber-request-AccountId"></a>
The `accountId` that is associated with the budget whose subscriber you want to delete.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** [BudgetName](#API_budgets_DeleteSubscriber_RequestSyntax) **   <a name="awscostmanagement-budgets_DeleteSubscriber-request-BudgetName"></a>
The name of the budget whose subscriber you want to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(?![^:\\]*/action/|(?i).*<script>.*</script>.*)[^:\\]+$`
Required: Yes

 ** [Notification](#API_budgets_DeleteSubscriber_RequestSyntax) **   <a name="awscostmanagement-budgets_DeleteSubscriber-request-Notification"></a>
The notification whose subscriber you want to delete.
Type: [Notification](API_budgets_Notification.md) object
Required: Yes

 ** [Subscriber](#API_budgets_DeleteSubscriber_RequestSyntax) **   <a name="awscostmanagement-budgets_DeleteSubscriber-request-Subscriber"></a>
The subscriber that you want to delete.
Type: [Subscriber](API_budgets_Subscriber.md) object
Required: Yes

## Response Elements
<a name="API_budgets_DeleteSubscriber_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_budgets_DeleteSubscriber_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to use this operation with the given parameters.
 ** Message **
The error message the exception carries.
HTTP Status Code: 400

 ** InternalErrorException **
An error on the server occurred during the processing of your request. Try again later.
 ** Message **
The error message the exception carries.
HTTP Status Code: 400

 ** InvalidParameterException **
An error on the client occurred. Typically, the cause is an invalid input value.
 ** Message **
The error message the exception carries.
HTTP Status Code: 400

 ** NotFoundException **
We can’t locate the resource that you specified.
 ** Message **
The error message the exception carries.
HTTP Status Code: 400

 ** ThrottlingException **
The number of API requests has exceeded the maximum allowed API request throttling limit for the account.
 ** Message **
The error message the exception carries.
HTTP Status Code: 400

## Examples
<a name="API_budgets_DeleteSubscriber_Examples"></a>

### Example
<a name="API_budgets_DeleteSubscriber_Example_1"></a>

The following is a sample request of the `DeleteSubscriber` operation.

#### Sample Request
<a name="API_budgets_DeleteSubscriber_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: awsbudgets.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSBudgetServiceGateway.DeleteSubscriber
{
   "AccountId": "111122223333",
   "BudgetName": "Example Budget",
   "Notification": {
       "ComparisonOperator": "GREATER_THAN",
       "NotificationType": "ACTUAL",
       "Threshold": 80,
       "ThresholdType": "PERCENTAGE"
   },
   "Subscribers": [
       {
           "Address": "example@example.com",
           "SubscriptionType": "EMAIL"
       }
   ]
}
```

## See Also
<a name="API_budgets_DeleteSubscriber_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/budgets-2016-10-20/DeleteSubscriber)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/budgets-2016-10-20/DeleteSubscriber)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/DeleteSubscriber)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/budgets-2016-10-20/DeleteSubscriber)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/DeleteSubscriber)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/budgets-2016-10-20/DeleteSubscriber)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/budgets-2016-10-20/DeleteSubscriber)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/budgets-2016-10-20/DeleteSubscriber)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/budgets-2016-10-20/DeleteSubscriber)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/DeleteSubscriber)
