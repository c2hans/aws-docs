---
source_url: https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_Summary.html
---

# Summary
<a name="API_Summary"></a>

A count of noncompliant resources.

## Contents
<a name="API_Summary_Contents"></a>

 ** LastUpdated **   <a name="resourcegrouptagging-Type-Summary-LastUpdated"></a>
The timestamp that shows when this summary was generated in this Region.
Type: String
Required: No

 ** NonCompliantResources **   <a name="resourcegrouptagging-Type-Summary-NonCompliantResources"></a>
The count of noncompliant resources.
Type: Long
Required: No

 ** Region **   <a name="resourcegrouptagging-Type-Summary-Region"></a>
The AWS Region that the summary applies to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** ResourceType **   <a name="resourcegrouptagging-Type-Summary-ResourceType"></a>
The AWS resource type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** TargetId **   <a name="resourcegrouptagging-Type-Summary-TargetId"></a>
The account identifier or the root identifier of the organization. If you don't know the root ID, you can call the AWS Organizations [ListRoots](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListRoots.html) API.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 68.
Pattern: `[a-zA-Z0-9-]*`
Required: No

 ** TargetIdType **   <a name="resourcegrouptagging-Type-Summary-TargetIdType"></a>
Whether the target is an account, an OU, or the organization root.
Type: String
Valid Values: `ACCOUNT | OU | ROOT`
Required: No

## See Also
<a name="API_Summary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resourcegroupstaggingapi-2017-01-26/Summary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resourcegroupstaggingapi-2017-01-26/Summary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resourcegroupstaggingapi-2017-01-26/Summary)
