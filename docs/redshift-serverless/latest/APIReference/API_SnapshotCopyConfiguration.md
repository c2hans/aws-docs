---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_SnapshotCopyConfiguration.html
---

# SnapshotCopyConfiguration
<a name="API_SnapshotCopyConfiguration"></a>

The object that you configure to copy snapshots from one namespace to a namespace in another AWS Region.

## Contents
<a name="API_SnapshotCopyConfiguration_Contents"></a>

 ** destinationKmsKeyId **   <a name="redshiftserverless-Type-SnapshotCopyConfiguration-destinationKmsKeyId"></a>
The ID of the KMS key to use to encrypt your snapshots in the destination AWS Region.
Type: String
Required: No

 ** destinationRegion **   <a name="redshiftserverless-Type-SnapshotCopyConfiguration-destinationRegion"></a>
The destination AWS Region to copy snapshots to.
Type: String
Required: No

 ** namespaceName **   <a name="redshiftserverless-Type-SnapshotCopyConfiguration-namespaceName"></a>
The name of the namespace to copy snapshots from in the source AWS Region.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: No

 ** snapshotCopyConfigurationArn **   <a name="redshiftserverless-Type-SnapshotCopyConfiguration-snapshotCopyConfigurationArn"></a>
The ARN of the snapshot copy configuration object.
Type: String
Required: No

 ** snapshotCopyConfigurationId **   <a name="redshiftserverless-Type-SnapshotCopyConfiguration-snapshotCopyConfigurationId"></a>
The ID of the snapshot copy configuration object.
Type: String
Required: No

 ** snapshotRetentionPeriod **   <a name="redshiftserverless-Type-SnapshotCopyConfiguration-snapshotRetentionPeriod"></a>
The retention period of snapshots that are copied to the destination AWS Region.
Type: Integer
Required: No

## See Also
<a name="API_SnapshotCopyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/SnapshotCopyConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/SnapshotCopyConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/SnapshotCopyConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
