---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_UpdateNotification.html
---

# UpdateNotification
<a name="API_budgets_UpdateNotification"></a>

Updates a notification.

## Request Syntax
<a name="API_budgets_UpdateNotification_RequestSyntax"></a>

```
{
   "AccountId": "{{string}}",
   "BudgetName": "{{string}}",
   "NewNotification": {
      "ComparisonOperator": "{{string}}",
      "NotificationState": "{{string}}",
      "NotificationType": "{{string}}",
      "Threshold": {{number}},
      "ThresholdType": "{{string}}"
   },
   "OldNotification": {
      "ComparisonOperator": "{{string}}",
      "NotificationState": "{{string}}",
      "NotificationType": "{{string}}",
      "Threshold": {{number}},
      "ThresholdType": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_budgets_UpdateNotification_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountId](#API_budgets_UpdateNotification_RequestSyntax) **   <a name="awscostmanagement-budgets_UpdateNotification-request-AccountId"></a>
The `accountId` that is associated with the budget whose notification you want to update.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** [BudgetName](#API_budgets_UpdateNotification_RequestSyntax) **   <a name="awscostmanagement-budgets_UpdateNotification-request-BudgetName"></a>
The name of the budget whose notification you want to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(?![^:\\]*/action/|(?i).*<script>.*</script>.*)[^:\\]+$`
Required: Yes

 ** [NewNotification](#API_budgets_UpdateNotification_RequestSyntax) **   <a name="awscostmanagement-budgets_UpdateNotification-request-NewNotification"></a>
The updated notification to be associated with a budget.
Type: [Notification](API_budgets_Notification.md) object
Required: Yes

 ** [OldNotification](#API_budgets_UpdateNotification_RequestSyntax) **   <a name="awscostmanagement-budgets_UpdateNotification-request-OldNotification"></a>
The previous notification that is associated with a budget.
Type: [Notification](API_budgets_Notification.md) object
Required: Yes

## Response Elements
<a name="API_budgets_UpdateNotification_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_budgets_UpdateNotification_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to use this operation with the given parameters.
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
<a name="API_budgets_UpdateNotification_Examples"></a>

### Example
<a name="API_budgets_UpdateNotification_Example_1"></a>

The following is a sample request of the `UpdateNotification` operation.

#### Sample Request
<a name="API_budgets_UpdateNotification_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: awsbudgets.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSBudgetServiceGateway.UpdateNotification
{
   "AccountId": "111122223333",
   "BudgetName": "Example Budget",
   "NewNotification": {
            "ComparisonOperator": "GREATER_THAN",
            "NotificationType": "ACTUAL",
            "Threshold": 80,
            "ThresholdType": "PERCENTAGE"
         }
    },
   "OldNotification": {
            "ComparisonOperator": "GREATER_THAN",
            "NotificationType": "ACTUAL",
            "Threshold": 80,
            "ThresholdType": "PERCENTAGE"
         }
    }
}
```

## See Also
<a name="API_budgets_UpdateNotification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/budgets-2016-10-20/UpdateNotification)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/budgets-2016-10-20/UpdateNotification)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/UpdateNotification)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/budgets-2016-10-20/UpdateNotification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/UpdateNotification)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/budgets-2016-10-20/UpdateNotification)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/budgets-2016-10-20/UpdateNotification)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/budgets-2016-10-20/UpdateNotification)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/budgets-2016-10-20/UpdateNotification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/UpdateNotification)
