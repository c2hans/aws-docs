---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_CreateSubscriber.html
---

# CreateSubscriber
<a name="API_budgets_CreateSubscriber"></a>

Creates a subscriber. You must create the associated budget and notification before you create the subscriber.

## Request Syntax
<a name="API_budgets_CreateSubscriber_RequestSyntax"></a>

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
<a name="API_budgets_CreateSubscriber_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountId](#API_budgets_CreateSubscriber_RequestSyntax) **   <a name="awscostmanagement-budgets_CreateSubscriber-request-AccountId"></a>
The `accountId` that is associated with the budget that you want to create a subscriber for.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** [BudgetName](#API_budgets_CreateSubscriber_RequestSyntax) **   <a name="awscostmanagement-budgets_CreateSubscriber-request-BudgetName"></a>
The name of the budget that you want to subscribe to. Budget names must be unique within an account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(?![^:\\]*/action/|(?i).*<script>.*</script>.*)[^:\\]+$`
Required: Yes

 ** [Notification](#API_budgets_CreateSubscriber_RequestSyntax) **   <a name="awscostmanagement-budgets_CreateSubscriber-request-Notification"></a>
The notification that you want to create a subscriber for.
Type: [Notification](API_budgets_Notification.md) object
Required: Yes

 ** [Subscriber](#API_budgets_CreateSubscriber_RequestSyntax) **   <a name="awscostmanagement-budgets_CreateSubscriber-request-Subscriber"></a>
The subscriber that you want to associate with a budget notification.
Type: [Subscriber](API_budgets_Subscriber.md) object
Required: Yes

## Response Elements
<a name="API_budgets_CreateSubscriber_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_budgets_CreateSubscriber_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to use this operation with the given parameters.
 ** Message **
The error message the exception carries.
HTTP Status Code: 400

 ** CreationLimitExceededException **
You've exceeded the notification or subscriber limit.
 ** Message **
The error message the exception carries.
HTTP Status Code: 400

 ** DuplicateRecordException **
The budget name already exists. Budget names must be unique within an account.
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
<a name="API_budgets_CreateSubscriber_Examples"></a>

### Example
<a name="API_budgets_CreateSubscriber_Example_1"></a>

The following is a sample request of the `CreateSubscriber` operation.

#### Sample Request
<a name="API_budgets_CreateSubscriber_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: awsbudgets.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSBudgetServiceGateway.CreateSubscriber
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
<a name="API_budgets_CreateSubscriber_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/budgets-2016-10-20/CreateSubscriber)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/budgets-2016-10-20/CreateSubscriber)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/CreateSubscriber)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/budgets-2016-10-20/CreateSubscriber)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/CreateSubscriber)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/budgets-2016-10-20/CreateSubscriber)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/budgets-2016-10-20/CreateSubscriber)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/budgets-2016-10-20/CreateSubscriber)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/budgets-2016-10-20/CreateSubscriber)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/CreateSubscriber)
