---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ContainerDetails.html
---

# ContainerDetails
<a name="API_ContainerDetails"></a>

Container details related to a finding.

## Contents
<a name="API_ContainerDetails_Contents"></a>

 ** ContainerRuntime **   <a name="securityhub-Type-ContainerDetails-ContainerRuntime"></a>
The runtime of the container.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ImageId **   <a name="securityhub-Type-ContainerDetails-ImageId"></a>
The identifier of the container image related to a finding.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ImageName **   <a name="securityhub-Type-ContainerDetails-ImageName"></a>
The name of the container image related to a finding.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LaunchedAt **   <a name="securityhub-Type-ContainerDetails-LaunchedAt"></a>
Indicates when the container started.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** Name **   <a name="securityhub-Type-ContainerDetails-Name"></a>
The name of the container related to a finding.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Privileged **   <a name="securityhub-Type-ContainerDetails-Privileged"></a>
When this parameter is `true`, the container is given elevated privileges on the host container instance (similar to the root user).
Type: Boolean
Required: No

 ** VolumeMounts **   <a name="securityhub-Type-ContainerDetails-VolumeMounts"></a>
Provides information about the mounting of a volume in a container.
Type: Array of [VolumeMount](API_VolumeMount.md) objects
Required: No

## See Also
<a name="API_ContainerDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ContainerDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ContainerDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ContainerDetails)
