---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateClusterSoftwareInstanceGroupSpecification.html
---

# UpdateClusterSoftwareInstanceGroupSpecification
<a name="API_UpdateClusterSoftwareInstanceGroupSpecification"></a>

The configuration that describes specifications of the instance groups to update.

## Contents
<a name="API_UpdateClusterSoftwareInstanceGroupSpecification_Contents"></a>

 ** InstanceGroupName **   <a name="sagemaker-Type-UpdateClusterSoftwareInstanceGroupSpecification-InstanceGroupName"></a>
The name of the instance group to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

 ** ImageReleaseVersion **   <a name="sagemaker-Type-UpdateClusterSoftwareInstanceGroupSpecification-ImageReleaseVersion"></a>
The version of the HyperPod-managed AMI to update to for the instance group. Uses semantic versioning in the format `MAJOR.MINOR.PATCH`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[0-9]+\.[0-9]+\.[0-9]+`
Required: No

## See Also
<a name="API_UpdateClusterSoftwareInstanceGroupSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateClusterSoftwareInstanceGroupSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateClusterSoftwareInstanceGroupSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateClusterSoftwareInstanceGroupSpecification)
