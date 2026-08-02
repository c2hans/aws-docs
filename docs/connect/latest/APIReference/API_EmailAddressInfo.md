---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EmailAddressInfo.html
---

# EmailAddressInfo
<a name="API_EmailAddressInfo"></a>

Contains information about a source or destination email address.

## Contents
<a name="API_EmailAddressInfo_Contents"></a>

 ** EmailAddress **   <a name="connect-Type-EmailAddressInfo-EmailAddress"></a>
The email address, including the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^\s@]+@[^\s@]+\.[^\s@]+`
Required: Yes

 ** DisplayName **   <a name="connect-Type-EmailAddressInfo-DisplayName"></a>
The display name of email address.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_EmailAddressInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EmailAddressInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EmailAddressInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EmailAddressInfo)
