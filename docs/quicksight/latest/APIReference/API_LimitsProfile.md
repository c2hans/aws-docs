---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_LimitsProfile.html
---

# LimitsProfile
<a name="API_LimitsProfile"></a>

A limits profile that defines resource usage limits for Amazon Quick Sight users. Limits profiles can be assigned to users, groups, or roles to control resource consumption.

## Contents
<a name="API_LimitsProfile_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** accountId **   <a name="QS-Type-LimitsProfile-accountId"></a>
The ID of the AWS account that contains the limits profile.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** arn **   <a name="QS-Type-LimitsProfile-arn"></a>
The Amazon Resource Name (ARN) of the limits profile.
Type: String
Required: Yes

 ** createdAt **   <a name="QS-Type-LimitsProfile-createdAt"></a>
The date and time that the limits profile was created.
Type: Timestamp
Required: Yes

 ** profileId **   <a name="QS-Type-LimitsProfile-profileId"></a>
The unique identifier for the limits profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `lp-[a-f0-9-]+`
Required: Yes

 ** profileName **   <a name="QS-Type-LimitsProfile-profileName"></a>
The display name of the limits profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** resourceLimits **   <a name="QS-Type-LimitsProfile-resourceLimits"></a>
A map of resource types to their limit values.
Type: String to [ProfileLimitValue](API_ProfileLimitValue.md) object map
Valid Keys: `INDEX_STORAGE | AGENT_HOURS`
Required: Yes

 ** updatedAt **   <a name="QS-Type-LimitsProfile-updatedAt"></a>
The date and time that the limits profile was last updated.
Type: Timestamp
Required: Yes

 ** description **   <a name="QS-Type-LimitsProfile-description"></a>
The description of the limits profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_LimitsProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/LimitsProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/LimitsProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/LimitsProfile)
