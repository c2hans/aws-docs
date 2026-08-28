---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_LayoutItem.html
---

# LayoutItem
<a name="API_connect-customer-profiles_LayoutItem"></a>

The layout object that contains LayoutDefinitionName, Description, DisplayName, IsDefault, LayoutType, Tags, CreatedAt, LastUpdatedAt

## Contents
<a name="API_connect-customer-profiles_LayoutItem_Contents"></a>

 ** CreatedAt **   <a name="connect-Type-connect-customer-profiles_LayoutItem-CreatedAt"></a>
The timestamp of when the layout was created.
Type: Timestamp
Required: Yes

 ** Description **   <a name="connect-Type-connect-customer-profiles_LayoutItem-Description"></a>
The description of the layout
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

 ** DisplayName **   <a name="connect-Type-connect-customer-profiles_LayoutItem-DisplayName"></a>
The display name of the layout
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-\s]*$`
Required: Yes

 ** LastUpdatedAt **   <a name="connect-Type-connect-customer-profiles_LayoutItem-LastUpdatedAt"></a>
The timestamp of when the layout was most recently updated.
Type: Timestamp
Required: Yes

 ** LayoutDefinitionName **   <a name="connect-Type-connect-customer-profiles_LayoutItem-LayoutDefinitionName"></a>
The unique name of the layout.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** LayoutType **   <a name="connect-Type-connect-customer-profiles_LayoutItem-LayoutType"></a>
The type of layout that can be used to view data under customer profiles domain.
Type: String
Valid Values: `PROFILE_EXPLORER`
Required: Yes

 ** IsDefault **   <a name="connect-Type-connect-customer-profiles_LayoutItem-IsDefault"></a>
If set to true for a layout, this layout will be used by default to view data. If set to false, then layout will not be used by default but it can be used to view data by explicit selection on UI.
Type: Boolean
Required: No

 ** Tags **   <a name="connect-Type-connect-customer-profiles_LayoutItem-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_connect-customer-profiles_LayoutItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/LayoutItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/LayoutItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/LayoutItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
