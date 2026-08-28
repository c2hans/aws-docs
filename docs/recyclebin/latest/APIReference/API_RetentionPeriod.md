---
source_url: https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_RetentionPeriod.html
---

# RetentionPeriod
<a name="API_RetentionPeriod"></a>

Information about the retention period for which the retention rule is to retain resources.

## Contents
<a name="API_RetentionPeriod_Contents"></a>

 ** RetentionPeriodUnit **   <a name="recyclebin-Type-RetentionPeriod-RetentionPeriodUnit"></a>
The unit of time in which the retention period is measured. Currently, only `DAYS` is supported.
Type: String
Valid Values: `DAYS`
Required: Yes

 ** RetentionPeriodValue **   <a name="recyclebin-Type-RetentionPeriod-RetentionPeriodValue"></a>
The period value for which the retention rule is to retain resources, measured in days. The supported retention periods are:
+ EBS volumes: 1 - 7 days
+ EBS snapshots and EBS-backed AMIs: 1 - 365 days
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 365.
Required: Yes

## See Also
<a name="API_RetentionPeriod_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rbin-2021-06-15/RetentionPeriod)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rbin-2021-06-15/RetentionPeriod)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rbin-2021-06-15/RetentionPeriod)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Recycle Bin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query recyclebin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
