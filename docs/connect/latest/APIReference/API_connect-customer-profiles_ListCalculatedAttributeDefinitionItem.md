---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_ListCalculatedAttributeDefinitionItem.html
---

# ListCalculatedAttributeDefinitionItem
<a name="API_connect-customer-profiles_ListCalculatedAttributeDefinitionItem"></a>

The details of a single calculated attribute definition.

## Contents
<a name="API_connect-customer-profiles_ListCalculatedAttributeDefinitionItem_Contents"></a>

 ** CalculatedAttributeName **   <a name="connect-Type-connect-customer-profiles_ListCalculatedAttributeDefinitionItem-CalculatedAttributeName"></a>
The unique name of the calculated attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
Required: No

 ** CreatedAt **   <a name="connect-Type-connect-customer-profiles_ListCalculatedAttributeDefinitionItem-CreatedAt"></a>
The threshold for the calculated attribute.
Type: Timestamp
Required: No

 ** Description **   <a name="connect-Type-connect-customer-profiles_ListCalculatedAttributeDefinitionItem-Description"></a>
The threshold for the calculated attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** DisplayName **   <a name="connect-Type-connect-customer-profiles_ListCalculatedAttributeDefinitionItem-DisplayName"></a>
The display name of the calculated attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-\s]*$`
Required: No

 ** LastUpdatedAt **   <a name="connect-Type-connect-customer-profiles_ListCalculatedAttributeDefinitionItem-LastUpdatedAt"></a>
The timestamp of when the calculated attribute definition was most recently edited.
Type: Timestamp
Required: No

 ** Status **   <a name="connect-Type-connect-customer-profiles_ListCalculatedAttributeDefinitionItem-Status"></a>
Status of the Calculated Attribute creation (whether all historical data has been indexed.)
Type: String
Valid Values: `PREPARING | IN_PROGRESS | COMPLETED | FAILED`
Required: No

 ** Tags **   <a name="connect-Type-connect-customer-profiles_ListCalculatedAttributeDefinitionItem-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** UseHistoricalData **   <a name="connect-Type-connect-customer-profiles_ListCalculatedAttributeDefinitionItem-UseHistoricalData"></a>
Whether historical data ingested before the Calculated Attribute was created should be included in calculations.
Type: Boolean
Required: No

## See Also
<a name="API_connect-customer-profiles_ListCalculatedAttributeDefinitionItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ListCalculatedAttributeDefinitionItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ListCalculatedAttributeDefinitionItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ListCalculatedAttributeDefinitionItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
