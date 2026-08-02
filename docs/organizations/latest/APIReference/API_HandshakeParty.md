---
source_url: https://docs.aws.amazon.com/organizations/latest/APIReference/API_HandshakeParty.html
---

# HandshakeParty
<a name="API_HandshakeParty"></a>

Contains details for a participant in a handshake.

## Contents
<a name="API_HandshakeParty_Contents"></a>

 ** Id **   <a name="organizations-Type-HandshakeParty-Id"></a>
ID for the participant: Acccount ID, organization ID, or email address.
The [regex pattern](http://wikipedia.org/wiki/regex) for handshake ID string requires "h-" followed by from 8 to 32 lowercase letters or digits.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\s\S]*`
Required: Yes

 ** Type **   <a name="organizations-Type-HandshakeParty-Type"></a>
The type of ID for the participant.
Type: String
Valid Values: `ACCOUNT | ORGANIZATION | EMAIL`
Required: Yes

## See Also
<a name="API_HandshakeParty_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/organizations-2016-11-28/HandshakeParty)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/organizations-2016-11-28/HandshakeParty)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/organizations-2016-11-28/HandshakeParty)
