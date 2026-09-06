---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListTestGridSessionArtifacts.html
---

# ListTestGridSessionArtifacts
<a name="API_ListTestGridSessionArtifacts"></a>

Retrieves a list of artifacts created during the session.

## Request Syntax
<a name="API_ListTestGridSessionArtifacts_RequestSyntax"></a>

```
{
   "maxResult": {{number}},
   "nextToken": "{{string}}",
   "sessionArn": "{{string}}",
   "type": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTestGridSessionArtifacts_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResult](#API_ListTestGridSessionArtifacts_RequestSyntax) **   <a name="devicefarm-ListTestGridSessionArtifacts-request-maxResult"></a>
The maximum number of results to be returned by a request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListTestGridSessionArtifacts_RequestSyntax) **   <a name="devicefarm-ListTestGridSessionArtifacts-request-nextToken"></a>
Pagination token.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.
Required: No

 ** [sessionArn](#API_ListTestGridSessionArtifacts_RequestSyntax) **   <a name="devicefarm-ListTestGridSessionArtifacts-request-sessionArn"></a>
The ARN of a [TestGridSession](API_TestGridSession.md).
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: Yes

 ** [type](#API_ListTestGridSessionArtifacts_RequestSyntax) **   <a name="devicefarm-ListTestGridSessionArtifacts-request-type"></a>
Limit results to a specified type of artifact.
Type: String
Valid Values: `VIDEO | LOG`
Required: No

## Response Syntax
<a name="API_ListTestGridSessionArtifacts_ResponseSyntax"></a>

```
{
   "artifacts": [
      {
         "filename": "string",
         "type": "string",
         "url": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListTestGridSessionArtifacts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [artifacts](#API_ListTestGridSessionArtifacts_ResponseSyntax) **   <a name="devicefarm-ListTestGridSessionArtifacts-response-artifacts"></a>
A list of test grid session artifacts for a [TestGridSession](API_TestGridSession.md).
Type: Array of [TestGridSessionArtifact](API_TestGridSessionArtifact.md) objects

 ** [nextToken](#API_ListTestGridSessionArtifacts_ResponseSyntax) **   <a name="devicefarm-ListTestGridSessionArtifacts-response-nextToken"></a>
Pagination token.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.

## Errors
<a name="API_ListTestGridSessionArtifacts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ArgumentException **
An invalid argument was specified.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** InternalServiceException **
An internal exception was raised in the service. Contact [aws-devicefarm-support@amazon.com](mailto:aws-devicefarm-support@amazon.com) if you see this error.
HTTP Status Code: 500

 ** NotFoundException **
The specified entity was not found.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListTestGridSessionArtifacts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/ListTestGridSessionArtifacts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/ListTestGridSessionArtifacts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/ListTestGridSessionArtifacts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/ListTestGridSessionArtifacts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/ListTestGridSessionArtifacts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/ListTestGridSessionArtifacts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/ListTestGridSessionArtifacts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/ListTestGridSessionArtifacts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/ListTestGridSessionArtifacts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/ListTestGridSessionArtifacts)
