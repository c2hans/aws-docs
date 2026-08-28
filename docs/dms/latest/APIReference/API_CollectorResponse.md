---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_CollectorResponse.html
---

# CollectorResponse
<a name="API_CollectorResponse"></a>

Describes a Fleet Advisor collector.

## Contents
<a name="API_CollectorResponse_Contents"></a>

 ** CollectorHealthCheck **   <a name="DMS-Type-CollectorResponse-CollectorHealthCheck"></a>
Describes the last Fleet Advisor collector health check.
Type: [CollectorHealthCheck](API_CollectorHealthCheck.md) object
Required: No

 ** CollectorName **   <a name="DMS-Type-CollectorResponse-CollectorName"></a>
The name of the Fleet Advisor collector .
Type: String
Required: No

 ** CollectorReferencedId **   <a name="DMS-Type-CollectorResponse-CollectorReferencedId"></a>
The reference ID of the Fleet Advisor collector.
Type: String
Required: No

 ** CollectorVersion **   <a name="DMS-Type-CollectorResponse-CollectorVersion"></a>
The version of your Fleet Advisor collector, in semantic versioning format, for example `1.0.2`
Type: String
Required: No

 ** CreatedDate **   <a name="DMS-Type-CollectorResponse-CreatedDate"></a>
The timestamp when you created the collector, in the following format: `2022-01-24T19:04:02.596113Z`
Type: String
Required: No

 ** Description **   <a name="DMS-Type-CollectorResponse-Description"></a>
A summary description of the Fleet Advisor collector.
Type: String
Required: No

 ** InventoryData **   <a name="DMS-Type-CollectorResponse-InventoryData"></a>
Describes a Fleet Advisor collector inventory.
Type: [InventoryData](API_InventoryData.md) object
Required: No

 ** LastDataReceived **   <a name="DMS-Type-CollectorResponse-LastDataReceived"></a>
The timestamp of the last time the collector received data, in the following format: `2022-01-24T19:04:02.596113Z`
Type: String
Required: No

 ** ModifiedDate **   <a name="DMS-Type-CollectorResponse-ModifiedDate"></a>
The timestamp when AWS DMS last modified the collector, in the following format: `2022-01-24T19:04:02.596113Z`
Type: String
Required: No

 ** RegisteredDate **   <a name="DMS-Type-CollectorResponse-RegisteredDate"></a>
The timestamp when AWS DMS registered the collector, in the following format: `2022-01-24T19:04:02.596113Z`
Type: String
Required: No

 ** S3BucketName **   <a name="DMS-Type-CollectorResponse-S3BucketName"></a>
The Amazon S3 bucket that the Fleet Advisor collector uses to store inventory metadata.
Type: String
Required: No

 ** ServiceAccessRoleArn **   <a name="DMS-Type-CollectorResponse-ServiceAccessRoleArn"></a>
The IAM role that grants permissions to access the specified Amazon S3 bucket.
Type: String
Required: No

 ** VersionStatus **   <a name="DMS-Type-CollectorResponse-VersionStatus"></a>
Whether the collector version is up to date.
Type: String
Valid Values: `UP_TO_DATE | OUTDATED | UNSUPPORTED`
Required: No

## See Also
<a name="API_CollectorResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/CollectorResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/CollectorResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/CollectorResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
