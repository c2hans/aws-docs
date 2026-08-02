---
source_url: https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_Unsubscribe.html
---

# Unsubscribe
<a name="API_Unsubscribe"></a>

Removes an association between a notification rule and an Amazon Q Developer in chat applications topic so that subscribers to that topic stop receiving notifications when the events described in the rule are triggered.

## Request Syntax
<a name="API_Unsubscribe_RequestSyntax"></a>

```
POST /unsubscribe HTTP/1.1
Content-type: application/json

{
   "Arn": "{{string}}",
   "TargetAddress": "{{string}}"
}
```

## URI Request Parameters
<a name="API_Unsubscribe_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_Unsubscribe_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Arn](#API_Unsubscribe_RequestSyntax) **   <a name="codestarnotifications-Unsubscribe-request-Arn"></a>
The Amazon Resource Name (ARN) of the notification rule.
Type: String
Pattern: `^arn:aws[^:\s]*:codestar-notifications:[^:\s]+:\d{12}:notificationrule\/(.*\S)?$`
Required: Yes

 ** [TargetAddress](#API_Unsubscribe_RequestSyntax) **   <a name="codestarnotifications-Unsubscribe-request-TargetAddress"></a>
The ARN of the Amazon Q Developer in chat applications topic to unsubscribe from the notification rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 320.
Required: Yes

## Response Syntax
<a name="API_Unsubscribe_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string"
}
```

## Response Elements
<a name="API_Unsubscribe_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_Unsubscribe_ResponseSyntax) **   <a name="codestarnotifications-Unsubscribe-response-Arn"></a>
The Amazon Resource Name (ARN) of the the notification rule from which you have removed a subscription.
Type: String
Pattern: `^arn:aws[^:\s]*:codestar-notifications:[^:\s]+:\d{12}:notificationrule\/(.*\S)?$`

## Errors
<a name="API_Unsubscribe_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ValidationException **
One or more parameter values are not valid.
HTTP Status Code: 400

## See Also
<a name="API_Unsubscribe_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codestar-notifications-2019-10-15/Unsubscribe)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codestar-notifications-2019-10-15/Unsubscribe)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codestar-notifications-2019-10-15/Unsubscribe)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codestar-notifications-2019-10-15/Unsubscribe)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codestar-notifications-2019-10-15/Unsubscribe)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codestar-notifications-2019-10-15/Unsubscribe)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codestar-notifications-2019-10-15/Unsubscribe)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codestar-notifications-2019-10-15/Unsubscribe)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codestar-notifications-2019-10-15/Unsubscribe)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codestar-notifications-2019-10-15/Unsubscribe)
