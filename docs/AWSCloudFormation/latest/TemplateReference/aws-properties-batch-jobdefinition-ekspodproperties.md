---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-ekspodproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition EksPodProperties
<a name="aws-properties-batch-jobdefinition-ekspodproperties"></a>

The properties for the pod.

## Syntax
<a name="aws-properties-batch-jobdefinition-ekspodproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-ekspodproperties-syntax.json"></a>

```
{
  "[Containers](#cfn-batch-jobdefinition-ekspodproperties-containers)" : {{[ EksContainer, ... ]}},
  "[DnsPolicy](#cfn-batch-jobdefinition-ekspodproperties-dnspolicy)" : {{String}},
  "[HostNetwork](#cfn-batch-jobdefinition-ekspodproperties-hostnetwork)" : {{Boolean}},
  "[ImagePullSecrets](#cfn-batch-jobdefinition-ekspodproperties-imagepullsecrets)" : {{[ ImagePullSecret, ... ]}},
  "[InitContainers](#cfn-batch-jobdefinition-ekspodproperties-initcontainers)" : {{[ EksContainer, ... ]}},
  "[Metadata](#cfn-batch-jobdefinition-ekspodproperties-metadata)" : {{EksMetadata}},
  "[ServiceAccountName](#cfn-batch-jobdefinition-ekspodproperties-serviceaccountname)" : {{String}},
  "[ShareProcessNamespace](#cfn-batch-jobdefinition-ekspodproperties-shareprocessnamespace)" : {{Boolean}},
  "[Volumes](#cfn-batch-jobdefinition-ekspodproperties-volumes)" : {{[ EksVolume, ... ]}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-ekspodproperties-syntax.yaml"></a>

```
  [Containers](#cfn-batch-jobdefinition-ekspodproperties-containers): {{
    - EksContainer}}
  [DnsPolicy](#cfn-batch-jobdefinition-ekspodproperties-dnspolicy): {{String}}
  [HostNetwork](#cfn-batch-jobdefinition-ekspodproperties-hostnetwork): {{Boolean}}
  [ImagePullSecrets](#cfn-batch-jobdefinition-ekspodproperties-imagepullsecrets): {{
    - ImagePullSecret}}
  [InitContainers](#cfn-batch-jobdefinition-ekspodproperties-initcontainers): {{
    - EksContainer}}
  [Metadata](#cfn-batch-jobdefinition-ekspodproperties-metadata): {{
    EksMetadata}}
  [ServiceAccountName](#cfn-batch-jobdefinition-ekspodproperties-serviceaccountname): {{String}}
  [ShareProcessNamespace](#cfn-batch-jobdefinition-ekspodproperties-shareprocessnamespace): {{Boolean}}
  [Volumes](#cfn-batch-jobdefinition-ekspodproperties-volumes): {{
    - EksVolume}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-ekspodproperties-properties"></a>

`Containers`  <a name="cfn-batch-jobdefinition-ekspodproperties-containers"></a>
The properties of the container that's used on the Amazon EKS pod.
This object is limited to 10 elements.
*Required*: No
*Type*: Array of [EksContainer](aws-properties-batch-jobdefinition-ekscontainer.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DnsPolicy`  <a name="cfn-batch-jobdefinition-ekspodproperties-dnspolicy"></a>
The DNS policy for the pod. The default value is `ClusterFirst`. If the `hostNetwork` parameter is not specified, the default is `ClusterFirstWithHostNet`. `ClusterFirst` indicates that any DNS query that does not match the configured cluster domain suffix is forwarded to the upstream nameserver inherited from the node. For more information, see [Pod's DNS policy](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/#pod-s-dns-policy) in the *Kubernetes documentation*.
Valid values: `Default` \| `ClusterFirst` \| `ClusterFirstWithHostNet`
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HostNetwork`  <a name="cfn-batch-jobdefinition-ekspodproperties-hostnetwork"></a>
Indicates if the pod uses the hosts' network IP address. The default value is `true`. Setting this to `false` enables the Kubernetes pod networking model. Most AWS Batch workloads are egress-only and don't require the overhead of IP allocation for each pod for incoming connections. For more information, see [Host namespaces](https://kubernetes.io/docs/concepts/security/pod-security-policy/#host-namespaces) and [Pod networking](https://kubernetes.io/docs/concepts/workloads/pods/#pod-networking) in the *Kubernetes documentation*.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImagePullSecrets`  <a name="cfn-batch-jobdefinition-ekspodproperties-imagepullsecrets"></a>
References a Kubernetes secret resource. It holds a list of secrets. These secrets help to gain access to pull an images from a private registry.
`ImagePullSecret$name` is required when this object is used.
*Required*: No
*Type*: Array of [ImagePullSecret](aws-properties-batch-jobdefinition-imagepullsecret.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InitContainers`  <a name="cfn-batch-jobdefinition-ekspodproperties-initcontainers"></a>
These containers run before application containers, always runs to completion, and must complete successfully before the next container starts. These containers are registered with the Amazon EKS Connector agent and persists the registration information in the Kubernetes backend data store. For more information, see [Init Containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/) in the *Kubernetes documentation*.
This object is limited to 10 elements.
*Required*: No
*Type*: Array of [EksContainer](aws-properties-batch-jobdefinition-ekscontainer.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Metadata`  <a name="cfn-batch-jobdefinition-ekspodproperties-metadata"></a>
Metadata about the Kubernetes pod. For more information, see [Understanding Kubernetes Objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) in the *Kubernetes documentation*.
*Required*: No
*Type*: [EksMetadata](aws-properties-batch-jobdefinition-eksmetadata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceAccountName`  <a name="cfn-batch-jobdefinition-ekspodproperties-serviceaccountname"></a>
The name of the service account that's used to run the pod. For more information, see [Kubernetes service accounts](https://docs.aws.amazon.com/eks/latest/userguide/service-accounts.html) and [Configure a Kubernetes service account to assume an IAM role](https://docs.aws.amazon.com/eks/latest/userguide/associate-service-account-role.html) in the *Amazon EKS User Guide* and [Configure service accounts for pods](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) in the *Kubernetes documentation*.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareProcessNamespace`  <a name="cfn-batch-jobdefinition-ekspodproperties-shareprocessnamespace"></a>
Indicates if the processes in a container are shared, or visible, to other containers in the same pod. For more information, see [Share Process Namespace between Containers in a Pod](https://kubernetes.io/docs/tasks/configure-pod-container/share-process-namespace/).
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Volumes`  <a name="cfn-batch-jobdefinition-ekspodproperties-volumes"></a>
Specifies the volumes for a job definition that uses Amazon EKS resources.
*Required*: No
*Type*: Array of [EksVolume](aws-properties-batch-jobdefinition-eksvolume.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
