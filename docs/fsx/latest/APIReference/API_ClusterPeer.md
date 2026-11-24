---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_ClusterPeer.html
---

# ClusterPeer

Describes an Amazon FSx for NetApp ONTAP cluster peer relationship.

## Contents
<a name="API_ClusterPeer_Contents"></a>

 ** AllowedSvmIds **   <a name="FSx-Type-ClusterPeer-AllowedSvmIds"></a>
The IDs of the SVMs on the file system that are preauthorized for SVM peering with the peer cluster, if `AllowedSvmMode` is `SPECIFIED`.
Type: Array of strings
Array Members: Maximum number of 24 items.
Length Constraints: Fixed length of 21.
Pattern: `^(svm-[0-9a-f]{17,})$`
Required: No

 ** AllowedSvmMode **   <a name="FSx-Type-ClusterPeer-AllowedSvmMode"></a>
Indicates which SVMs on the file system are preauthorized for SVM peering with the peer cluster.
Type: String
Valid Values: `ALL | NONE | SPECIFIED`
Required: No

 ** AuthenticationStatus **   <a name="FSx-Type-ClusterPeer-AuthenticationStatus"></a>
The authentication status of the cluster peer relationship.
Type: [ClusterPeerAuthenticationStatus](API_ClusterPeerAuthenticationStatus.md) object
Required: No

 ** ClusterPeerId **   <a name="FSx-Type-ClusterPeer-ClusterPeerId"></a>
The system-generated, unique ID of the cluster peer.
Type: String
Pattern: `^(clusterpeer-[0-9a-f]{17})$`
Required: No

 ** FileSystemId **   <a name="FSx-Type-ClusterPeer-FileSystemId"></a>
The globally unique ID of the file system, assigned by Amazon FSx.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 21.
Pattern: `^(fs-[0-9a-f]{8,})$`
Required: No

 ** Lifecycle **   <a name="FSx-Type-ClusterPeer-Lifecycle"></a>
The lifecycle status of the cluster peer can be one of the following:
+  `CREATED` – The cluster peer is fully available for use.
+  `CREATING` – Amazon FSx is creating the cluster peer.
+  `DELETING` – Amazon FSx is deleting the cluster peer.
+  `FAILED` – Amazon FSx was unable to create the cluster peer.
Type: String
Valid Values: `CREATING | CREATED | DELETING | FAILED`
Required: No

 ** LifecycleTransitionReason **   <a name="FSx-Type-ClusterPeer-LifecycleTransitionReason"></a>
The reason why the cluster peer lifecycle status changed.
Type: [LifecycleTransitionReason](API_LifecycleTransitionReason.md) object
Required: No

 ** PassphraseSecretArn **   <a name="FSx-Type-ClusterPeer-PassphraseSecretArn"></a>
The Amazon Resource Name (ARN) of the AWS Secrets Manager secret containing the cluster peering passphrase.
Type: String
Length Constraints: Minimum length of 64. Maximum length of 1024.
Pattern: `^arn:[^:]{1,63}:secretsmanager:[a-z0-9-]+:[0-9]{12}:secret:[a-zA-Z0-9/_+=.@-]+-[a-zA-Z0-9]{6}$`
Required: No

 ** PeerAddresses **   <a name="FSx-Type-ClusterPeer-PeerAddresses"></a>
The IP addresses of the intercluster logical interfaces (LIFs) on the peer cluster.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 288 items.
Length Constraints: Minimum length of 1. Maximum length of 45.
Pattern: `(^((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))$|^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$)`
Required: No

 ** PeerClusterName **   <a name="FSx-Type-ClusterPeer-PeerClusterName"></a>
The name that the file system uses to identify the peer cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 44.
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,44}$`
Required: No

 ** ResourceARN **   <a name="FSx-Type-ClusterPeer-ResourceARN"></a>
The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify AWS resources. We require an ARN when you need to specify a resource unambiguously across all of AWS. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 512.
Pattern: `^arn:(?=[^:]+:fsx:[^:]+:\d{12}:)((|(?=[a-z0-9-.]{1,63})(?!\d{1,3}(\.\d{1,3}){3})(?![^:]*-{2})(?![^:]*-\.)(?![^:]*\.-)[a-z0-9].*(?<!-)):){4}(?!/).{0,1024}$`
Required: No

 ** Status **   <a name="FSx-Type-ClusterPeer-Status"></a>
The status of the connection to the peer cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Tags **   <a name="FSx-Type-ClusterPeer-Tags"></a>
A list of `Tag` values, with a maximum of 50 elements.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** UUID **   <a name="FSx-Type-ClusterPeer-UUID"></a>
The cluster peer's universally unique identifier (UUID).
Type: String
Length Constraints: Maximum length of 36.
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,36}$`
Required: No

## See Also
<a name="API_ClusterPeer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/ClusterPeer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/ClusterPeer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/ClusterPeer)
