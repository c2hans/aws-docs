---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListConnectorScanConfigurations.html
---

# ListConnectorScanConfigurations
<a name="API_ListConnectorScanConfigurations"></a>

Lists scan configurations for AWS Config connectors. Results are paginated. Use the `nextToken` parameter to retrieve the next page of results.

## Request Syntax
<a name="API_ListConnectorScanConfigurations_RequestSyntax"></a>

```
POST /connectorscanconfigurations/list HTTP/1.1
Content-type: application/json

{
   "awsConfigConnectorArns": [ "{{string}}" ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListConnectorScanConfigurations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListConnectorScanConfigurations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [awsConfigConnectorArns](#API_ListConnectorScanConfigurations_RequestSyntax) **   <a name="inspector2-ListConnectorScanConfigurations-request-awsConfigConnectorArns"></a>
The list of AWS Config connector ARNs to filter results.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:([^:]+):config:([^:]+):([^:]+):connector/([^/]+)/([^/]+)/([^/:\s]+)`
Required: No

 ** [maxResults](#API_ListConnectorScanConfigurations_RequestSyntax) **   <a name="inspector2-ListConnectorScanConfigurations-request-maxResults"></a>
The maximum number of results to return in a single call. Valid range is 1 to 50. To retrieve the remaining results, make another request with the `nextToken` value returned from this request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_ListConnectorScanConfigurations_RequestSyntax) **   <a name="inspector2-ListConnectorScanConfigurations-request-nextToken"></a>
A token to use for paginating results. Set this value to null for the first request. For subsequent calls, use the `nextToken` value returned from the previous request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListConnectorScanConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "scanConfigurations": [
      {
         "awsConfigConnectorArn": "string",
         "connectorArns": [ "string" ],
         "scanConfiguration": {
            "containerImageScanning": {
               "pullDuration": "string",
               "pushDuration": "string"
            }
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListConnectorScanConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListConnectorScanConfigurations_ResponseSyntax) **   <a name="inspector2-ListConnectorScanConfigurations-response-nextToken"></a>
A pagination token. If this value is not null, there are additional results available. Use this token in the `nextToken` parameter of a subsequent request to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [scanConfigurations](#API_ListConnectorScanConfigurations_ResponseSyntax) **   <a name="inspector2-ListConnectorScanConfigurations-response-scanConfigurations"></a>
A list of scan configuration items.
Type: Array of [ConnectorScanConfigurationItem](API_ConnectorScanConfigurationItem.md) objects

## Errors
<a name="API_ListConnectorScanConfigurations_Errors"></a>

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
<a name="API_ListConnectorScanConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/ListConnectorScanConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/ListConnectorScanConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ListConnectorScanConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/ListConnectorScanConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ListConnectorScanConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/ListConnectorScanConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/ListConnectorScanConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/ListConnectorScanConfigurations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/ListConnectorScanConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ListConnectorScanConfigurations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
