---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeAccountSettings.html
---

# DescribeAccountSettings
<a name="API_DescribeAccountSettings"></a>

Describes the account-level settings for Amazon Kinesis Data Streams. This operation returns information about the minimum throughput billing commitments and other account-level configurations.

This API has a call limit of 5 transactions per second (TPS) for each AWS account. TPS over 5 will initiate the `LimitExceededException`.

## Response Syntax
<a name="API_DescribeAccountSettings_ResponseSyntax"></a>

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
<a name="API_DescribeAccountSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MinimumThroughputBillingCommitment](#API_DescribeAccountSettings_ResponseSyntax) **   <a name="Streams-DescribeAccountSettings-response-MinimumThroughputBillingCommitment"></a>
The current configuration of the minimum throughput billing commitment for your AWS account.
Type: [MinimumThroughputBillingCommitmentOutput](API_MinimumThroughputBillingCommitmentOutput.md) object

## Errors
<a name="API_DescribeAccountSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LimitExceededException **
The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

## See Also
<a name="API_DescribeAccountSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/DescribeAccountSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/DescribeAccountSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/DescribeAccountSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/DescribeAccountSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/DescribeAccountSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/DescribeAccountSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/DescribeAccountSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/DescribeAccountSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/DescribeAccountSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/DescribeAccountSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
