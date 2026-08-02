---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ContainerFindingResource.html
---

# ContainerFindingResource
<a name="API_ContainerFindingResource"></a>

Contains information about container resources involved in a GuardDuty finding. This structure provides details about containers that were identified as part of suspicious or malicious activity.

## Contents
<a name="API_ContainerFindingResource_Contents"></a>

 ** image **   <a name="guardduty-Type-ContainerFindingResource-image"></a>
The container image information, including the image name and tag used to run the container that was involved in the finding.
Type: String
Required: Yes

 ** imageUid **   <a name="guardduty-Type-ContainerFindingResource-imageUid"></a>
The unique ID associated with the container image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_ContainerFindingResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ContainerFindingResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ContainerFindingResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ContainerFindingResource)
