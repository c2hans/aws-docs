---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListManagedNotificationChannelAssociations.html
---

# ListManagedNotificationChannelAssociations
<a name="API_ListManagedNotificationChannelAssociations"></a>

Returns a list of Account contacts and Channels associated with a `ManagedNotificationConfiguration`, in paginated format.

## Request Syntax
<a name="API_ListManagedNotificationChannelAssociations_RequestSyntax"></a>

```
GET /channels/list-managed-notification-channel-associations?managedNotificationConfigurationArn={{managedNotificationConfigurationArn}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListManagedNotificationChannelAssociations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [managedNotificationConfigurationArn](#API_ListManagedNotificationChannelAssociations_RequestSyntax) **   <a name="Notifications-ListManagedNotificationChannelAssociations-request-uri-managedNotificationConfigurationArn"></a>
The Amazon Resource Name (ARN) of the `ManagedNotificationConfiguration` to match.
Pattern: `arn:[-.a-z0-9]{1,63}:notifications::[0-9]{12}:managed-notification-configuration/category/[a-zA-Z0-9\-]{3,64}/sub-category/[a-zA-Z0-9\-]{3,64}`
Required: Yes

 ** [maxResults](#API_ListManagedNotificationChannelAssociations_RequestSyntax) **   <a name="Notifications-ListManagedNotificationChannelAssociations-request-uri-maxResults"></a>
The maximum number of results to be returned in this call. Defaults to 20.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListManagedNotificationChannelAssociations_RequestSyntax) **   <a name="Notifications-ListManagedNotificationChannelAssociations-request-uri-nextToken"></a>
The start token for paginated calls. Retrieved from the response of a previous `ListManagedNotificationChannelAssociations` call.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[\w+-/=]+`

## Request Body
<a name="API_ListManagedNotificationChannelAssociations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListManagedNotificationChannelAssociations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "channelAssociations": [
      {
         "channelIdentifier": "string",
         "channelType": "string",
         "overrideOption": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListManagedNotificationChannelAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [channelAssociations](#API_ListManagedNotificationChannelAssociations_ResponseSyntax) **   <a name="Notifications-ListManagedNotificationChannelAssociations-response-channelAssociations"></a>
A list that contains the following information about a channel association.
Type: Array of [ManagedNotificationChannelAssociationSummary](API_ManagedNotificationChannelAssociationSummary.md) objects

 ** [nextToken](#API_ListManagedNotificationChannelAssociations_ResponseSyntax) **   <a name="Notifications-ListManagedNotificationChannelAssociations-response-nextToken"></a>
A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[\w+-/=]+`

## Errors
<a name="API_ListManagedNotificationChannelAssociations_Errors"></a>

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
<a name="API_ListManagedNotificationChannelAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/notifications-2018-05-10/ListManagedNotificationChannelAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/notifications-2018-05-10/ListManagedNotificationChannelAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/ListManagedNotificationChannelAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/notifications-2018-05-10/ListManagedNotificationChannelAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/ListManagedNotificationChannelAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/notifications-2018-05-10/ListManagedNotificationChannelAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/notifications-2018-05-10/ListManagedNotificationChannelAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/notifications-2018-05-10/ListManagedNotificationChannelAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/notifications-2018-05-10/ListManagedNotificationChannelAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/ListManagedNotificationChannelAssociations)
