---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_SegmentDefinitionItem.html
---

# SegmentDefinitionItem
<a name="API_connect-customer-profiles_SegmentDefinitionItem"></a>

Object holding the segment definition fields.

## Contents
<a name="API_connect-customer-profiles_SegmentDefinitionItem_Contents"></a>

 ** CreatedAt **   <a name="connect-Type-connect-customer-profiles_SegmentDefinitionItem-CreatedAt"></a>
When the segment definition was created.
Type: Timestamp
Required: No

 ** Description **   <a name="connect-Type-connect-customer-profiles_SegmentDefinitionItem-Description"></a>
The description of the segment definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4000.
Required: No

 ** DisplayName **   <a name="connect-Type-connect-customer-profiles_SegmentDefinitionItem-DisplayName"></a>
Display name of the segment definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** SegmentDefinitionArn **   <a name="connect-Type-connect-customer-profiles_SegmentDefinitionItem-SegmentDefinitionArn"></a>
The arn of the segment definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** SegmentDefinitionName **   <a name="connect-Type-connect-customer-profiles_SegmentDefinitionItem-SegmentDefinitionName"></a>
Name of the segment definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: No

 ** SegmentType **   <a name="connect-Type-connect-customer-profiles_SegmentDefinitionItem-SegmentType"></a>
The segment type.
 Classic : Segments created using traditional SegmentGroup structure
 Enhanced : Segments created using SQL queries
Type: String
Valid Values: `CLASSIC | ENHANCED`
Required: No

 ** Tags **   <a name="connect-Type-connect-customer-profiles_SegmentDefinitionItem-Tags"></a>
The tags belonging to the segment definition.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_connect-customer-profiles_SegmentDefinitionItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/SegmentDefinitionItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/SegmentDefinitionItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/SegmentDefinitionItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
