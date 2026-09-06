---
source_url: https://docs.aws.amazon.com/voiceid/latest/APIReference/API_RegistrationConfig.html
---

# RegistrationConfig
<a name="API_connect-voice-id_RegistrationConfig"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

The registration configuration to be used during the batch fraudster registration job.

## Contents
<a name="API_connect-voice-id_RegistrationConfig_Contents"></a>

 ** DuplicateRegistrationAction **   <a name="connect-Type-connect-voice-id_RegistrationConfig-DuplicateRegistrationAction"></a>
The action to take when a fraudster is identified as a duplicate. The default action is `SKIP`, which skips registering the duplicate fraudster. Setting the value to `REGISTER_AS_NEW` always registers a new fraudster into the specified domain.
Type: String
Valid Values: `SKIP | REGISTER_AS_NEW`
Required: No

 ** FraudsterSimilarityThreshold **   <a name="connect-Type-connect-voice-id_RegistrationConfig-FraudsterSimilarityThreshold"></a>
The minimum similarity score between the new and old fraudsters in order to consider the new fraudster a duplicate.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** WatchlistIds **   <a name="connect-Type-connect-voice-id_RegistrationConfig-WatchlistIds"></a>
The identifiers of watchlists that a fraudster is registered to. If a watchlist isn't provided, the fraudsters are registered to the default watchlist.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Fixed length of 22.
Pattern: `[a-zA-Z0-9]{22}`
Required: No

## See Also
<a name="API_connect-voice-id_RegistrationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/voice-id-2021-09-27/RegistrationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/voice-id-2021-09-27/RegistrationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/voice-id-2021-09-27/RegistrationConfig)
