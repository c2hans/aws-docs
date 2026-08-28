---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeDeliveryChannelStatus.html
---

# DescribeDeliveryChannelStatus
<a name="API_DescribeDeliveryChannelStatus"></a>

Returns the current status of the specified delivery channel. If a delivery channel is not specified, this operation returns the current status of all delivery channels associated with the account.

**Note**
Currently, you can specify only one delivery channel per region in your account.

## Request Syntax
<a name="API_DescribeDeliveryChannelStatus_RequestSyntax"></a>

```
{
   "DeliveryChannelNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeDeliveryChannelStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DeliveryChannelNames](#API_DescribeDeliveryChannelStatus_RequestSyntax) **   <a name="config-DescribeDeliveryChannelStatus-request-DeliveryChannelNames"></a>
A list of delivery channel names.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_DescribeDeliveryChannelStatus_ResponseSyntax"></a>

```
{
   "DeliveryChannelsStatus": [
      {
         "configHistoryDeliveryInfo": {
            "lastAttemptTime": number,
            "lastErrorCode": "string",
            "lastErrorMessage": "string",
            "lastStatus": "string",
            "lastSuccessfulTime": number,
            "nextDeliveryTime": number
         },
         "configSnapshotDeliveryInfo": {
            "lastAttemptTime": number,
            "lastErrorCode": "string",
            "lastErrorMessage": "string",
            "lastStatus": "string",
            "lastSuccessfulTime": number,
            "nextDeliveryTime": number
         },
         "configStreamDeliveryInfo": {
            "lastErrorCode": "string",
            "lastErrorMessage": "string",
            "lastStatus": "string",
            "lastStatusChangeTime": number
         },
         "name": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeDeliveryChannelStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DeliveryChannelsStatus](#API_DescribeDeliveryChannelStatus_ResponseSyntax) **   <a name="config-DescribeDeliveryChannelStatus-response-DeliveryChannelsStatus"></a>
A list that contains the status of a specified delivery channel.
Type: Array of [DeliveryChannelStatus](API_DeliveryChannelStatus.md) objects

## Errors
<a name="API_DescribeDeliveryChannelStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** NoSuchDeliveryChannelException **
You have specified a delivery channel that does not exist.
HTTP Status Code: 400

## See Also
<a name="API_DescribeDeliveryChannelStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/DescribeDeliveryChannelStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/DescribeDeliveryChannelStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/DescribeDeliveryChannelStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/DescribeDeliveryChannelStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/DescribeDeliveryChannelStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/DescribeDeliveryChannelStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/DescribeDeliveryChannelStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/DescribeDeliveryChannelStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/DescribeDeliveryChannelStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/DescribeDeliveryChannelStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
