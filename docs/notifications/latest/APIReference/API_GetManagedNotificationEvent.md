---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_GetManagedNotificationEvent.html
---

# GetManagedNotificationEvent
<a name="API_GetManagedNotificationEvent"></a>

Returns a specified `ManagedNotificationEvent`.

## Request Syntax
<a name="API_GetManagedNotificationEvent_RequestSyntax"></a>

```
GET /managed-notification-events/{{arn}}?locale={{locale}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetManagedNotificationEvent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [arn](#API_GetManagedNotificationEvent_RequestSyntax) **   <a name="Notifications-GetManagedNotificationEvent-request-uri-arn"></a>
The Amazon Resource Name (ARN) of the `ManagedNotificationEvent` to return.
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:managed-notification-configuration/category/[a-zA-Z0-9\-]{3,64}/sub-category/[a-zA-Z0-9\-]{3,64}/event/[a-z0-9]{27}`
Required: Yes

 ** [locale](#API_GetManagedNotificationEvent_RequestSyntax) **   <a name="Notifications-GetManagedNotificationEvent-request-uri-locale"></a>
The locale code of the language used for the retrieved `ManagedNotificationEvent`. The default locale is English `(en_US)`.
Valid Values: `de_DE | en_CA | en_US | en_UK | es_ES | fr_CA | fr_FR | id_ID | it_IT | ja_JP | ko_KR | pt_BR | tr_TR | zh_CN | zh_TW`

## Request Body
<a name="API_GetManagedNotificationEvent_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetManagedNotificationEvent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "content": {
      "aggregationEventType": "string",
      "aggregationSummary": {
         "additionalSummarizationDimensions": [
            {
               "count": number,
               "name": "string",
               "sampleValues": [ "string" ]
            }
         ],
         "aggregatedAccounts": {
            "count": number,
            "name": "string",
            "sampleValues": [ "string" ]
         },
         "aggregatedBy": [
            {
               "name": "string",
               "value": "string"
            }
         ],
         "aggregatedOrganizationalUnits": {
            "count": number,
            "name": "string",
            "sampleValues": [ "string" ]
         },
         "aggregatedRegions": {
            "count": number,
            "name": "string",
            "sampleValues": [ "string" ]
         },
         "eventCount": number
      },
      "endTime": "string",
      "eventStatus": "string",
      "id": "string",
      "messageComponents": {
         "completeDescription": "string",
         "dimensions": [
            {
               "name": "string",
               "value": "string"
            }
         ],
         "headline": "string",
         "paragraphSummary": "string"
      },
      "notificationType": "string",
      "organizationalUnitId": "string",
      "schemaVersion": "string",
      "sourceEventDetailUrl": "string",
      "sourceEventDetailUrlDisplayText": "string",
      "startTime": "string",
      "textParts": {
         "string" : {
            "displayText": "string",
            "textByLocale": {
               "string" : "string"
            },
            "type": "string",
            "url": "string"
         }
      }
   },
   "creationTime": "string",
   "managedNotificationConfigurationArn": "string"
}
```

## Response Elements
<a name="API_GetManagedNotificationEvent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetManagedNotificationEvent_ResponseSyntax) **   <a name="Notifications-GetManagedNotificationEvent-response-arn"></a>
The ARN of the resource.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:managed-notification-configuration/category/[a-zA-Z0-9\-]{3,64}/sub-category/[a-zA-Z0-9\-]{3,64}/event/[a-z0-9]{27}`

 ** [content](#API_GetManagedNotificationEvent_ResponseSyntax) **   <a name="Notifications-GetManagedNotificationEvent-response-content"></a>
The content of the `ManagedNotificationEvent`.
Type: [ManagedNotificationEvent](API_ManagedNotificationEvent.md) object

 ** [creationTime](#API_GetManagedNotificationEvent_ResponseSyntax) **   <a name="Notifications-GetManagedNotificationEvent-response-creationTime"></a>
The creation time of the `ManagedNotificationEvent`.
Type: Timestamp

 ** [managedNotificationConfigurationArn](#API_GetManagedNotificationEvent_ResponseSyntax) **   <a name="Notifications-GetManagedNotificationEvent-response-managedNotificationConfigurationArn"></a>
The ARN of the `ManagedNotificationConfiguration`.
Type: String
Pattern: `arn:[-.a-z0-9]{1,63}:notifications::[0-9]{12}:managed-notification-configuration/category/[a-zA-Z0-9\-]{3,64}/sub-category/[a-zA-Z0-9\-]{3,64}`

## Errors
<a name="API_GetManagedNotificationEvent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** resourceId **
The ID of the resource that wasn't found.
HTTP Status Code: 404

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
<a name="API_GetManagedNotificationEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/notifications-2018-05-10/GetManagedNotificationEvent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/notifications-2018-05-10/GetManagedNotificationEvent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/GetManagedNotificationEvent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/notifications-2018-05-10/GetManagedNotificationEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/GetManagedNotificationEvent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/notifications-2018-05-10/GetManagedNotificationEvent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/notifications-2018-05-10/GetManagedNotificationEvent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/notifications-2018-05-10/GetManagedNotificationEvent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/notifications-2018-05-10/GetManagedNotificationEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/GetManagedNotificationEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS User Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
