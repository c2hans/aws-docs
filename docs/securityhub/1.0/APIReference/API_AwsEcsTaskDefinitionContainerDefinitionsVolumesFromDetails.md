---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetails.html
---

# AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetails
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetails"></a>

A data volume to mount from another container.

## Contents
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetails_Contents"></a>

 ** ReadOnly **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetails-ReadOnly"></a>
Whether the container has read-only access to the volume.
Type: Boolean
Required: No

 ** SourceContainer **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetails-SourceContainer"></a>
The name of another container within the same task definition from which to mount volumes.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetails)
