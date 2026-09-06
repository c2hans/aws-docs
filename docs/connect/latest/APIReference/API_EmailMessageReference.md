---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EmailMessageReference.html
---

# EmailMessageReference
<a name="API_EmailMessageReference"></a>

Information about the reference when the referenceType is `EMAIL_MESSAGE`. Otherwise, null.

## Contents
<a name="API_EmailMessageReference_Contents"></a>

 ** Arn **   <a name="connect-Type-EmailMessageReference-Arn"></a>
The Amazon Resource Name (ARN) of the email message reference
Type: String
Length Constraints: Minimum length of 20. Maximum length of 256.
Pattern: `^[-:/A-Za-z0-9]+`
Required: No

 ** Name **   <a name="connect-Type-EmailMessageReference-Name"></a>
The name of the email message reference
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## See Also
<a name="API_EmailMessageReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EmailMessageReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EmailMessageReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EmailMessageReference)
