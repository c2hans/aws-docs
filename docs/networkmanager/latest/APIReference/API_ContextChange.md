---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_ContextChange.html
---

# ContextChange
<a name="API_ContextChange"></a>

Describes a context entry that was added to or removed from a context store.

## Contents
<a name="API_ContextChange_Contents"></a>

 ** ChangeType **   <a name="networkmanager-Type-ContextChange-ChangeType"></a>
The type of change. The possible values are the following:
+  `ADDED`: The context entry was added to the context store.
+  `REMOVED`: The context entry was removed from the context store.
Type: String
Valid Values: `ADDED | REMOVED`
Required: No

 ** Context **   <a name="networkmanager-Type-ContextChange-Context"></a>
The context entry that was added or removed.
Type: [ContextEntry](API_ContextEntry.md) object
Required: No

## See Also
<a name="API_ContextChange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ContextChange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ContextChange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ContextChange)
