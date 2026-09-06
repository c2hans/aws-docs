---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_RdsConfiguration.html
---

# RdsConfiguration
<a name="API_RdsConfiguration"></a>

Provides information that describes the configuration of the recommended target engine on Amazon RDS.

## Contents
<a name="API_RdsConfiguration_Contents"></a>

 ** DeploymentOption **   <a name="DMS-Type-RdsConfiguration-DeploymentOption"></a>
Describes the deployment option for the recommended Amazon RDS DB instance. The deployment options include Multi-AZ and Single-AZ deployments. Valid values include `"MULTI_AZ"` and `"SINGLE_AZ"`.
Type: String
Required: No

 ** EngineEdition **   <a name="DMS-Type-RdsConfiguration-EngineEdition"></a>
Describes the recommended target Amazon RDS engine edition.
Type: String
Required: No

 ** EngineVersion **   <a name="DMS-Type-RdsConfiguration-EngineVersion"></a>
Describes the recommended target Amazon RDS engine version.
Type: String
Required: No

 ** InstanceMemory **   <a name="DMS-Type-RdsConfiguration-InstanceMemory"></a>
Describes the memory on the recommended Amazon RDS DB instance that meets your requirements.
Type: Double
Required: No

 ** InstanceType **   <a name="DMS-Type-RdsConfiguration-InstanceType"></a>
Describes the recommended target Amazon RDS instance type.
Type: String
Required: No

 ** InstanceVcpu **   <a name="DMS-Type-RdsConfiguration-InstanceVcpu"></a>
Describes the number of virtual CPUs (vCPU) on the recommended Amazon RDS DB instance that meets your requirements.
Type: Double
Required: No

 ** StorageIops **   <a name="DMS-Type-RdsConfiguration-StorageIops"></a>
Describes the number of I/O operations completed each second (IOPS) on the recommended Amazon RDS DB instance that meets your requirements.
Type: Integer
Required: No

 ** StorageSize **   <a name="DMS-Type-RdsConfiguration-StorageSize"></a>
Describes the storage size of the recommended Amazon RDS DB instance that meets your requirements.
Type: Integer
Required: No

 ** StorageType **   <a name="DMS-Type-RdsConfiguration-StorageType"></a>
Describes the storage type of the recommended Amazon RDS DB instance that meets your requirements.
Amazon RDS provides three storage types: General Purpose SSD (also known as gp2 and gp3), Provisioned IOPS SSD (also known as io1), and magnetic (also known as standard).
Type: String
Required: No

## See Also
<a name="API_RdsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/RdsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/RdsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/RdsConfiguration)
