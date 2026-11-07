---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_IterableFormItem.html
---

# IterableFormItem
<a name="API_IterableFormItem"></a>

A full iterable form item with its forms.

## Contents
<a name="API_IterableFormItem_Contents"></a>

 ** Attachments **   <a name="Glue-Type-IterableFormItem-Attachments"></a>
Additional attachments on the item for more context, keyed by attachment name.
Type: String to [AssetFormEntry](API_AssetFormEntry.md) object map
Required: No

 ** Forms **   <a name="Glue-Type-IterableFormItem-Forms"></a>
The forms on the item, keyed by form name.
Type: String to [AssetFormEntry](API_AssetFormEntry.md) object map
Required: No

 ** GlossaryTerms **   <a name="Glue-Type-IterableFormItem-GlossaryTerms"></a>
The identifiers of the glossary terms associated with the item.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** ItemId **   <a name="Glue-Type-IterableFormItem-ItemId"></a>
The unique identifier of the item.
Type: String
Required: No

 ** ItemName **   <a name="Glue-Type-IterableFormItem-ItemName"></a>
The name of the item.
Type: String
Required: No

## See Also
<a name="API_IterableFormItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/IterableFormItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/IterableFormItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/IterableFormItem)
