---
source_url: https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_RequiredTag.html
---

# RequiredTag
<a name="API_RequiredTag"></a>

Information that describes the required tags for a given resource type.

## Contents
<a name="API_RequiredTag_Contents"></a>

 ** CloudFormationResourceTypes **   <a name="resourcegrouptagging-Type-RequiredTag-CloudFormationResourceTypes"></a>
Describes the CloudFormation resource type assigned the required tag keys.
Type: Array of strings
Required: No

 ** ReportingTagKeys **   <a name="resourcegrouptagging-Type-RequiredTag-ReportingTagKeys"></a>
These tag keys are marked as `required` in the `report_required_tag_for` block of the effective tag policy.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\s\S]*`
Required: No

 ** ResourceType **   <a name="resourcegrouptagging-Type-RequiredTag-ResourceType"></a>
Describes the resource type for the required tag keys.
Type: String
Required: No

## See Also
<a name="API_RequiredTag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resourcegroupstaggingapi-2017-01-26/RequiredTag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resourcegroupstaggingapi-2017-01-26/RequiredTag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resourcegroupstaggingapi-2017-01-26/RequiredTag)
