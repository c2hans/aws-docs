---
source_url: https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_Item.html
---

# Item
<a name="API_UBS_Item"></a>

Represents item metadata added to an Items dataset using the `PutItems` API. For more information see [Importing items individually](https://docs.aws.amazon.com/personalize/latest/dg/importing-items.html).

## Contents
<a name="API_UBS_Item_Contents"></a>

 ** itemId **   <a name="personalize-Type-UBS_Item-itemId"></a>
The ID associated with the item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** properties **   <a name="personalize-Type-UBS_Item-properties"></a>
A string map of item-specific metadata. Each element in the map consists of a key-value pair. For example, `{"numberOfRatings": "12"}`.
The keys use camel case names that match the fields in the schema for the Items dataset. In the previous example, the `numberOfRatings` matches the 'NUMBER\_OF\_RATINGS' field defined in the Items schema. For categorical string data, to include multiple categories for a single item, separate each category with a pipe separator (`|`). For example, `\"Horror|Action\"`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32000.
Required: No

## See Also
<a name="API_UBS_Item_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-events-2018-03-22/Item)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-events-2018-03-22/Item)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-events-2018-03-22/Item)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Personalize. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query personalize` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
