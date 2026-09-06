---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EmailAddressMetadata.html
---

# EmailAddressMetadata
<a name="API_EmailAddressMetadata"></a>

Contains information about an email address for a contact center.

## Contents
<a name="API_EmailAddressMetadata_Contents"></a>

 ** AliasConfigurations **   <a name="connect-Type-EmailAddressMetadata-AliasConfigurations"></a>
A list of alias configurations for this email address, showing which email addresses forward to this primary address. Each configuration contains the email address ID of an alias that forwards emails to this address.
Type: Array of [AliasConfiguration](API_AliasConfiguration.md) objects
Array Members: Maximum number of 1 item.
Required: No

 ** Description **   <a name="connect-Type-EmailAddressMetadata-Description"></a>
The description of the email address.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** DisplayName **   <a name="connect-Type-EmailAddressMetadata-DisplayName"></a>
The display name of email address.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** EmailAddress **   <a name="connect-Type-EmailAddressMetadata-EmailAddress"></a>
The email address, including the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^\s@]+@[^\s@]+\.[^\s@]+`
Required: No

 ** EmailAddressArn **   <a name="connect-Type-EmailAddressMetadata-EmailAddressArn"></a>
The Amazon Resource Name (ARN) of the email address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** EmailAddressId **   <a name="connect-Type-EmailAddressMetadata-EmailAddressId"></a>
The identifier of the email address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

## See Also
<a name="API_EmailAddressMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EmailAddressMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EmailAddressMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EmailAddressMetadata)
