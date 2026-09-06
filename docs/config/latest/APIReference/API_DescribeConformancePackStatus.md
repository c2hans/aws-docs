---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConformancePackStatus.html
---

# DescribeConformancePackStatus
<a name="API_DescribeConformancePackStatus"></a>

Provides one or more conformance packs deployment status.

**Note**
If there are no conformance packs then you will see an empty result.

## Request Syntax
<a name="API_DescribeConformancePackStatus_RequestSyntax"></a>

```
{
   "ConformancePackNames": [ "{{string}}" ],
   "Limit": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeConformancePackStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConformancePackNames](#API_DescribeConformancePackStatus_RequestSyntax) **   <a name="config-DescribeConformancePackStatus-request-ConformancePackNames"></a>
Comma-separated list of conformance pack names.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z][-a-zA-Z0-9]*`
Required: No

 ** [Limit](#API_DescribeConformancePackStatus_RequestSyntax) **   <a name="config-DescribeConformancePackStatus-request-Limit"></a>
The maximum number of conformance packs status returned on each page.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 20.
Required: No

 ** [NextToken](#API_DescribeConformancePackStatus_RequestSyntax) **   <a name="config-DescribeConformancePackStatus-request-NextToken"></a>
The `nextToken` string returned in a previous request that you use to request the next page of results in a paginated response.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeConformancePackStatus_ResponseSyntax"></a>

```
{
   "ConformancePackStatusDetails": [
      {
         "ConformancePackArn": "string",
         "ConformancePackId": "string",
         "ConformancePackName": "string",
         "ConformancePackState": "string",
         "ConformancePackStatusReason": "string",
         "LastUpdateCompletedTime": number,
         "LastUpdateRequestedTime": number,
         "StackArn": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeConformancePackStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConformancePackStatusDetails](#API_DescribeConformancePackStatus_ResponseSyntax) **   <a name="config-DescribeConformancePackStatus-response-ConformancePackStatusDetails"></a>
A list of `ConformancePackStatusDetail` objects.
Type: Array of [ConformancePackStatusDetail](API_ConformancePackStatusDetail.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.

 ** [NextToken](#API_DescribeConformancePackStatus_ResponseSyntax) **   <a name="config-DescribeConformancePackStatus-response-NextToken"></a>
The `nextToken` string returned in a previous request that you use to request the next page of results in a paginated response.
Type: String

## Errors
<a name="API_DescribeConformancePackStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidLimitException **
The specified limit is outside the allowable range.
HTTP Status Code: 400

 ** InvalidNextTokenException **
The specified next token is not valid. Specify the `nextToken` string that was returned in the previous response to get the next page of results.
HTTP Status Code: 400

 ** InvalidParameterValueException **
One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.
HTTP Status Code: 400

## See Also
<a name="API_DescribeConformancePackStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/DescribeConformancePackStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/DescribeConformancePackStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/DescribeConformancePackStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/DescribeConformancePackStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/DescribeConformancePackStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/DescribeConformancePackStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/DescribeConformancePackStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/DescribeConformancePackStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/DescribeConformancePackStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/DescribeConformancePackStatus)
