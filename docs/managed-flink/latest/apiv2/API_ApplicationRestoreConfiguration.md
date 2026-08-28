---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ApplicationRestoreConfiguration.html
---

# ApplicationRestoreConfiguration
<a name="API_ApplicationRestoreConfiguration"></a>

Specifies the method and snapshot to use when restarting an application using previously saved application state.

## Contents
<a name="API_ApplicationRestoreConfiguration_Contents"></a>

 ** ApplicationRestoreType **   <a name="APIReference-Type-ApplicationRestoreConfiguration-ApplicationRestoreType"></a>
Specifies how the application should be restored.
Type: String
Valid Values: `SKIP_RESTORE_FROM_SNAPSHOT | RESTORE_FROM_LATEST_SNAPSHOT | RESTORE_FROM_CUSTOM_SNAPSHOT`
Required: Yes

 ** SnapshotName **   <a name="APIReference-Type-ApplicationRestoreConfiguration-SnapshotName"></a>
The identifier of an existing snapshot of application state to use to restart an application. The application uses this value if `RESTORE_FROM_CUSTOM_SNAPSHOT` is specified for the `ApplicationRestoreType`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## See Also
<a name="API_ApplicationRestoreConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ApplicationRestoreConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ApplicationRestoreConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ApplicationRestoreConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
