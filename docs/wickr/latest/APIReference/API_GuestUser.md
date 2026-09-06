---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_GuestUser.html
---

# GuestUser
<a name="API_GuestUser"></a>

Represents a guest user who has accessed the network from a federated Wickr network.

## Contents
<a name="API_GuestUser_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** billingPeriod **   <a name="wickr-Type-GuestUser-billingPeriod"></a>
The billing period when this guest user accessed the network (e.g., '2024-01').
Type: String
Pattern: `[\S\s]*`
Required: Yes

 ** username **   <a name="wickr-Type-GuestUser-username"></a>
The username of the guest user.
Type: String
Pattern: `[\S\s]*`
Required: Yes

 ** usernameHash **   <a name="wickr-Type-GuestUser-usernameHash"></a>
The unique username hash identifier for the guest user.
Type: String
Pattern: `[\S\s]*`
Required: Yes

## See Also
<a name="API_GuestUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/GuestUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/GuestUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/GuestUser)
