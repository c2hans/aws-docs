---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListInferenceComponents.html
---

# ListInferenceComponents
<a name="API_ListInferenceComponents"></a>

Lists the inference components in your account and their properties.

## Request Syntax
<a name="API_ListInferenceComponents_RequestSyntax"></a>

```
{
   "EndpointNameEquals": "{{string}}",
   "MaxResults": {{number}},
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "StatusEquals": "{{string}}",
   "VariantNameEquals": "{{string}}"
}
```

## Request Parameters
<a name="API_ListInferenceComponents_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EndpointNameEquals](#API_ListInferenceComponents_RequestSyntax) **   <a name="sagemaker-ListInferenceComponents-request-EndpointNameEquals"></a>
An endpoint name to filter the listed inference components. The response includes only those inference components that are hosted at the specified endpoint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** [MaxResults](#API_ListInferenceComponents_RequestSyntax) **   <a name="sagemaker-ListInferenceComponents-request-MaxResults"></a>
The maximum number of inference components to return in the response. This value defaults to 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListInferenceComponents_RequestSyntax) **   <a name="sagemaker-ListInferenceComponents-request-NameContains"></a>
Filters the results to only those inference components with a name that contains the specified string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** [NextToken](#API_ListInferenceComponents_RequestSyntax) **   <a name="sagemaker-ListInferenceComponents-request-NextToken"></a>
A token that you use to get the next set of results following a truncated response. If the response to the previous request was truncated, that response provides the value for this token.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListInferenceComponents_RequestSyntax) **   <a name="sagemaker-ListInferenceComponents-request-SortBy"></a>
The field by which to sort the inference components in the response. The default is `CreationTime`.
Type: String
Valid Values: `Name | CreationTime | Status`
Required: No

 ** [SortOrder](#API_ListInferenceComponents_RequestSyntax) **   <a name="sagemaker-ListInferenceComponents-request-SortOrder"></a>
The sort order for results. The default is `Descending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [StatusEquals](#API_ListInferenceComponents_RequestSyntax) **   <a name="sagemaker-ListInferenceComponents-request-StatusEquals"></a>
Filters the results to only those inference components with the specified status.
Type: String
Valid Values: `InService | Creating | Updating | Failed | Deleting`
Required: No

 ** [VariantNameEquals](#API_ListInferenceComponents_RequestSyntax) **   <a name="sagemaker-ListInferenceComponents-request-VariantNameEquals"></a>
A production variant name to filter the listed inference components. The response includes only those inference components that are hosted at the specified variant.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

## Response Syntax
<a name="API_ListInferenceComponents_ResponseSyntax"></a>

```
{
   "InferenceComponents": [
      {
         "EndpointArn": "string",
         "EndpointName": "string",
         "InferenceComponentArn": "string",
         "InferenceComponentName": "string",
         "InferenceComponentStatus": "string",
         "VariantName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListInferenceComponents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InferenceComponents](#API_ListInferenceComponents_ResponseSyntax) **   <a name="sagemaker-ListInferenceComponents-response-InferenceComponents"></a>
A list of inference components and their properties that matches any of the filters you specified in the request.
Type: Array of [InferenceComponentSummary](API_InferenceComponentSummary.md) objects

 ** [NextToken](#API_ListInferenceComponents_ResponseSyntax) **   <a name="sagemaker-ListInferenceComponents-response-NextToken"></a>
The token to use in a subsequent request to get the next set of results following a truncated response.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListInferenceComponents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListInferenceComponents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListInferenceComponents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListInferenceComponents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListInferenceComponents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListInferenceComponents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListInferenceComponents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListInferenceComponents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListInferenceComponents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListInferenceComponents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListInferenceComponents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListInferenceComponents)
