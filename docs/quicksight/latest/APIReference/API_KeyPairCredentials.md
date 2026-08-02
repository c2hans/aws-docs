---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_KeyPairCredentials.html
---

# KeyPairCredentials
<a name="API_KeyPairCredentials"></a>

The combination of username, private key and passphrase that are used as credentials.

## Contents
<a name="API_KeyPairCredentials_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** KeyPairUsername **   <a name="QS-Type-KeyPairCredentials-KeyPairUsername"></a>
Username
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** PrivateKey **   <a name="QS-Type-KeyPairCredentials-PrivateKey"></a>
PrivateKey
Type: String
Length Constraints: Minimum length of 1600. Maximum length of 8000.
Pattern: `^-{5}BEGIN (ENCRYPTED )?PRIVATE KEY-{5}\u000D?\u000A([A-Za-z0-9/+]{64}\u000D?\u000A)*[A-Za-z0-9/+]{1,64}={0,2}\u000D?\u000A-{5}END (ENCRYPTED )?PRIVATE KEY-{5}(\u000D?\u000A)?$`
Required: Yes

 ** PrivateKeyPassphrase **   <a name="QS-Type-KeyPairCredentials-PrivateKeyPassphrase"></a>
PrivateKeyPassphrase
Type: String
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_KeyPairCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/KeyPairCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/KeyPairCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/KeyPairCredentials)
