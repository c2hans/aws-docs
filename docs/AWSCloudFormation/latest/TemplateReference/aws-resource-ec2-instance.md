---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::Instance
<a name="aws-resource-ec2-instance"></a>

Specifies an EC2 instance.

If an Elastic IP address is attached to your instance, AWS CloudFormation reattaches the Elastic IP address after it updates the instance. For more information about updating stacks, see [AWS CloudFormation Stacks Updates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks.html).

## Syntax
<a name="aws-resource-ec2-instance-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-instance-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::Instance",
  "Properties" : {
      "[AdditionalInfo](#cfn-ec2-instance-additionalinfo)" : {{String}},
      "[Affinity](#cfn-ec2-instance-affinity)" : {{String}},
      "[AvailabilityZone](#cfn-ec2-instance-availabilityzone)" : {{String}},
      "[BlockDeviceMappings](#cfn-ec2-instance-blockdevicemappings)" : {{[ BlockDeviceMapping, ... ]}},
      "[CpuOptions](#cfn-ec2-instance-cpuoptions)" : {{CpuOptions}},
      "[CreditSpecification](#cfn-ec2-instance-creditspecification)" : {{CreditSpecification}},
      "[DisableApiTermination](#cfn-ec2-instance-disableapitermination)" : {{Boolean}},
      "[EbsOptimized](#cfn-ec2-instance-ebsoptimized)" : {{Boolean}},
      "[ElasticGpuSpecifications](#cfn-ec2-instance-elasticgpuspecifications)" : {{[ ElasticGpuSpecification, ... ]}},
      "[ElasticInferenceAccelerators](#cfn-ec2-instance-elasticinferenceaccelerators)" : {{[ ElasticInferenceAccelerator, ... ]}},
      "[EnclaveOptions](#cfn-ec2-instance-enclaveoptions)" : {{EnclaveOptions}},
      "[HibernationOptions](#cfn-ec2-instance-hibernationoptions)" : {{HibernationOptions}},
      "[HostId](#cfn-ec2-instance-hostid)" : {{String}},
      "[HostResourceGroupArn](#cfn-ec2-instance-hostresourcegrouparn)" : {{String}},
      "[IamInstanceProfile](#cfn-ec2-instance-iaminstanceprofile)" : {{String}},
      "[ImageId](#cfn-ec2-instance-imageid)" : {{String}},
      "[InstanceInitiatedShutdownBehavior](#cfn-ec2-instance-instanceinitiatedshutdownbehavior)" : {{String}},
      "[InstanceType](#cfn-ec2-instance-instancetype)" : {{String}},
      "[Ipv6AddressCount](#cfn-ec2-instance-ipv6addresscount)" : {{Integer}},
      "[Ipv6Addresses](#cfn-ec2-instance-ipv6addresses)" : {{[ InstanceIpv6Address, ... ]}},
      "[KernelId](#cfn-ec2-instance-kernelid)" : {{String}},
      "[KeyName](#cfn-ec2-instance-keyname)" : {{String}},
      "[LaunchTemplate](#cfn-ec2-instance-launchtemplate)" : {{LaunchTemplateSpecification}},
      "[LicenseSpecifications](#cfn-ec2-instance-licensespecifications)" : {{[ LicenseSpecification, ... ]}},
      "[MetadataOptions](#cfn-ec2-instance-metadataoptions)" : {{MetadataOptions}},
      "[Monitoring](#cfn-ec2-instance-monitoring)" : {{Boolean}},
      "[NetworkInterfaces](#cfn-ec2-instance-networkinterfaces)" : {{[ NetworkInterface, ... ]}},
      "[PlacementGroupName](#cfn-ec2-instance-placementgroupname)" : {{String}},
      "[PrivateDnsNameOptions](#cfn-ec2-instance-privatednsnameoptions)" : {{PrivateDnsNameOptions}},
      "[PrivateIpAddress](#cfn-ec2-instance-privateipaddress)" : {{String}},
      "[PropagateTagsToVolumeOnCreation](#cfn-ec2-instance-propagatetagstovolumeoncreation)" : {{Boolean}},
      "[RamdiskId](#cfn-ec2-instance-ramdiskid)" : {{String}},
      "[SecurityGroupIds](#cfn-ec2-instance-securitygroupids)" : {{[ String, ... ]}},
      "[SecurityGroups](#cfn-ec2-instance-securitygroups)" : {{[ String, ... ]}},
      "[SourceDestCheck](#cfn-ec2-instance-sourcedestcheck)" : {{Boolean}},
      "[SsmAssociations](#cfn-ec2-instance-ssmassociations)" : {{[ SsmAssociation, ... ]}},
      "[SubnetId](#cfn-ec2-instance-subnetid)" : {{String}},
      "[Tags](#cfn-ec2-instance-tags)" : {{[ Tag, ... ]}},
      "[Tenancy](#cfn-ec2-instance-tenancy)" : {{String}},
      "[UserData](#cfn-ec2-instance-userdata)" : {{String}},
      "[Volumes](#cfn-ec2-instance-volumes)" : {{[ Volume, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ec2-instance-syntax.yaml"></a>

```
Type: AWS::EC2::Instance
Properties:
  [AdditionalInfo](#cfn-ec2-instance-additionalinfo): {{String}}
  [Affinity](#cfn-ec2-instance-affinity): {{String}}
  [AvailabilityZone](#cfn-ec2-instance-availabilityzone): {{String}}
  [BlockDeviceMappings](#cfn-ec2-instance-blockdevicemappings): {{
    - BlockDeviceMapping}}
  [CpuOptions](#cfn-ec2-instance-cpuoptions): {{
    CpuOptions}}
  [CreditSpecification](#cfn-ec2-instance-creditspecification): {{
    CreditSpecification}}
  [DisableApiTermination](#cfn-ec2-instance-disableapitermination): {{Boolean}}
  [EbsOptimized](#cfn-ec2-instance-ebsoptimized): {{Boolean}}
  [ElasticGpuSpecifications](#cfn-ec2-instance-elasticgpuspecifications): {{
    - ElasticGpuSpecification}}
  [ElasticInferenceAccelerators](#cfn-ec2-instance-elasticinferenceaccelerators): {{
    - ElasticInferenceAccelerator}}
  [EnclaveOptions](#cfn-ec2-instance-enclaveoptions): {{
    EnclaveOptions}}
  [HibernationOptions](#cfn-ec2-instance-hibernationoptions): {{
    HibernationOptions}}
  [HostId](#cfn-ec2-instance-hostid): {{String}}
  [HostResourceGroupArn](#cfn-ec2-instance-hostresourcegrouparn): {{String}}
  [IamInstanceProfile](#cfn-ec2-instance-iaminstanceprofile): {{String}}
  [ImageId](#cfn-ec2-instance-imageid): {{String}}
  [InstanceInitiatedShutdownBehavior](#cfn-ec2-instance-instanceinitiatedshutdownbehavior): {{String}}
  [InstanceType](#cfn-ec2-instance-instancetype): {{String}}
  [Ipv6AddressCount](#cfn-ec2-instance-ipv6addresscount): {{Integer}}
  [Ipv6Addresses](#cfn-ec2-instance-ipv6addresses): {{
    - InstanceIpv6Address}}
  [KernelId](#cfn-ec2-instance-kernelid): {{String}}
  [KeyName](#cfn-ec2-instance-keyname): {{String}}
  [LaunchTemplate](#cfn-ec2-instance-launchtemplate): {{
    LaunchTemplateSpecification}}
  [LicenseSpecifications](#cfn-ec2-instance-licensespecifications): {{
    - LicenseSpecification}}
  [MetadataOptions](#cfn-ec2-instance-metadataoptions): {{
    MetadataOptions}}
  [Monitoring](#cfn-ec2-instance-monitoring): {{Boolean}}
  [NetworkInterfaces](#cfn-ec2-instance-networkinterfaces): {{
    - NetworkInterface}}
  [PlacementGroupName](#cfn-ec2-instance-placementgroupname): {{String}}
  [PrivateDnsNameOptions](#cfn-ec2-instance-privatednsnameoptions): {{
    PrivateDnsNameOptions}}
  [PrivateIpAddress](#cfn-ec2-instance-privateipaddress): {{String}}
  [PropagateTagsToVolumeOnCreation](#cfn-ec2-instance-propagatetagstovolumeoncreation): {{Boolean}}
  [RamdiskId](#cfn-ec2-instance-ramdiskid): {{String}}
  [SecurityGroupIds](#cfn-ec2-instance-securitygroupids): {{
    - String}}
  [SecurityGroups](#cfn-ec2-instance-securitygroups): {{
    - String}}
  [SourceDestCheck](#cfn-ec2-instance-sourcedestcheck): {{Boolean}}
  [SsmAssociations](#cfn-ec2-instance-ssmassociations): {{
    - SsmAssociation}}
  [SubnetId](#cfn-ec2-instance-subnetid): {{String}}
  [Tags](#cfn-ec2-instance-tags): {{
    - Tag}}
  [Tenancy](#cfn-ec2-instance-tenancy): {{String}}
  [UserData](#cfn-ec2-instance-userdata): {{String}}
  [Volumes](#cfn-ec2-instance-volumes): {{
    - Volume}}
```

## Properties
<a name="aws-resource-ec2-instance-properties"></a>

`AdditionalInfo`  <a name="cfn-ec2-instance-additionalinfo"></a>
This property is reserved for internal use. If you use it, the stack fails with this error: `Bad property set: [Testing this property] (Service: AmazonEC2; Status Code: 400; Error Code: InvalidParameterCombination; Request ID: 0XXXXXX-49c7-4b40-8bcc-76885dcXXXXX)`.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Affinity`  <a name="cfn-ec2-instance-affinity"></a>
Indicates whether the instance is associated with a dedicated host. If you want the instance to always restart on the same host on which it was launched, specify `host`. If you want the instance to restart on any available host, but try to launch onto the last host it ran on (on a best-effort basis), specify `default`.
*Required*: No
*Type*: String
*Allowed values*: `default | host`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`AvailabilityZone`  <a name="cfn-ec2-instance-availabilityzone"></a>
The Availability Zone of the instance.
If not specified, an Availability Zone will be automatically chosen for you based on the load balancing criteria for the Region.
This parameter is not supported by [DescribeImageAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImageAttribute.html).
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BlockDeviceMappings`  <a name="cfn-ec2-instance-blockdevicemappings"></a>
The block device mapping entries that defines the block devices to attach to the instance at launch.
By default, the block devices specified in the block device mapping for the AMI are used. You can override the AMI block device mapping using the instance block device mapping. For the root volume, you can override only the volume size, volume type, volume encryption settings, and the `DeleteOnTermination` setting.
After the instance is running, you can modify only the `DeleteOnTermination` parameter for the attached volumes without interrupting the instance. Modifying any other parameter results in instance [ replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement).
*Required*: No
*Type*: Array of [BlockDeviceMapping](aws-properties-ec2-instance-blockdevicemapping.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`CpuOptions`  <a name="cfn-ec2-instance-cpuoptions"></a>
The CPU options for the instance. For more information, see [Optimize CPU options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html) in the *Amazon Elastic Compute Cloud User Guide*.
*Required*: No
*Type*: [CpuOptions](aws-properties-ec2-instance-cpuoptions.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CreditSpecification`  <a name="cfn-ec2-instance-creditspecification"></a>
The credit option for CPU usage of the burstable performance instance. Valid values are `standard` and `unlimited`. To change this attribute after launch, use [ ModifyInstanceCreditSpecification](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceCreditSpecification.html). For more information, see [Burstable performance instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html) in the *Amazon EC2 User Guide*.
Default: `standard` (T2 instances) or `unlimited` (T3/T3a/T4g instances)
For T3 instances with `host` tenancy, only `standard` is supported.
*Required*: No
*Type*: [CreditSpecification](aws-properties-ec2-instance-creditspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisableApiTermination`  <a name="cfn-ec2-instance-disableapitermination"></a>
Indicates whether termination protection is enabled for the instance. The default is `false`, which means that you can terminate the instance using the Amazon EC2 console, command line tools, or API. You can enable termination protection when you launch an instance, while the instance is running, or while the instance is stopped.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EbsOptimized`  <a name="cfn-ec2-instance-ebsoptimized"></a>
Indicates whether the instance is optimized for Amazon EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal Amazon EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS-optimized instance.
Default: `false`
*Required*: No
*Type*: Boolean
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`ElasticGpuSpecifications`  <a name="cfn-ec2-instance-elasticgpuspecifications"></a>
An elastic GPU to associate with the instance.
Amazon Elastic Graphics reached end of life on January 8, 2024.
*Required*: No
*Type*: Array of [ElasticGpuSpecification](aws-properties-ec2-instance-elasticgpuspecification.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ElasticInferenceAccelerators`  <a name="cfn-ec2-instance-elasticinferenceaccelerators"></a>
An elastic inference accelerator to associate with the instance.
Amazon Elastic Inference is no longer available.
*Required*: No
*Type*: Array of [ElasticInferenceAccelerator](aws-properties-ec2-instance-elasticinferenceaccelerator.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnclaveOptions`  <a name="cfn-ec2-instance-enclaveoptions"></a>
Indicates whether the instance is enabled for AWS Nitro Enclaves.
*Required*: No
*Type*: [EnclaveOptions](aws-properties-ec2-instance-enclaveoptions.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HibernationOptions`  <a name="cfn-ec2-instance-hibernationoptions"></a>
Indicates whether an instance is enabled for hibernation. This parameter is valid only if the instance meets the [hibernation prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hibernating-prerequisites.html). For more information, see [Hibernate your Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html) in the *Amazon EC2 User Guide*.
You can't enable hibernation and AWS Nitro Enclaves on the same instance.
*Required*: No
*Type*: [HibernationOptions](aws-properties-ec2-instance-hibernationoptions.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HostId`  <a name="cfn-ec2-instance-hostid"></a>
If you specify host for the `Affinity` property, the ID of a dedicated host that the instance is associated with. If you don't specify an ID, Amazon EC2 launches the instance onto any available, compatible dedicated host in your account. This type of launch is called an untargeted launch. Note that for untargeted launches, you must have a compatible, dedicated host available to successfully launch instances.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`HostResourceGroupArn`  <a name="cfn-ec2-instance-hostresourcegrouparn"></a>
The ARN of the host resource group in which to launch the instances. If you specify a host resource group ARN, omit the **Tenancy** parameter or set it to `host`.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IamInstanceProfile`  <a name="cfn-ec2-instance-iaminstanceprofile"></a>
The name of an IAM instance profile. To create a new IAM instance profile, use the [AWS::IAM::InstanceProfile](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html) resource.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageId`  <a name="cfn-ec2-instance-imageid"></a>
The ID of the AMI. An AMI ID is required to launch an instance and must be specified here or in a launch template.
*Required*: Conditional
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstanceInitiatedShutdownBehavior`  <a name="cfn-ec2-instance-instanceinitiatedshutdownbehavior"></a>
Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).
Default: `stop`
*Required*: No
*Type*: String
*Allowed values*: `stop | terminate`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceType`  <a name="cfn-ec2-instance-instancetype"></a>
The instance type. For more information, see [Instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon EC2 User Guide*.
When you change your EBS-backed instance type, instance restart or replacement behavior depends on the instance type compatibility between the old and new types. An instance with an instance store volume as the root volume is always replaced. For more information, see [Change the instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html) in the *Amazon EC2 User Guide*.
*Required*: No
*Type*: String
*Allowed values*: `a1.medium | a1.large | a1.xlarge | a1.2xlarge | a1.4xlarge | a1.metal | c1.medium | c1.xlarge | c3.large | c3.xlarge | c3.2xlarge | c3.4xlarge | c3.8xlarge | c4.large | c4.xlarge | c4.2xlarge | c4.4xlarge | c4.8xlarge | c5.large | c5.xlarge | c5.2xlarge | c5.4xlarge | c5.9xlarge | c5.12xlarge | c5.18xlarge | c5.24xlarge | c5.metal | c5a.large | c5a.xlarge | c5a.2xlarge | c5a.4xlarge | c5a.8xlarge | c5a.12xlarge | c5a.16xlarge | c5a.24xlarge | c5ad.large | c5ad.xlarge | c5ad.2xlarge | c5ad.4xlarge | c5ad.8xlarge | c5ad.12xlarge | c5ad.16xlarge | c5ad.24xlarge | c5d.large | c5d.xlarge | c5d.2xlarge | c5d.4xlarge | c5d.9xlarge | c5d.12xlarge | c5d.18xlarge | c5d.24xlarge | c5d.metal | c5n.large | c5n.xlarge | c5n.2xlarge | c5n.4xlarge | c5n.9xlarge | c5n.18xlarge | c5n.metal | c6g.medium | c6g.large | c6g.xlarge | c6g.2xlarge | c6g.4xlarge | c6g.8xlarge | c6g.12xlarge | c6g.16xlarge | c6g.metal | c6gd.medium | c6gd.large | c6gd.xlarge | c6gd.2xlarge | c6gd.4xlarge | c6gd.8xlarge | c6gd.12xlarge | c6gd.16xlarge | c6gd.metal | c6gn.medium | c6gn.large | c6gn.xlarge | c6gn.2xlarge | c6gn.4xlarge | c6gn.8xlarge | c6gn.12xlarge | c6gn.16xlarge | c6i.large | c6i.xlarge | c6i.2xlarge | c6i.4xlarge | c6i.8xlarge | c6i.12xlarge | c6i.16xlarge | c6i.24xlarge | c6i.32xlarge | c6i.metal | cc1.4xlarge | cc2.8xlarge | cg1.4xlarge | cr1.8xlarge | d2.xlarge | d2.2xlarge | d2.4xlarge | d2.8xlarge | d3.xlarge | d3.2xlarge | d3.4xlarge | d3.8xlarge | d3en.xlarge | d3en.2xlarge | d3en.4xlarge | d3en.6xlarge | d3en.8xlarge | d3en.12xlarge | dl1.24xlarge | f1.2xlarge | f1.4xlarge | f1.16xlarge | g2.2xlarge | g2.8xlarge | g3.4xlarge | g3.8xlarge | g3.16xlarge | g3s.xlarge | g4ad.xlarge | g4ad.2xlarge | g4ad.4xlarge | g4ad.8xlarge | g4ad.16xlarge | g4dn.xlarge | g4dn.2xlarge | g4dn.4xlarge | g4dn.8xlarge | g4dn.12xlarge | g4dn.16xlarge | g4dn.metal | g5.xlarge | g5.2xlarge | g5.4xlarge | g5.8xlarge | g5.12xlarge | g5.16xlarge | g5.24xlarge | g5.48xlarge | g5g.xlarge | g5g.2xlarge | g5g.4xlarge | g5g.8xlarge | g5g.16xlarge | g5g.metal | hi1.4xlarge | hpc6a.48xlarge | hs1.8xlarge | h1.2xlarge | h1.4xlarge | h1.8xlarge | h1.16xlarge | i2.xlarge | i2.2xlarge | i2.4xlarge | i2.8xlarge | i3.large | i3.xlarge | i3.2xlarge | i3.4xlarge | i3.8xlarge | i3.16xlarge | i3.metal | i3en.large | i3en.xlarge | i3en.2xlarge | i3en.3xlarge | i3en.6xlarge | i3en.12xlarge | i3en.24xlarge | i3en.metal | im4gn.large | im4gn.xlarge | im4gn.2xlarge | im4gn.4xlarge | im4gn.8xlarge | im4gn.16xlarge | inf1.xlarge | inf1.2xlarge | inf1.6xlarge | inf1.24xlarge | is4gen.medium | is4gen.large | is4gen.xlarge | is4gen.2xlarge | is4gen.4xlarge | is4gen.8xlarge | m1.small | m1.medium | m1.large | m1.xlarge | m2.xlarge | m2.2xlarge | m2.4xlarge | m3.medium | m3.large | m3.xlarge | m3.2xlarge | m4.large | m4.xlarge | m4.2xlarge | m4.4xlarge | m4.10xlarge | m4.16xlarge | m5.large | m5.xlarge | m5.2xlarge | m5.4xlarge | m5.8xlarge | m5.12xlarge | m5.16xlarge | m5.24xlarge | m5.metal | m5a.large | m5a.xlarge | m5a.2xlarge | m5a.4xlarge | m5a.8xlarge | m5a.12xlarge | m5a.16xlarge | m5a.24xlarge | m5ad.large | m5ad.xlarge | m5ad.2xlarge | m5ad.4xlarge | m5ad.8xlarge | m5ad.12xlarge | m5ad.16xlarge | m5ad.24xlarge | m5d.large | m5d.xlarge | m5d.2xlarge | m5d.4xlarge | m5d.8xlarge | m5d.12xlarge | m5d.16xlarge | m5d.24xlarge | m5d.metal | m5dn.large | m5dn.xlarge | m5dn.2xlarge | m5dn.4xlarge | m5dn.8xlarge | m5dn.12xlarge | m5dn.16xlarge | m5dn.24xlarge | m5dn.metal | m5n.large | m5n.xlarge | m5n.2xlarge | m5n.4xlarge | m5n.8xlarge | m5n.12xlarge | m5n.16xlarge | m5n.24xlarge | m5n.metal | m5zn.large | m5zn.xlarge | m5zn.2xlarge | m5zn.3xlarge | m5zn.6xlarge | m5zn.12xlarge | m5zn.metal | m6a.large | m6a.xlarge | m6a.2xlarge | m6a.4xlarge | m6a.8xlarge | m6a.12xlarge | m6a.16xlarge | m6a.24xlarge | m6a.32xlarge | m6a.48xlarge | m6g.metal | m6g.medium | m6g.large | m6g.xlarge | m6g.2xlarge | m6g.4xlarge | m6g.8xlarge | m6g.12xlarge | m6g.16xlarge | m6gd.metal | m6gd.medium | m6gd.large | m6gd.xlarge | m6gd.2xlarge | m6gd.4xlarge | m6gd.8xlarge | m6gd.12xlarge | m6gd.16xlarge | m6i.large | m6i.xlarge | m6i.2xlarge | m6i.4xlarge | m6i.8xlarge | m6i.12xlarge | m6i.16xlarge | m6i.24xlarge | m6i.32xlarge | m6i.metal | mac1.metal | p2.xlarge | p2.8xlarge | p2.16xlarge | p3.2xlarge | p3.8xlarge | p3.16xlarge | p3dn.24xlarge | p4d.24xlarge | r3.large | r3.xlarge | r3.2xlarge | r3.4xlarge | r3.8xlarge | r4.large | r4.xlarge | r4.2xlarge | r4.4xlarge | r4.8xlarge | r4.16xlarge | r5.large | r5.xlarge | r5.2xlarge | r5.4xlarge | r5.8xlarge | r5.12xlarge | r5.16xlarge | r5.24xlarge | r5.metal | r5a.large | r5a.xlarge | r5a.2xlarge | r5a.4xlarge | r5a.8xlarge | r5a.12xlarge | r5a.16xlarge | r5a.24xlarge | r5ad.large | r5ad.xlarge | r5ad.2xlarge | r5ad.4xlarge | r5ad.8xlarge | r5ad.12xlarge | r5ad.16xlarge | r5ad.24xlarge | r5b.large | r5b.xlarge | r5b.2xlarge | r5b.4xlarge | r5b.8xlarge | r5b.12xlarge | r5b.16xlarge | r5b.24xlarge | r5b.metal | r5d.large | r5d.xlarge | r5d.2xlarge | r5d.4xlarge | r5d.8xlarge | r5d.12xlarge | r5d.16xlarge | r5d.24xlarge | r5d.metal | r5dn.large | r5dn.xlarge | r5dn.2xlarge | r5dn.4xlarge | r5dn.8xlarge | r5dn.12xlarge | r5dn.16xlarge | r5dn.24xlarge | r5dn.metal | r5n.large | r5n.xlarge | r5n.2xlarge | r5n.4xlarge | r5n.8xlarge | r5n.12xlarge | r5n.16xlarge | r5n.24xlarge | r5n.metal | r6g.medium | r6g.large | r6g.xlarge | r6g.2xlarge | r6g.4xlarge | r6g.8xlarge | r6g.12xlarge | r6g.16xlarge | r6g.metal | r6gd.medium | r6gd.large | r6gd.xlarge | r6gd.2xlarge | r6gd.4xlarge | r6gd.8xlarge | r6gd.12xlarge | r6gd.16xlarge | r6gd.metal | r6i.large | r6i.xlarge | r6i.2xlarge | r6i.4xlarge | r6i.8xlarge | r6i.12xlarge | r6i.16xlarge | r6i.24xlarge | r6i.32xlarge | r6i.metal | t1.micro | t2.nano | t2.micro | t2.small | t2.medium | t2.large | t2.xlarge | t2.2xlarge | t3.nano | t3.micro | t3.small | t3.medium | t3.large | t3.xlarge | t3.2xlarge | t3a.nano | t3a.micro | t3a.small | t3a.medium | t3a.large | t3a.xlarge | t3a.2xlarge | t4g.nano | t4g.micro | t4g.small | t4g.medium | t4g.large | t4g.xlarge | t4g.2xlarge | u-6tb1.56xlarge | u-6tb1.112xlarge | u-9tb1.112xlarge | u-12tb1.112xlarge | u-6tb1.metal | u-9tb1.metal | u-12tb1.metal | u-18tb1.metal | u-24tb1.metal | vt1.3xlarge | vt1.6xlarge | vt1.24xlarge | x1.16xlarge | x1.32xlarge | x1e.xlarge | x1e.2xlarge | x1e.4xlarge | x1e.8xlarge | x1e.16xlarge | x1e.32xlarge | x2iezn.2xlarge | x2iezn.4xlarge | x2iezn.6xlarge | x2iezn.8xlarge | x2iezn.12xlarge | x2iezn.metal | x2gd.medium | x2gd.large | x2gd.xlarge | x2gd.2xlarge | x2gd.4xlarge | x2gd.8xlarge | x2gd.12xlarge | x2gd.16xlarge | x2gd.metal | z1d.large | z1d.xlarge | z1d.2xlarge | z1d.3xlarge | z1d.6xlarge | z1d.12xlarge | z1d.metal | x2idn.16xlarge | x2idn.24xlarge | x2idn.32xlarge | x2iedn.xlarge | x2iedn.2xlarge | x2iedn.4xlarge | x2iedn.8xlarge | x2iedn.16xlarge | x2iedn.24xlarge | x2iedn.32xlarge | c6a.large | c6a.xlarge | c6a.2xlarge | c6a.4xlarge | c6a.8xlarge | c6a.12xlarge | c6a.16xlarge | c6a.24xlarge | c6a.32xlarge | c6a.48xlarge | c6a.metal | m6a.metal | i4i.large | i4i.xlarge | i4i.2xlarge | i4i.4xlarge | i4i.8xlarge | i4i.16xlarge | i4i.32xlarge | i4i.metal | x2idn.metal | x2iedn.metal | c7g.medium | c7g.large | c7g.xlarge | c7g.2xlarge | c7g.4xlarge | c7g.8xlarge | c7g.12xlarge | c7g.16xlarge | mac2.metal | c6id.large | c6id.xlarge | c6id.2xlarge | c6id.4xlarge | c6id.8xlarge | c6id.12xlarge | c6id.16xlarge | c6id.24xlarge | c6id.32xlarge | c6id.metal | m6id.large | m6id.xlarge | m6id.2xlarge | m6id.4xlarge | m6id.8xlarge | m6id.12xlarge | m6id.16xlarge | m6id.24xlarge | m6id.32xlarge | m6id.metal | r6id.large | r6id.xlarge | r6id.2xlarge | r6id.4xlarge | r6id.8xlarge | r6id.12xlarge | r6id.16xlarge | r6id.24xlarge | r6id.32xlarge | r6id.metal | r6a.large | r6a.xlarge | r6a.2xlarge | r6a.4xlarge | r6a.8xlarge | r6a.12xlarge | r6a.16xlarge | r6a.24xlarge | r6a.32xlarge | r6a.48xlarge | r6a.metal | p4de.24xlarge | u-3tb1.56xlarge | u-18tb1.112xlarge | u-24tb1.112xlarge | trn1.2xlarge | trn1.32xlarge | hpc6id.32xlarge | c6in.large | c6in.xlarge | c6in.2xlarge | c6in.4xlarge | c6in.8xlarge | c6in.12xlarge | c6in.16xlarge | c6in.24xlarge | c6in.32xlarge | m6in.large | m6in.xlarge | m6in.2xlarge | m6in.4xlarge | m6in.8xlarge | m6in.12xlarge | m6in.16xlarge | m6in.24xlarge | m6in.32xlarge | m6idn.large | m6idn.xlarge | m6idn.2xlarge | m6idn.4xlarge | m6idn.8xlarge | m6idn.12xlarge | m6idn.16xlarge | m6idn.24xlarge | m6idn.32xlarge | r6in.large | r6in.xlarge | r6in.2xlarge | r6in.4xlarge | r6in.8xlarge | r6in.12xlarge | r6in.16xlarge | r6in.24xlarge | r6in.32xlarge | r6idn.large | r6idn.xlarge | r6idn.2xlarge | r6idn.4xlarge | r6idn.8xlarge | r6idn.12xlarge | r6idn.16xlarge | r6idn.24xlarge | r6idn.32xlarge | c7g.metal | m7g.medium | m7g.large | m7g.xlarge | m7g.2xlarge | m7g.4xlarge | m7g.8xlarge | m7g.12xlarge | m7g.16xlarge | m7g.metal | r7g.medium | r7g.large | r7g.xlarge | r7g.2xlarge | r7g.4xlarge | r7g.8xlarge | r7g.12xlarge | r7g.16xlarge | r7g.metal | c6in.metal | m6in.metal | m6idn.metal | r6in.metal | r6idn.metal | inf2.xlarge | inf2.8xlarge | inf2.24xlarge | inf2.48xlarge | trn1n.32xlarge | i4g.large | i4g.xlarge | i4g.2xlarge | i4g.4xlarge | i4g.8xlarge | i4g.16xlarge | hpc7g.4xlarge | hpc7g.8xlarge | hpc7g.16xlarge | c7gn.medium | c7gn.large | c7gn.xlarge | c7gn.2xlarge | c7gn.4xlarge | c7gn.8xlarge | c7gn.12xlarge | c7gn.16xlarge | p5.48xlarge | m7i.large | m7i.xlarge | m7i.2xlarge | m7i.4xlarge | m7i.8xlarge | m7i.12xlarge | m7i.16xlarge | m7i.24xlarge | m7i.48xlarge | m7i-flex.large | m7i-flex.xlarge | m7i-flex.2xlarge | m7i-flex.4xlarge | m7i-flex.8xlarge | m7a.medium | m7a.large | m7a.xlarge | m7a.2xlarge | m7a.4xlarge | m7a.8xlarge | m7a.12xlarge | m7a.16xlarge | m7a.24xlarge | m7a.32xlarge | m7a.48xlarge | m7a.metal-48xl | hpc7a.12xlarge | hpc7a.24xlarge | hpc7a.48xlarge | hpc7a.96xlarge | c7gd.medium | c7gd.large | c7gd.xlarge | c7gd.2xlarge | c7gd.4xlarge | c7gd.8xlarge | c7gd.12xlarge | c7gd.16xlarge | m7gd.medium | m7gd.large | m7gd.xlarge | m7gd.2xlarge | m7gd.4xlarge | m7gd.8xlarge | m7gd.12xlarge | m7gd.16xlarge | r7gd.medium | r7gd.large | r7gd.xlarge | r7gd.2xlarge | r7gd.4xlarge | r7gd.8xlarge | r7gd.12xlarge | r7gd.16xlarge | r7a.medium | r7a.large | r7a.xlarge | r7a.2xlarge | r7a.4xlarge | r7a.8xlarge | r7a.12xlarge | r7a.16xlarge | r7a.24xlarge | r7a.32xlarge | r7a.48xlarge | c7i.large | c7i.xlarge | c7i.2xlarge | c7i.4xlarge | c7i.8xlarge | c7i.12xlarge | c7i.16xlarge | c7i.24xlarge | c7i.48xlarge | mac2-m2pro.metal | r7iz.large | r7iz.xlarge | r7iz.2xlarge | r7iz.4xlarge | r7iz.8xlarge | r7iz.12xlarge | r7iz.16xlarge | r7iz.32xlarge | c7a.medium | c7a.large | c7a.xlarge | c7a.2xlarge | c7a.4xlarge | c7a.8xlarge | c7a.12xlarge | c7a.16xlarge | c7a.24xlarge | c7a.32xlarge | c7a.48xlarge | c7a.metal-48xl | r7a.metal-48xl | r7i.large | r7i.xlarge | r7i.2xlarge | r7i.4xlarge | r7i.8xlarge | r7i.12xlarge | r7i.16xlarge | r7i.24xlarge | r7i.48xlarge | dl2q.24xlarge | mac2-m2.metal | i4i.12xlarge | i4i.24xlarge | c7i.metal-24xl | c7i.metal-48xl | m7i.metal-24xl | m7i.metal-48xl | r7i.metal-24xl | r7i.metal-48xl | r7iz.metal-16xl | r7iz.metal-32xl | c7gd.metal | m7gd.metal | r7gd.metal | g6.xlarge | g6.2xlarge | g6.4xlarge | g6.8xlarge | g6.12xlarge | g6.16xlarge | g6.24xlarge | g6.48xlarge | gr6.4xlarge | gr6.8xlarge | c7i-flex.large | c7i-flex.xlarge | c7i-flex.2xlarge | c7i-flex.4xlarge | c7i-flex.8xlarge | u7i-12tb.224xlarge | u7in-16tb.224xlarge | u7in-24tb.224xlarge | u7in-32tb.224xlarge | u7ib-12tb.224xlarge | c7gn.metal | r8g.medium | r8g.large | r8g.xlarge | r8g.2xlarge | r8g.4xlarge | r8g.8xlarge | r8g.12xlarge | r8g.16xlarge | r8g.24xlarge | r8g.48xlarge | r8g.metal-24xl | r8g.metal-48xl | mac2-m1ultra.metal | g6e.xlarge | g6e.2xlarge | g6e.4xlarge | g6e.8xlarge | g6e.12xlarge | g6e.16xlarge | g6e.24xlarge | g6e.48xlarge | c8g.medium | c8g.large | c8g.xlarge | c8g.2xlarge | c8g.4xlarge | c8g.8xlarge | c8g.12xlarge | c8g.16xlarge | c8g.24xlarge | c8g.48xlarge | c8g.metal-24xl | c8g.metal-48xl | m8g.medium | m8g.large | m8g.xlarge | m8g.2xlarge | m8g.4xlarge | m8g.8xlarge | m8g.12xlarge | m8g.16xlarge | m8g.24xlarge | m8g.48xlarge | m8g.metal-24xl | m8g.metal-48xl | x8g.medium | x8g.large | x8g.xlarge | x8g.2xlarge | x8g.4xlarge | x8g.8xlarge | x8g.12xlarge | x8g.16xlarge | x8g.24xlarge | x8g.48xlarge | x8g.metal-24xl | x8g.metal-48xl | i7ie.large | i7ie.xlarge | i7ie.2xlarge | i7ie.3xlarge | i7ie.6xlarge | i7ie.12xlarge | i7ie.18xlarge | i7ie.24xlarge | i7ie.48xlarge | i8g.large | i8g.xlarge | i8g.2xlarge | i8g.4xlarge | i8g.8xlarge | i8g.12xlarge | i8g.16xlarge | i8g.24xlarge | i8g.metal-24xl | u7i-6tb.112xlarge | u7i-8tb.112xlarge | u7inh-32tb.480xlarge | p5e.48xlarge | p5en.48xlarge | f2.12xlarge | f2.48xlarge | trn2.48xlarge | c7i-flex.12xlarge | c7i-flex.16xlarge | m7i-flex.12xlarge | m7i-flex.16xlarge | i7ie.metal-24xl | i7ie.metal-48xl | i8g.48xlarge | c8gd.medium | c8gd.large | c8gd.xlarge | c8gd.2xlarge | c8gd.4xlarge | c8gd.8xlarge | c8gd.12xlarge | c8gd.16xlarge | c8gd.24xlarge | c8gd.48xlarge | c8gd.metal-24xl | c8gd.metal-48xl | i7i.large | i7i.xlarge | i7i.2xlarge | i7i.4xlarge | i7i.8xlarge | i7i.12xlarge | i7i.16xlarge | i7i.24xlarge | i7i.48xlarge | i7i.metal-24xl | i7i.metal-48xl | p6-b200.48xlarge | m8gd.medium | m8gd.large | m8gd.xlarge | m8gd.2xlarge | m8gd.4xlarge | m8gd.8xlarge | m8gd.12xlarge | m8gd.16xlarge | m8gd.24xlarge | m8gd.48xlarge | m8gd.metal-24xl | m8gd.metal-48xl | r8gd.medium | r8gd.large | r8gd.xlarge | r8gd.2xlarge | r8gd.4xlarge | r8gd.8xlarge | r8gd.12xlarge | r8gd.16xlarge | r8gd.24xlarge | r8gd.48xlarge | r8gd.metal-24xl | r8gd.metal-48xl | c8gn.medium | c8gn.large | c8gn.xlarge | c8gn.2xlarge | c8gn.4xlarge | c8gn.8xlarge | c8gn.12xlarge | c8gn.16xlarge | c8gn.24xlarge | c8gn.48xlarge | c8gn.metal-24xl | c8gn.metal-48xl | f2.6xlarge | p6e-gb200.36xlarge | g6f.large | g6f.xlarge | g6f.2xlarge | g6f.4xlarge | gr6f.4xlarge | p5.4xlarge | r8i.large | r8i.xlarge | r8i.2xlarge | r8i.4xlarge | r8i.8xlarge | r8i.12xlarge | r8i.16xlarge | r8i.24xlarge | r8i.32xlarge | r8i.48xlarge | r8i.96xlarge | r8i.metal-48xl | r8i.metal-96xl | r8i-flex.large | r8i-flex.xlarge | r8i-flex.2xlarge | r8i-flex.4xlarge | r8i-flex.8xlarge | r8i-flex.12xlarge | r8i-flex.16xlarge`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Ipv6AddressCount`  <a name="cfn-ec2-instance-ipv6addresscount"></a>
The number of IPv6 addresses to associate with the primary network interface. Amazon EC2 chooses the IPv6 addresses from the range of your subnet. You cannot specify this option and the option to assign specific IPv6 addresses in the same request. You can specify this option if you've specified a minimum number of instances to launch.
You cannot specify this option and the network interfaces option in the same request.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Ipv6Addresses`  <a name="cfn-ec2-instance-ipv6addresses"></a>
The IPv6 addresses from the range of the subnet to associate with the primary network interface. You cannot specify this option and the option to assign a number of IPv6 addresses in the same request. You cannot specify this option if you've specified a minimum number of instances to launch.
You cannot specify this option and the network interfaces option in the same request.
*Required*: No
*Type*: Array of [InstanceIpv6Address](aws-properties-ec2-instance-instanceipv6address.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KernelId`  <a name="cfn-ec2-instance-kernelid"></a>
The ID of the kernel.
We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see [PV-GRUB](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedkernels.html) in the *Amazon EC2 User Guide*.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`KeyName`  <a name="cfn-ec2-instance-keyname"></a>
The name of the key pair. For more information, see [Create a key pair for your EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html).
If you do not specify a key pair, you can't connect to the instance unless you choose an AMI that is configured to allow users another way to log in.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LaunchTemplate`  <a name="cfn-ec2-instance-launchtemplate"></a>
The launch template. Any additional parameters that you specify for the new instance overwrite the corresponding parameters included in the launch template.
*Required*: No
*Type*: [LaunchTemplateSpecification](aws-properties-ec2-instance-launchtemplatespecification.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LicenseSpecifications`  <a name="cfn-ec2-instance-licensespecifications"></a>
The license configurations.
*Required*: No
*Type*: Array of [LicenseSpecification](aws-properties-ec2-instance-licensespecification.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MetadataOptions`  <a name="cfn-ec2-instance-metadataoptions"></a>
The metadata options for the instance.
*Required*: No
*Type*: [MetadataOptions](aws-properties-ec2-instance-metadataoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Monitoring`  <a name="cfn-ec2-instance-monitoring"></a>
Specifies whether detailed monitoring is enabled for the instance. Specify `true` to enable detailed monitoring. Otherwise, basic monitoring is enabled. For more information about detailed monitoring, see [Enable or turn off detailed monitoring for your instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch-new.html) in the *Amazon EC2 User Guide*.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkInterfaces`  <a name="cfn-ec2-instance-networkinterfaces"></a>
The network interfaces to associate with the instance.
If you use this property to point to a network interface, you must terminate the original interface before attaching a new one to allow the update of the instance to succeed.
If this resource has a public IP address and is also in a VPC that is defined in the same template, you must use the [ DependsOn Attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html) to declare a dependency on the VPC-gateway attachment.
*Required*: No
*Type*: Array of [NetworkInterface](aws-properties-ec2-instance-networkinterface.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PlacementGroupName`  <a name="cfn-ec2-instance-placementgroupname"></a>
The name of an existing placement group that you want to launch the instance into (cluster \| partition \| spread).
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrivateDnsNameOptions`  <a name="cfn-ec2-instance-privatednsnameoptions"></a>
The options for the instance hostname.
*Required*: No
*Type*: [PrivateDnsNameOptions](aws-properties-ec2-instance-privatednsnameoptions.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`PrivateIpAddress`  <a name="cfn-ec2-instance-privateipaddress"></a>
The primary IPv4 address. You must specify a value from the IPv4 address range of the subnet.
Only one private IP address can be designated as primary. You can't specify this option if you've specified the option to designate a private IP address as the primary IP address in a network interface specification. You cannot specify this option if you're launching more than one instance in the request.
You cannot specify this option and the network interfaces option in the same request.
If you make an update to an instance that requires replacement, you must assign a new private IP address. During a replacement, AWS CloudFormation creates a new instance but doesn't delete the old instance until the stack has successfully updated. If the stack update fails, AWS CloudFormation uses the old instance to roll back the stack to the previous working state. The old and new instances cannot have the same private IP address.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PropagateTagsToVolumeOnCreation`  <a name="cfn-ec2-instance-propagatetagstovolumeoncreation"></a>
Indicates whether to assign the tags specified in the `Tags` property to the volumes specified in the `BlockDeviceMappings` property.
Note that using this feature does not assign the tags to volumes that are created separately and then attached using `AWS::EC2::VolumeAttachment`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RamdiskId`  <a name="cfn-ec2-instance-ramdiskid"></a>
The ID of the RAM disk to select. Some kernels require additional drivers at launch. Check the kernel requirements for information about whether you need to specify a RAM disk. To find kernel requirements, go to the AWS Resource Center and search for the kernel ID.
We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see [PV-GRUB](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedkernels.html) in the *Amazon EC2 User Guide*.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`SecurityGroupIds`  <a name="cfn-ec2-instance-securitygroupids"></a>
The IDs of the security groups. You can specify the IDs of existing security groups and references to resources created by the stack template.
If you specify a network interface, you must specify any security groups as part of the network interface.
*Required*: Conditional
*Type*: Array of String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`SecurityGroups`  <a name="cfn-ec2-instance-securitygroups"></a>
[Default VPC] The names of the security groups. For a nondefault VPC, you must use security group IDs instead.
You cannot specify this option and the network interfaces option in the same request. The list can contain both the name of existing Amazon EC2 security groups or references to AWS::EC2::SecurityGroup resources created in the template.
Default: Amazon EC2 uses the default security group.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceDestCheck`  <a name="cfn-ec2-instance-sourcedestcheck"></a>
Enable or disable source/destination checks, which ensure that the instance is either the source or the destination of any traffic that it receives. If the value is `true`, source/destination checks are enabled; otherwise, they are disabled. The default value is `true`. You must disable source/destination checks if the instance runs services such as network address translation, routing, or firewalls.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SsmAssociations`  <a name="cfn-ec2-instance-ssmassociations"></a>
The SSM [ document](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html) and parameter values in AWS Systems Manager to associate with this instance. To use this property, you must specify an IAM instance profile role for the instance. For more information, see [Create an IAM instance profile for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-configuring-access-role.html) in the *AWS Systems Manager User Guide*.
You can associate only one document with an instance.
*Required*: No
*Type*: Array of [SsmAssociation](aws-properties-ec2-instance-ssmassociation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetId`  <a name="cfn-ec2-instance-subnetid"></a>
The ID of the subnet to launch the instance into.
If you specify a network interface, you must specify any subnets as part of the network interface instead of using this parameter.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ec2-instance-tags"></a>
The tags to add to the instance. These tags are not applied to the EBS volumes, such as the root volume, unless [PropagateTagsToVolumeOnCreation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-propagatetagstovolumeoncreation) is `true`.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-instance-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tenancy`  <a name="cfn-ec2-instance-tenancy"></a>
The tenancy of the instance. An instance with a tenancy of `dedicated` runs on single-tenant hardware.
*Required*: No
*Type*: String
*Allowed values*: `default | dedicated | host`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`UserData`  <a name="cfn-ec2-instance-userdata"></a>
The parameters or scripts to store as user data. Any scripts in user data are run when you launch the instance. User data is limited to 16 KB. You must provide base64-encoded text. For more information, see [Fn::Base64](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-base64.html).
If the root volume is an EBS volume and you update user data, CloudFormation restarts the instance. If the root volume is an instance store volume and you update user data, the instance is replaced.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Volumes`  <a name="cfn-ec2-instance-volumes"></a>
The volumes to attach to the instance.
*Required*: No
*Type*: Array of [Volume](aws-properties-ec2-instance-volume.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-instance-return-values"></a>

### Ref
<a name="aws-resource-ec2-instance-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the instance ID. For example: `i-1234567890abcdef0`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-instance-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-instance-return-values-fn--getatt-fn--getatt"></a>

`InstanceId`  <a name="InstanceId-fn::getatt"></a>
The ID of the instance.

`PrivateDnsName`  <a name="PrivateDnsName-fn::getatt"></a>
The private DNS name of the specified instance. For example: `ip-10-24-34-0.ec2.internal`.

`PrivateIp`  <a name="PrivateIp-fn::getatt"></a>
The private IP address of the specified instance. For example: `10.24.34.0`.

`PublicDnsName`  <a name="PublicDnsName-fn::getatt"></a>
The public DNS name of the specified instance. For example: `ec2-107-20-50-45.compute-1.amazonaws.com`.

`PublicIp`  <a name="PublicIp-fn::getatt"></a>
The public IP address of the specified instance. For example: `192.0.2.0`.

`VpcId`  <a name="VpcId-fn::getatt"></a>
The ID of the VPC in which the instance is running.

## Examples
<a name="aws-resource-ec2-instance--examples"></a>

**Topics**
+ [EC2 instance with an EBS block device mapping](#aws-resource-ec2-instance--examples--EC2_instance_with_an_EBS_block_device_mapping)
+ [EC2 instance with user data](#aws-resource-ec2-instance--examples--EC2_instance_with_user_data)
+ [Launch an instance from a launch template](#aws-resource-ec2-instance--examples--Launch_an_instance_from_a_launch_template)
+ [Automatically assign a public IP address](#aws-resource-ec2-instance--examples--Automatically_assign_a_public_IP_address)

### EC2 instance with an EBS block device mapping
<a name="aws-resource-ec2-instance--examples--EC2_instance_with_an_EBS_block_device_mapping"></a>

The following example creates an EC2 instance with a block device mapping with an entry that specifies an io1 volume with a size of 20 GB and an entry that uses NoDevice to override a device specified in the AMI block device mapping.

#### JSON
<a name="aws-resource-ec2-instance--examples--EC2_instance_with_an_EBS_block_device_mapping--json"></a>

```
"MyEC2Instance" : {
   "Type" : "AWS::EC2::Instance",
   "Properties" : {
      "ImageId" : "ami-79fd7eee",
      "KeyName" : "testkey",
      "BlockDeviceMappings" : [
         {
            "DeviceName" : "/dev/sdm",
            "Ebs" : {
              "VolumeType" : "io1",
              "Iops" : "200",
              "DeleteOnTermination" : "false",
              "VolumeSize" : "20"
            }
          },
          {
            "DeviceName" : "/dev/sdk",
            "NoDevice" : {}
          }
      ]
   }
}
```

#### YAML
<a name="aws-resource-ec2-instance--examples--EC2_instance_with_an_EBS_block_device_mapping--yaml"></a>

```
  MyEC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: "ami-79fd7eee"
      KeyName: "testkey"
      BlockDeviceMappings:
      - DeviceName: "/dev/sdm"
        Ebs:
          VolumeType: "io1"
          Iops: "200"
          DeleteOnTermination: "false"
          VolumeSize: "20"
      - DeviceName: "/dev/sdk"
        NoDevice: {}
```

### EC2 instance with user data
<a name="aws-resource-ec2-instance--examples--EC2_instance_with_user_data"></a>

The following example creates an EC2 instance with user data. The user data must be base64-encoded.

#### JSON
<a name="aws-resource-ec2-instance--examples--EC2_instance_with_user_data--json"></a>

```
{
    "Resources": {
        "myInstance": {
            "Type": "AWS::EC2::Instance",
            "Properties": {
                "ImageId": "ami-0a70b9d193ae8a799",
                "InstanceType": "t2.micro",
                "KeyName": "my-key-pair",
                "SecurityGroupIds": [
                    "sg-12a4c434"
                ],
                "UserData": {
                    "Fn::Base64": {
                        "Fn::Sub": "#!/bin/bash\nyum update -y\nservice httpd start\nchkconfig httpd on\n"
                    }
                }
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-ec2-instance--examples--EC2_instance_with_user_data--yaml"></a>

```
Resources:
   myInstance:
     Type: 'AWS::EC2::Instance'
     Properties:
        ImageId: ami-0a70b9d193ae8a799
        InstanceType: t2.micro
        KeyName: my-key-pair
        SecurityGroupIds:
          - sg-12a4c434
        UserData:
          Fn::Base64: !Sub |
             #!/bin/bash
             yum update -y
             service httpd start
             chkconfig httpd on
```

### Launch an instance from a launch template
<a name="aws-resource-ec2-instance--examples--Launch_an_instance_from_a_launch_template"></a>

You can use the parameters contained in a launch template to launch an instance. The following example defines a launch template that specifies an AMI, instance type, security group, and tag for the instance. It also enables access to the instance tags through instance metadata.

#### JSON
<a name="aws-resource-ec2-instance--examples--Launch_an_instance_from_a_launch_template--json"></a>

```
{
    "Resources": {
        "myInstance": {
            "Type": "AWS::EC2::Instance",
            "Properties": {
                "LaunchTemplate": {
                    "LaunchTemplateId": {
                        "Ref": "myLaunchTemplate"
                    },
                    "Version": {
                        "Fn::GetAtt": [
                            "myLaunchTemplate",
                            "DefaultVersionNumber"
                        ]
                    }
                }
            }
        },
        "myLaunchTemplate": {
            "Type": "AWS::EC2::LaunchTemplate",
            "Properties": {
                "LaunchTemplateData": {
                    "ImageId": "ami-0a70b9d193ae8a799",
                    "InstanceType": "t2.micro",
                    "MetadataOptions": {
                        "InstanceMetadataTags": "enabled"
                    },
                    "SecurityGroupIds": [
                        "sg-12a4c434"
                    ],
                    "TagSpecifications": [
                        {
                            "ResourceType": "instance",
                            "Tags": [
                                {
                                    "Key": "department",
                                    "Value": "dev"
                                }
                            ]
                        }
                    ]
                }
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-ec2-instance--examples--Launch_an_instance_from_a_launch_template--yaml"></a>

```
Resources:
   myInstance:
     Type: 'AWS::EC2::Instance'
     Properties:
        LaunchTemplate:
          LaunchTemplateId: !Ref myLaunchTemplate
          Version: !GetAtt myLaunchTemplate.DefaultVersionNumber
   myLaunchTemplate:
     Type: 'AWS::EC2::LaunchTemplate'
     Properties:
       LaunchTemplateData:
          ImageId: ami-0a70b9d193ae8a799
          InstanceType: t2.micro
          MetadataOptions:
            InstanceMetadataTags: enabled
          SecurityGroupIds:
            - sg-12a4c434
          TagSpecifications:
            - ResourceType: instance
              Tags:
              - Key: department
                Value: dev
```

### Automatically assign a public IP address
<a name="aws-resource-ec2-instance--examples--Automatically_assign_a_public_IP_address"></a>

You can associate a public IP address with a network interface only if it is the primary network interface (the device index is 0) and if you are creating a new network interface, not attaching an existing network interface.

#### JSON
<a name="aws-resource-ec2-instance--examples--Automatically_assign_a_public_IP_address--json"></a>

```
"Ec2Instance" : {
  "Type" : "AWS::EC2::Instance",
  "Properties" : {
    "ImageId" : { "Fn::FindInMap" : [ "RegionMap", { "Ref" : "AWS::Region" }, "AMI" ]},
    "KeyName" : { "Ref" : "KeyName" },
    "NetworkInterfaces": [ {
      "AssociatePublicIpAddress": "true",
      "DeviceIndex": "0",
      "GroupSet": [{ "Ref" : "myVPCEC2SecurityGroup" }],
      "SubnetId": { "Ref" : "PublicSubnet" }
    } ]
  }
}
```

#### YAML
<a name="aws-resource-ec2-instance--examples--Automatically_assign_a_public_IP_address--yaml"></a>

```
Ec2Instance:
  Type: AWS::EC2::Instance
  Properties:
    ImageId:
      Fn::FindInMap:
        - "RegionMap"
        - Ref: "AWS::Region"
        - "AMI"
    KeyName:
      Ref: "KeyName"
    NetworkInterfaces:
      - AssociatePublicIpAddress: "true"
        DeviceIndex: "0"
        GroupSet:
          - Ref: "myVPCEC2SecurityGroup"
        SubnetId:
          Ref: "PublicSubnet"
```

## See also
<a name="aws-resource-ec2-instance--seealso"></a>
+ [ RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html) in the *Amazon EC2 API Reference*
+ [ Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Instances.html) in the *Amazon EC2 User Guide*
