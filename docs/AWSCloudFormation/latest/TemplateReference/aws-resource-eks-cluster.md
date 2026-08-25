---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-eks-cluster.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Cluster
<a name="aws-resource-eks-cluster"></a>

Creates an Amazon EKS control plane.

The Amazon EKS control plane consists of control plane instances that run the Kubernetes software, such as `etcd` and the API server. The control plane runs in an account managed by AWS, and the Kubernetes API is exposed by the Amazon EKS API server endpoint. Each Amazon EKS cluster control plane is single tenant and unique. It runs on its own set of Amazon EC2 instances.

The cluster control plane is provisioned across multiple Availability Zones and fronted by an Elastic Load Balancing Network Load Balancer. Amazon EKS also provisions elastic network interfaces in your VPC subnets to provide connectivity from the control plane instances to the nodes (for example, to support `kubectl exec`, `logs`, and `proxy` data flows).

Amazon EKS nodes run in your AWS account and connect to your cluster's control plane over the Kubernetes API server endpoint and a certificate file that is created for your cluster.

You can use the `endpointPublicAccess` and `endpointPrivateAccess` parameters to enable or disable public and private access to your cluster's Kubernetes API server endpoint. By default, public access is enabled, and private access is disabled. The endpoint domain name and IP address family depends on the value of the `ipFamily` for the cluster. For more information, see [Amazon EKS Cluster Endpoint Access Control](https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html) in the * *Amazon EKS User Guide* *.

You can use the `logging` parameter to enable or disable exporting the Kubernetes control plane logs for your cluster to CloudWatch Logs. By default, cluster control plane logs aren't exported to CloudWatch Logs. For more information, see [Amazon EKS Cluster Control Plane Logs](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html) in the * *Amazon EKS User Guide* *.

