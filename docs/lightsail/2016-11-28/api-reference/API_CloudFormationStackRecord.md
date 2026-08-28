---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CloudFormationStackRecord.html
---

# CloudFormationStackRecord
<a name="API_CloudFormationStackRecord"></a>

Describes a CloudFormation stack record created as a result of the `create cloud formation stack` action.

A CloudFormation stack record provides information about the AWS CloudFormation stack used to create a new Amazon Elastic Compute Cloud instance from an exported Lightsail instance snapshot.

## Contents
<a name="API_CloudFormationStackRecord_Contents"></a>

 ** arn **   <a name="Lightsail-Type-CloudFormationStackRecord-arn"></a>
The Amazon Resource Name (ARN) of the CloudFormation stack record.
Type: String
Pattern: `.*\S.*`
Required: No

 ** createdAt **   <a name="Lightsail-Type-CloudFormationStackRecord-createdAt"></a>
The date when the CloudFormation stack record was created.
Type: Timestamp
Required: No

 ** destinationInfo **   <a name="Lightsail-Type-CloudFormationStackRecord-destinationInfo"></a>
A list of objects describing the destination service, which is AWS CloudFormation, and the Amazon Resource Name (ARN) of the AWS CloudFormation stack.
Type: [DestinationInfo](API_DestinationInfo.md) object
Required: No

 ** location **   <a name="Lightsail-Type-CloudFormationStackRecord-location"></a>
A list of objects describing the Availability Zone and AWS Region of the CloudFormation stack record.
Type: [ResourceLocation](API_ResourceLocation.md) object
Required: No

 ** name **   <a name="Lightsail-Type-CloudFormationStackRecord-name"></a>
The name of the CloudFormation stack record. It starts with `CloudFormationStackRecord` followed by a GUID.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** resourceType **   <a name="Lightsail-Type-CloudFormationStackRecord-resourceType"></a>
The Lightsail resource type (`CloudFormationStackRecord`).
Type: String
Valid Values: `ContainerService | Instance | StaticIp | KeyPair | InstanceSnapshot | Domain | PeeredVpc | LoadBalancer | LoadBalancerTlsCertificate | Disk | DiskSnapshot | RelationalDatabase | RelationalDatabaseSnapshot | ExportSnapshotRecord | CloudFormationStackRecord | Alarm | ContactMethod | Distribution | Certificate | Bucket`
Required: No

 ** sourceInfo **   <a name="Lightsail-Type-CloudFormationStackRecord-sourceInfo"></a>
A list of objects describing the source of the CloudFormation stack record.
Type: Array of [CloudFormationStackRecordSourceInfo](API_CloudFormationStackRecordSourceInfo.md) objects
Required: No

 ** state **   <a name="Lightsail-Type-CloudFormationStackRecord-state"></a>
The current state of the CloudFormation stack record.
Type: String
Valid Values: `Started | Succeeded | Failed`
Required: No

## See Also
<a name="API_CloudFormationStackRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/CloudFormationStackRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/CloudFormationStackRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/CloudFormationStackRecord)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
