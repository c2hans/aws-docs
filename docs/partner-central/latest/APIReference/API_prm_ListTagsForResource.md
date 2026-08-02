---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_ListTagsForResource.html
---

# ListTagsForResource
<a name="API_prm_ListTagsForResource"></a>

Returns the tags associated with the specified resource.

## Request Parameters
<a name="API_prm_ListTagsForResource_RequestParameters"></a>

 ** resourceArn **
The Amazon Resource Name (ARN) of the resource to list tags for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[a-zA-Z]+/(revenue-attribution/[a-zA-Z0-9-]+|marketplace-revenue-share/prod-[a-z0-9]{13})`
Required: Yes

## Response Elements
<a name="API_prm_ListTagsForResource_ResponseElements"></a>

The following element is returned by the service.

 ** tags **
The tags associated with the resource.
Type: Array of [Tag](API_prm_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.

## Errors
<a name="API_prm_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied due to insufficient permissions.
 ** Reason **
The reason for the access denial.
HTTP Status Code: 403

 ** InternalServerException **
An internal server error occurred. Retry your request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Reason **
The reason the resource was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled due to too many requests. Retry your request.
 ** QuotaCode **
The quota code associated with the throttling error.
 ** ServiceCode **
The service code associated with the throttling error.
HTTP Status Code: 429

 ** ValidationException **
The request failed validation due to invalid input parameters.
 ** FieldList **
A list of fields that failed validation.
 ** Reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_prm_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-revenue-measurement-2022-07-26/ListTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-revenue-measurement-2022-07-26/ListTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/ListTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-revenue-measurement-2022-07-26/ListTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/ListTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-revenue-measurement-2022-07-26/ListTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-revenue-measurement-2022-07-26/ListTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-revenue-measurement-2022-07-26/ListTagsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-revenue-measurement-2022-07-26/ListTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/ListTagsForResource)
