---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SendOutboundWebNotification.html
---

# SendOutboundWebNotification
<a name="API_SendOutboundWebNotification"></a>

Sends an outbound web notification to a customer's web browser for outbound campaigns. For more information about outbound campaigns, see [Set up Connect Customer outbound campaigns](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html).

**Note**
Only the Connect Customer outbound campaigns service principal is allowed to assume a role in your account and call this API.

## Request Syntax
<a name="API_SendOutboundWebNotification_RequestSyntax"></a>

```
POST /instance/{{InstanceId}}/outbound-web-notification HTTP/1.1
Content-type: application/json

{
   "BrowserId": "{{string}}",
   "ClientToken": "{{string}}",
   "Content": {
      "Attributes": {
         "RecommenderConfig": {
            "Context": {
               "{{string}}" : "{{string}}"
            },
            "DomainName": "{{string}}",
            "RecommenderName": "{{string}}"
         }
      },
      "Type": "{{string}}",
      "ViewArn": "{{string}}"
   },
   "Destination": {
      "ProfileId": "{{string}}",
      "WidgetId": "{{string}}"
   },
   "ExpiresAt": {{number}},
   "SessionId": "{{string}}",
   "Source": {
      "SourceCampaign": {
         "CampaignId": "{{string}}",
         "OutboundRequestId": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_SendOutboundWebNotification_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_SendOutboundWebNotification_RequestSyntax) **   <a name="connect-SendOutboundWebNotification-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_SendOutboundWebNotification_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [BrowserId](#API_SendOutboundWebNotification_RequestSyntax) **   <a name="connect-SendOutboundWebNotification-request-BrowserId"></a>
A unique identifier for the customer's web browser instance to which the notification is being sent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: Yes

 ** [ClientToken](#API_SendOutboundWebNotification_RequestSyntax) **   <a name="connect-SendOutboundWebNotification-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [Content](#API_SendOutboundWebNotification_RequestSyntax) **   <a name="connect-SendOutboundWebNotification-request-Content"></a>
The content of the web notification, including the notification type, the view to render, and any optional attributes used to populate it.
Type: [WebNotificationContent](API_WebNotificationContent.md) object
Required: Yes

 ** [Destination](#API_SendOutboundWebNotification_RequestSyntax) **   <a name="connect-SendOutboundWebNotification-request-Destination"></a>
The destination for the web notification, specifying the communication widget that delivers the notification and the customer profile of the recipient.
Type: [WidgetDestination](API_WidgetDestination.md) object
Required: Yes

 ** [ExpiresAt](#API_SendOutboundWebNotification_RequestSyntax) **   <a name="connect-SendOutboundWebNotification-request-ExpiresAt"></a>
The timestamp, in Unix epoch time format, at which the web notification expires. After this time, the notification is no longer delivered to the customer's browser.
Type: Timestamp
Required: Yes

 ** [SessionId](#API_SendOutboundWebNotification_RequestSyntax) **   <a name="connect-SendOutboundWebNotification-request-SessionId"></a>
A unique identifier for the customer's web session to which the notification is being sent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: Yes

 ** [Source](#API_SendOutboundWebNotification_RequestSyntax) **   <a name="connect-SendOutboundWebNotification-request-Source"></a>
The source of the web notification. A `SourceCampaign` object identifies the campaign and outbound request that triggered this notification.
Type: [WebNotificationSource](API_WebNotificationSource.md) object
Required: Yes

## Response Syntax
<a name="API_SendOutboundWebNotification_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_SendOutboundWebNotification_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SendOutboundWebNotification_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_SendOutboundWebNotification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/SendOutboundWebNotification)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/SendOutboundWebNotification)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SendOutboundWebNotification)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/SendOutboundWebNotification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SendOutboundWebNotification)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/SendOutboundWebNotification)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/SendOutboundWebNotification)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/SendOutboundWebNotification)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/SendOutboundWebNotification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SendOutboundWebNotification)
