---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CrossAccountReplicaEntry.html
---

# CrossAccountReplicaEntry
<a name="API_CrossAccountReplicaEntry"></a>

Information about a cross-account replica secret. This information is only available for cross-account primary secrets.

## Contents
<a name="API_CrossAccountReplicaEntry_Contents"></a>

 ** ReplicaSecretARN **   <a name="SecretsManager-Type-CrossAccountReplicaEntry-ReplicaSecretARN"></a>
The ARN of the replica secret.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** ReplicationRoleARN **   <a name="SecretsManager-Type-CrossAccountReplicaEntry-ReplicationRoleARN"></a>
The ARN of the IAM role that Secrets Manager assumes to replicate to this replica, if one was specified when the replica was associated.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** ReplicationStatus **   <a name="SecretsManager-Type-CrossAccountReplicaEntry-ReplicationStatus"></a>
The status of replication from this primary secret. The status can be:
+  `InSync`: Replication from the primary secret is complete.
+  `Failed`: Replication from the primary secret was unable to be completed.
+  `InProgress`: Replication from the primary secret has started but is not complete.
+  `Detached`: Replication from the primary secret was stopped by the replica.
Type: String
Valid Values: `InSync | Failed | InProgress | Pending | Detached`
Required: No

 ** StatusMessage **   <a name="SecretsManager-Type-CrossAccountReplicaEntry-StatusMessage"></a>
A message that describes the replication status, if Secrets Manager has more information to provide.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## See Also
<a name="API_CrossAccountReplicaEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/secretsmanager-2017-10-17/CrossAccountReplicaEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/secretsmanager-2017-10-17/CrossAccountReplicaEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/secretsmanager-2017-10-17/CrossAccountReplicaEntry)
