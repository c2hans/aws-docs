---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteLens.html
---

# DeleteLens
<a name="API_DeleteLens"></a>

Delete an existing lens.

Only the owner of a lens can delete it. After the lens is deleted, AWS accounts and users that you shared the lens with can continue to use it, but they will no longer be able to apply it to new workloads.

**Note**
 **Disclaimer**
By sharing your custom lenses with other AWS accounts, you acknowledge that AWS will make your custom lenses available to those other accounts. Those other accounts may continue to access and use your shared custom lenses even if you delete the custom lenses from your own AWS account or terminate your AWS account.

## Request Syntax
<a name="API_DeleteLens_RequestSyntax"></a>

```
DELETE /lenses/{{LensAlias}}?ClientRequestToken={{ClientRequestToken}}&LensStatus={{LensStatus}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteLens_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ClientRequestToken](#API_DeleteLens_RequestSyntax) **   <a name="wellarchitected-DeleteLens-request-uri-ClientRequestToken"></a>
A unique case-sensitive string used to ensure that this request is idempotent (executes only once).
You should not reuse the same token for other requests. If you retry a request with the same client request token and the same parameters after the original request has completed successfully, the result of the original request is returned.
This token is listed as required, however, if you do not specify it, the AWS SDKs automatically generate one for you. If you are not using the AWS SDK or the AWS CLI, you must provide this token or the request will fail.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[\x00-\x7F]*$`
Required: Yes

 ** [LensAlias](#API_DeleteLens_RequestSyntax) **   <a name="wellarchitected-DeleteLens-request-uri-LensAlias"></a>
The alias of the lens.
For AWS official lenses, this is either the lens alias, such as `serverless`, or the lens ARN, such as `arn:aws:wellarchitected:us-east-1::lens/serverless`. Note that some operations (such as ExportLens and CreateLensShare) are not permitted on AWS official lenses.
For custom lenses, this is the lens ARN, such as `arn:aws:wellarchitected:us-west-2:123456789012:lens/0123456789abcdef01234567890abcdef`.
Each lens is identified by its [LensSummary:LensAlias](API_LensSummary.md#wellarchitected-Type-LensSummary-LensAlias).
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [LensStatus](#API_DeleteLens_RequestSyntax) **   <a name="wellarchitected-DeleteLens-request-uri-LensStatus"></a>
The status of the lens to be deleted.
Valid Values: `ALL | DRAFT | PUBLISHED`
Required: Yes

## Request Body
<a name="API_DeleteLens_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteLens_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteLens_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteLens_Errors"></a>

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
<a name="API_DeleteLens_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/DeleteLens)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/DeleteLens)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/DeleteLens)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/DeleteLens)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/DeleteLens)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/DeleteLens)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/DeleteLens)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/DeleteLens)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/DeleteLens)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/DeleteLens)
