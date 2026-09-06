---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_UpdateAccountSettings.html
---

# UpdateAccountSettings
<a name="API_UpdateAccountSettings"></a>

Updates the account-level settings for Amazon Kinesis Data Streams.

Updating account settings is a synchronous operation. Upon receiving the request, Kinesis Data Streams will return immediately with your account’s updated settings.

 **API limits**
+ Certain account configurations have minimum commitment windows. Attempting to update your settings prior to the end of the minimum commitment window might have certain restrictions.
+ This API has a call limit of 5 transactions per second (TPS) for each AWS account. TPS over 5 will initiate the `LimitExceededException`.

## Request Syntax
<a name="API_UpdateAccountSettings_RequestSyntax"></a>

```
{
   "MinimumThroughputBillingCommitment": {
      "Status": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_UpdateAccountSettings_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [MinimumThroughputBillingCommitment](#API_UpdateAccountSettings_RequestSyntax) **   <a name="Streams-UpdateAccountSettings-request-MinimumThroughputBillingCommitment"></a>
Specifies the minimum throughput billing commitment configuration for your account.
Type: [MinimumThroughputBillingCommitmentInput](API_MinimumThroughputBillingCommitmentInput.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateAccountSettings_ResponseSyntax"></a>

```
{
   "MinimumThroughputBillingCommitment": {
      "EarliestAllowedEndAt": number,
      "EndedAt": number,
      "StartedAt": number,
      "Status": "string"
   }
}
```

## Response Elements
<a name="API_UpdateAccountSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MinimumThroughputBillingCommitment](#API_UpdateAccountSettings_ResponseSyntax) **   <a name="Streams-UpdateAccountSettings-response-MinimumThroughputBillingCommitment"></a>
The updated configuration of the minimum throughput billing commitment for your account.
Type: [MinimumThroughputBillingCommitmentOutput](API_MinimumThroughputBillingCommitmentOutput.md) object

## Errors
<a name="API_UpdateAccountSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArgumentException **
A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** LimitExceededException **
The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ValidationException **
Specifies that you tried to invoke this API for a data stream with the on-demand capacity mode. This API is only supported for data streams with the provisioned capacity mode.
HTTP Status Code: 400

## See Also
<a name="API_UpdateAccountSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/UpdateAccountSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/UpdateAccountSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/UpdateAccountSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/UpdateAccountSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/UpdateAccountSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/UpdateAccountSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/UpdateAccountSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/UpdateAccountSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/UpdateAccountSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/UpdateAccountSettings)
