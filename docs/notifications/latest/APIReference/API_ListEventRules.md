---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListEventRules.html
---

# ListEventRules
<a name="API_ListEventRules"></a>

Returns a list of `EventRules` according to specified filters, in reverse chronological order (newest first).

## Request Syntax
<a name="API_ListEventRules_RequestSyntax"></a>

```
GET /event-rules?maxResults={{maxResults}}&nextToken={{nextToken}}&notificationConfigurationArn={{notificationConfigurationArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListEventRules_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListEventRules_RequestSyntax) **   <a name="Notifications-ListEventRules-request-uri-maxResults"></a>
The maximum number of results to be returned in this call. The default value is 20.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListEventRules_RequestSyntax) **   <a name="Notifications-ListEventRules-request-uri-nextToken"></a>
The start token for paginated calls. Retrieved from the response of a previous `ListEventRules` call. Next token uses Base64 encoding.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[\w+-/=]+`

 ** [notificationConfigurationArn](#API_ListEventRules_RequestSyntax) **   <a name="Notifications-ListEventRules-request-uri-notificationConfigurationArn"></a>
The Amazon Resource Name (ARN) of the `NotificationConfiguration`.
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:configuration/[a-z0-9]{27}`
Required: Yes

## Request Body
<a name="API_ListEventRules_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListEventRules_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "eventRules": [
      {
         "arn": "string",
         "creationTime": "string",
         "eventPattern": "string",
         "eventType": "string",
         "managedRules": [ "string" ],
         "notificationConfigurationArn": "string",
         "regions": [ "string" ],
         "source": "string",
         "statusSummaryByRegion": {
            "string" : {
               "reason": "string",
               "status": "string"
            }
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListEventRules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [eventRules](#API_ListEventRules_ResponseSyntax) **   <a name="Notifications-ListEventRules-response-eventRules"></a>
A list of `EventRules`.
Type: Array of [EventRuleStructure](API_EventRuleStructure.md) objects

 ** [nextToken](#API_ListEventRules_ResponseSyntax) **   <a name="Notifications-ListEventRules-response-nextToken"></a>
A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[\w+-/=]+`

## Errors
<a name="API_ListEventRules_Errors"></a>

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
<a name="API_ListEventRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/notifications-2018-05-10/ListEventRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/notifications-2018-05-10/ListEventRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/ListEventRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/notifications-2018-05-10/ListEventRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/ListEventRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/notifications-2018-05-10/ListEventRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/notifications-2018-05-10/ListEventRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/notifications-2018-05-10/ListEventRules)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/notifications-2018-05-10/ListEventRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/ListEventRules)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS User Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
