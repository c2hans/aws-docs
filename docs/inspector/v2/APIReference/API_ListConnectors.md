---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListConnectors.html
---

# ListConnectors
<a name="API_ListConnectors"></a>

Lists connectors in your account. Results are paginated. Use the `nextToken` parameter to retrieve the next page of results.

## Request Syntax
<a name="API_ListConnectors_RequestSyntax"></a>

```
POST /connector/list HTTP/1.1
Content-type: application/json

{
   "filterCriteria": {
      "accounts": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "awsConfigConnectorArns": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "connectorArns": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "connectorType": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "provider": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ]
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListConnectors_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListConnectors_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filterCriteria](#API_ListConnectors_RequestSyntax) **   <a name="inspector2-ListConnectors-request-filterCriteria"></a>
The filter criteria to apply to the list of connectors.
Type: [ConnectorFilterCriteria](API_ConnectorFilterCriteria.md) object
Required: No

 ** [maxResults](#API_ListConnectors_RequestSyntax) **   <a name="inspector2-ListConnectors-request-maxResults"></a>
The maximum number of results to return in a single call. To retrieve the remaining results, make another request with the `nextToken` value returned from this request.
Type: Integer
Required: No

 ** [nextToken](#API_ListConnectors_RequestSyntax) **   <a name="inspector2-ListConnectors-request-nextToken"></a>
A token to use for paginating results. Set this value to null for the first request. For subsequent calls, use the `nextToken` value returned from the previous request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListConnectors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "autoInstallVMScanner": boolean,
         "awsConfigConnectorArn": "string",
         "azureRegions": [ "string" ],
         "connectorArn": "string",
         "createdAt": "string",
         "description": "string",
         "enablementStatus": "string",
         "enablementStatusReason": "string",
         "health": {
            "connectorStatus": "string",
            "lastCheckedAt": "string",
            "message": "string"
         },
         "name": "string",
         "provider": "string",
         "scopeConfiguration": {
            "containerImageScanning": {
               "scopeType": "string",
               "scopeValues": [ "string" ],
               "state": "string",
               "stateReason": "string"
            },
            "serverlessScanning": {
               "scopeType": "string",
               "scopeValues": [ "string" ],
               "state": "string",
               "stateReason": "string"
            },
            "vmScanning": {
               "scopeType": "string",
               "scopeValues": [ "string" ],
               "state": "string",
               "stateReason": "string"
            }
         },
         "tags": {
            "string" : "string"
         },
         "updatedAt": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListConnectors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListConnectors_ResponseSyntax) **   <a name="inspector2-ListConnectors-response-items"></a>
A list of connectors.
Type: Array of [Connector](API_Connector.md) objects

 ** [nextToken](#API_ListConnectors_ResponseSyntax) **   <a name="inspector2-ListConnectors-response-nextToken"></a>
A pagination token. If this value is not null, there are additional results available. Use this token in the `nextToken` parameter of a subsequent request to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListConnectors_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 For `Enable`, you receive this error if you attempt to use a feature in an unsupported AWS Region.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed due to an internal failure of the Amazon Inspector service.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation due to missing required fields or having invalid inputs.
 ** fields **
The fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_ListConnectors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/ListConnectors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/ListConnectors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ListConnectors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/ListConnectors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ListConnectors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/ListConnectors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/ListConnectors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/ListConnectors)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/ListConnectors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ListConnectors)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
