---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_OrderableReplicationInstance.html
---

# OrderableReplicationInstance
<a name="API_OrderableReplicationInstance"></a>

In response to the `DescribeOrderableReplicationInstances` operation, this object describes an available replication instance. This description includes the replication instance's type, engine version, and allocated storage.

## Contents
<a name="API_OrderableReplicationInstance_Contents"></a>

 ** AvailabilityZones **   <a name="DMS-Type-OrderableReplicationInstance-AvailabilityZones"></a>
List of Availability Zones for this replication instance.
Type: Array of strings
Required: No

 ** DefaultAllocatedStorage **   <a name="DMS-Type-OrderableReplicationInstance-DefaultAllocatedStorage"></a>
The default amount of storage (in gigabytes) that is allocated for the replication instance.
Type: Integer
Required: No

 ** EngineVersion **   <a name="DMS-Type-OrderableReplicationInstance-EngineVersion"></a>
The version of the replication engine.
Type: String
Required: No

 ** IncludedAllocatedStorage **   <a name="DMS-Type-OrderableReplicationInstance-IncludedAllocatedStorage"></a>
The amount of storage (in gigabytes) that is allocated for the replication instance.
Type: Integer
Required: No

 ** MaxAllocatedStorage **   <a name="DMS-Type-OrderableReplicationInstance-MaxAllocatedStorage"></a>
The minimum amount of storage (in gigabytes) that can be allocated for the replication instance.
Type: Integer
Required: No

 ** MinAllocatedStorage **   <a name="DMS-Type-OrderableReplicationInstance-MinAllocatedStorage"></a>
The minimum amount of storage (in gigabytes) that can be allocated for the replication instance.
Type: Integer
Required: No

 ** ReleaseStatus **   <a name="DMS-Type-OrderableReplicationInstance-ReleaseStatus"></a>
The value returned when the specified `EngineVersion` of the replication instance is in Beta or test mode. This indicates some features might not work as expected.
 AWS DMS supports the `ReleaseStatus` parameter in versions 3.1.4 and later.
Type: String
Valid Values: `beta | prod`
Required: No

 ** ReplicationInstanceClass **   <a name="DMS-Type-OrderableReplicationInstance-ReplicationInstanceClass"></a>
The compute and memory capacity of the replication instance as defined for the specified replication instance class. For example to specify the instance class dms.c4.large, set this parameter to `"dms.c4.large"`.
For more information on the settings and capacities for the available replication instance classes, see [ Selecting the right AWS DMS replication instance for your migration](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html#CHAP_ReplicationInstance.InDepth).
Type: String
Length Constraints: Maximum length of 30.
Required: No

 ** StorageType **   <a name="DMS-Type-OrderableReplicationInstance-StorageType"></a>
The type of storage used by the replication instance.
Type: String
Required: No

## See Also
<a name="API_OrderableReplicationInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/OrderableReplicationInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/OrderableReplicationInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/OrderableReplicationInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
