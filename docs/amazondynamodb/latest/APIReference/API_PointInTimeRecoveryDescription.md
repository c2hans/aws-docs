---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PointInTimeRecoveryDescription.html
---

# PointInTimeRecoveryDescription
<a name="API_PointInTimeRecoveryDescription"></a>

The description of the point in time settings applied to the table.

## Contents
<a name="API_PointInTimeRecoveryDescription_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** EarliestRestorableDateTime **   <a name="DDB-Type-PointInTimeRecoveryDescription-EarliestRestorableDateTime"></a>
Specifies the earliest point in time you can restore your table to. You can restore your table to any point in time during the last 35 days.
Type: Timestamp
Required: No

 ** LatestRestorableDateTime **   <a name="DDB-Type-PointInTimeRecoveryDescription-LatestRestorableDateTime"></a>
 `LatestRestorableDateTime` is typically 5 minutes before the current time.
Type: Timestamp
Required: No

 ** PointInTimeRecoveryStatus **   <a name="DDB-Type-PointInTimeRecoveryDescription-PointInTimeRecoveryStatus"></a>
The current state of point in time recovery:
+  `ENABLED` - Point in time recovery is enabled.
+  `DISABLED` - Point in time recovery is disabled.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** RecoveryPeriodInDays **   <a name="DDB-Type-PointInTimeRecoveryDescription-RecoveryPeriodInDays"></a>
The number of preceding days for which continuous backups are taken and maintained. Your table data is only recoverable to any point-in-time from within the configured recovery period. This parameter is optional.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 35.
Required: No

## See Also
<a name="API_PointInTimeRecoveryDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/PointInTimeRecoveryDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/PointInTimeRecoveryDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/PointInTimeRecoveryDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
