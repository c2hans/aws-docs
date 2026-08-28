---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetails.html
---

# AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetails
<a name="API_AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetails"></a>

Information about a Docker volume.

## Contents
<a name="API_AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetails_Contents"></a>

 ** Autoprovision **   <a name="securityhub-Type-AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetails-Autoprovision"></a>
Whether to create the Docker volume automatically if it does not already exist.
Type: Boolean
Required: No

 ** Driver **   <a name="securityhub-Type-AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetails-Driver"></a>
The Docker volume driver to use.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DriverOpts **   <a name="securityhub-Type-AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetails-DriverOpts"></a>
A map of Docker driver-specific options that are passed through.
Type: String to string map
Key Pattern: `.*\S.*`
Value Pattern: `.*\S.*`
Required: No

 ** Labels **   <a name="securityhub-Type-AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetails-Labels"></a>
Custom metadata to add to the Docker volume.
Type: String to string map
Key Pattern: `.*\S.*`
Value Pattern: `.*\S.*`
Required: No

 ** Scope **   <a name="securityhub-Type-AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetails-Scope"></a>
The scope for the Docker volume that determines its lifecycle. Docker volumes that are scoped to a task are provisioned automatically when the task starts and destroyed when the task stops. Docker volumes that are shared persist after the task stops. Valid values are `shared` or `task`.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
