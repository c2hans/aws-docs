---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_NumberAttributeBoostingConfiguration.html
---

# NumberAttributeBoostingConfiguration
<a name="API_NumberAttributeBoostingConfiguration"></a>

Provides information on boosting `NUMBER` type document attributes.

In the current boosting implementation, boosting focuses primarily on `DATE` attributes for recency and `STRING` attributes for source prioritization. `NUMBER` attributes can serve as additional boosting factors when needed, but are not supported when using `NativeIndexConfiguration` version 2.

For more information on how boosting document attributes work in Amazon Q Business, see [Boosting using document attributes](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/metadata-boosting.html).

## Contents
<a name="API_NumberAttributeBoostingConfiguration_Contents"></a>

 ** boostingLevel **   <a name="qbusiness-Type-NumberAttributeBoostingConfiguration-boostingLevel"></a>
Specifies the priority of boosted document attributes in relation to other boosted attributes. This parameter determines how strongly the attribute influences document ranking in search results. `NUMBER` attributes can serve as additional boosting factors when needed, but are not supported when using `NativeIndexConfiguration` version 2.
Type: String
Valid Values: `NONE | LOW | MEDIUM | HIGH | VERY_HIGH | ONE | TWO`
Required: Yes

 ** boostingType **   <a name="qbusiness-Type-NumberAttributeBoostingConfiguration-boostingType"></a>
Specifies whether higher or lower numeric values should be prioritized when boosting. Valid values are ASCENDING (higher numbers are more important) and DESCENDING (lower numbers are more important).
Type: String
Valid Values: `PRIORITIZE_LARGER_VALUES | PRIORITIZE_SMALLER_VALUES`
Required: No

## See Also
<a name="API_NumberAttributeBoostingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/NumberAttributeBoostingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/NumberAttributeBoostingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/NumberAttributeBoostingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
