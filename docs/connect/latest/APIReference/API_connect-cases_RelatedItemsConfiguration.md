---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_RelatedItemsConfiguration.html
---

# RelatedItemsConfiguration
<a name="API_connect-cases_RelatedItemsConfiguration"></a>

Specifies which types of related items to move from the secondary case to the primary case when you merge cases. Moved related items keep their related item ID, creator, association time, and tags.

## Contents
<a name="API_connect-cases_RelatedItemsConfiguration_Contents"></a>

 ** comment **   <a name="connect-Type-connect-cases_RelatedItemsConfiguration-comment"></a>
Whether to move Comment related items to the primary case.
Type: Boolean
Required: No

 ** connectCase **   <a name="connect-Type-connect-cases_RelatedItemsConfiguration-connectCase"></a>
Whether to move Case related items to the primary case. If the primary case already links to the same case, the secondary case's link is removed instead of moved.
Type: Boolean
Required: No

 ** contact **   <a name="connect-Type-connect-cases_RelatedItemsConfiguration-contact"></a>
Whether to move Contact related items to the primary case. If the same contact is related to both cases, the primary case keeps its related item and gets any tag keys that only the secondary case's related item has.
Type: Boolean
Required: No

 ** custom **   <a name="connect-Type-connect-cases_RelatedItemsConfiguration-custom"></a>
Whether to move Custom related items to the primary case.
Type: Boolean
Required: No

## See Also
<a name="API_connect-cases_RelatedItemsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/RelatedItemsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/RelatedItemsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/RelatedItemsConfiguration)
