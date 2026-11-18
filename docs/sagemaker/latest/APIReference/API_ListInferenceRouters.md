---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListInferenceRouters.html
---

# ListInferenceRouters
<a name="API_ListInferenceRouters"></a>

Lists the inference routers in your account in the current AWS Region. A router that you just created might not appear in the list right away.

## Request Syntax
<a name="API_ListInferenceRouters_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListInferenceRouters_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListInferenceRouters_RequestSyntax) **   <a name="sagemaker-ListInferenceRouters-request-MaxResults"></a>
The maximum number of inference routers to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListInferenceRouters_RequestSyntax) **   <a name="sagemaker-ListInferenceRouters-request-NextToken"></a>
If the previous response was truncated, you receive this token. To get the next set of inference routers, use it in your next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_ListInferenceRouters_ResponseSyntax"></a>

```
{
   "InferenceRouters": [
      {
         "CreationTime": number,
         "InferenceRouterArn": "string",
         "InferenceRouterName": "string",
         "LastModifiedTime": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListInferenceRouters_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InferenceRouters](#API_ListInferenceRouters_ResponseSyntax) **   <a name="sagemaker-ListInferenceRouters-response-InferenceRouters"></a>
A list of summaries of the inference routers.
Type: Array of [InferenceRouterSummary](API_InferenceRouterSummary.md) objects

 ** [NextToken](#API_ListInferenceRouters_ResponseSyntax) **   <a name="sagemaker-ListInferenceRouters-response-NextToken"></a>
If the response is truncated, SageMaker AI returns this token. To get the next set of inference routers, use it in your next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListInferenceRouters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListInferenceRouters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListInferenceRouters)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListInferenceRouters)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListInferenceRouters)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListInferenceRouters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListInferenceRouters)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListInferenceRouters)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListInferenceRouters)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListInferenceRouters)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListInferenceRouters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListInferenceRouters)
