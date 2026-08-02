---
source_url: https://docs.aws.amazon.com/voiceid/latest/APIReference/API_Watchlist.html
---

# Watchlist
<a name="API_connect-voice-id_Watchlist"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

Contains all the information about a watchlist.

## Contents
<a name="API_connect-voice-id_Watchlist_Contents"></a>

 ** CreatedAt **   <a name="connect-Type-connect-voice-id_Watchlist-CreatedAt"></a>
The timestamp of when the watchlist was created.
Type: Timestamp
Required: No

 ** DefaultWatchlist **   <a name="connect-Type-connect-voice-id_Watchlist-DefaultWatchlist"></a>
Whether the specified watchlist is the default watchlist of a domain.
Type: Boolean
Required: No

 ** Description **   <a name="connect-Type-connect-voice-id_Watchlist-Description"></a>
The description of the watchlist.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)`
Required: No

 ** DomainId **   <a name="connect-Type-connect-voice-id_Watchlist-DomainId"></a>
The identifier of the domain that contains the watchlist.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `[a-zA-Z0-9]{22}`
Required: No

 ** Name **   <a name="connect-Type-connect-voice-id_Watchlist-Name"></a>
The name for the watchlist.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: No

 ** UpdatedAt **   <a name="connect-Type-connect-voice-id_Watchlist-UpdatedAt"></a>
The timestamp of when the watchlist was updated.
Type: Timestamp
Required: No

 ** WatchlistId **   <a name="connect-Type-connect-voice-id_Watchlist-WatchlistId"></a>
The identifier of the watchlist.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `[a-zA-Z0-9]{22}`
Required: No

## See Also
<a name="API_connect-voice-id_Watchlist_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/voice-id-2021-09-27/Watchlist)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/voice-id-2021-09-27/Watchlist)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/voice-id-2021-09-27/Watchlist)
