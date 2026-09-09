---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListModelCardVersions.html
---

# ListModelCardVersions
<a name="API_ListModelCardVersions"></a>

List existing versions of an Amazon SageMaker Model Card.

## Request Syntax
<a name="API_ListModelCardVersions_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "ModelCardName": "{{string}}",
   "ModelCardStatus": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListModelCardVersions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListModelCardVersions_RequestSyntax) **   <a name="sagemaker-ListModelCardVersions-request-MaxResults"></a>
The maximum number of model card versions to list.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [ModelCardName](#API_ListModelCardVersions_RequestSyntax) **   <a name="sagemaker-ListModelCardVersions-request-ModelCardName"></a>
List model card versions for the model card with the specified name or Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:model-card/.*)?([a-zA-Z0-9](-*[a-zA-Z0-9]){0,62})`
Required: Yes

 ** [ModelCardStatus](#API_ListModelCardVersions_RequestSyntax) **   <a name="sagemaker-ListModelCardVersions-request-ModelCardStatus"></a>
Only list model card versions with the specified approval status.
Type: String
Valid Values: `Draft | PendingReview | Approved | Archived`
Required: No

 ** [NextToken](#API_ListModelCardVersions_RequestSyntax) **   <a name="sagemaker-ListModelCardVersions-request-NextToken"></a>
If the response to a previous `ListModelCardVersions` request was truncated, the response includes a `NextToken`. To retrieve the next set of model card versions, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListModelCardVersions_RequestSyntax) **   <a name="sagemaker-ListModelCardVersions-request-SortBy"></a>
Sort listed model card versions by version. Sorts by version by default.
Type: String
Valid Values: `Version`
Required: No

 ** [SortOrder](#API_ListModelCardVersions_RequestSyntax) **   <a name="sagemaker-ListModelCardVersions-request-SortOrder"></a>
Sort model card versions by ascending or descending order.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListModelCardVersions_ResponseSyntax"></a>

```
{
   "ModelCardVersionSummaryList": [
      {
         "ModelCardArn": "string",
         "ModelCardName": "string",
         "ModelCardStatus": "string",
         "ModelCardVersion": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListModelCardVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ModelCardVersionSummaryList](#API_ListModelCardVersions_ResponseSyntax) **   <a name="sagemaker-ListModelCardVersions-response-ModelCardVersionSummaryList"></a>
The summaries of the listed versions of the model card.
Type: Array of [ModelCardVersionSummary](API_ModelCardVersionSummary.md) objects

 ** [NextToken](#API_ListModelCardVersions_ResponseSyntax) **   <a name="sagemaker-ListModelCardVersions-response-NextToken"></a>
If the response is truncated, SageMaker returns this token. To retrieve the next set of model card versions, use it in the subsequent request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListModelCardVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_ListModelCardVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListModelCardVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListModelCardVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListModelCardVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListModelCardVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListModelCardVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListModelCardVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListModelCardVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListModelCardVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListModelCardVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListModelCardVersions)
