---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_LatestRevokeRequest.html
---

# LatestRevokeRequest
<a name="API_LatestRevokeRequest"></a>

Contains information about the latest request to revoke access to a backup vault.

## Contents
<a name="API_LatestRevokeRequest_Contents"></a>

 ** ExpiryDate **   <a name="Backup-Type-LatestRevokeRequest-ExpiryDate"></a>
The date and time when the revoke request will expire.
Type: Timestamp
Required: No

 ** InitiationDate **   <a name="Backup-Type-LatestRevokeRequest-InitiationDate"></a>
The date and time when the revoke request was initiated.
Type: Timestamp
Required: No

 ** MpaSessionArn **   <a name="Backup-Type-LatestRevokeRequest-MpaSessionArn"></a>
The ARN of the MPA session associated with this revoke request.
Type: String
Required: No

 ** Status **   <a name="Backup-Type-LatestRevokeRequest-Status"></a>
The current status of the revoke request.
Type: String
Valid Values: `PENDING | FAILED`
Required: No

 ** StatusMessage **   <a name="Backup-Type-LatestRevokeRequest-StatusMessage"></a>
A message describing the current status of the revoke request.
Type: String
Required: No

## See Also
<a name="API_LatestRevokeRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/LatestRevokeRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/LatestRevokeRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/LatestRevokeRequest)
