---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_AssetFormEntry.html
---

# AssetFormEntry
<a name="API_AssetFormEntry"></a>

A form on an asset, consisting of the form type identifier and its JSON content.

## Contents
<a name="API_AssetFormEntry_Contents"></a>

 ** Content **   <a name="Glue-Type-AssetFormEntry-Content"></a>
The JSON content of the form, conforming to the schema of the specified form type.
Type: String
Required: No

 ** FormTypeId **   <a name="Glue-Type-AssetFormEntry-FormTypeId"></a>
The identifier of the form type that defines this form's schema.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_AssetFormEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/AssetFormEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/AssetFormEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/AssetFormEntry)
