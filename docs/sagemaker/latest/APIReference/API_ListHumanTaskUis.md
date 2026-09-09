---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListHumanTaskUis.html
---

# ListHumanTaskUis
<a name="API_ListHumanTaskUis"></a>

Returns information about the human task user interfaces in your account.

## Request Syntax
<a name="API_ListHumanTaskUis_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListHumanTaskUis_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListHumanTaskUis_RequestSyntax) **   <a name="sagemaker-ListHumanTaskUis-request-MaxResults"></a>
The total number of items to return. If the total number of available items is more than the value specified in `MaxResults`, then a `NextToken` will be provided in the output that you can use to resume pagination.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListHumanTaskUis_RequestSyntax) **   <a name="sagemaker-ListHumanTaskUis-request-NextToken"></a>
A token to resume pagination.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortOrder](#API_ListHumanTaskUis_RequestSyntax) **   <a name="sagemaker-ListHumanTaskUis-request-SortOrder"></a>
An optional value that specifies whether you want the results sorted in `Ascending` or `Descending` order.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListHumanTaskUis_ResponseSyntax"></a>

```
{
   "HumanTaskUiSummaries": [
      {
         "HumanTaskUiArn": "string",
         "HumanTaskUiName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListHumanTaskUis_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HumanTaskUiSummaries](#API_ListHumanTaskUis_ResponseSyntax) **   <a name="sagemaker-ListHumanTaskUis-response-HumanTaskUiSummaries"></a>
An array of objects describing the human task user interfaces.
Type: Array of [HumanTaskUiSummary](API_HumanTaskUiSummary.md) objects

 ** [NextToken](#API_ListHumanTaskUis_ResponseSyntax) **   <a name="sagemaker-ListHumanTaskUis-response-NextToken"></a>
A token to resume pagination.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListHumanTaskUis_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListHumanTaskUis_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListHumanTaskUis)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListHumanTaskUis)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListHumanTaskUis)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListHumanTaskUis)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListHumanTaskUis)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListHumanTaskUis)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListHumanTaskUis)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListHumanTaskUis)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListHumanTaskUis)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListHumanTaskUis)
