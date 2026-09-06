---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_CloudExadataInfrastructureUnallocatedResources.html
---

# CloudExadataInfrastructureUnallocatedResources
<a name="API_CloudExadataInfrastructureUnallocatedResources"></a>

Information about unallocated resources in the Cloud Exadata infrastructure.

## Contents
<a name="API_CloudExadataInfrastructureUnallocatedResources_Contents"></a>

 ** cloudAutonomousVmClusters **   <a name="odb-Type-CloudExadataInfrastructureUnallocatedResources-cloudAutonomousVmClusters"></a>
A list of Autonomous VM clusters associated with this Cloud Exadata Infrastructure.
Type: Array of [CloudAutonomousVmClusterResourceDetails](API_CloudAutonomousVmClusterResourceDetails.md) objects
Required: No

 ** cloudExadataInfrastructureDisplayName **   <a name="odb-Type-CloudExadataInfrastructureUnallocatedResources-cloudExadataInfrastructureDisplayName"></a>
The display name of the Cloud Exadata infrastructure.
Type: String
Required: No

 ** cloudExadataInfrastructureId **   <a name="odb-Type-CloudExadataInfrastructureUnallocatedResources-cloudExadataInfrastructureId"></a>
The unique identifier of the Cloud Exadata infrastructure.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: No

 ** exadataStorageInTBs **   <a name="odb-Type-CloudExadataInfrastructureUnallocatedResources-exadataStorageInTBs"></a>
The amount of unallocated Exadata storage available, in terabytes (TB).
Type: Double
Required: No

 ** localStorageInGBs **   <a name="odb-Type-CloudExadataInfrastructureUnallocatedResources-localStorageInGBs"></a>
The amount of unallocated local storage available, in gigabytes (GB).
Type: Integer
Required: No

 ** memoryInGBs **   <a name="odb-Type-CloudExadataInfrastructureUnallocatedResources-memoryInGBs"></a>
The amount of unallocated memory available, in gigabytes (GB).
Type: Integer
Required: No

 ** ocpus **   <a name="odb-Type-CloudExadataInfrastructureUnallocatedResources-ocpus"></a>
The number of unallocated Oracle CPU Units (OCPUs) available.
Type: Integer
Required: No

## See Also
<a name="API_CloudExadataInfrastructureUnallocatedResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/CloudExadataInfrastructureUnallocatedResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/CloudExadataInfrastructureUnallocatedResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/CloudExadataInfrastructureUnallocatedResources)
