---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateBrandPublishedVersion.html
---

# UpdateBrandPublishedVersion
<a name="API_UpdateBrandPublishedVersion"></a>

Updates the published version of a brand.

## Request Syntax
<a name="API_UpdateBrandPublishedVersion_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/brands/{{BrandId}}/publishedversion HTTP/1.1
Content-type: application/json

{
   "VersionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateBrandPublishedVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateBrandPublishedVersion_RequestSyntax) **   <a name="QS-UpdateBrandPublishedVersion-request-uri-AwsAccountId"></a>
The ID of the AWS account that owns the brand.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [BrandId](#API_UpdateBrandPublishedVersion_RequestSyntax) **   <a name="QS-UpdateBrandPublishedVersion-request-uri-BrandId"></a>
The ID of the Quick brand.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

## Request Body
<a name="API_UpdateBrandPublishedVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [VersionId](#API_UpdateBrandPublishedVersion_RequestSyntax) **   <a name="QS-UpdateBrandPublishedVersion-request-VersionId"></a>
The ID of the published version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

## Response Syntax
<a name="API_UpdateBrandPublishedVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "RequestId": "string",
   "VersionId": "string"
}
```

## Response Elements
<a name="API_UpdateBrandPublishedVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RequestId](#API_UpdateBrandPublishedVersion_ResponseSyntax) **   <a name="QS-UpdateBrandPublishedVersion-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

 ** [VersionId](#API_UpdateBrandPublishedVersion_ResponseSyntax) **   <a name="QS-UpdateBrandPublishedVersion-response-VersionId"></a>
The ID of the published version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`

## Errors
<a name="API_UpdateBrandPublishedVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalServerException **
An internal service exception.
HTTP Status Code: 500

 ** InvalidRequestException **
You don't have this feature activated for your account. To fix this issue, contact AWS support.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_UpdateBrandPublishedVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateBrandPublishedVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateBrandPublishedVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateBrandPublishedVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateBrandPublishedVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateBrandPublishedVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateBrandPublishedVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateBrandPublishedVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateBrandPublishedVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateBrandPublishedVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateBrandPublishedVersion)
