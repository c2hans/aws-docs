---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ScanResultConditionRequest.html
---

# ScanResultConditionRequest
<a name="API_ScanResultConditionRequest"></a>

The Amazon Inspector scan-result criteria that an AMI must meet to be allowed. The criteria can limit the highest finding severity. They can also limit, for each severity, the days since Amazon Inspector reported a fix as available.

The severity limit applies to all findings, whether or not a fix is available. The day limits for each severity apply only to findings that have a fix available. A scanned AMI that has no fix-available finding of a given severity meets that severity's day limit. AMIs that Amazon Inspector has not scanned are not allowed when you specify this condition.

## Contents
<a name="API_ScanResultConditionRequest_Contents"></a>

 ** MaxDaysSinceCriticalFixAvailable **
The maximum number of days since Amazon Inspector reported a fix as available for a `critical` severity finding on the AMI. For example, a value of `7` does not allow an AMI if Amazon Inspector reported such a fix more than 7 days ago.
A scanned AMI that has no `critical` severity finding with a fix available meets this limit. AMIs that Amazon Inspector has not scanned are not allowed.
Constraints: Minimum value of 0. Maximum value of 2147483647.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** MaxDaysSinceHighFixAvailable **
The maximum number of days since Amazon Inspector reported a fix as available for a `high` severity finding on the AMI. For example, a value of `7` does not allow an AMI if Amazon Inspector reported such a fix more than 7 days ago.
A scanned AMI that has no `high` severity finding with a fix available meets this limit. AMIs that Amazon Inspector has not scanned are not allowed.
Constraints: Minimum value of 0. Maximum value of 2147483647.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** MaxDaysSinceInformationalFixAvailable **
The maximum number of days since Amazon Inspector reported a fix as available for an `informational` severity finding on the AMI. For example, a value of `7` does not allow an AMI if Amazon Inspector reported such a fix more than 7 days ago.
A scanned AMI that has no `informational` severity finding with a fix available meets this limit. AMIs that Amazon Inspector has not scanned are not allowed.
Constraints: Minimum value of 0. Maximum value of 2147483647.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** MaxDaysSinceLastFindingScan **
The maximum number of days that have elapsed since Amazon Inspector last scanned the AMI. For example, a value of `7` allows AMIs that were scanned within the last 7 days. AMIs that Amazon Inspector has not scanned are not allowed.
Constraints: Minimum value of 0. Maximum value of 2147483647.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** MaxDaysSinceLowFixAvailable **
The maximum number of days since Amazon Inspector reported a fix as available for a `low` severity finding on the AMI. For example, a value of `7` does not allow an AMI if Amazon Inspector reported such a fix more than 7 days ago.
A scanned AMI that has no `low` severity finding with a fix available meets this limit. AMIs that Amazon Inspector has not scanned are not allowed.
Constraints: Minimum value of 0. Maximum value of 2147483647.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** MaxDaysSinceMediumFixAvailable **
The maximum number of days since Amazon Inspector reported a fix as available for a `medium` severity finding on the AMI. For example, a value of `7` does not allow an AMI if Amazon Inspector reported such a fix more than 7 days ago.
A scanned AMI that has no `medium` severity finding with a fix available meets this limit. AMIs that Amazon Inspector has not scanned are not allowed.
Constraints: Minimum value of 0. Maximum value of 2147483647.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** MaximumSeverityLabel **
The maximum severity that an AMI's Amazon Inspector findings can have for the AMI to be allowed. Findings count whether or not a fix is available. For example, a value of `medium` allows AMIs whose highest severity is `informational`, `low`, or `medium`.
The valid values are the following Amazon Inspector severity levels, which correspond to CVSS score ranges:
+  `informational` - CVSS score of 0.
+  `low` - CVSS score of 0.1 to 3.9.
+  `medium` - CVSS score of 4.0 to 6.9.
+  `high` - CVSS score of 7.0 to 8.9.
+  `critical` - CVSS score of 9.0 to 10.0.
For more information, see [Software package vulnerability severity](https://docs.aws.amazon.com/inspector/latest/user/findings-understanding-severity.html#findings-understanding-package-score) in the *Amazon Inspector User Guide*.
A scanned AMI that has no findings meets this limit.
AMIs that Amazon Inspector has not scanned are not allowed when you specify this condition.
Type: String
Valid Values: `informational | low | medium | high | critical`
Required: No

## See Also
<a name="API_ScanResultConditionRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ScanResultConditionRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ScanResultConditionRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ScanResultConditionRequest)
