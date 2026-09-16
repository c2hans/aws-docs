---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CancelSubscription.html
---

# CancelSubscription
<a name="API_CancelSubscription"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Unsubscribes a user or a group from their pricing tier in an Amazon Q Business application. An unsubscribed user or group loses all Amazon Q Business feature access at the start of next month.

## Request Syntax
<a name="API_CancelSubscription_RequestSyntax"></a>

```
DELETE /applications/{{applicationId}}/subscriptions/{{subscriptionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_CancelSubscription_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_CancelSubscription_RequestSyntax) **   <a name="qbusiness-CancelSubscription-request-uri-applicationId"></a>
The identifier of the Amazon Q Business application for which the subscription is being cancelled.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [subscriptionId](#API_CancelSubscription_RequestSyntax) **   <a name="qbusiness-CancelSubscription-request-uri-subscriptionId"></a>
The identifier of the Amazon Q Business subscription being cancelled.
Length Constraints: Minimum length of 0. Maximum length of 1224.
Required: Yes

## Request Body
<a name="API_CancelSubscription_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CancelSubscription_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "currentSubscription": {
      "type": "string"
   },
   "nextSubscription": {
      "type": "string"
   },
   "subscriptionArn": "string"
}
```

## Response Elements
<a name="API_CancelSubscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [currentSubscription](#API_CancelSubscription_ResponseSyntax) **   <a name="qbusiness-CancelSubscription-response-currentSubscription"></a>
The type of your current Amazon Q Business subscription.
Type: [SubscriptionDetails](API_SubscriptionDetails.md) object

 ** [nextSubscription](#API_CancelSubscription_ResponseSyntax) **   <a name="qbusiness-CancelSubscription-response-nextSubscription"></a>
The type of the Amazon Q Business subscription for the next month.
Type: [SubscriptionDetails](API_SubscriptionDetails.md) object

 ** [subscriptionArn](#API_CancelSubscription_ResponseSyntax) **   <a name="qbusiness-CancelSubscription-response-subscriptionArn"></a>
The Amazon Resource Name (ARN) of the Amazon Q Business subscription being cancelled.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

## Errors
<a name="API_CancelSubscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.
HTTP Status Code: 403

 ** InternalServerException **
An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact [Support](http://aws.amazon.com/contact-us/) for help.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.
 ** message **
The message describing a `ResourceNotFoundException`.
 ** resourceId **
The identifier of the resource affected.
 ** resourceType **
The type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to throttling. Reduce the number of requests and try again.
HTTP Status Code: 429

 ** ValidationException **
The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.
 ** fields **
The input field(s) that failed validation.
 ** message **
The message describing the `ValidationException`.
 ** reason **
The reason for the `ValidationException`.
HTTP Status Code: 400

## See Also
<a name="API_CancelSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/CancelSubscription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/CancelSubscription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/CancelSubscription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/CancelSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/CancelSubscription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/CancelSubscription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/CancelSubscription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/CancelSubscription)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/CancelSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/CancelSubscription)
