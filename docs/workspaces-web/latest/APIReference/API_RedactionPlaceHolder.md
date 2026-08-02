---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_RedactionPlaceHolder.html
---

# RedactionPlaceHolder
<a name="API_RedactionPlaceHolder"></a>

The redaction placeholder that will replace the redacted text in session.

## Contents
<a name="API_RedactionPlaceHolder_Contents"></a>

 ** redactionPlaceHolderType **   <a name="workspacesweb-Type-RedactionPlaceHolder-redactionPlaceHolderType"></a>
The redaction placeholder type that will replace the redacted text in session.
Type: String
Valid Values: `CustomText`
Required: Yes

 ** redactionPlaceHolderText **   <a name="workspacesweb-Type-RedactionPlaceHolder-redactionPlaceHolderText"></a>
The redaction placeholder text that will replace the redacted text in session for the custom text redaction placeholder type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[*_\-\d\w]+`
Required: No

## See Also
<a name="API_RedactionPlaceHolder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/RedactionPlaceHolder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/RedactionPlaceHolder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/RedactionPlaceHolder)
