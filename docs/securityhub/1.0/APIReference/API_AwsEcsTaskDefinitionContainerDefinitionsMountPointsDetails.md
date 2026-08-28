---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetails.html
---

# AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetails
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetails"></a>

A mount point for the data volumes in the container.

## Contents
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetails_Contents"></a>

 ** ContainerPath **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetails-ContainerPath"></a>
The path on the container to mount the host volume at.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ReadOnly **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetails-ReadOnly"></a>
Whether the container has read-only access to the volume.
Type: Boolean
Required: No

 ** SourceVolume **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetails-SourceVolume"></a>
The name of the volume to mount. Must match the name of a volume listed in `VolumeDetails` for the task definition.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
