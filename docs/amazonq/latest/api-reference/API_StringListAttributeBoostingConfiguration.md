---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_StringListAttributeBoostingConfiguration.html
---

# StringListAttributeBoostingConfiguration
<a name="API_StringListAttributeBoostingConfiguration"></a>

Provides information on boosting `STRING_LIST` type document attributes.

In the current boosting implementation, boosting focuses primarily on `DATE` attributes for recency and `STRING` attributes for source prioritization. `STRING_LIST` attributes can serve as additional boosting factors when needed, but are not supported when using `NativeIndexConfiguration` version 2.

**Note**
For `STRING` and `STRING_LIST` type document attributes to be used for boosting on the console and the API, they must be enabled for search using the [DocumentAttributeConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeConfiguration.html) object of the [UpdateIndex](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateIndex.html) API. If you haven't enabled searching on these attributes, you can't boost attributes of these data types on either the console or the API.

For more information on how boosting document attributes work in Amazon Q Business, see [Boosting using document attributes](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/metadata-boosting.html).

## Contents
<a name="API_StringListAttributeBoostingConfiguration_Contents"></a>

 ** boostingLevel **   <a name="qbusiness-Type-StringListAttributeBoostingConfiguration-boostingLevel"></a>
Specifies the priority of boosted document attributes in relation to other boosted attributes. This parameter determines how strongly the attribute influences document ranking in search results. `STRING_LIST` attributes can serve as additional boosting factors when needed, but are not supported when using `NativeIndexConfiguration` version 2.
Type: String
Valid Values: `NONE | LOW | MEDIUM | HIGH | VERY_HIGH | ONE | TWO`
Required: Yes

## See Also
<a name="API_StringListAttributeBoostingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/StringListAttributeBoostingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/StringListAttributeBoostingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/StringListAttributeBoostingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
