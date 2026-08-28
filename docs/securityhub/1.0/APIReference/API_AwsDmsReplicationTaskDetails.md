---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsDmsReplicationTaskDetails.html
---

# AwsDmsReplicationTaskDetails
<a name="API_AwsDmsReplicationTaskDetails"></a>

 Provides details about an AWS Database Migration Service (AWS DMS) replication task. A replication task moves a set of data from the source endpoint to the target endpoint.

## Contents
<a name="API_AwsDmsReplicationTaskDetails_Contents"></a>

 ** CdcStartPosition **   <a name="securityhub-Type-AwsDmsReplicationTaskDetails-CdcStartPosition"></a>
 Indicates when you want a change data capture (CDC) operation to start. `CCdcStartPosition` or `CCdcStartTime` specifies when you want a CDC operation to start. Only a value for one of these fields is included.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CdcStartTime **   <a name="securityhub-Type-AwsDmsReplicationTaskDetails-CdcStartTime"></a>
 Indicates the start time for a CDC operation. `CdcStartPosition` or `CCdcStartTime` specifies when you want a CDC operation to start. Only a value for one of these fields is included.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CdcStopPosition **   <a name="securityhub-Type-AwsDmsReplicationTaskDetails-CdcStopPosition"></a>
 Indicates when you want a CDC operation to stop. The value can be either server time or commit time.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Id **   <a name="securityhub-Type-AwsDmsReplicationTaskDetails-Id"></a>
 The identifier of the replication task.
Type: String
Pattern: `.*\S.*`
Required: No

 ** MigrationType **   <a name="securityhub-Type-AwsDmsReplicationTaskDetails-MigrationType"></a>
 The migration type.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ReplicationInstanceArn **   <a name="securityhub-Type-AwsDmsReplicationTaskDetails-ReplicationInstanceArn"></a>
 The Amazon Resource Name (ARN) of a replication instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ReplicationTaskIdentifier **   <a name="securityhub-Type-AwsDmsReplicationTaskDetails-ReplicationTaskIdentifier"></a>
 The user-defined replication task identifier or name.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ReplicationTaskSettings **   <a name="securityhub-Type-AwsDmsReplicationTaskDetails-ReplicationTaskSettings"></a>
 The settings for the replication task.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ResourceIdentifier **   <a name="securityhub-Type-AwsDmsReplicationTaskDetails-ResourceIdentifier"></a>
 A display name for the resource identifier at the end of the `EndpointArn` response parameter. If you don't specify a `ResourceIdentifier` value, DMS generates a default identifier value for the end of `EndpointArn`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SourceEndpointArn **   <a name="securityhub-Type-AwsDmsReplicationTaskDetails-SourceEndpointArn"></a>
 The ARN of the source endpoint.
Type: String
Pattern: `.*\S.*`
Required: No

 ** TableMappings **   <a name="securityhub-Type-AwsDmsReplicationTaskDetails-TableMappings"></a>
 The table mappings for the replication task, in JSON format.
Type: String
Pattern: `.*\S.*`
Required: No

 ** TargetEndpointArn **   <a name="securityhub-Type-AwsDmsReplicationTaskDetails-TargetEndpointArn"></a>
 The ARN of the target endpoint.
Type: String
Pattern: `.*\S.*`
Required: No

 ** TaskData **   <a name="securityhub-Type-AwsDmsReplicationTaskDetails-TaskData"></a>
 Supplemental information that the task requires to migrate the data for certain source and target endpoints.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsDmsReplicationTaskDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsDmsReplicationTaskDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsDmsReplicationTaskDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsDmsReplicationTaskDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
