---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsTaskDefinitionVolumesDetails.html
---

# AwsEcsTaskDefinitionVolumesDetails
<a name="API_AwsEcsTaskDefinitionVolumesDetails"></a>

A data volume to mount from another container.

## Contents
<a name="API_AwsEcsTaskDefinitionVolumesDetails_Contents"></a>

 ** DockerVolumeConfiguration **   <a name="securityhub-Type-AwsEcsTaskDefinitionVolumesDetails-DockerVolumeConfiguration"></a>
Information about a Docker volume.
Type: [AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetails](API_AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetails.md) object
Required: No

 ** EfsVolumeConfiguration **   <a name="securityhub-Type-AwsEcsTaskDefinitionVolumesDetails-EfsVolumeConfiguration"></a>
Information about the Amazon Elastic File System file system that is used for task storage.
Type: [AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetails](API_AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetails.md) object
Required: No

 ** Host **   <a name="securityhub-Type-AwsEcsTaskDefinitionVolumesDetails-Host"></a>
Information about a bind mount host volume.
Type: [AwsEcsTaskDefinitionVolumesHostDetails](API_AwsEcsTaskDefinitionVolumesHostDetails.md) object
Required: No

 ** Name **   <a name="securityhub-Type-AwsEcsTaskDefinitionVolumesDetails-Name"></a>
The name of the data volume.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEcsTaskDefinitionVolumesDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsTaskDefinitionVolumesDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsTaskDefinitionVolumesDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsTaskDefinitionVolumesDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
