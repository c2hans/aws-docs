---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_MissionProfileListItem.html
---

# MissionProfileListItem
<a name="API_MissionProfileListItem"></a>

Item in a list of mission profiles.

## Contents
<a name="API_MissionProfileListItem_Contents"></a>

 ** missionProfileArn **   <a name="groundstation-Type-MissionProfileListItem-missionProfileArn"></a>
ARN of a mission profile.
Type: String
Length Constraints: Minimum length of 89. Maximum length of 138.
Pattern: `arn:aws:groundstation:[-a-z0-9]{1,50}:[0-9]{12}:mission-profile/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** missionProfileId **   <a name="groundstation-Type-MissionProfileListItem-missionProfileId"></a>
UUID of a mission profile.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** name **   <a name="groundstation-Type-MissionProfileListItem-name"></a>
Name of a mission profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[ a-zA-Z0-9_:-]{1,256}`
Required: No

 ** region **   <a name="groundstation-Type-MissionProfileListItem-region"></a>
Region of a mission profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w-]+`
Required: No

## See Also
<a name="API_MissionProfileListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/MissionProfileListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/MissionProfileListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/MissionProfileListItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
