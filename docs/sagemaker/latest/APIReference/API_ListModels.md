---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListModels.html
---

# ListModels
<a name="API_ListModels"></a>

Lists models created with the `CreateModel` API.

## Request Syntax
<a name="API_ListModels_RequestSyntax"></a>

```
{
   "CreationTimeAfter": {{number}},
   "CreationTimeBefore": {{number}},
   "MaxResults": {{number}},
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListModels_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreationTimeAfter](#API_ListModels_RequestSyntax) **   <a name="sagemaker-ListModels-request-CreationTimeAfter"></a>
A filter that returns only models with a creation time greater than or equal to the specified time (timestamp).
Type: Timestamp
Required: No

 ** [CreationTimeBefore](#API_ListModels_RequestSyntax) **   <a name="sagemaker-ListModels-request-CreationTimeBefore"></a>
A filter that returns only models created before the specified time (timestamp).
Type: Timestamp
Required: No

 ** [MaxResults](#API_ListModels_RequestSyntax) **   <a name="sagemaker-ListModels-request-MaxResults"></a>
The maximum number of models to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListModels_RequestSyntax) **   <a name="sagemaker-ListModels-request-NameContains"></a>
A string in the model name. This filter returns only models whose name contains the specified string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** [NextToken](#API_ListModels_RequestSyntax) **   <a name="sagemaker-ListModels-request-NextToken"></a>
If the response to a previous `ListModels` request was truncated, the response includes a `NextToken`. To retrieve the next set of models, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListModels_RequestSyntax) **   <a name="sagemaker-ListModels-request-SortBy"></a>
Sorts the list of results. The default is `CreationTime`.
Type: String
Valid Values: `Name | CreationTime`
Required: No

 ** [SortOrder](#API_ListModels_RequestSyntax) **   <a name="sagemaker-ListModels-request-SortOrder"></a>
The sort order for results. The default is `Descending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListModels_ResponseSyntax"></a>

```
{
   "Models": [
      {
         "CreationTime": number,
         "ModelArn": "string",
         "ModelName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListModels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Models](#API_ListModels_ResponseSyntax) **   <a name="sagemaker-ListModels-response-Models"></a>
An array of `ModelSummary` objects, each of which lists a model.
Type: Array of [ModelSummary](API_ModelSummary.md) objects

 ** [NextToken](#API_ListModels_ResponseSyntax) **   <a name="sagemaker-ListModels-response-NextToken"></a>
 If the response is truncated, SageMaker returns this token. To retrieve the next set of models, use it in the subsequent request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListModels_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListModels_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListModels)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListModels)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListModels)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListModels)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListModels)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListModels)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListModels)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListModels)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListModels)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListModels)
