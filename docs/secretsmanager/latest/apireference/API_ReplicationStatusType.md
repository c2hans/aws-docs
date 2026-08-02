---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ReplicationStatusType.html
---

# ReplicationStatusType
<a name="API_ReplicationStatusType"></a>

A replication object consisting of a `RegionReplicationStatus` object and includes a Region, KMSKeyId, status, and status message.

## Contents
<a name="API_ReplicationStatusType_Contents"></a>

 ** KmsKeyId **   <a name="SecretsManager-Type-ReplicationStatusType-KmsKeyId"></a>
Can be an `ARN`, `Key ID`, or `Alias`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** LastAccessedDate **   <a name="SecretsManager-Type-ReplicationStatusType-LastAccessedDate"></a>
The date that the secret was last accessed in the Region. This field is omitted if the secret has never been retrieved in the Region.
Type: Timestamp
Required: No

 ** Region **   <a name="SecretsManager-Type-ReplicationStatusType-Region"></a>
The Region where replication occurs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([a-z]+-)+\d+$`
Required: No

 ** Status **   <a name="SecretsManager-Type-ReplicationStatusType-Status"></a>
The status can be `InProgress`, `Failed`, or `InSync`.
Type: String
Valid Values: `InSync | Failed | InProgress`
Required: No

 ** StatusMessage **   <a name="SecretsManager-Type-ReplicationStatusType-StatusMessage"></a>
Status message such as "*Secret with this name already exists in this region*".
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## See Also
<a name="API_ReplicationStatusType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/secretsmanager-2017-10-17/ReplicationStatusType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/secretsmanager-2017-10-17/ReplicationStatusType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/secretsmanager-2017-10-17/ReplicationStatusType)
