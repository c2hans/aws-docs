---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-voice-id_FraudsterSummary.html
---

# FraudsterSummary
<a name="API_connect-voice-id_FraudsterSummary"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

Contains a summary of information about a fraudster.

## Contents
<a name="API_connect-voice-id_FraudsterSummary_Contents"></a>

 ** CreatedAt **   <a name="connect-Type-connect-voice-id_FraudsterSummary-CreatedAt"></a>
The timestamp of when the fraudster summary was created.
Type: Timestamp
Required: No

 ** DomainId **   <a name="connect-Type-connect-voice-id_FraudsterSummary-DomainId"></a>
The identifier of the domain that contains the fraudster summary.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `[a-zA-Z0-9]{22}`
Required: No

 ** GeneratedFraudsterId **   <a name="connect-Type-connect-voice-id_FraudsterSummary-GeneratedFraudsterId"></a>
The service-generated identifier for the fraudster.
Type: String
Length Constraints: Fixed length of 25.
Pattern: `id#[a-zA-Z0-9]{22}`
Required: No

 ** WatchlistIds **   <a name="connect-Type-connect-voice-id_FraudsterSummary-WatchlistIds"></a>
The identifier of the watchlists the fraudster is a part of.
Type: Array of strings
Length Constraints: Fixed length of 22.
Pattern: `[a-zA-Z0-9]{22}`
Required: No

## See Also
<a name="API_connect-voice-id_FraudsterSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/voice-id-2021-09-27/FraudsterSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/voice-id-2021-09-27/FraudsterSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/voice-id-2021-09-27/FraudsterSummary)
