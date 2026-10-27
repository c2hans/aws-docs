---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_FlexComponentSummary.html
---

# FlexComponentSummary
<a name="API_FlexComponentSummary"></a>

Information about a flex component that's available for an Exadata infrastructure. A flex component defines the hardware resources, such as CPU cores, memory, and storage, that can be allocated to a shape.

## Contents
<a name="API_FlexComponentSummary_Contents"></a>

 ** availableCoreCount **   <a name="odb-Type-FlexComponentSummary-availableCoreCount"></a>
The maximum number of CPU cores that can be enabled for the flex component.
Type: Integer
Required: No

 ** availableDbStorageInGBs **   <a name="odb-Type-FlexComponentSummary-availableDbStorageInGBs"></a>
The maximum amount of database storage, in gigabytes (GB), that can be enabled for the flex component.
Type: Integer
Required: No

 ** availableLocalStorageInGBs **   <a name="odb-Type-FlexComponentSummary-availableLocalStorageInGBs"></a>
The maximum amount of local storage, in gigabytes (GB), that can be enabled for the flex component.
Type: Integer
Required: No

 ** availableMemoryInGBs **   <a name="odb-Type-FlexComponentSummary-availableMemoryInGBs"></a>
The maximum amount of memory, in gigabytes (GB), that can be enabled for the flex component.
Type: Integer
Required: No

 ** computeModel **   <a name="odb-Type-FlexComponentSummary-computeModel"></a>
The OCI model compute model used when you create or clone an instance: ECPU or OCPU. An ECPU is an abstracted measure of compute resources. ECPUs are based on the number of cores elastically allocated from a pool of compute and storage servers. An OCPU is a legacy physical measure of compute resources. OCPUs are based on the physical core of a processor with hyper-threading enabled.
Type: String
Valid Values: `ECPU | OCPU`
Required: No

 ** descriptionSummary **   <a name="odb-Type-FlexComponentSummary-descriptionSummary"></a>
A summary description of the flex component.
Type: String
Required: No

 ** hardwareType **   <a name="odb-Type-FlexComponentSummary-hardwareType"></a>
The type of hardware for the flex component. Valid values are `COMPUTE` for compute servers and `CELL` for storage servers.
Type: String
Valid Values: `COMPUTE | CELL`
Required: No

 ** minimumCoreCount **   <a name="odb-Type-FlexComponentSummary-minimumCoreCount"></a>
The minimum number of CPU cores that can be enabled for the flex component.
Type: Integer
Required: No

 ** name **   <a name="odb-Type-FlexComponentSummary-name"></a>
The name of the flex component.
Type: String
Required: No

 ** runtimeMinimumCoreCount **   <a name="odb-Type-FlexComponentSummary-runtimeMinimumCoreCount"></a>
The runtime minimum number of CPU cores that can be enabled for the flex component.
Type: Integer
Required: No

 ** shape **   <a name="odb-Type-FlexComponentSummary-shape"></a>
The shape that uses the flex component.
Type: String
Required: No

## See Also
<a name="API_FlexComponentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/FlexComponentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/FlexComponentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/FlexComponentSummary)
