---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_AcceptorContact.html
---

# AcceptorContact

The contact information of the acceptor.

## Contents
<a name="API_marketplace-agreements_AcceptorContact_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** companyName **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AcceptorContact-companyName"></a>
The name of the company that the acceptor contact represents.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(.)+`
Required: Yes

 ** countryCode **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AcceptorContact-countryCode"></a>
The ISO-3166 two-letter country code for the acceptor contact.
Type: String
Pattern: `[A-Z]{2}`
Required: Yes

 ** emailAddress **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AcceptorContact-emailAddress"></a>
The email address of the acceptor contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}`
Required: Yes

 ** firstName **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AcceptorContact-firstName"></a>
The first name of the acceptor contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `(.)+`
Required: Yes

 ** lastName **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AcceptorContact-lastName"></a>
The last name of the acceptor contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `(.)+`
Required: Yes

## See Also
<a name="API_marketplace-agreements_AcceptorContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/AcceptorContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/AcceptorContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/AcceptorContact)
