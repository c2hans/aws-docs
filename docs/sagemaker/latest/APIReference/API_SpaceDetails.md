---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SpaceDetails.html
---

# SpaceDetails
<a name="API_SpaceDetails"></a>

The space's details.

## Contents
<a name="API_SpaceDetails_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-SpaceDetails-CreationTime"></a>
The creation time.
Type: Timestamp
Required: No

 ** DomainId **   <a name="sagemaker-Type-SpaceDetails-DomainId"></a>
The ID of the associated domain.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `d-(-*[a-z0-9]){1,61}`
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-SpaceDetails-LastModifiedTime"></a>
The last modified time.
Type: Timestamp
Required: No

 ** OwnershipSettingsSummary **   <a name="sagemaker-Type-SpaceDetails-OwnershipSettingsSummary"></a>
Specifies summary information about the ownership settings.
Type: [OwnershipSettingsSummary](API_OwnershipSettingsSummary.md) object
Required: No

 ** SpaceDisplayName **   <a name="sagemaker-Type-SpaceDetails-SpaceDisplayName"></a>
The name of the space that appears in the Studio UI.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `(?!\s*$).+`
Required: No

 ** SpaceName **   <a name="sagemaker-Type-SpaceDetails-SpaceName"></a>
The name of the space.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** SpaceSettingsSummary **   <a name="sagemaker-Type-SpaceDetails-SpaceSettingsSummary"></a>
Specifies summary information about the space settings.
Type: [SpaceSettingsSummary](API_SpaceSettingsSummary.md) object
Required: No

 ** SpaceSharingSettingsSummary **   <a name="sagemaker-Type-SpaceDetails-SpaceSharingSettingsSummary"></a>
Specifies summary information about the space sharing settings.
Type: [SpaceSharingSettingsSummary](API_SpaceSharingSettingsSummary.md) object
Required: No

 ** Status **   <a name="sagemaker-Type-SpaceDetails-Status"></a>
The status.
Type: String
Valid Values: `Deleting | Failed | InService | Pending | Updating | Update_Failed | Delete_Failed`
Required: No

## See Also
<a name="API_SpaceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/SpaceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/SpaceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/SpaceDetails)
