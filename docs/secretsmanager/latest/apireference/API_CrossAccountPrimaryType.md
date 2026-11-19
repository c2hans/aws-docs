---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CrossAccountPrimaryType.html
---

# CrossAccountPrimaryType

Contains information about the primary secret that a cross-account replica secret replicates from, including its ARN and replication status. This information is only available for cross-account replica secrets.

## Contents
<a name="API_CrossAccountPrimaryType_Contents"></a>

 ** PrimarySecretARN **   <a name="SecretsManager-Type-CrossAccountPrimaryType-PrimarySecretARN"></a>
The ARN of the primary secret replicating into this replica secret.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** ReplicationStatus **   <a name="SecretsManager-Type-CrossAccountPrimaryType-ReplicationStatus"></a>
The status of replication from the primary secret to this replica. The status can be:
+  `InSync`: Replication to the replica secret is complete.
+  `Failed`: Replication to the replica secret was unable to be completed.
+  `InProgress`: Replication to the replica secret has started but is not complete.
+  `Pending`: Replication has not yet started for the replica secret.
+  `Detached`: Replication to the replica secret was stopped by the primary.
Type: String
Valid Values: `InSync | Failed | InProgress | Pending | Detached`
Required: No

 ** StatusMessage **   <a name="SecretsManager-Type-CrossAccountPrimaryType-StatusMessage"></a>
A message that describes the replication status, if Secrets Manager has more information to provide.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## See Also
<a name="API_CrossAccountPrimaryType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/secretsmanager-2017-10-17/CrossAccountPrimaryType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/secretsmanager-2017-10-17/CrossAccountPrimaryType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/secretsmanager-2017-10-17/CrossAccountPrimaryType)
