---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeBoostingConfiguration.html
---

# DocumentAttributeBoostingConfiguration
<a name="API_DocumentAttributeBoostingConfiguration"></a>

Provides information on boosting supported Amazon Q Business document attribute types. When an end user chat query matches document attributes that have been boosted, Amazon Q Business prioritizes generating responses from content that matches the boosted document attributes.

In version 2, boosting uses numeric values (ONE, TWO) to indicate priority tiers that establish clear hierarchical relationships between boosted attributes. This allows for more precise control over how different attributes influence search results.

**Note**
For `STRING` and `STRING_LIST` type document attributes to be used for boosting on the console and the API, they must be enabled for search using the [DocumentAttributeConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeConfiguration.html) object of the [UpdateIndex](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateIndex.html) API. If you haven't enabled searching on these attributes, you can't boost attributes of these data types on either the console or the API.

For more information on how boosting document attributes work in Amazon Q Business, see [Boosting using document attributes](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/metadata-boosting.html).

## Contents
<a name="API_DocumentAttributeBoostingConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** dateConfiguration **   <a name="qbusiness-Type-DocumentAttributeBoostingConfiguration-dateConfiguration"></a>
Provides information on boosting `DATE` type document attributes.
Version 2 assigns priority tiers to `DATE` attributes, establishing clear hierarchical relationships with other boosted attributes.
Type: [DateAttributeBoostingConfiguration](API_DateAttributeBoostingConfiguration.md) object
Required: No

 ** numberConfiguration **   <a name="qbusiness-Type-DocumentAttributeBoostingConfiguration-numberConfiguration"></a>
Provides information on boosting `NUMBER` type document attributes.
 `NUMBER` attributes are not supported when using `NativeIndexConfiguration` version 2, which focuses on `DATE` attributes for recency and `STRING` attributes for source prioritization.
Type: [NumberAttributeBoostingConfiguration](API_NumberAttributeBoostingConfiguration.md) object
Required: No

 ** stringConfiguration **   <a name="qbusiness-Type-DocumentAttributeBoostingConfiguration-stringConfiguration"></a>
Provides information on boosting `STRING` type document attributes.
Version 2 assigns priority tiers to `STRING` attributes, establishing clear hierarchical relationships with other boosted attributes.
Type: [StringAttributeBoostingConfiguration](API_StringAttributeBoostingConfiguration.md) object
Required: No

 ** stringListConfiguration **   <a name="qbusiness-Type-DocumentAttributeBoostingConfiguration-stringListConfiguration"></a>
Provides information on boosting `STRING_LIST` type document attributes.
 `STRING_LIST` attributes are not supported when using `NativeIndexConfiguration` version 2, which focuses on `DATE` attributes for recency and `STRING` attributes for source prioritization.
Type: [StringListAttributeBoostingConfiguration](API_StringListAttributeBoostingConfiguration.md) object
Required: No

## See Also
<a name="API_DocumentAttributeBoostingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/DocumentAttributeBoostingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/DocumentAttributeBoostingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/DocumentAttributeBoostingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
