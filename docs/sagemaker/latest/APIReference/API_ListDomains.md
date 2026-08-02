---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListDomains.html
---

# ListDomains
<a name="API_ListDomains"></a>

Lists the domains.

## Request Syntax
<a name="API_ListDomains_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDomains_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListDomains_RequestSyntax) **   <a name="sagemaker-ListDomains-request-MaxResults"></a>
This parameter defines the maximum number of results that can be return in a single response. The `MaxResults` parameter is an upper bound, not a target. If there are more results available than the value specified, a `NextToken` is provided in the response. The `NextToken` indicates that the user should get the next set of results by providing this token as a part of a subsequent call. The default value for `MaxResults` is 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListDomains_RequestSyntax) **   <a name="sagemaker-ListDomains-request-NextToken"></a>
If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_ListDomains_ResponseSyntax"></a>

```
{
   "Domains": [
      {
         "CreationTime": number,
         "DomainArn": "string",
         "DomainId": "string",
         "DomainName": "string",
         "LastModifiedTime": number,
         "Status": "string",
         "Url": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDomains_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Domains](#API_ListDomains_ResponseSyntax) **   <a name="sagemaker-ListDomains-response-Domains"></a>
The list of domains.
Type: Array of [DomainDetails](API_DomainDetails.md) objects

 ** [NextToken](#API_ListDomains_ResponseSyntax) **   <a name="sagemaker-ListDomains-response-NextToken"></a>
If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListDomains_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListDomains_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListDomains)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListDomains)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListDomains)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListDomains)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListDomains)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListDomains)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListDomains)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListDomains)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListDomains)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListDomains)
