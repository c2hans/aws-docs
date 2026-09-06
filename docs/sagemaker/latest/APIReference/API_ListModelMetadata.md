---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListModelMetadata.html
---

# ListModelMetadata
<a name="API_ListModelMetadata"></a>

Lists the domain, framework, task, and model name of standard machine learning models found in common model zoos.

## Request Syntax
<a name="API_ListModelMetadata_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SearchExpression": {
      "Filters": [
         {
            "Name": "{{string}}",
            "Value": "{{string}}"
         }
      ]
   }
}
```

## Request Parameters
<a name="API_ListModelMetadata_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListModelMetadata_RequestSyntax) **   <a name="sagemaker-ListModelMetadata-request-MaxResults"></a>
The maximum number of models to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListModelMetadata_RequestSyntax) **   <a name="sagemaker-ListModelMetadata-request-NextToken"></a>
If the response to a previous `ListModelMetadataResponse` request was truncated, the response includes a NextToken. To retrieve the next set of model metadata, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SearchExpression](#API_ListModelMetadata_RequestSyntax) **   <a name="sagemaker-ListModelMetadata-request-SearchExpression"></a>
One or more filters that searches for the specified resource or resources in a search. All resource objects that satisfy the expression's condition are included in the search results. Specify the Framework, FrameworkVersion, Domain or Task to filter supported. Filter names and values are case-sensitive.
Type: [ModelMetadataSearchExpression](API_ModelMetadataSearchExpression.md) object
Required: No

## Response Syntax
<a name="API_ListModelMetadata_ResponseSyntax"></a>

```
{
   "ModelMetadataSummaries": [
      {
         "Domain": "string",
         "Framework": "string",
         "FrameworkVersion": "string",
         "Model": "string",
         "Task": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListModelMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ModelMetadataSummaries](#API_ListModelMetadata_ResponseSyntax) **   <a name="sagemaker-ListModelMetadata-response-ModelMetadataSummaries"></a>
A structure that holds model metadata.
Type: Array of [ModelMetadataSummary](API_ModelMetadataSummary.md) objects

 ** [NextToken](#API_ListModelMetadata_ResponseSyntax) **   <a name="sagemaker-ListModelMetadata-response-NextToken"></a>
A token for getting the next set of recommendations, if there are any.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListModelMetadata_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListModelMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListModelMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListModelMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListModelMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListModelMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListModelMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListModelMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListModelMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListModelMetadata)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListModelMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListModelMetadata)
