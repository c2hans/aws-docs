---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_BlockedGuestUser.html
---

# BlockedGuestUser
<a name="API_BlockedGuestUser"></a>

Represents a guest user who has been blocked from accessing a Wickr network.

## Contents
<a name="API_BlockedGuestUser_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** admin **   <a name="wickr-Type-BlockedGuestUser-admin"></a>
The username of the administrator who blocked this guest user.
Type: String
Pattern: `[\S\s]*`
Required: Yes

 ** modified **   <a name="wickr-Type-BlockedGuestUser-modified"></a>
The timestamp when the guest user was blocked or last modified.
Type: String
Pattern: `[\S\s]*`
Required: Yes

 ** username **   <a name="wickr-Type-BlockedGuestUser-username"></a>
The username of the blocked guest user.
Type: String
Pattern: `[\S\s]*`
Required: Yes

 ** usernameHash **   <a name="wickr-Type-BlockedGuestUser-usernameHash"></a>
The unique username hash identifier for the blocked guest user.
Type: String
Pattern: `[\S\s]*`
Required: Yes

## See Also
<a name="API_BlockedGuestUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/BlockedGuestUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/BlockedGuestUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/BlockedGuestUser)
