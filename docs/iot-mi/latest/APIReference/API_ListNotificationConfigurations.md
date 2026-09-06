---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_ListNotificationConfigurations.html
---

# ListNotificationConfigurations
<a name="API_ListNotificationConfigurations"></a>

 List all notification configurations.

## Request Syntax
<a name="API_ListNotificationConfigurations_RequestSyntax"></a>

```
GET /notification-configurations?MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListNotificationConfigurations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListNotificationConfigurations_RequestSyntax) **   <a name="managedintegrations-ListNotificationConfigurations-request-uri-MaxResults"></a>
The maximum number of results to return at one time.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListNotificationConfigurations_RequestSyntax) **   <a name="managedintegrations-ListNotificationConfigurations-request-uri-NextToken"></a>
A token that can be used to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 65535.
Pattern: `[a-zA-Z0-9=_-]+`

## Request Body
<a name="API_ListNotificationConfigurations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListNotificationConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "NotificationConfigurationList": [
      {
         "DestinationName": "string",
         "EventType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListNotificationConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListNotificationConfigurations_ResponseSyntax) **   <a name="managedintegrations-ListNotificationConfigurations-response-NextToken"></a>
A token that can be used to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Pattern: `[a-zA-Z0-9=_-]+`

 ** [NotificationConfigurationList](#API_ListNotificationConfigurations_ResponseSyntax) **   <a name="managedintegrations-ListNotificationConfigurations-response-NotificationConfigurationList"></a>
The list of notification configurations.
Type: Array of [NotificationConfigurationSummary](API_NotificationConfigurationSummary.md) objects

## Errors
<a name="API_ListNotificationConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User is not authorized.
HTTP Status Code: 403

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
A validation error occurred when performing the API request.
HTTP Status Code: 400

## See Also
<a name="API_ListNotificationConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/ListNotificationConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/ListNotificationConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/ListNotificationConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/ListNotificationConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/ListNotificationConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/ListNotificationConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/ListNotificationConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/ListNotificationConfigurations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/ListNotificationConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/ListNotificationConfigurations)
