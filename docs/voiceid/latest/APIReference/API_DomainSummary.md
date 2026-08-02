---
source_url: https://docs.aws.amazon.com/voiceid/latest/APIReference/API_DomainSummary.html
---

# DomainSummary
<a name="API_connect-voice-id_DomainSummary"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

Contains a summary of information about a domain.

## Contents
<a name="API_connect-voice-id_DomainSummary_Contents"></a>

 ** Arn **   <a name="connect-Type-connect-voice-id_DomainSummary-Arn"></a>
The Amazon Resource Name (ARN) for the domain.
Type: String
Pattern: `arn:aws(-[^:]+)?:voiceid.+:[0-9]{12}:domain/[a-zA-Z0-9]{22}`
Required: No

 ** CreatedAt **   <a name="connect-Type-connect-voice-id_DomainSummary-CreatedAt"></a>
The timestamp of when the domain was created.
Type: Timestamp
Required: No

 ** Description **   <a name="connect-Type-connect-voice-id_DomainSummary-Description"></a>
The description of the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)`
Required: No

 ** DomainId **   <a name="connect-Type-connect-voice-id_DomainSummary-DomainId"></a>
The identifier of the domain.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `[a-zA-Z0-9]{22}`
Required: No

 ** DomainStatus **   <a name="connect-Type-connect-voice-id_DomainSummary-DomainStatus"></a>
The current status of the domain.
Type: String
Valid Values: `ACTIVE | PENDING | SUSPENDED`
Required: No

 ** Name **   <a name="connect-Type-connect-voice-id_DomainSummary-Name"></a>
The client-provided name for the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: No

 ** ServerSideEncryptionConfiguration **   <a name="connect-Type-connect-voice-id_DomainSummary-ServerSideEncryptionConfiguration"></a>
The server-side encryption configuration containing the KMS key identifier you want Voice ID to use to encrypt your data.
Type: [ServerSideEncryptionConfiguration](API_connect-voice-id_ServerSideEncryptionConfiguration.md) object
Required: No

 ** ServerSideEncryptionUpdateDetails **   <a name="connect-Type-connect-voice-id_DomainSummary-ServerSideEncryptionUpdateDetails"></a>
Details about the most recent server-side encryption configuration update. When the server-side encryption configuration is changed, dependency on the old KMS key is removed through an asynchronous process. When this update is complete, the domain's data can only be accessed using the new KMS key.
Type: [ServerSideEncryptionUpdateDetails](API_connect-voice-id_ServerSideEncryptionUpdateDetails.md) object
Required: No

 ** UpdatedAt **   <a name="connect-Type-connect-voice-id_DomainSummary-UpdatedAt"></a>
The timestamp of when the domain was last updated.
Type: Timestamp
Required: No

 ** WatchlistDetails **   <a name="connect-Type-connect-voice-id_DomainSummary-WatchlistDetails"></a>
Provides information about `watchlistDetails` and `DefaultWatchlistID`.
Type: [WatchlistDetails](API_connect-voice-id_WatchlistDetails.md) object
Required: No

## See Also
<a name="API_connect-voice-id_DomainSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/voice-id-2021-09-27/DomainSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/voice-id-2021-09-27/DomainSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/voice-id-2021-09-27/DomainSummary)
