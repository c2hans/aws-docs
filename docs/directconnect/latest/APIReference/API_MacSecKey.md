---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_MacSecKey.html
---

# MacSecKey
<a name="API_MacSecKey"></a>

Information about the MAC Security (MACsec) secret key.

## Contents
<a name="API_MacSecKey_Contents"></a>

 ** ckn **   <a name="DX-Type-MacSecKey-ckn"></a>
The Connection Key Name (CKN) for the MAC Security secret key.
Type: String
Required: No

 ** secretARN **   <a name="DX-Type-MacSecKey-secretARN"></a>
The Amazon Resource Name (ARN) of the MAC Security (MACsec) secret key.
Type: String
Required: No

 ** startOn **   <a name="DX-Type-MacSecKey-startOn"></a>
The date that the MAC Security (MACsec) secret key takes effect. The value is displayed in UTC format.
Type: String
Required: No

 ** state **   <a name="DX-Type-MacSecKey-state"></a>
The state of the MAC Security (MACsec) secret key.
The possible values are:
+  `associating`: The MAC Security (MACsec) secret key is being validated and not yet associated with the connection or LAG.
+  `associated`: The MAC Security (MACsec) secret key is validated and associated with the connection or LAG.
+  `disassociating`: The MAC Security (MACsec) secret key is being disassociated from the connection or LAG
+  `disassociated`: The MAC Security (MACsec) secret key is no longer associated with the connection or LAG.
Type: String
Required: No

## See Also
<a name="API_MacSecKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/MacSecKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/MacSecKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/MacSecKey)
