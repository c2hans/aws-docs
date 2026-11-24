---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-fsx-clusterpeer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::ClusterPeer

Describes an Amazon FSx for NetApp ONTAP cluster peer relationship.

## Syntax
<a name="aws-resource-fsx-clusterpeer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-fsx-clusterpeer-syntax.json"></a>

```json
{
  "Type" : "AWS::FSx::ClusterPeer",
  "Properties" : {
      "[AllowedSvmIds](#cfn-fsx-clusterpeer-allowedsvmids)" : {{[ String, ... ]}},
      "[AllowedSvmMode](#cfn-fsx-clusterpeer-allowedsvmmode)" : {{String}},
      "[FileSystemId](#cfn-fsx-clusterpeer-filesystemid)" : {{String}},
      "[PassphraseSecretArn](#cfn-fsx-clusterpeer-passphrasesecretarn)" : {{String}},
      "[PeerAddresses](#cfn-fsx-clusterpeer-peeraddresses)" : {{[ String, ... ]}},
      "[PeerClusterName](#cfn-fsx-clusterpeer-peerclustername)" : {{String}},
      "[Tags](#cfn-fsx-clusterpeer-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-fsx-clusterpeer-syntax.yaml"></a>

```yaml
Type: AWS::FSx::ClusterPeer
Properties:
  [AllowedSvmIds](#cfn-fsx-clusterpeer-allowedsvmids): {{
    - String}}
  [AllowedSvmMode](#cfn-fsx-clusterpeer-allowedsvmmode): {{String}}
  [FileSystemId](#cfn-fsx-clusterpeer-filesystemid): {{String}}
  [PassphraseSecretArn](#cfn-fsx-clusterpeer-passphrasesecretarn): {{String}}
  [PeerAddresses](#cfn-fsx-clusterpeer-peeraddresses): {{
    - String}}
  [PeerClusterName](#cfn-fsx-clusterpeer-peerclustername): {{String}}
  [Tags](#cfn-fsx-clusterpeer-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-fsx-clusterpeer-properties"></a>

`AllowedSvmIds`  <a name="cfn-fsx-clusterpeer-allowedsvmids"></a>
The IDs of the SVMs on the file system that are preauthorized for SVM peering with the peer cluster, if `AllowedSvmMode` is `SPECIFIED`.
*Required*: No
*Type*: Array of String
*Minimum*: `21`
*Maximum*: `21 | 24`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AllowedSvmMode`  <a name="cfn-fsx-clusterpeer-allowedsvmmode"></a>
Indicates which SVMs on the file system are preauthorized for SVM peering with the peer cluster.
*Required*: Yes
*Type*: String
*Allowed values*: `ALL | NONE | SPECIFIED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FileSystemId`  <a name="cfn-fsx-clusterpeer-filesystemid"></a>
The globally unique ID of the file system, assigned by Amazon FSx.
*Required*: Yes
*Type*: String
*Pattern*: `^(fs-[0-9a-f]{8,})$`
*Minimum*: `11`
*Maximum*: `21`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PassphraseSecretArn`  <a name="cfn-fsx-clusterpeer-passphrasesecretarn"></a>
The Amazon Resource Name (ARN) of the AWS Secrets Manager secret containing the cluster peering passphrase.
*Required*: No
*Type*: String
*Pattern*: `^arn:[^:]{1,63}:secretsmanager:[a-z0-9-]+:[0-9]{12}:secret:[a-zA-Z0-9/_+=.@-]+-[a-zA-Z0-9]{6}$`
*Minimum*: `64`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PeerAddresses`  <a name="cfn-fsx-clusterpeer-peeraddresses"></a>
The IP addresses of the intercluster logical interfaces (LIFs) on the peer cluster.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `45 | 24`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PeerClusterName`  <a name="cfn-fsx-clusterpeer-peerclustername"></a>
The name that the file system uses to identify the peer cluster.
*Required*: No
*Type*: String
*Pattern*: `^[^\u0000\u0085\u2028\u2029\r\n]{1,44}$`
*Minimum*: `1`
*Maximum*: `44`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-fsx-clusterpeer-tags"></a>
A list of `Tag` values, with a maximum of 50 elements.
*Required*: No
*Type*: Array of [Tag](aws-properties-fsx-clusterpeer-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-fsx-clusterpeer-return-values"></a>

### Ref
<a name="aws-resource-fsx-clusterpeer-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-fsx-clusterpeer-return-values-fn--getatt"></a>

####
<a name="aws-resource-fsx-clusterpeer-return-values-fn--getatt-fn--getatt"></a>

`ClusterPeerId`  <a name="ClusterPeerId-fn::getatt"></a>
The system-generated, unique ID of the cluster peer.

`Lifecycle`  <a name="Lifecycle-fn::getatt"></a>
The lifecycle status of the cluster peer can be one of the following:
+ `CREATED` – The cluster peer is fully available for use.
+ `CREATING` – Amazon FSx is creating the cluster peer.
+ `DELETING` – Amazon FSx is deleting the cluster peer.
+ `FAILED` – Amazon FSx was unable to create the cluster peer.

`ResourceARN`  <a name="ResourceARN-fn::getatt"></a>
The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify AWS resources. We require an ARN when you need to specify a resource unambiguously across all of AWS. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *AWS General Reference*.

`Status`  <a name="Status-fn::getatt"></a>
The status of the connection to the peer cluster.

`UUID`  <a name="UUID-fn::getatt"></a>
The cluster peer's universally unique identifier (UUID).
