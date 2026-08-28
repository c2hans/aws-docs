---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListCodeSecurityScanConfigurationAssociations.html
---

# ListCodeSecurityScanConfigurationAssociations
<a name="API_ListCodeSecurityScanConfigurationAssociations"></a>

Lists the associations between code repositories and Amazon Inspector code security scan configurations.

## Request Syntax
<a name="API_ListCodeSecurityScanConfigurationAssociations_RequestSyntax"></a>

```
POST /codesecurity/scan-configuration/associations/list?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
Content-type: application/json

{
   "scanConfigurationArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListCodeSecurityScanConfigurationAssociations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListCodeSecurityScanConfigurationAssociations_RequestSyntax) **   <a name="inspector2-ListCodeSecurityScanConfigurationAssociations-request-uri-maxResults"></a>
The maximum number of results to return in the response. If your request would return more than the maximum the response will return a `nextToken` value, use this value when you call the action again to get the remaining results.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListCodeSecurityScanConfigurationAssociations_RequestSyntax) **   <a name="inspector2-ListCodeSecurityScanConfigurationAssociations-request-uri-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the `NextToken` value returned from the previous request to continue listing results after the first page.
Length Constraints: Minimum length of 0. Maximum length of 1000000.

## Request Body
<a name="API_ListCodeSecurityScanConfigurationAssociations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [scanConfigurationArn](#API_ListCodeSecurityScanConfigurationAssociations_RequestSyntax) **   <a name="inspector2-ListCodeSecurityScanConfigurationAssociations-request-scanConfigurationArn"></a>
The Amazon Resource Name (ARN) of the scan configuration to list associations for.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:owner/(\d{12}|o-[a-z0-9]{10,32})/codesecurity-configuration/[a-f0-9-]{36}`
Required: Yes

## Response Syntax
<a name="API_ListCodeSecurityScanConfigurationAssociations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "associations": [
      {
         "resource": { ... }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCodeSecurityScanConfigurationAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [associations](#API_ListCodeSecurityScanConfigurationAssociations_ResponseSyntax) **   <a name="inspector2-ListCodeSecurityScanConfigurationAssociations-response-associations"></a>
A list of associations between code repositories and scan configurations.
Type: Array of [CodeSecurityScanConfigurationAssociationSummary](API_CodeSecurityScanConfigurationAssociationSummary.md) objects

 ** [nextToken](#API_ListCodeSecurityScanConfigurationAssociations_ResponseSyntax) **   <a name="inspector2-ListCodeSecurityScanConfigurationAssociations-response-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the `NextToken` value returned from the previous request to continue listing results after the first page.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000000.

## Errors
<a name="API_ListCodeSecurityScanConfigurationAssociations_Errors"></a>

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

 ** ResourceNotFoundException **
The operation tried to access an invalid resource. Make sure the resource is specified correctly.
HTTP Status Code: 404

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
<a name="API_ListCodeSecurityScanConfigurationAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/ListCodeSecurityScanConfigurationAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/ListCodeSecurityScanConfigurationAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ListCodeSecurityScanConfigurationAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/ListCodeSecurityScanConfigurationAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ListCodeSecurityScanConfigurationAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/ListCodeSecurityScanConfigurationAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/ListCodeSecurityScanConfigurationAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/ListCodeSecurityScanConfigurationAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/ListCodeSecurityScanConfigurationAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ListCodeSecurityScanConfigurationAssociations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
