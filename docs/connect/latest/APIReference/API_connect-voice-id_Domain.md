---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-voice-id_Domain.html
---

# Domain
<a name="API_connect-voice-id_Domain"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

Contains all the information about a domain.

## Contents
<a name="API_connect-voice-id_Domain_Contents"></a>

 ** Arn **   <a name="connect-Type-connect-voice-id_Domain-Arn"></a>
The Amazon Resource Name (ARN) for the domain.
Type: String
Pattern: `arn:aws(-[^:]+)?:voiceid.+:[0-9]{12}:domain/[a-zA-Z0-9]{22}`
Required: No

 ** CreatedAt **   <a name="connect-Type-connect-voice-id_Domain-CreatedAt"></a>
The timestamp of when the domain was created.
Type: Timestamp
Required: No

 ** Description **   <a name="connect-Type-connect-voice-id_Domain-Description"></a>
The description of the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)`
Required: No

 ** DomainId **   <a name="connect-Type-connect-voice-id_Domain-DomainId"></a>
The identifier of the domain.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `[a-zA-Z0-9]{22}`
Required: No

 ** DomainStatus **   <a name="connect-Type-connect-voice-id_Domain-DomainStatus"></a>
The current status of the domain.
Type: String
Valid Values: `ACTIVE | PENDING | SUSPENDED`
Required: No

 ** Name **   <a name="connect-Type-connect-voice-id_Domain-Name"></a>
The name for the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: No

 ** ServerSideEncryptionConfiguration **   <a name="connect-Type-connect-voice-id_Domain-ServerSideEncryptionConfiguration"></a>
The server-side encryption configuration containing the KMS key identifier you want Voice ID to use to encrypt your data.
Type: [ServerSideEncryptionConfiguration](API_connect-voice-id_ServerSideEncryptionConfiguration.md) object
Required: No

 ** ServerSideEncryptionUpdateDetails **   <a name="connect-Type-connect-voice-id_Domain-ServerSideEncryptionUpdateDetails"></a>
Details about the most recent server-side encryption configuration update. When the server-side encryption configuration is changed, dependency on the old KMS key is removed through an asynchronous process. When this update is complete, the domain's data can only be accessed using the new KMS key.
Type: [ServerSideEncryptionUpdateDetails](API_connect-voice-id_ServerSideEncryptionUpdateDetails.md) object
Required: No

 ** UpdatedAt **   <a name="connect-Type-connect-voice-id_Domain-UpdatedAt"></a>
The timestamp of when the domain was last update.
Type: Timestamp
Required: No

 ** WatchlistDetails **   <a name="connect-Type-connect-voice-id_Domain-WatchlistDetails"></a>
The watchlist details of a domain. Contains the default watchlist ID of the domain.
Type: [WatchlistDetails](API_connect-voice-id_WatchlistDetails.md) object
Required: No

## See Also
<a name="API_connect-voice-id_Domain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/voice-id-2021-09-27/Domain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/voice-id-2021-09-27/Domain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/voice-id-2021-09-27/Domain)
