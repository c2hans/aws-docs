---
source_url: https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_ListRooms.html
---

# ListRooms
<a name="API_ListRooms"></a>

Gets summary information about all your rooms in the AWS region where the API request is processed. Results are sorted in descending order of `updateTime`.

## Request Syntax
<a name="API_ListRooms_RequestSyntax"></a>

```
POST /ListRooms HTTP/1.1
Content-type: application/json

{
   "loggingConfigurationIdentifier": "{{string}}",
   "maxResults": {{number}},
   "messageReviewHandlerUri": "{{string}}",
   "name": "{{string}}",
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListRooms_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListRooms_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [loggingConfigurationIdentifier](#API_ListRooms_RequestSyntax) **   <a name="ivs-ListRooms-request-loggingConfigurationIdentifier"></a>
Logging-configuration identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivschat:[a-z0-9-]+:[0-9]+:logging-configuration/[a-zA-Z0-9-]+`
Required: No

 ** [maxResults](#API_ListRooms_RequestSyntax) **   <a name="ivs-ListRooms-request-maxResults"></a>
Maximum number of rooms to return. Default: 50.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [messageReviewHandlerUri](#API_ListRooms_RequestSyntax) **   <a name="ivs-ListRooms-request-messageReviewHandlerUri"></a>
Filters the list to match the specified message review handler URI.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 170.
Pattern: `$|^arn:aws:lambda:[a-z0-9-]+:[0-9]{12}:function:.+.*`
Required: No

 ** [name](#API_ListRooms_RequestSyntax) **   <a name="ivs-ListRooms-request-name"></a>
Filters the list to match the specified room name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** [nextToken](#API_ListRooms_RequestSyntax) **   <a name="ivs-ListRooms-request-nextToken"></a>
The first room to retrieve. This is used for pagination; see the `nextToken` response field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListRooms_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "rooms": [
      {
         "arn": "string",
         "createTime": "string",
         "id": "string",
         "loggingConfigurationIdentifiers": [ "string" ],
         "messageReviewHandler": {
            "fallbackResult": "string",
            "uri": "string"
         },
         "name": "string",
         "tags": {
            "string" : "string"
         },
         "updateTime": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRooms_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListRooms_ResponseSyntax) **   <a name="ivs-ListRooms-response-nextToken"></a>
If there are more rooms than `maxResults`, use `nextToken` in the request to get the next set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [rooms](#API_ListRooms_ResponseSyntax) **   <a name="ivs-ListRooms-response-rooms"></a>
List of the matching rooms (summary information only).
Type: Array of [RoomSummary](API_RoomSummary.md) objects

## Errors
<a name="API_ListRooms_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **

HTTP Status Code: 403

 ** ResourceNotFoundException **

HTTP Status Code: 404

 ** ValidationException **

HTTP Status Code: 400

## See Also
<a name="API_ListRooms_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivschat-2020-07-14/ListRooms)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivschat-2020-07-14/ListRooms)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivschat-2020-07-14/ListRooms)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivschat-2020-07-14/ListRooms)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivschat-2020-07-14/ListRooms)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivschat-2020-07-14/ListRooms)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivschat-2020-07-14/ListRooms)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivschat-2020-07-14/ListRooms)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivschat-2020-07-14/ListRooms)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivschat-2020-07-14/ListRooms)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
