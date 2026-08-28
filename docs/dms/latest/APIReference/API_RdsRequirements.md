---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_RdsRequirements.html
---

# RdsRequirements
<a name="API_RdsRequirements"></a>

Provides information that describes the requirements to the target engine on Amazon RDS.

## Contents
<a name="API_RdsRequirements_Contents"></a>

 ** DeploymentOption **   <a name="DMS-Type-RdsRequirements-DeploymentOption"></a>
The required deployment option for the Amazon RDS DB instance. Valid values include `"MULTI_AZ"` for Multi-AZ deployments and `"SINGLE_AZ"` for Single-AZ deployments.
Type: String
Required: No

 ** EngineEdition **   <a name="DMS-Type-RdsRequirements-EngineEdition"></a>
The required target Amazon RDS engine edition.
Type: String
Required: No

 ** EngineVersion **   <a name="DMS-Type-RdsRequirements-EngineVersion"></a>
The required target Amazon RDS engine version.
Type: String
Required: No

 ** InstanceMemory **   <a name="DMS-Type-RdsRequirements-InstanceMemory"></a>
The required memory on the Amazon RDS DB instance.
Type: Double
Required: No

 ** InstanceVcpu **   <a name="DMS-Type-RdsRequirements-InstanceVcpu"></a>
The required number of virtual CPUs (vCPU) on the Amazon RDS DB instance.
Type: Double
Required: No

 ** StorageIops **   <a name="DMS-Type-RdsRequirements-StorageIops"></a>
The required number of I/O operations completed each second (IOPS) on your Amazon RDS DB instance.
Type: Integer
Required: No

 ** StorageSize **   <a name="DMS-Type-RdsRequirements-StorageSize"></a>
The required Amazon RDS DB instance storage size.
Type: Integer
Required: No

## See Also
<a name="API_RdsRequirements_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/RdsRequirements)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/RdsRequirements)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/RdsRequirements)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
