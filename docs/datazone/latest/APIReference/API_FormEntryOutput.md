---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_FormEntryOutput.html
---

# FormEntryOutput
<a name="API_FormEntryOutput"></a>

The details of the form entry.

## Contents
<a name="API_FormEntryOutput_Contents"></a>

 ** typeName **   <a name="datazone-Type-FormEntryOutput-typeName"></a>
The name of the type of the form entry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(amazon.datazone.)?(?![0-9_])\w+$|^_\w*[a-zA-Z0-9]\w*`
Required: Yes

 ** typeRevision **   <a name="datazone-Type-FormEntryOutput-typeRevision"></a>
The type revision of the form entry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** required **   <a name="datazone-Type-FormEntryOutput-required"></a>
Specifies whether a form entry is required.
Type: Boolean
Required: No

## See Also
<a name="API_FormEntryOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/FormEntryOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/FormEntryOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/FormEntryOutput)
