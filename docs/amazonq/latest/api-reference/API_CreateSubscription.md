---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateSubscription.html
---

# CreateSubscription
<a name="API_CreateSubscription"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Subscribes an IAM Identity Center user or a group to a pricing tier for an Amazon Q Business application.

Amazon Q Business offers two subscription tiers: `Q_LITE` and `Q_BUSINESS`. Subscription tier determines feature access for the user. For more information on subscriptions and pricing tiers, see [Amazon Q Business pricing](https://aws.amazon.com/q/business/pricing/).

**Note**
For an example IAM role policy for assigning subscriptions, see [Set up required permissions](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/setting-up.html#permissions) in the Amazon Q Business User Guide.

## Request Syntax
<a name="API_CreateSubscription_RequestSyntax"></a>

```
POST /applications/{{applicationId}}/subscriptions HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "principal": { ... },
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateSubscription_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_CreateSubscription_RequestSyntax) **   <a name="qbusiness-CreateSubscription-request-uri-applicationId"></a>
The identifier of the Amazon Q Business application the subscription should be added to.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

## Request Body
<a name="API_CreateSubscription_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateSubscription_RequestSyntax) **   <a name="qbusiness-CreateSubscription-request-clientToken"></a>
A token that you provide to identify the request to create a subscription for your Amazon Q Business application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [principal](#API_CreateSubscription_RequestSyntax) **   <a name="qbusiness-CreateSubscription-request-principal"></a>
The IAM Identity Center `UserId` or `GroupId` of a user or group in the IAM Identity Center instance connected to the Amazon Q Business application.
Type: [SubscriptionPrincipal](API_SubscriptionPrincipal.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [type](#API_CreateSubscription_RequestSyntax) **   <a name="qbusiness-CreateSubscription-request-type"></a>
The type of Amazon Q Business subscription you want to create.
Type: String
Valid Values: `Q_LITE | Q_BUSINESS`
Required: Yes

## Response Syntax
<a name="API_CreateSubscription_ResponseSyntax"></a>

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
   "subscriptionArn": "string",
   "subscriptionId": "string"
}
```

## Response Elements
<a name="API_CreateSubscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [currentSubscription](#API_CreateSubscription_ResponseSyntax) **   <a name="qbusiness-CreateSubscription-response-currentSubscription"></a>
The type of your current Amazon Q Business subscription.
Type: [SubscriptionDetails](API_SubscriptionDetails.md) object

 ** [nextSubscription](#API_CreateSubscription_ResponseSyntax) **   <a name="qbusiness-CreateSubscription-response-nextSubscription"></a>
The type of the Amazon Q Business subscription for the next month.
Type: [SubscriptionDetails](API_SubscriptionDetails.md) object

 ** [subscriptionArn](#API_CreateSubscription_ResponseSyntax) **   <a name="qbusiness-CreateSubscription-response-subscriptionArn"></a>
The Amazon Resource Name (ARN) of the Amazon Q Business subscription created.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [subscriptionId](#API_CreateSubscription_ResponseSyntax) **   <a name="qbusiness-CreateSubscription-response-subscriptionId"></a>
The identifier of the Amazon Q Business subscription created.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1224.

## Errors
<a name="API_CreateSubscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.
HTTP Status Code: 403

 ** ConflictException **
You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.
 ** message **
The message describing a `ConflictException`.
 ** resourceId **
The identifier of the resource affected.
 ** resourceType **
The type of the resource affected.
HTTP Status Code: 409

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
<a name="API_CreateSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/CreateSubscription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/CreateSubscription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/CreateSubscription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/CreateSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/CreateSubscription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/CreateSubscription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/CreateSubscription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/CreateSubscription)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/CreateSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/CreateSubscription)
