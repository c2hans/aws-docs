---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ApplicationSummary.html
---

# ApplicationSummary
<a name="API_ApplicationSummary"></a>

Provides application summary information, including the application Amazon Resource Name (ARN), name, and status.

## Contents
<a name="API_ApplicationSummary_Contents"></a>

 ** ApplicationARN **   <a name="APIReference-Type-ApplicationSummary-ApplicationARN"></a>
The ARN of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

 ** ApplicationName **   <a name="APIReference-Type-ApplicationSummary-ApplicationName"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** ApplicationStatus **   <a name="APIReference-Type-ApplicationSummary-ApplicationStatus"></a>
The status of the application.
Type: String
Valid Values: `DELETING | STARTING | STOPPING | READY | RUNNING | UPDATING | AUTOSCALING | FORCE_STOPPING | ROLLING_BACK | MAINTENANCE | ROLLED_BACK`
Required: Yes

 ** ApplicationVersionId **   <a name="APIReference-Type-ApplicationSummary-ApplicationVersionId"></a>
Provides the current application version.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.
Required: Yes

 ** RuntimeEnvironment **   <a name="APIReference-Type-ApplicationSummary-RuntimeEnvironment"></a>
The runtime environment for the application.
Type: String
Valid Values: `SQL-1_0 | FLINK-1_6 | FLINK-1_8 | ZEPPELIN-FLINK-1_0 | FLINK-1_11 | FLINK-1_13 | ZEPPELIN-FLINK-2_0 | FLINK-1_15 | ZEPPELIN-FLINK-3_0 | FLINK-1_18 | FLINK-1_19 | FLINK-1_20`
Required: Yes

 ** ApplicationMode **   <a name="APIReference-Type-ApplicationSummary-ApplicationMode"></a>
For a Managed Service for Apache Flink application, the mode is `STREAMING`. For a Managed Service for Apache Flink Studio notebook, it is `INTERACTIVE`.
Type: String
Valid Values: `STREAMING | INTERACTIVE`
Required: No

## See Also
<a name="API_ApplicationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ApplicationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ApplicationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ApplicationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
