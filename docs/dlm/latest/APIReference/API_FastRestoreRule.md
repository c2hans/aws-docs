---
source_url: https://docs.aws.amazon.com/dlm/latest/APIReference/API_FastRestoreRule.html
---

# FastRestoreRule
<a name="API_FastRestoreRule"></a>

 **[Custom snapshot policies only]** Specifies a rule for enabling fast snapshot restore for snapshots created by snapshot policies. You can enable fast snapshot restore based on either a count or a time interval.

## Contents
<a name="API_FastRestoreRule_Contents"></a>

 ** AvailabilityZoneIds **   <a name="dlm-Type-FastRestoreRule-AvailabilityZoneIds"></a>
The Availability Zone Ids in which to enable fast snapshot restore.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 0. Maximum length of 16.
Pattern: `[a-z]{3,4}\d-az\d+`
Required: No

 ** AvailabilityZones **   <a name="dlm-Type-FastRestoreRule-AvailabilityZones"></a>
The Availability Zones in which to enable fast snapshot restore.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 0. Maximum length of 16.
Pattern: `([a-z]+-){2,3}\d[a-z]`
Required: No

 ** Count **   <a name="dlm-Type-FastRestoreRule-Count"></a>
The number of snapshots to be enabled with fast snapshot restore.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** Interval **   <a name="dlm-Type-FastRestoreRule-Interval"></a>
The amount of time to enable fast snapshot restore. The maximum is 100 years. This is equivalent to 1200 months, 5200 weeks, or 36500 days.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** IntervalUnit **   <a name="dlm-Type-FastRestoreRule-IntervalUnit"></a>
The unit of time for enabling fast snapshot restore.
Type: String
Valid Values: `HOURS | DAYS | WEEKS | MONTHS | YEARS`
Required: No

## See Also
<a name="API_FastRestoreRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dlm-2018-01-12/FastRestoreRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dlm-2018-01-12/FastRestoreRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dlm-2018-01-12/FastRestoreRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Lifecycle Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dlm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
