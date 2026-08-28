---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DescribeSubscribersForNotification.html
---

# DescribeSubscribersForNotification
<a name="API_budgets_DescribeSubscribersForNotification"></a>

Lists the subscribers that are associated with a notification.

## Request Syntax
<a name="API_budgets_DescribeSubscribersForNotification_RequestSyntax"></a>

```
{
   "AccountId": "{{string}}",
   "BudgetName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Notification": {
      "ComparisonOperator": "{{string}}",
      "NotificationState": "{{string}}",
      "NotificationType": "{{string}}",
      "Threshold": {{number}},
      "ThresholdType": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_budgets_DescribeSubscribersForNotification_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountId](#API_budgets_DescribeSubscribersForNotification_RequestSyntax) **   <a name="awscostmanagement-budgets_DescribeSubscribersForNotification-request-AccountId"></a>
The `accountId` that is associated with the budget whose subscribers you want descriptions of.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** [BudgetName](#API_budgets_DescribeSubscribersForNotification_RequestSyntax) **   <a name="awscostmanagement-budgets_DescribeSubscribersForNotification-request-BudgetName"></a>
The name of the budget whose subscribers you want descriptions of.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(?![^:\\]*/action/|(?i).*<script>.*</script>.*)[^:\\]+$`
Required: Yes

 ** [MaxResults](#API_budgets_DescribeSubscribersForNotification_RequestSyntax) **   <a name="awscostmanagement-budgets_DescribeSubscribersForNotification-request-MaxResults"></a>
An optional integer that represents how many entries a paginated response contains.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_budgets_DescribeSubscribersForNotification_RequestSyntax) **   <a name="awscostmanagement-budgets_DescribeSubscribersForNotification-request-NextToken"></a>
The pagination token that you include in your request to indicate the next set of results that you want to retrieve.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2147483647.
Pattern: `.*`
Required: No

 ** [Notification](#API_budgets_DescribeSubscribersForNotification_RequestSyntax) **   <a name="awscostmanagement-budgets_DescribeSubscribersForNotification-request-Notification"></a>
The notification whose subscribers you want to list.
Type: [Notification](API_budgets_Notification.md) object
Required: Yes

## Response Syntax
<a name="API_budgets_DescribeSubscribersForNotification_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Subscribers": [
      {
         "Address": "string",
         "SubscriptionType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_budgets_DescribeSubscribersForNotification_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_budgets_DescribeSubscribersForNotification_ResponseSyntax) **   <a name="awscostmanagement-budgets_DescribeSubscribersForNotification-response-NextToken"></a>
The pagination token in the service response that indicates the next set of results that you can retrieve.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2147483647.
Pattern: `.*`

 ** [Subscribers](#API_budgets_DescribeSubscribersForNotification_ResponseSyntax) **   <a name="awscostmanagement-budgets_DescribeSubscribersForNotification-response-Subscribers"></a>
A list of subscribers that are associated with a notification.
Type: Array of [Subscriber](API_budgets_Subscriber.md) objects
Array Members: Minimum number of 1 item. Maximum number of 11 items.

## Errors
<a name="API_budgets_DescribeSubscribersForNotification_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to use this operation with the given parameters.
 ** Message **
The error message the exception carries.
HTTP Status Code: 400

 ** ExpiredNextTokenException **
The pagination token expired.
 ** Message **
The error message the exception carries.
HTTP Status Code: 400

 ** InternalErrorException **
An error on the server occurred during the processing of your request. Try again later.
 ** Message **
The error message the exception carries.
HTTP Status Code: 400

 ** InvalidNextTokenException **
The pagination token is invalid.
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
<a name="API_budgets_DescribeSubscribersForNotification_Examples"></a>

### Example
<a name="API_budgets_DescribeSubscribersForNotification_Example_1"></a>

The following is a sample request and response of the `DescribeSubscribersForNotification` operation.

#### Sample Request
<a name="API_budgets_DescribeSubscribersForNotification_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: awsbudgets.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSBudgetServiceGateway.DescribeSubscribersForNotification
{
   "AccountId": "111122223333",
   "BudgetName": "Example Budget",
   "MaxResults": 5,
   "Notification": {
      "ComparisonOperator": "GREATER_THAN",
      "NotificationType": "ACTUAL",
      "Threshold": 80,
      "ThresholdType": "PERCENTAGE"
    }
}
```

#### Sample Response
<a name="API_budgets_DescribeSubscribersForNotification_Example_1_Response"></a>

```
{
   "NextToken": "string",
   "Subscribers": [
      {
           "Address": "example@example.com",
           "SubscriptionType": "EMAIL"
      }
   ]
}
```

## See Also
<a name="API_budgets_DescribeSubscribersForNotification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/budgets-2016-10-20/DescribeSubscribersForNotification)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/budgets-2016-10-20/DescribeSubscribersForNotification)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/DescribeSubscribersForNotification)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/budgets-2016-10-20/DescribeSubscribersForNotification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/DescribeSubscribersForNotification)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/budgets-2016-10-20/DescribeSubscribersForNotification)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/budgets-2016-10-20/DescribeSubscribersForNotification)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/budgets-2016-10-20/DescribeSubscribersForNotification)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/budgets-2016-10-20/DescribeSubscribersForNotification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/DescribeSubscribersForNotification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
