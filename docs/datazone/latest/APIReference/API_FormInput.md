---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_FormInput.html
---

# FormInput
<a name="API_FormInput"></a>

The details of a metadata form.

## Contents
<a name="API_FormInput_Contents"></a>

 ** formName **   <a name="datazone-Type-FormInput-formName"></a>
The name of the metadata form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(?![0-9_])\w+$|^_\w*[a-zA-Z0-9]\w*`
Required: Yes

 ** content **   <a name="datazone-Type-FormInput-content"></a>
The content of the metadata form.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 300000.
Required: No

 ** typeIdentifier **   <a name="datazone-Type-FormInput-typeIdentifier"></a>
The ID of the metadata form type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 385.
Pattern: `(?!\.)[\w\.]*\w`
Required: No

 ** typeRevision **   <a name="datazone-Type-FormInput-typeRevision"></a>
The revision of the metadata form type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

## See Also
<a name="API_FormInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/FormInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/FormInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/FormInput)
