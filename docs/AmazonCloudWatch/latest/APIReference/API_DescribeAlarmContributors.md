---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarmContributors.html
---

# DescribeAlarmContributors
<a name="API_DescribeAlarmContributors"></a>

Returns the information of the current alarm contributors that are in `ALARM` state. This operation returns details about the individual time series that contribute to the alarm's state.

## Request Parameters
<a name="API_DescribeAlarmContributors_RequestParameters"></a>

 ** AlarmName **
The name of the alarm for which to retrieve contributor information.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** NextToken **
The token returned by a previous call to indicate that there is more data available.
Type: String
Required: No

## Response Elements
<a name="API_DescribeAlarmContributors_ResponseElements"></a>

The following elements are returned by the service.

 ** AlarmContributors **
A list of alarm contributors that provide details about the individual time series contributing to the alarm's state.
Type: Array of [AlarmContributor](API_AlarmContributor.md) objects

 ** NextToken **
The token that marks the start of the next batch of returned results.
Type: String

## Errors
<a name="API_DescribeAlarmContributors_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextToken **
The next token specified is invalid.
 ** message **

HTTP Status Code: 400

 ** ResourceNotFoundException **
The named resource does not exist.
HTTP Status Code: 404

## See Also
<a name="API_DescribeAlarmContributors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/DescribeAlarmContributors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DescribeAlarmContributors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/DescribeAlarmContributors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/DescribeAlarmContributors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DescribeAlarmContributors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/DescribeAlarmContributors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/DescribeAlarmContributors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/DescribeAlarmContributors)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/DescribeAlarmContributors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DescribeAlarmContributors)
