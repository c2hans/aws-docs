---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EmailAddressConfig.html
---

# EmailAddressConfig
<a name="API_EmailAddressConfig"></a>

Configuration object that specifies an email address to be associated with a queue. This configuration contains the identifier of the email address that should be linked to the queue for routing email contacts.

## Contents
<a name="API_EmailAddressConfig_Contents"></a>

 ** EmailAddressId **   <a name="connect-Type-EmailAddressConfig-EmailAddressId"></a>
The identifier of the email address that should be associated with the queue. This email address must already exist in the Connect Customer instance and will be used to route incoming email contacts to the specified queue.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## See Also
<a name="API_EmailAddressConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EmailAddressConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EmailAddressConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EmailAddressConfig)