**Note**
CloudWatch Logs ingestion, archive storage, and data scanning rates apply to exported control plane logs. For more information, see [CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

In most cases, it takes several minutes to create a cluster. After you create an Amazon EKS cluster, you must configure your Kubernetes tooling to communicate with the API server and launch nodes into your cluster. For more information, see [Allowing users to access your cluster](https://docs.aws.amazon.com/eks/latest/userguide/cluster-auth.html) and [Launching Amazon EKS nodes](https://docs.aws.amazon.com/eks/latest/userguide/launch-workers.html) in the *Amazon EKS User Guide*.

## Syntax
<a name="aws-resource-eks-cluster-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-eks-cluster-syntax.json"></a>

```
{
  "Type" : "AWS::EKS::Cluster",
  "Properties" : {
      "[AccessConfig](#cfn-eks-cluster-accessconfig)" : {{AccessConfig}},
      "[ActiveCertificateAuthorityId](#cfn-eks-cluster-activecertificateauthorityid)" : {{String}},
      "[BootstrapSelfManagedAddons](#cfn-eks-cluster-bootstrapselfmanagedaddons)" : {{Boolean}},
      "[CertificateAuthority](#cfn-eks-cluster-certificateauthority)" : {{CertificateAuthority}},
      "[ComputeConfig](#cfn-eks-cluster-computeconfig)" : {{ComputeConfig}},
      "[ControlPlaneScalingConfig](#cfn-eks-cluster-controlplanescalingconfig)" : {{ControlPlaneScalingConfig}},
      "[DeletionProtection](#cfn-eks-cluster-deletionprotection)" : {{Boolean}},
      "[EncryptionConfig](#cfn-eks-cluster-encryptionconfig)" : {{[ EncryptionConfig, ... ]}},
      "[Force](#cfn-eks-cluster-force)" : {{Boolean}},
      "[KubeApiServerConfig](#cfn-eks-cluster-kubeapiserverconfig)" : {{KubeApiServerConfig}},
      "[KubeControllerManagerConfig](#cfn-eks-cluster-kubecontrollermanagerconfig)" : {{KubeControllerManagerConfig}},
      "[KubernetesNetworkConfig](#cfn-eks-cluster-kubernetesnetworkconfig)" : {{KubernetesNetworkConfig}},
      "[KubeSchedulerConfig](#cfn-eks-cluster-kubeschedulerconfig)" : {{KubeSchedulerConfig}},
      "[Logging](#cfn-eks-cluster-logging)" : {{Logging}},
      "[Name](#cfn-eks-cluster-name)" : {{String}},
      "[OutpostConfig](#cfn-eks-cluster-outpostconfig)" : {{OutpostConfig}},
      "[RemoteNetworkConfig](#cfn-eks-cluster-remotenetworkconfig)" : {{RemoteNetworkConfig}},
      "[ResourcesVpcConfig](#cfn-eks-cluster-resourcesvpcconfig)" : {{ResourcesVpcConfig}},
      "[RoleArn](#cfn-eks-cluster-rolearn)" : {{String}},
      "[RollbackConfig](#cfn-eks-cluster-rollbackconfig)" : {{RollbackConfig}},
      "[StorageConfig](#cfn-eks-cluster-storageconfig)" : {{StorageConfig}},
      "[Tags](#cfn-eks-cluster-tags)" : {{[ Tag, ... ]}},
      "[UpgradePolicy](#cfn-eks-cluster-upgradepolicy)" : {{UpgradePolicy}},
      "[Version](#cfn-eks-cluster-version)" : {{String}},
      "[ZonalShiftConfig](#cfn-eks-cluster-zonalshiftconfig)" : {{ZonalShiftConfig}}
    }
}
```

### YAML
<a name="aws-resource-eks-cluster-syntax.yaml"></a>

```
Type: AWS::EKS::Cluster
Properties:
  [AccessConfig](#cfn-eks-cluster-accessconfig): {{
    AccessConfig}}
  [ActiveCertificateAuthorityId](#cfn-eks-cluster-activecertificateauthorityid): {{String}}
  [BootstrapSelfManagedAddons](#cfn-eks-cluster-bootstrapselfmanagedaddons): {{Boolean}}
  [CertificateAuthority](#cfn-eks-cluster-certificateauthority): {{
    CertificateAuthority}}
  [ComputeConfig](#cfn-eks-cluster-computeconfig): {{
    ComputeConfig}}
  [ControlPlaneScalingConfig](#cfn-eks-cluster-controlplanescalingconfig): {{
    ControlPlaneScalingConfig}}
  [DeletionProtection](#cfn-eks-cluster-deletionprotection): {{Boolean}}
  [EncryptionConfig](#cfn-eks-cluster-encryptionconfig): {{
    - EncryptionConfig}}
  [Force](#cfn-eks-cluster-force): {{Boolean}}
  [KubeApiServerConfig](#cfn-eks-cluster-kubeapiserverconfig): {{
    KubeApiServerConfig}}
  [KubeControllerManagerConfig](#cfn-eks-cluster-kubecontrollermanagerconfig): {{
    KubeControllerManagerConfig}}
  [KubernetesNetworkConfig](#cfn-eks-cluster-kubernetesnetworkconfig): {{
    KubernetesNetworkConfig}}
  [KubeSchedulerConfig](#cfn-eks-cluster-kubeschedulerconfig): {{
    KubeSchedulerConfig}}
  [Logging](#cfn-eks-cluster-logging): {{
    Logging}}
  [Name](#cfn-eks-cluster-name): {{String}}
  [OutpostConfig](#cfn-eks-cluster-outpostconfig): {{
    OutpostConfig}}
  [RemoteNetworkConfig](#cfn-eks-cluster-remotenetworkconfig): {{
    RemoteNetworkConfig}}
  [ResourcesVpcConfig](#cfn-eks-cluster-resourcesvpcconfig): {{
    ResourcesVpcConfig}}
  [RoleArn](#cfn-eks-cluster-rolearn): {{String}}
  [RollbackConfig](#cfn-eks-cluster-rollbackconfig): {{
    RollbackConfig}}
  [StorageConfig](#cfn-eks-cluster-storageconfig): {{
    StorageConfig}}
  [Tags](#cfn-eks-cluster-tags): {{
    - Tag}}
  [UpgradePolicy](#cfn-eks-cluster-upgradepolicy): {{
    UpgradePolicy}}
  [Version](#cfn-eks-cluster-version): {{String}}
  [ZonalShiftConfig](#cfn-eks-cluster-zonalshiftconfig): {{
    ZonalShiftConfig}}
```

## Properties
<a name="aws-resource-eks-cluster-properties"></a>

`AccessConfig`  <a name="cfn-eks-cluster-accessconfig"></a>
The access configuration for the cluster.
*Required*: No
*Type*: [AccessConfig](aws-properties-eks-cluster-accessconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ActiveCertificateAuthorityId`  <a name="cfn-eks-cluster-activecertificateauthorityid"></a>
The ID of the certificate authority (CA) to activate as the cluster's signing CA, completing a CA rotation. Set this to the `Id` of an `AWS::EKS::CertificateAuthority` resource whose distribution status is `COMPLETE`; the previously active CA is retired but remains trusted.
This is a write-only property that triggers activation. It isn't stored in the stack's state or returned on read, so subsequent stack updates that omit it don't revert or deactivate the CA, and CloudFormation doesn't detect drift if the active CA changes outside of CloudFormation (for example, through auto-activation by Amazon EKS). For more information, see [Rotate the Amazon EKS cluster certificate authority](https://docs.aws.amazon.com/eks/latest/userguide/certificate-authority-rotation.html) in the *Amazon EKS User Guide*.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BootstrapSelfManagedAddons`  <a name="cfn-eks-cluster-bootstrapselfmanagedaddons"></a>
If you set this value to `False` when creating a cluster, the default networking add-ons will not be installed.
The default networking add-ons include `vpc-cni`, `coredns`, and `kube-proxy`.
Use this option when you plan to install third-party alternative add-ons or self-manage the default networking add-ons.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CertificateAuthority`  <a name="cfn-eks-cluster-certificateauthority"></a>
The `certificate-authority-data` for your cluster.
*Required*: No
*Type*: [CertificateAuthority](aws-properties-eks-cluster-certificateauthority.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComputeConfig`  <a name="cfn-eks-cluster-computeconfig"></a>
Indicates the current configuration of the compute capability on your EKS Auto Mode cluster. For example, if the capability is enabled or disabled. If the compute capability is enabled, EKS Auto Mode will create and delete EC2 Managed Instances in your AWS account. For more information, see EKS Auto Mode compute capability in the *Amazon EKS User Guide*.
*Required*: No
*Type*: [ComputeConfig](aws-properties-eks-cluster-computeconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ControlPlaneScalingConfig`  <a name="cfn-eks-cluster-controlplanescalingconfig"></a>
The control plane scaling tier configuration. For more information, see EKS Provisioned Control Plane in the Amazon EKS User Guide.
*Required*: No
*Type*: [ControlPlaneScalingConfig](aws-properties-eks-cluster-controlplanescalingconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeletionProtection`  <a name="cfn-eks-cluster-deletionprotection"></a>
The current deletion protection setting for the cluster. When `true`, deletion protection is enabled and the cluster cannot be deleted until protection is disabled. When `false`, the cluster can be deleted normally. This setting only applies to clusters in an active state.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionConfig`  <a name="cfn-eks-cluster-encryptionconfig"></a>
The encryption configuration for the cluster.
*Required*: No
*Type*: [Array](aws-properties-eks-cluster-encryptionconfig.md) of [EncryptionConfig](aws-properties-eks-cluster-encryptionconfig.md)
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Force`  <a name="cfn-eks-cluster-force"></a>
Set this value to `true` to override upgrade-blocking or rollback-blocking readiness checks when updating a cluster.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KubeApiServerConfig`  <a name="cfn-eks-cluster-kubeapiserverconfig"></a>
The Kubernetes API server configuration for the cluster.
*Required*: No
*Type*: [KubeApiServerConfig](aws-properties-eks-cluster-kubeapiserverconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KubeControllerManagerConfig`  <a name="cfn-eks-cluster-kubecontrollermanagerconfig"></a>
The Kubernetes controller manager configuration for the cluster.
*Required*: No
*Type*: [KubeControllerManagerConfig](aws-properties-eks-cluster-kubecontrollermanagerconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KubernetesNetworkConfig`  <a name="cfn-eks-cluster-kubernetesnetworkconfig"></a>
The Kubernetes network configuration for the cluster.
*Required*: No
*Type*: [KubernetesNetworkConfig](aws-properties-eks-cluster-kubernetesnetworkconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KubeSchedulerConfig`  <a name="cfn-eks-cluster-kubeschedulerconfig"></a>
The Kubernetes scheduler configuration for the cluster.
*Required*: No
*Type*: [KubeSchedulerConfig](aws-properties-eks-cluster-kubeschedulerconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Logging`  <a name="cfn-eks-cluster-logging"></a>
The logging configuration for your cluster.
*Required*: No
*Type*: [Logging](aws-properties-eks-cluster-logging.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-eks-cluster-name"></a>
The unique name to give to your cluster. The name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphanumeric character and can't be longer than 100 characters. The name must be unique within the AWS Region and AWS account that you're creating the cluster in. Note that underscores can't be used in CloudFormation.
*Required*: No
*Type*: String
*Pattern*: `^[0-9A-Za-z][A-Za-z0-9\-_]*`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OutpostConfig`  <a name="cfn-eks-cluster-outpostconfig"></a>
An object representing the configuration of your local Amazon EKS cluster on an AWS Outpost. This object isn't available for clusters on the AWS cloud.
*Required*: No
*Type*: [OutpostConfig](aws-properties-eks-cluster-outpostconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RemoteNetworkConfig`  <a name="cfn-eks-cluster-remotenetworkconfig"></a>
The configuration in the cluster for EKS Hybrid Nodes. You can add, change, or remove this configuration after the cluster is created.
*Required*: No
*Type*: [RemoteNetworkConfig](aws-properties-eks-cluster-remotenetworkconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourcesVpcConfig`  <a name="cfn-eks-cluster-resourcesvpcconfig"></a>
The VPC configuration that's used by the cluster control plane. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see [Cluster VPC Considerations](https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html) and [Cluster Security Group Considerations](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html) in the *Amazon EKS User Guide*. You must specify at least two subnets. You can specify up to five security groups, but we recommend that you use a dedicated security group for your cluster control plane.
*Required*: Yes
*Type*: [ResourcesVpcConfig](aws-properties-eks-cluster-resourcesvpcconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-eks-cluster-rolearn"></a>
The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf. For more information, see [Amazon EKS Service IAM Role](https://docs.aws.amazon.com/eks/latest/userguide/service_IAM_role.html) in the * *Amazon EKS User Guide* *.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RollbackConfig`  <a name="cfn-eks-cluster-rollbackconfig"></a>
The rollback configuration for the cluster version rollback.
*Required*: No
*Type*: [RollbackConfig](aws-properties-eks-cluster-rollbackconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StorageConfig`  <a name="cfn-eks-cluster-storageconfig"></a>
Indicates the current configuration of the block storage capability on your EKS Auto Mode cluster. For example, if the capability is enabled or disabled. If the block storage capability is enabled, EKS Auto Mode will create and delete EBS volumes in your AWS account. For more information, see EKS Auto Mode block storage capability in the *Amazon EKS User Guide*.
*Required*: No
*Type*: [StorageConfig](aws-properties-eks-cluster-storageconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-eks-cluster-tags"></a>
The metadata that you apply to the cluster to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Cluster tags don't propagate to any other resources associated with the cluster.
You must have the `eks:TagResource` and `eks:UntagResource` permissions for your [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html) to manage the CloudFormation stack. If you don't have these permissions, there might be unexpected behavior with stack-level tags propagating to the resource during resource creation and update.
*Required*: No
*Type*: Array of [Tag](aws-properties-eks-cluster-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpgradePolicy`  <a name="cfn-eks-cluster-upgradepolicy"></a>
This value indicates if extended support is enabled or disabled for the cluster.
 [Learn more about EKS Extended Support in the *Amazon EKS User Guide*.](https://docs.aws.amazon.com/eks/latest/userguide/extended-support-control.html)
*Required*: No
*Type*: [UpgradePolicy](aws-properties-eks-cluster-upgradepolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Version`  <a name="cfn-eks-cluster-version"></a>
The desired Kubernetes version for your cluster. If you don't specify a value here, the default version available in Amazon EKS is used.
The default version might not be the latest version available.
*Required*: No
*Type*: String
*Pattern*: `1\.\d\d`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ZonalShiftConfig`  <a name="cfn-eks-cluster-zonalshiftconfig"></a>
The configuration for zonal shift for the cluster.
*Required*: No
*Type*: [ZonalShiftConfig](aws-properties-eks-cluster-zonalshiftconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-eks-cluster-return-values"></a>

### Ref
<a name="aws-resource-eks-cluster-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name. For example:

 `{ "Ref": "myCluster" }`

For the Amazon EKS cluster `myCluster`, `Ref` returns the name of the cluster.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-eks-cluster-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-eks-cluster-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the cluster, such as `arn:aws:eks:us-west-2:666666666666:cluster/prod`.

`CertificateAuthority.Active.ActivatedBy`  <a name="CertificateAuthority.Active.ActivatedBy-fn::getatt"></a>
The entity that activated the current signing certificate authority, either `CUSTOMER` or `EKS`.

`CertificateAuthority.Active.Id`  <a name="CertificateAuthority.Active.Id-fn::getatt"></a>
The ID of the certificate authority that is currently signing certificates for the cluster.

`CertificateAuthority.Data`  <a name="CertificateAuthority.Data-fn::getatt"></a>
The Base64-encoded certificate-authority trust bundle for the cluster. During a CA rotation's dual trust period, this bundle contains both the outgoing CA and the successor CA.

`CertificateAuthorityData`  <a name="CertificateAuthorityData-fn::getatt"></a>
The `certificate-authority-data` for your cluster.

`ClusterSecurityGroupId`  <a name="ClusterSecurityGroupId-fn::getatt"></a>
The cluster security group that was created by Amazon EKS for the cluster. Managed node groups use this security group for control plane to data plane communication.
This parameter is only returned by Amazon EKS clusters that support managed node groups. For more information, see [Managed node groups](https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html) in the *Amazon EKS User Guide*.

`EncryptionConfigKeyArn`  <a name="EncryptionConfigKeyArn-fn::getatt"></a>
Amazon Resource Name (ARN) or alias of the customer master key (CMK).

`Endpoint`  <a name="Endpoint-fn::getatt"></a>
The endpoint for your Kubernetes API server, such as `https://5E1D0CEXAMPLEA591B746AFC5AB30262.yl4.us-west-2.eks.amazonaws.com`.

`Id`  <a name="Id-fn::getatt"></a>
The ID of your local Amazon EKS cluster on an AWS Outpost. This property isn't available for an Amazon EKS cluster on the AWS cloud.

`KubernetesNetworkConfig.ServiceIpv6Cidr`  <a name="KubernetesNetworkConfig.ServiceIpv6Cidr-fn::getatt"></a>
The CIDR block that Kubernetes Service IP addresses are assigned from if you created a `1.21` or later cluster with version `>1.10.1` or later of the Amazon VPC CNI add-on and specified `ipv6` for **ipFamily** when you created the cluster. Kubernetes assigns Service addresses from the unique local address range (`fc00::/7`) because you can't specify a custom `IPv6` CIDR block when you create the cluster.

`OpenIdConnectIssuerUrl`  <a name="OpenIdConnectIssuerUrl-fn::getatt"></a>
The issuer URL for the OIDC identity provider of the cluster, such as `https://oidc.eks.us-west-2.amazonaws.com/id/EXAMPLED539D4633E53DE1B716D3041E`. If you need to remove `https://` from this output value, you can include the following code in your template.
 `!Select [1, !Split ["//", !GetAtt EKSCluster.OpenIdConnectIssuerUrl]]`

## Examples
<a name="aws-resource-eks-cluster--examples"></a>

### Create a cluster
<a name="aws-resource-eks-cluster--examples--Create_a_cluster"></a>

The following example creates an Amazon EKS cluster named `Prod`.

#### JSON
<a name="aws-resource-eks-cluster--examples--Create_a_cluster--json"></a>

```
{
    "EKSCluster": {
       "Type": "AWS::EKS::Cluster",
       "Properties": {
          "Name": "Prod",
          "Version": "1.20",
          "RoleArn": "arn:aws:iam::012345678910:role/eks-service-role-AWSServiceRoleForAmazonEKS-EXAMPLEBQ4PI",
          "ResourcesVpcConfig": {
             "SecurityGroupIds": [
                "sg-6979fe18"
             ],
             "SubnetIds": [
                "subnet-6782e71e",
                "subnet-e7e761ac"
             ],
             "EndpointPublicAccess": true,
             "EndpointPrivateAccess": true,
             "PublicAccessCidrs": [
                "1.1.1.2/32"
             ]
          },
          "Logging": {
             "ClusterLogging": {
                "EnabledTypes": [
                   {
                      "Type": "api"
                   },
                   {
                      "Type": "audit"
                   }
                ]
             }
          },
          "Tags": [
             {
                "Key": "key",
                "Value": "val"
             }
          ]
       }
    }
 }
```

#### YAML
<a name="aws-resource-eks-cluster--examples--Create_a_cluster--yaml"></a>

```
EKSCluster:
    Type: AWS::EKS::Cluster
    Properties:
      Name: Prod
      Version: "1.20"
      RoleArn: "arn:aws:iam::012345678910:role/eks-service-role-AWSServiceRoleForAmazonEKS-EXAMPLEBQ4PI"
      ResourcesVpcConfig:
        SecurityGroupIds:
          - sg-6979fe18
        SubnetIds:
          - subnet-6782e71e
          - subnet-e7e761ac
        EndpointPublicAccess: true
        EndpointPrivateAccess: true
        PublicAccessCidrs: [ "1.1.1.2/32" ]
      Logging:
        ClusterLogging:
          EnabledTypes:
            - Type: api
            - Type: audit
      Tags:
        - Key: "key"
          Value: "val"
```

## See also
<a name="aws-resource-eks-cluster--seealso"></a>
+ [Clusters](https://docs.aws.amazon.com/eks/latest/userguide/clusters.html) in the *Amazon EKS User Guide*.
+ [`CreateCluster`](https://docs.aws.amazon.com/eks/latest/APIReference/API_CreateCluster.html) in the *Amazon EKS API Reference*.
