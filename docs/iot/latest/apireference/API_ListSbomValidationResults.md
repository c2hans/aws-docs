---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListSbomValidationResults.html
---

# ListSbomValidationResults
<a name="API_ListSbomValidationResults"></a>

The validation results for all software bill of materials (SBOM) attached to a specific software package version.

Requires permission to access the [ListSbomValidationResults](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListSbomValidationResults_RequestSyntax"></a>

```
GET /packages/{{packageName}}/versions/{{versionName}}/sbom-validation-results?maxResults={{maxResults}}&nextToken={{nextToken}}&validationResult={{validationResult}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSbomValidationResults_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListSbomValidationResults_RequestSyntax) **   <a name="iot-ListSbomValidationResults-request-uri-maxResults"></a>
The maximum number of results to return at one time.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListSbomValidationResults_RequestSyntax) **   <a name="iot-ListSbomValidationResults-request-uri-nextToken"></a>
A token that can be used to retrieve the next set of results, or null if there are no additional results.

 ** [packageName](#API_ListSbomValidationResults_RequestSyntax) **   <a name="iot-ListSbomValidationResults-request-uri-packageName"></a>
The name of the new software package.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_.]+`
Required: Yes

 ** [validationResult](#API_ListSbomValidationResults_RequestSyntax) **   <a name="iot-ListSbomValidationResults-request-uri-validationResult"></a>
The end result of the
Valid Values: `FAILED | SUCCEEDED`

 ** [versionName](#API_ListSbomValidationResults_RequestSyntax) **   <a name="iot-ListSbomValidationResults-request-uri-versionName"></a>
The name of the new package version.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_.]+`
Required: Yes

## Request Body
<a name="API_ListSbomValidationResults_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListSbomValidationResults_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "validationResultSummaries": [
      {
         "errorCode": "string",
         "errorMessage": "string",
         "fileName": "string",
         "validationResult": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSbomValidationResults_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSbomValidationResults_ResponseSyntax) **   <a name="iot-ListSbomValidationResults-response-nextToken"></a>
A token that can be used to retrieve the next set of results, or null if there are no additional results.
Type: String

 ** [validationResultSummaries](#API_ListSbomValidationResults_ResponseSyntax) **   <a name="iot-ListSbomValidationResults-response-validationResultSummaries"></a>
A summary of the validation results for each software bill of materials attached to a software package version.
Type: Array of [SbomValidationResultSummary](API_SbomValidationResultSummary.md) objects

## Errors
<a name="API_ListSbomValidationResults_Errors"></a>

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ValidationException **
The request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListSbomValidationResults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListSbomValidationResults)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListSbomValidationResults)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListSbomValidationResults)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListSbomValidationResults)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListSbomValidationResults)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListSbomValidationResults)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListSbomValidationResults)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListSbomValidationResults)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListSbomValidationResults)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListSbomValidationResults)
