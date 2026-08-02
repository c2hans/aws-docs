---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetAnalyzedResource.html
---

# GetAnalyzedResource
<a name="API_GetAnalyzedResource"></a>

Retrieves information about a resource that was analyzed.

**Note**
This action is supported only for external access analyzers.

## Request Syntax
<a name="API_GetAnalyzedResource_RequestSyntax"></a>

```
GET /analyzed-resource?analyzerArn={{analyzerArn}}&resourceArn={{resourceArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAnalyzedResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [analyzerArn](#API_GetAnalyzedResource_RequestSyntax) **   <a name="accessanalyzer-GetAnalyzedResource-request-uri-analyzerArn"></a>
The [ARN of the analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources) to retrieve information from.
Pattern: `[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:analyzer/.{1,255}`
Required: Yes

 ** [resourceArn](#API_GetAnalyzedResource_RequestSyntax) **   <a name="accessanalyzer-GetAnalyzedResource-request-uri-resourceArn"></a>
The ARN of the resource to retrieve information about.
Pattern: `arn:[^:]*:[^:]*:[^:]*:[^:]*:.*`
Required: Yes

## Request Body
<a name="API_GetAnalyzedResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAnalyzedResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "resource": {
      "actions": [ "string" ],
      "analyzedAt": "string",
      "createdAt": "string",
      "error": "string",
      "isPublic": boolean,
      "resourceArn": "string",
      "resourceOwnerAccount": "string",
      "resourceType": "string",
      "sharedVia": [ "string" ],
      "status": "string",
      "updatedAt": "string"
   }
}
```

## Response Elements
<a name="API_GetAnalyzedResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [resource](#API_GetAnalyzedResource_ResponseSyntax) **   <a name="accessanalyzer-GetAnalyzedResource-response-resource"></a>
An `AnalyzedResource` object that contains information that IAM Access Analyzer found when it analyzed the resource.
Type: [AnalyzedResource](API_AnalyzedResource.md) object

## Errors
<a name="API_GetAnalyzedResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_GetAnalyzedResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/GetAnalyzedResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/GetAnalyzedResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/GetAnalyzedResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/GetAnalyzedResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/GetAnalyzedResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/GetAnalyzedResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/GetAnalyzedResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/GetAnalyzedResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/GetAnalyzedResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/GetAnalyzedResource)
