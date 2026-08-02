---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SecurityKey.html
---

# SecurityKey
<a name="API_SecurityKey"></a>

Configuration information of the security key.

## Contents
<a name="API_SecurityKey_Contents"></a>

 ** AssociationId **   <a name="connect-Type-SecurityKey-AssociationId"></a>
The existing association identifier that uniquely identifies the resource type and storage config for the given instance ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** CreationTime **   <a name="connect-Type-SecurityKey-CreationTime"></a>
When the security key was created.
Type: Timestamp
Required: No

 ** Key **   <a name="connect-Type-SecurityKey-Key"></a>
The key of the security key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_SecurityKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SecurityKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SecurityKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SecurityKey)
