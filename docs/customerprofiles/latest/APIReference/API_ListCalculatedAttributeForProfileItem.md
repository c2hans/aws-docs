---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListCalculatedAttributeForProfileItem.html
---

# ListCalculatedAttributeForProfileItem
<a name="API_connect-customer-profiles_ListCalculatedAttributeForProfileItem"></a>

The details of a single calculated attribute for a profile.

## Contents
<a name="API_connect-customer-profiles_ListCalculatedAttributeForProfileItem_Contents"></a>

 ** CalculatedAttributeName **   <a name="connect-Type-connect-customer-profiles_ListCalculatedAttributeForProfileItem-CalculatedAttributeName"></a>
The unique name of the calculated attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
Required: No

 ** DisplayName **   <a name="connect-Type-connect-customer-profiles_ListCalculatedAttributeForProfileItem-DisplayName"></a>
The display name of the calculated attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-\s]*$`
Required: No

 ** IsDataPartial **   <a name="connect-Type-connect-customer-profiles_ListCalculatedAttributeForProfileItem-IsDataPartial"></a>
Indicates whether the calculated attribute’s value is based on partial data. If data is partial, it is set to true.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** LastObjectTimestamp **   <a name="connect-Type-connect-customer-profiles_ListCalculatedAttributeForProfileItem-LastObjectTimestamp"></a>
The timestamp of the newest object included in the calculated attribute calculation.
Type: Timestamp
Required: No

 ** Value **   <a name="connect-Type-connect-customer-profiles_ListCalculatedAttributeForProfileItem-Value"></a>
The value of the calculated attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_connect-customer-profiles_ListCalculatedAttributeForProfileItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ListCalculatedAttributeForProfileItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ListCalculatedAttributeForProfileItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ListCalculatedAttributeForProfileItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
