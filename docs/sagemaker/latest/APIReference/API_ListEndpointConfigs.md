---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListEndpointConfigs.html
---

# ListEndpointConfigs
<a name="API_ListEndpointConfigs"></a>

Lists endpoint configurations.

## Request Syntax
<a name="API_ListEndpointConfigs_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListEndpointConfigs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListEndpointConfigs_RequestSyntax) **   <a name="sagemaker-ListEndpointConfigs-request-MaxResults"></a>
The maximum number of training jobs to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListEndpointConfigs_RequestSyntax) **   <a name="sagemaker-ListEndpointConfigs-request-NameContains"></a>
A string in the endpoint configuration name. This filter returns only endpoint configurations whose name contains the specified string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** [NextToken](#API_ListEndpointConfigs_RequestSyntax) **   <a name="sagemaker-ListEndpointConfigs-request-NextToken"></a>
If the result of the previous `ListEndpointConfig` request was truncated, the response includes a `NextToken`. To retrieve the next set of endpoint configurations, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListEndpointConfigs_RequestSyntax) **   <a name="sagemaker-ListEndpointConfigs-request-SortBy"></a>
The field to sort results by. The default is `CreationTime`.
Type: String
Valid Values: `Name | CreationTime`
Required: No

 ** [SortOrder](#API_ListEndpointConfigs_RequestSyntax) **   <a name="sagemaker-ListEndpointConfigs-request-SortOrder"></a>
The sort order for results. The default is `Descending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListEndpointConfigs_ResponseSyntax"></a>

```
{
   "EndpointConfigs": [
      {
         "EndpointConfigArn": "string",
         "EndpointConfigName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListEndpointConfigs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EndpointConfigs](#API_ListEndpointConfigs_ResponseSyntax) **   <a name="sagemaker-ListEndpointConfigs-response-EndpointConfigs"></a>
An array of endpoint configurations.
Type: Array of [EndpointConfigSummary](API_EndpointConfigSummary.md) objects

 ** [NextToken](#API_ListEndpointConfigs_ResponseSyntax) **   <a name="sagemaker-ListEndpointConfigs-response-NextToken"></a>
 If the response is truncated, SageMaker returns this token. To retrieve the next set of endpoint configurations, use it in the subsequent request
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListEndpointConfigs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListEndpointConfigs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListEndpointConfigs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListEndpointConfigs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListEndpointConfigs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListEndpointConfigs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListEndpointConfigs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListEndpointConfigs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListEndpointConfigs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListEndpointConfigs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListEndpointConfigs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListEndpointConfigs)
