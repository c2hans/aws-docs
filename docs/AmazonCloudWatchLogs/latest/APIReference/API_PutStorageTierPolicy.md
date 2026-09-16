---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutStorageTierPolicy.html
---

# PutStorageTierPolicy
<a name="API_PutStorageTierPolicy"></a>

Sets the storage tier policy for the account. When you set the storage tier to `INTELLIGENT_TIERING`, the service automatically moves log data to the most cost-effective storage tier based on access frequency.

## Request Syntax
<a name="API_PutStorageTierPolicy_RequestSyntax"></a>

```
{
   "storageTier": "{{string}}"
}
```

## Request Parameters
<a name="API_PutStorageTierPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [storageTier](#API_PutStorageTierPolicy_RequestSyntax) **   <a name="CWL-PutStorageTierPolicy-request-storageTier"></a>
The storage tier to set for the account. Use `INTELLIGENT_TIERING` to automatically optimize storage costs by moving log data to the appropriate tier based on access frequency.
Type: String
Valid Values: `STANDARD | INTELLIGENT_TIERING`
Required: Yes

## Response Syntax
<a name="API_PutStorageTierPolicy_ResponseSyntax"></a>

```
{
   "lastUpdatedTime": number,
   "storageTier": "string"
}
```

## Response Elements
<a name="API_PutStorageTierPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [lastUpdatedTime](#API_PutStorageTierPolicy_ResponseSyntax) **   <a name="CWL-PutStorageTierPolicy-response-lastUpdatedTime"></a>
The time when the storage tier policy was last updated, expressed as the number of milliseconds after `January 1, 1970 00:00:00 UTC`.
Type: Long
Valid Range: Minimum value of 0.

 ** [storageTier](#API_PutStorageTierPolicy_ResponseSyntax) **   <a name="CWL-PutStorageTierPolicy-response-storageTier"></a>
The storage tier for the account.
Type: String
Valid Values: `STANDARD | INTELLIGENT_TIERING`

## Errors
<a name="API_PutStorageTierPolicy_Errors"></a>

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
<a name="API_PutStorageTierPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/PutStorageTierPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/PutStorageTierPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/PutStorageTierPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/PutStorageTierPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/PutStorageTierPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/PutStorageTierPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/PutStorageTierPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/PutStorageTierPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/PutStorageTierPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/PutStorageTierPolicy)
