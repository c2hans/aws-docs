---
source_url: https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_DescribeNotificationRule.html
---

# DescribeNotificationRule
<a name="API_DescribeNotificationRule"></a>

Returns information about a specified notification rule.

## Request Syntax
<a name="API_DescribeNotificationRule_RequestSyntax"></a>

```
POST /describeNotificationRule HTTP/1.1
Content-type: application/json

{
   "Arn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeNotificationRule_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeNotificationRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Arn](#API_DescribeNotificationRule_RequestSyntax) **   <a name="codestarnotifications-DescribeNotificationRule-request-Arn"></a>
The Amazon Resource Name (ARN) of the notification rule.
Type: String
Pattern: `^arn:aws[^:\s]*:codestar-notifications:[^:\s]+:\d{12}:notificationrule\/(.*\S)?$`
Required: Yes

## Response Syntax
<a name="API_DescribeNotificationRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "CreatedBy": "string",
   "CreatedTimestamp": number,
   "DetailType": "string",
   "EventTypes": [
      {
         "EventTypeId": "string",
         "EventTypeName": "string",
         "ResourceType": "string",
         "ServiceName": "string"
      }
   ],
   "LastModifiedTimestamp": number,
   "Name": "string",
   "Resource": "string",
   "Status": "string",
   "Tags": {
      "string" : "string"
   },
   "Targets": [
      {
         "TargetAddress": "string",
         "TargetStatus": "string",
         "TargetType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeNotificationRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_DescribeNotificationRule_ResponseSyntax) **   <a name="codestarnotifications-DescribeNotificationRule-response-Arn"></a>
The Amazon Resource Name (ARN) of the notification rule.
Type: String
Pattern: `^arn:aws[^:\s]*:codestar-notifications:[^:\s]+:\d{12}:notificationrule\/(.*\S)?$`

 ** [CreatedBy](#API_DescribeNotificationRule_ResponseSyntax) **   <a name="codestarnotifications-DescribeNotificationRule-response-CreatedBy"></a>
The name or email alias of the person who created the notification rule.
Type: String
Length Constraints: Minimum length of 1.

 ** [CreatedTimestamp](#API_DescribeNotificationRule_ResponseSyntax) **   <a name="codestarnotifications-DescribeNotificationRule-response-CreatedTimestamp"></a>
The date and time the notification rule was created, in timestamp format.
Type: Timestamp

 ** [DetailType](#API_DescribeNotificationRule_ResponseSyntax) **   <a name="codestarnotifications-DescribeNotificationRule-response-DetailType"></a>
The level of detail included in the notifications for this resource. BASIC will include only the contents of the event as it would appear in Amazon CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created.
Type: String
Valid Values: `BASIC | FULL`

 ** [EventTypes](#API_DescribeNotificationRule_ResponseSyntax) **   <a name="codestarnotifications-DescribeNotificationRule-response-EventTypes"></a>
A list of the event types associated with the notification rule.
Type: Array of [EventTypeSummary](API_EventTypeSummary.md) objects

 ** [LastModifiedTimestamp](#API_DescribeNotificationRule_ResponseSyntax) **   <a name="codestarnotifications-DescribeNotificationRule-response-LastModifiedTimestamp"></a>
The date and time the notification rule was most recently updated, in timestamp format.
Type: Timestamp

 ** [Name](#API_DescribeNotificationRule_ResponseSyntax) **   <a name="codestarnotifications-DescribeNotificationRule-response-Name"></a>
The name of the notification rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9\-_ ]+$`

 ** [Resource](#API_DescribeNotificationRule_ResponseSyntax) **   <a name="codestarnotifications-DescribeNotificationRule-response-Resource"></a>
The Amazon Resource Name (ARN) of the resource associated with the notification rule.
Type: String
Pattern: `^arn:aws[^:\s]*:[^:\s]*:[^:\s]*:[0-9]{12}:[^\s]+$`

 ** [Status](#API_DescribeNotificationRule_ResponseSyntax) **   <a name="codestarnotifications-DescribeNotificationRule-response-Status"></a>
The status of the notification rule. Valid statuses are on (sending notifications) or off (not sending notifications).
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [Tags](#API_DescribeNotificationRule_ResponseSyntax) **   <a name="codestarnotifications-DescribeNotificationRule-response-Tags"></a>
The tags associated with the notification rule.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Value Length Constraints: Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

 ** [Targets](#API_DescribeNotificationRule_ResponseSyntax) **   <a name="codestarnotifications-DescribeNotificationRule-response-Targets"></a>
A list of the Amazon Q Developer in chat applications topics and Amazon Q Developer in chat applications clients associated with the notification rule.
Type: Array of [TargetSummary](API_TargetSummary.md) objects

## Errors
<a name="API_DescribeNotificationRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
 AWS CodeStar Notifications can't find a resource that matches the provided ARN.
HTTP Status Code: 404

 ** ValidationException **
One or more parameter values are not valid.
HTTP Status Code: 400

## See Also
<a name="API_DescribeNotificationRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codestar-notifications-2019-10-15/DescribeNotificationRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codestar-notifications-2019-10-15/DescribeNotificationRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codestar-notifications-2019-10-15/DescribeNotificationRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codestar-notifications-2019-10-15/DescribeNotificationRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codestar-notifications-2019-10-15/DescribeNotificationRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codestar-notifications-2019-10-15/DescribeNotificationRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codestar-notifications-2019-10-15/DescribeNotificationRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codestar-notifications-2019-10-15/DescribeNotificationRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codestar-notifications-2019-10-15/DescribeNotificationRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codestar-notifications-2019-10-15/DescribeNotificationRule)
