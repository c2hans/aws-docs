---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_UpdateAnalyzer.html
---

# UpdateAnalyzer
<a name="API_UpdateAnalyzer"></a>

Modifies the configuration of an existing analyzer.

**Note**
This action is not supported for external access analyzers.

## Request Syntax
<a name="API_UpdateAnalyzer_RequestSyntax"></a>

```
PUT /analyzer/{{analyzerName}} HTTP/1.1
Content-type: application/json

{
   "configuration": { ... }
}
```

## URI Request Parameters
<a name="API_UpdateAnalyzer_RequestParameters"></a>

The request uses the following URI parameters.

 ** [analyzerName](#API_UpdateAnalyzer_RequestSyntax) **   <a name="accessanalyzer-UpdateAnalyzer-request-uri-analyzerName"></a>
The name of the analyzer to modify.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z][A-Za-z0-9_.-]*`
Required: Yes

## Request Body
<a name="API_UpdateAnalyzer_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [configuration](#API_UpdateAnalyzer_RequestSyntax) **   <a name="accessanalyzer-UpdateAnalyzer-request-configuration"></a>
Contains information about the configuration of an analyzer for an AWS organization or account.
Type: [AnalyzerConfiguration](API_AnalyzerConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## Response Syntax
<a name="API_UpdateAnalyzer_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configuration": { ... }
}
```

## Response Elements
<a name="API_UpdateAnalyzer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configuration](#API_UpdateAnalyzer_ResponseSyntax) **   <a name="accessanalyzer-UpdateAnalyzer-response-configuration"></a>
Contains information about the configuration of an analyzer for an AWS organization or account.
Type: [AnalyzerConfiguration](API_AnalyzerConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

## Errors
<a name="API_UpdateAnalyzer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
A conflict exception error.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The resource type.
HTTP Status Code: 409

 ** InternalServerException **
Internal server error.
 ** retryAfterSeconds **
The seconds to wait to retry.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource could not be found.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 404

 ** ThrottlingException **
Throttling limit exceeded error.
 ** retryAfterSeconds **
The seconds to wait to retry.
HTTP Status Code: 429

 ** ValidationException **
Validation exception error.
 ** fieldList **
A list of fields that didn't validate.
 ** reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_UpdateAnalyzer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/UpdateAnalyzer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/UpdateAnalyzer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/UpdateAnalyzer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/UpdateAnalyzer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/UpdateAnalyzer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/UpdateAnalyzer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/UpdateAnalyzer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/UpdateAnalyzer)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/UpdateAnalyzer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/UpdateAnalyzer)
