---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_Relay.html
---

# Relay
<a name="API_Relay"></a>

The relay resource that can be used as a rule to relay receiving emails to the destination relay server.

## Contents
<a name="API_Relay_Contents"></a>

 ** LastModifiedTimestamp **   <a name="sesmailmanager-Type-Relay-LastModifiedTimestamp"></a>
The timestamp of when the relay was last modified.
Type: Timestamp
Required: No

 ** RelayId **   <a name="sesmailmanager-Type-Relay-RelayId"></a>
The unique relay identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** RelayName **   <a name="sesmailmanager-Type-Relay-RelayName"></a>
The unique relay name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-_]+`
Required: No

## See Also
<a name="API_Relay_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/Relay)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/Relay)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/Relay)
