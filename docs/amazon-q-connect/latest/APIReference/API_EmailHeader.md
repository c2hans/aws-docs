---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_EmailHeader.html
---

# EmailHeader
<a name="API_amazon-q-connect_EmailHeader"></a>

The email header to include in email messages.

## Contents
<a name="API_amazon-q-connect_EmailHeader_Contents"></a>

 ** name **   <a name="connect-Type-amazon-q-connect_EmailHeader-name"></a>
The name of the email header.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 126.
Pattern: `[!-9;-@A-~]+`
Required: No

 ** value **   <a name="connect-Type-amazon-q-connect_EmailHeader-value"></a>
The value of the email header.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 870.
Pattern: `.*[ -~]*.*`
Required: No

## See Also
<a name="API_amazon-q-connect_EmailHeader_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/EmailHeader)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/EmailHeader)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/EmailHeader)
