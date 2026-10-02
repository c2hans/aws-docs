---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ImportLens.html
---

# ImportLens
<a name="API_ImportLens"></a>

Import a new custom lens or update an existing custom lens.

To update an existing custom lens, specify its ARN as the `LensAlias`. If no ARN is specified, a new custom lens is created.

The new or updated lens will have a status of `DRAFT`. The lens cannot be applied to workloads or shared with other AWS accounts until it's published with [CreateLensVersion](API_CreateLensVersion.md).

Lenses are defined in JSON. For more information, see [JSON format specification](https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-format-specification.html) in the * AWS Well-Architected Tool User Guide*.

A custom lens cannot exceed 500 KB in size.

**Note**
 **Disclaimer**
Do not include or gather personal identifiable information (PII) of end users or other identifiable individuals in or via your custom lenses. If your custom lens or those shared with you and used in your account do include or collect PII you are responsible for: ensuring that the included PII is processed in accordance with applicable law, providing adequate privacy notices, and obtaining necessary consents for processing such data.

## Request Syntax
<a name="API_ImportLens_RequestSyntax"></a>

```
PUT /importLens HTTP/1.1
Content-type: application/json

{
   "ClientRequestToken": "{{string}}",
   "JSONString": "{{string}}",
   "LensAlias": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_ImportLens_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ImportLens_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_ImportLens_RequestSyntax) **   <a name="wellarchitected-ImportLens-request-ClientRequestToken"></a>
A unique case-sensitive string used to ensure that this request is idempotent (executes only once).
You should not reuse the same token for other requests. If you retry a request with the same client request token and the same parameters after the original request has completed successfully, the result of the original request is returned.
This token is listed as required, however, if you do not specify it, the AWS SDKs automatically generate one for you. If you are not using the AWS SDK or the AWS CLI, you must provide this token or the request will fail.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\x00-\x7F]*`
Required: Yes

 ** [JSONString](#API_ImportLens_RequestSyntax) **   <a name="wellarchitected-ImportLens-request-JSONString"></a>
The JSON representation of a lens.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 500000.
Required: Yes

 ** [LensAlias](#API_ImportLens_RequestSyntax) **   <a name="wellarchitected-ImportLens-request-LensAlias"></a>
The alias of the lens.
For AWS official lenses, this is either the lens alias, such as `serverless`, or the lens ARN, such as `arn:aws:wellarchitected:us-east-1::lens/serverless`. Note that some operations (such as ExportLens and CreateLensShare) are not permitted on AWS official lenses.
For custom lenses, this is the lens ARN, such as `arn:aws:wellarchitected:us-west-2:123456789012:lens/0123456789abcdef01234567890abcdef`.
Each lens is identified by its [LensSummary:LensAlias](API_LensSummary.md#wellarchitected-Type-LensSummary-LensAlias).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [Tags](#API_ImportLens_RequestSyntax) **   <a name="wellarchitected-ImportLens-request-Tags"></a>
Tags to associate to a lens.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\p{L}\p{N}\p{Z}_.:/=+@-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_ImportLens_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "LensArn": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_ImportLens_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LensArn](#API_ImportLens_ResponseSyntax) **   <a name="wellarchitected-ImportLens-response-LensArn"></a>
The ARN for the lens that was created or updated.
Type: String

 ** [Status](#API_ImportLens_ResponseSyntax) **   <a name="wellarchitected-ImportLens-response-Status"></a>
The status of the imported lens.
Type: String
Valid Values: `IN_PROGRESS | COMPLETE | ERROR`

## Errors
<a name="API_ImportLens_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

 ** ConflictException **
The resource has already been processed, was deleted, or is too large.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 409

 ** InternalServerException **
There is a problem with the AWS Well-Architected Tool API service.
 ** Message **
Description of the error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource was not found.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The user has reached their resource quota.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 402

 ** ThrottlingException **
Request was denied due to request throttling.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 429

 ** ValidationException **
The user input is not valid.
 ** Fields **
The fields that caused the error, if applicable.
 ** Message **
Description of the error.
 ** Reason **
The reason why the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_ImportLens_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/ImportLens)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/ImportLens)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ImportLens)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/ImportLens)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ImportLens)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/ImportLens)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/ImportLens)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/ImportLens)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/ImportLens)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ImportLens)
