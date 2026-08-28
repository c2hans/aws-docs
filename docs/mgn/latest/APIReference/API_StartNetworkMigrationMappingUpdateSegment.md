---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_StartNetworkMigrationMappingUpdateSegment.html
---

# StartNetworkMigrationMappingUpdateSegment
<a name="API_StartNetworkMigrationMappingUpdateSegment"></a>

A segment update to apply during a mapping update operation.

## Contents
<a name="API_StartNetworkMigrationMappingUpdateSegment_Contents"></a>

 ** segmentID **   <a name="mgn-Type-StartNetworkMigrationMappingUpdateSegment-segmentID"></a>
The ID of the segment to update.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** scopeTags **   <a name="mgn-Type-StartNetworkMigrationMappingUpdateSegment-scopeTags"></a>
The updated scope tags for the segment.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 40 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z0-9\s+\-=._:/@]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[a-zA-Z0-9\s+\-=._:/@]*`
Required: No

 ** targetAccount **   <a name="mgn-Type-StartNetworkMigrationMappingUpdateSegment-targetAccount"></a>
The updated target AWS account for the segment.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

## See Also
<a name="API_StartNetworkMigrationMappingUpdateSegment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/StartNetworkMigrationMappingUpdateSegment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/StartNetworkMigrationMappingUpdateSegment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/StartNetworkMigrationMappingUpdateSegment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
