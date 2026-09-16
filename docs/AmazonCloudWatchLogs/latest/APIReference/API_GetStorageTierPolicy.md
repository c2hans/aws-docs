---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetStorageTierPolicy.html
---

# GetStorageTierPolicy
<a name="API_GetStorageTierPolicy"></a>

Returns the storage tier policy for the account.

## Response Syntax
<a name="API_GetStorageTierPolicy_ResponseSyntax"></a>

```
{
   "lastUpdatedTime": number,
   "storageTier": "string"
}
```

## Response Elements
<a name="API_GetStorageTierPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [lastUpdatedTime](#API_GetStorageTierPolicy_ResponseSyntax) **   <a name="CWL-GetStorageTierPolicy-response-lastUpdatedTime"></a>
The time when the storage tier policy was last updated, expressed as the number of milliseconds after `January 1, 1970 00:00:00 UTC`.
Type: Long
Valid Range: Minimum value of 0.

 ** [storageTier](#API_GetStorageTierPolicy_ResponseSyntax) **   <a name="CWL-GetStorageTierPolicy-response-storageTier"></a>
The current storage tier for the account.
Type: String
Valid Values: `STANDARD | INTELLIGENT_TIERING`

## Errors
<a name="API_GetStorageTierPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 400

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** OperationAbortedException **
Multiple concurrent requests to update the same resource were in conflict.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

## See Also
<a name="API_GetStorageTierPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/GetStorageTierPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/GetStorageTierPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/GetStorageTierPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/GetStorageTierPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/GetStorageTierPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/GetStorageTierPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/GetStorageTierPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/GetStorageTierPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/GetStorageTierPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/GetStorageTierPolicy)
