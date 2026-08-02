---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_DbSystemShapeSummary.html
---

# DbSystemShapeSummary
<a name="API_DbSystemShapeSummary"></a>

Information about a hardware system model (shape) that's available for an Exadata infrastructure. The shape determines resources, such as CPU cores, memory, and storage, to allocate to the Exadata infrastructure.

## Contents
<a name="API_DbSystemShapeSummary_Contents"></a>

 ** areServerTypesSupported **   <a name="odb-Type-DbSystemShapeSummary-areServerTypesSupported"></a>
Indicates whether the hardware system model supports configurable database and server storage types.
Type: Boolean
Required: No

 ** availableCoreCount **   <a name="odb-Type-DbSystemShapeSummary-availableCoreCount"></a>
The maximum number of CPU cores that can be enabled for the shape.
Type: Integer
Required: No

 ** availableCoreCountPerNode **   <a name="odb-Type-DbSystemShapeSummary-availableCoreCountPerNode"></a>
The maximum number of CPU cores per DB node that can be enabled for the shape.
Type: Integer
Required: No

 ** availableDataStorageInTBs **   <a name="odb-Type-DbSystemShapeSummary-availableDataStorageInTBs"></a>
The maximum amount of data storage, in terabytes (TB), that can be enabled for the shape.
Type: Integer
Required: No

 ** availableDataStoragePerServerInTBs **   <a name="odb-Type-DbSystemShapeSummary-availableDataStoragePerServerInTBs"></a>
The maximum amount of data storage, in terabytes (TB), that's available per storage server for the shape.
Type: Integer
Required: No

 ** availableDbNodePerNodeInGBs **   <a name="odb-Type-DbSystemShapeSummary-availableDbNodePerNodeInGBs"></a>
The maximum amount of DB node storage, in gigabytes (GB), that's available per DB node for the shape.
Type: Integer
Required: No

 ** availableDbNodeStorageInGBs **   <a name="odb-Type-DbSystemShapeSummary-availableDbNodeStorageInGBs"></a>
The maximum amount of DB node storage, in gigabytes (GB), that can be enabled for the shape.
Type: Integer
Required: No

 ** availableMemoryInGBs **   <a name="odb-Type-DbSystemShapeSummary-availableMemoryInGBs"></a>
The maximum amount of memory, in gigabytes (GB), that can be enabled for the shape.
Type: Integer
Required: No

 ** availableMemoryPerNodeInGBs **   <a name="odb-Type-DbSystemShapeSummary-availableMemoryPerNodeInGBs"></a>
The maximum amount of memory, in gigabytes (GB), that's available per DB node for the shape.
Type: Integer
Required: No

 ** computeModel **   <a name="odb-Type-DbSystemShapeSummary-computeModel"></a>
The OCI model compute model used when you create or clone an instance: ECPU or OCPU. An ECPU is an abstracted measure of compute resources. ECPUs are based on the number of cores elastically allocated from a pool of compute and storage servers. An OCPU is a legacy physical measure of compute resources. OCPUs are based on the physical core of a processor with hyper-threading enabled.
Type: String
Valid Values: `ECPU | OCPU`
Required: No

 ** coreCountIncrement **   <a name="odb-Type-DbSystemShapeSummary-coreCountIncrement"></a>
The discrete number by which the CPU core count for the shape can be increased or decreased.
Type: Integer
Required: No

 ** maximumNodeCount **   <a name="odb-Type-DbSystemShapeSummary-maximumNodeCount"></a>
The maximum number of compute servers that is available for the shape.
Type: Integer
Required: No

 ** maxStorageCount **   <a name="odb-Type-DbSystemShapeSummary-maxStorageCount"></a>
The maximum number of Exadata storage servers that's available for the shape.
Type: Integer
Required: No

 ** minCoreCountPerNode **   <a name="odb-Type-DbSystemShapeSummary-minCoreCountPerNode"></a>
The minimum number of CPU cores that can be enabled per node for the shape.
Type: Integer
Required: No

 ** minDataStorageInTBs **   <a name="odb-Type-DbSystemShapeSummary-minDataStorageInTBs"></a>
The minimum amount of data storage, in terabytes (TB), that must be allocated for the shape.
Type: Integer
Required: No

 ** minDbNodeStoragePerNodeInGBs **   <a name="odb-Type-DbSystemShapeSummary-minDbNodeStoragePerNodeInGBs"></a>
The minimum amount of DB node storage, in gigabytes (GB), that must be allocated per DB node for the shape.
Type: Integer
Required: No

 ** minimumCoreCount **   <a name="odb-Type-DbSystemShapeSummary-minimumCoreCount"></a>
The minimum number of CPU cores that can be enabled for the shape.
Type: Integer
Required: No

 ** minimumNodeCount **   <a name="odb-Type-DbSystemShapeSummary-minimumNodeCount"></a>
The minimum number of compute servers that are available for the shape.
Type: Integer
Required: No

 ** minMemoryPerNodeInGBs **   <a name="odb-Type-DbSystemShapeSummary-minMemoryPerNodeInGBs"></a>
The minimum amount of memory, in gigabytes (GB), that must be allocated per DB node for the shape.
Type: Integer
Required: No

 ** minStorageCount **   <a name="odb-Type-DbSystemShapeSummary-minStorageCount"></a>
The minimum number of Exadata storage servers that are available for the shape.
Type: Integer
Required: No

 ** name **   <a name="odb-Type-DbSystemShapeSummary-name"></a>
The name of the shape.
Type: String
Required: No

 ** runtimeMinimumCoreCount **   <a name="odb-Type-DbSystemShapeSummary-runtimeMinimumCoreCount"></a>
The runtime minimum number of CPU cores that can be enabled for the shape.
Type: Integer
Required: No

 ** shapeFamily **   <a name="odb-Type-DbSystemShapeSummary-shapeFamily"></a>
The family of the shape.
Type: String
Required: No

 ** shapeType **   <a name="odb-Type-DbSystemShapeSummary-shapeType"></a>
The shape type. This property is determined by the CPU hardware.
Type: String
Valid Values: `AMD | INTEL | INTEL_FLEX_X9 | AMPERE_FLEX_A1`
Required: No

## See Also
<a name="API_DbSystemShapeSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/DbSystemShapeSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/DbSystemShapeSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/DbSystemShapeSummary)
