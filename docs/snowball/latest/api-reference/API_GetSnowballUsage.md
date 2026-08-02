---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_GetSnowballUsage.html
---

# GetSnowballUsage
<a name="API_GetSnowballUsage"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Returns information about the Snowball Edge service limit for your account, and also the number of Snow devices your account has in use.

The default service limit for the number of Snow devices that you can have at one time is 1. If you want to increase your service limit, contact AWS Support.

## Response Syntax
<a name="API_GetSnowballUsage_ResponseSyntax"></a>

```
{
   "SnowballLimit": number,
   "SnowballsInUse": number
}
```

## Response Elements
<a name="API_GetSnowballUsage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SnowballLimit](#API_GetSnowballUsage_ResponseSyntax) **   <a name="Snowball-GetSnowballUsage-response-SnowballLimit"></a>
The service limit for number of Snow devices this account can have at once. The default service limit is 1 (one).
Type: Integer

 ** [SnowballsInUse](#API_GetSnowballUsage_ResponseSyntax) **   <a name="Snowball-GetSnowballUsage-response-SnowballsInUse"></a>
The number of Snow devices that this account is currently using.
Type: Integer

## Errors
<a name="API_GetSnowballUsage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetSnowballUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snowball-2016-06-30/GetSnowballUsage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snowball-2016-06-30/GetSnowballUsage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/GetSnowballUsage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snowball-2016-06-30/GetSnowballUsage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/GetSnowballUsage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snowball-2016-06-30/GetSnowballUsage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snowball-2016-06-30/GetSnowballUsage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snowball-2016-06-30/GetSnowballUsage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/snowball-2016-06-30/GetSnowballUsage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/GetSnowballUsage)
