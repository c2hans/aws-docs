---
source_url: https://docs.aws.amazon.com/voiceid/latest/APIReference/API_Fraudster.html
---

# Fraudster
<a name="API_connect-voice-id_Fraudster"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

Contains all the information about a fraudster.

## Contents
<a name="API_connect-voice-id_Fraudster_Contents"></a>

 ** CreatedAt **   <a name="connect-Type-connect-voice-id_Fraudster-CreatedAt"></a>
The timestamp of when Voice ID identified the fraudster.
Type: Timestamp
Required: No

 ** DomainId **   <a name="connect-Type-connect-voice-id_Fraudster-DomainId"></a>
The identifier of the domain that contains the fraudster.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `[a-zA-Z0-9]{22}`
Required: No

 ** GeneratedFraudsterId **   <a name="connect-Type-connect-voice-id_Fraudster-GeneratedFraudsterId"></a>
The service-generated identifier for the fraudster.
Type: String
Length Constraints: Fixed length of 25.
Pattern: `id#[a-zA-Z0-9]{22}`
Required: No

 ** WatchlistIds **   <a name="connect-Type-connect-voice-id_Fraudster-WatchlistIds"></a>
The identifier of the watchlists the fraudster is a part of.
Type: Array of strings
Length Constraints: Fixed length of 22.
Pattern: `[a-zA-Z0-9]{22}`
Required: No

## See Also
<a name="API_connect-voice-id_Fraudster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/voice-id-2021-09-27/Fraudster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/voice-id-2021-09-27/Fraudster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/voice-id-2021-09-27/Fraudster)
