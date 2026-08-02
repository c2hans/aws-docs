---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_GetNotificationsAccessForOrganization.html
---

# GetNotificationsAccessForOrganization
<a name="API_GetNotificationsAccessForOrganization"></a>

Returns the AccessStatus of Service Trust Enablement for AWS User Notifications and AWS Organizations.

## Request Syntax
<a name="API_GetNotificationsAccessForOrganization_RequestSyntax"></a>

```
GET /organization/access HTTP/1.1
```

## URI Request Parameters
<a name="API_GetNotificationsAccessForOrganization_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetNotificationsAccessForOrganization_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetNotificationsAccessForOrganization_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "notificationsAccessForOrganization": {
      "accessStatus": "string"
   }
}
```

## Response Elements
<a name="API_GetNotificationsAccessForOrganization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [notificationsAccessForOrganization](#API_GetNotificationsAccessForOrganization_ResponseSyntax) **   <a name="Notifications-GetNotificationsAccessForOrganization-response-notificationsAccessForOrganization"></a>
The `AccessStatus` of Service Trust Enablement for AWS User Notifications to AWS Organizations.
Type: [NotificationsAccessForOrganization](API_NotificationsAccessForOrganization.md) object

## Errors
<a name="API_GetNotificationsAccessForOrganization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ThrottlingException **
Request was denied due to request throttling.
 ** quotaCode **
Identifies the quota that is being throttled.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
 ** serviceCode **
Identifies the service being throttled.
HTTP Status Code: 429

 ** ValidationException **
This exception is thrown when the notification event fails validation.
 ** fieldList **
The list of input fields that are invalid.
 ** reason **
The reason why your input is considered invalid.
HTTP Status Code: 400

## See Also
<a name="API_GetNotificationsAccessForOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/notifications-2018-05-10/GetNotificationsAccessForOrganization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/notifications-2018-05-10/GetNotificationsAccessForOrganization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/GetNotificationsAccessForOrganization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/notifications-2018-05-10/GetNotificationsAccessForOrganization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/GetNotificationsAccessForOrganization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/notifications-2018-05-10/GetNotificationsAccessForOrganization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/notifications-2018-05-10/GetNotificationsAccessForOrganization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/notifications-2018-05-10/GetNotificationsAccessForOrganization)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/notifications-2018-05-10/GetNotificationsAccessForOrganization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/GetNotificationsAccessForOrganization)
