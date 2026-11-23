---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_CustomConfiguration.html
---

# CustomConfiguration

Associates blueprints with a project to produce custom structured output. A fallback blueprint can be supplied for documents that do not match a primary blueprint.

## Contents
<a name="API_CustomConfiguration_Contents"></a>

 ** Blueprints **   <a name="Textract-Type-CustomConfiguration-Blueprints"></a>
The blueprints used to extract custom structured output.
Type: Array of [BlueprintItem](API_BlueprintItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Required: Yes

 ** FallbackBlueprints **   <a name="Textract-Type-CustomConfiguration-FallbackBlueprints"></a>
The blueprint used when a document does not match any of the primary blueprints. Requires at least one blueprint in `Blueprints`.
Type: Array of [BlueprintItem](API_BlueprintItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

## See Also
<a name="API_CustomConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/CustomConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/CustomConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/CustomConfiguration)
