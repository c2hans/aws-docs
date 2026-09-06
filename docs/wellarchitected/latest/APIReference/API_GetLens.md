---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetLens.html
---

# GetLens
<a name="API_GetLens"></a>

Get an existing lens.

## Request Syntax
<a name="API_GetLens_RequestSyntax"></a>

```
GET /lenses/{{LensAlias}}?LensVersion={{LensVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetLens_RequestParameters"></a>

The request uses the following URI parameters.

 ** [LensAlias](#API_GetLens_RequestSyntax) **   <a name="wellarchitected-GetLens-request-uri-LensAlias"></a>
The alias of the lens.
For AWS official lenses, this is either the lens alias, such as `serverless`, or the lens ARN, such as `arn:aws:wellarchitected:us-east-1::lens/serverless`. Note that some operations (such as ExportLens and CreateLensShare) are not permitted on AWS official lenses.
For custom lenses, this is the lens ARN, such as `arn:aws:wellarchitected:us-west-2:123456789012:lens/0123456789abcdef01234567890abcdef`.
Each lens is identified by its [LensSummary:LensAlias](API_LensSummary.md#wellarchitected-Type-LensSummary-LensAlias).
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [LensVersion](#API_GetLens_RequestSyntax) **   <a name="wellarchitected-GetLens-request-uri-LensVersion"></a>
The lens version to be retrieved.
Length Constraints: Minimum length of 1. Maximum length of 32.

## Request Body
<a name="API_GetLens_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetLens_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Lens": {
      "Description": "string",
      "LensArn": "string",
      "LensVersion": "string",
      "Name": "string",
      "Owner": "string",
      "ShareInvitationId": "string",
      "Tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_GetLens_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Lens](#API_GetLens_ResponseSyntax) **   <a name="wellarchitected-GetLens-response-Lens"></a>
A lens return object.
Type: [Lens](API_Lens.md) object

## Errors
<a name="API_GetLens_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

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
<a name="API_GetLens_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/GetLens)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/GetLens)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/GetLens)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/GetLens)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/GetLens)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/GetLens)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/GetLens)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/GetLens)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/GetLens)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/GetLens)
