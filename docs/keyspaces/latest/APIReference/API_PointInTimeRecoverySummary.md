---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_PointInTimeRecoverySummary.html
---

# PointInTimeRecoverySummary
<a name="API_PointInTimeRecoverySummary"></a>

The point-in-time recovery status of the specified table.

## Contents
<a name="API_PointInTimeRecoverySummary_Contents"></a>

 ** status **   <a name="keyspaces-Type-PointInTimeRecoverySummary-status"></a>
Shows if point-in-time recovery is enabled or disabled for the specified table.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** earliestRestorableTimestamp **   <a name="keyspaces-Type-PointInTimeRecoverySummary-earliestRestorableTimestamp"></a>
Specifies the earliest possible restore point of the table in ISO 8601 format.
Type: Timestamp
Required: No

## See Also
<a name="API_PointInTimeRecoverySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/PointInTimeRecoverySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/PointInTimeRecoverySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/PointInTimeRecoverySummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces (for Apache Cassandra). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
