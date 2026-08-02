---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_VerificationInfo.html
---

# VerificationInfo
<a name="API_VerificationInfo"></a>

An object that contains additional information about the verification status for the identity.

## Contents
<a name="API_VerificationInfo_Contents"></a>

 ** ErrorType **   <a name="SES-Type-VerificationInfo-ErrorType"></a>
Provides the reason for the failure describing why Amazon SES was not able to successfully verify the identity. Below are the possible values:
+  `INVALID_VALUE` – Amazon SES was able to find the record, but the value contained within the record was invalid. Ensure you have published the correct values for the record.
+  `TYPE_NOT_FOUND` – The queried hostname exists but does not have the requested type of DNS record. Ensure that you have published the correct type of DNS record.
+  `HOST_NOT_FOUND` – The queried hostname does not exist or was not reachable at the time of the request. Ensure that you have published the required DNS record(s).
+  `SERVICE_ERROR` – A temporary issue is preventing Amazon SES from determining the verification status of the domain.
+  `DNS_SERVER_ERROR` – The DNS server encountered an issue and was unable to complete the request.
+  `REPLICATION_ACCESS_DENIED` – The verification failed because the user does not have the required permissions to replicate the DKIM key from the primary region. Ensure you have the necessary permissions in both primary and replica regions.
+  `REPLICATION_PRIMARY_NOT_FOUND` – The verification failed because no corresponding identity was found in the specified primary region. Ensure the identity exists in the primary region before attempting replication.
+  `REPLICATION_PRIMARY_BYO_DKIM_NOT_SUPPORTED` – The verification failed because the identity in the primary region is configured with Bring Your Own DKIM (BYODKIM). DKIM key replication is only supported for identities using Easy DKIM.
+  `REPLICATION_REPLICA_AS_PRIMARY_NOT_SUPPORTED` – The verification failed because the specified primary identity is a replica of another identity, and multi-level replication is not supported; the primary identity must be a non-replica identity.
+  `REPLICATION_PRIMARY_INVALID_REGION` – The verification failed due to an invalid primary region specified. Ensure you provide a valid AWS region where Amazon SES is available and different from the replica region.
Type: String
Valid Values: `SERVICE_ERROR | DNS_SERVER_ERROR | HOST_NOT_FOUND | TYPE_NOT_FOUND | INVALID_VALUE | REPLICATION_ACCESS_DENIED | REPLICATION_PRIMARY_NOT_FOUND | REPLICATION_PRIMARY_BYO_DKIM_NOT_SUPPORTED | REPLICATION_REPLICA_AS_PRIMARY_NOT_SUPPORTED | REPLICATION_PRIMARY_INVALID_REGION`
Required: No

 ** LastCheckedTimestamp **   <a name="SES-Type-VerificationInfo-LastCheckedTimestamp"></a>
The last time a verification attempt was made for this identity.
Type: Timestamp
Required: No

 ** LastSuccessTimestamp **   <a name="SES-Type-VerificationInfo-LastSuccessTimestamp"></a>
The last time a successful verification was made for this identity.
Type: Timestamp
Required: No

 ** SOARecord **   <a name="SES-Type-VerificationInfo-SOARecord"></a>
An object that contains information about the start of authority (SOA) record associated with the identity.
Type: [SOARecord](API_SOARecord.md) object
Required: No

## See Also
<a name="API_VerificationInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/VerificationInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/VerificationInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/VerificationInfo)
