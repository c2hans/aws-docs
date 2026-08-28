---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestLaunchTemplateData.html
---

# RequestLaunchTemplateData
<a name="API_RequestLaunchTemplateData"></a>

The information to include in the launch template.

**Note**
You must specify at least one parameter for the launch template data.

## Contents
<a name="API_RequestLaunchTemplateData_Contents"></a>

 ** BlockDeviceMapping.N **
The block device mapping.
Type: Array of [LaunchTemplateBlockDeviceMappingRequest](API_LaunchTemplateBlockDeviceMappingRequest.md) objects
Required: No

 ** CapacityReservationSpecification **
The Capacity Reservation targeting option. If you do not specify this parameter, the instance's Capacity Reservation preference defaults to `open`, which enables it to run in any open Capacity Reservation that has matching attributes (instance type, platform, Availability Zone).
Type: [LaunchTemplateCapacityReservationSpecificationRequest](API_LaunchTemplateCapacityReservationSpecificationRequest.md) object
Required: No

 ** CpuOptions **
The CPU options for the instance. For more information, see [CPU options for Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html) in the *Amazon EC2 User Guide*.
Type: [LaunchTemplateCpuOptionsRequest](API_LaunchTemplateCpuOptionsRequest.md) object
Required: No

 ** CreditSpecification **
The credit option for CPU usage of the instance. Valid only for T instances.
Type: [CreditSpecificationRequest](API_CreditSpecificationRequest.md) object
Required: No

 ** DisableApiStop **
Indicates whether to enable the instance for stop protection. For more information, see [Enable stop protection for your EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-stop-protection.html) in the *Amazon EC2 User Guide*.
Type: Boolean
Required: No

 ** DisableApiTermination **
Indicates whether termination protection is enabled for the instance. The default is `false`, which means that you can terminate the instance using the Amazon EC2 console, command line tools, or API. You can enable termination protection when you launch an instance, while the instance is running, or while the instance is stopped.
Type: Boolean
Required: No

 ** EbsOptimized **
Indicates whether the instance is optimized for Amazon EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal Amazon EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS-optimized instance.
Type: Boolean
Required: No

 ** ElasticGpuSpecification.N **
Deprecated.
Amazon Elastic Graphics reached end of life on January 8, 2024.
Type: Array of [ElasticGpuSpecification](API_ElasticGpuSpecification.md) objects
Required: No

 ** ElasticInferenceAccelerator.N **
 *This member has been deprecated.*
Amazon Elastic Inference is no longer available.
An elastic inference accelerator to associate with the instance. Elastic inference accelerators are a resource you can attach to your Amazon EC2 instances to accelerate your Deep Learning (DL) inference workloads.
You cannot specify accelerators from different generations in the same request.
Type: Array of [LaunchTemplateElasticInferenceAccelerator](API_LaunchTemplateElasticInferenceAccelerator.md) objects
Required: No

 ** EnclaveOptions **
Indicates whether the instance is enabled for AWS Nitro Enclaves. For more information, see [What is Nitro Enclaves?](https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave.html) in the * AWS Nitro Enclaves User Guide*.
You can't enable AWS Nitro Enclaves and hibernation on the same instance.
Type: [LaunchTemplateEnclaveOptionsRequest](API_LaunchTemplateEnclaveOptionsRequest.md) object
Required: No

 ** HibernationOptions **
Indicates whether an instance is enabled for hibernation. This parameter is valid only if the instance meets the [hibernation prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hibernating-prerequisites.html). For more information, see [Hibernate your Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html) in the *Amazon EC2 User Guide*.
Type: [LaunchTemplateHibernationOptionsRequest](API_LaunchTemplateHibernationOptionsRequest.md) object
Required: No

 ** IamInstanceProfile **
The name or Amazon Resource Name (ARN) of an IAM instance profile.
Type: [LaunchTemplateIamInstanceProfileSpecificationRequest](API_LaunchTemplateIamInstanceProfileSpecificationRequest.md) object
Required: No

 ** ImageId **
The ID of the AMI in the format `ami-0ac394d6a3example`.
Alternatively, you can specify a Systems Manager parameter, using one of the following formats. The Systems Manager parameter will resolve to an AMI ID on launch.
To reference a public parameter:
+  `resolve:ssm:public-parameter `
To reference a parameter stored in the same account:
+  `resolve:ssm:parameter-name `
+  `resolve:ssm:parameter-name:version-number `
+  `resolve:ssm:parameter-name:label `
To reference a parameter shared from another AWS account:
+  `resolve:ssm:parameter-ARN `
+  `resolve:ssm:parameter-ARN:version-number `
+  `resolve:ssm:parameter-ARN:label `
For more information, see [Use a Systems Manager parameter instead of an AMI ID](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-launch-template.html#use-an-ssm-parameter-instead-of-an-ami-id) in the *Amazon EC2 User Guide*.
If the launch template will be used for an EC2 Fleet or Spot Fleet, note the following:
+ Only EC2 Fleets of type `instant` support specifying a Systems Manager parameter.
+ For EC2 Fleets of type `maintain` or `request`, or for Spot Fleets, you must specify the AMI ID.
Type: String
Required: No

 ** InstanceInitiatedShutdownBehavior **
Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).
Default: `stop`
Type: String
Valid Values: `stop | terminate`
Required: No

 ** InstanceMarketOptions **
The market (purchasing) option for the instances.
Type: [LaunchTemplateInstanceMarketOptionsRequest](API_LaunchTemplateInstanceMarketOptionsRequest.md) object
Required: No

 ** InstanceRequirements **
The attributes for the instance types. When you specify instance attributes, Amazon EC2 will identify instance types with these attributes.
You must specify `VCpuCount` and `MemoryMiB`. All other attributes are optional. Any unspecified optional attribute is set to its default.
When you specify multiple attributes, you get instance types that satisfy all of the specified attributes. If you specify multiple values for an attribute, you get instance types that satisfy any of the specified values.
To limit the list of instance types from which Amazon EC2 can identify matching instance types, you can use one of the following parameters, but not both in the same request:
+  `AllowedInstanceTypes` - The instance types to include in the list. All other instance types are ignored, even if they match your specified attributes.
+  `ExcludedInstanceTypes` - The instance types to exclude from the list, even if they match your specified attributes.
If you specify `InstanceRequirements`, you can't specify `InstanceType`.
Attribute-based instance type selection is only supported when using Auto Scaling groups, EC2 Fleet, and Spot Fleet to launch instances. If you plan to use the launch template in the [launch instance wizard](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.html), or with the [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html) API or [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html) AWS CloudFormation resource, you can't specify `InstanceRequirements`.
For more information, see [Specify attributes for instance type selection for EC2 Fleet or Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html) and [Spot placement score](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-placement-score.html) in the *Amazon EC2 User Guide*.
Type: [InstanceRequirementsRequest](API_InstanceRequirementsRequest.md) object
Required: No

 ** InstanceType **
The instance type. For more information, see [Amazon EC2 instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon EC2 User Guide*.
If you specify `InstanceType`, you can't specify `InstanceRequirements`.
Type: String
Valid Values: `a1.medium | a1.large | a1.xlarge | a1.2xlarge | a1.4xlarge | a1.metal | c1.medium | c1.xlarge | c3.large | c3.xlarge | c3.2xlarge | c3.4xlarge | c3.8xlarge | c4.large | c4.xlarge | c4.2xlarge | c4.4xlarge | c4.8xlarge | c5.large | c5.xlarge | c5.2xlarge | c5.4xlarge | c5.9xlarge | c5.12xlarge | c5.18xlarge | c5.24xlarge | c5.metal | c5a.large | c5a.xlarge | c5a.2xlarge | c5a.4xlarge | c5a.8xlarge | c5a.12xlarge | c5a.16xlarge | c5a.24xlarge | c5ad.large | c5ad.xlarge | c5ad.2xlarge | c5ad.4xlarge | c5ad.8xlarge | c5ad.12xlarge | c5ad.16xlarge | c5ad.24xlarge | c5d.large | c5d.xlarge | c5d.2xlarge | c5d.4xlarge | c5d.9xlarge | c5d.12xlarge | c5d.18xlarge | c5d.24xlarge | c5d.metal | c5n.large | c5n.xlarge | c5n.2xlarge | c5n.4xlarge | c5n.9xlarge | c5n.18xlarge | c5n.metal | c6g.medium | c6g.large | c6g.xlarge | c6g.2xlarge | c6g.4xlarge | c6g.8xlarge | c6g.12xlarge | c6g.16xlarge | c6g.metal | c6gd.medium | c6gd.large | c6gd.xlarge | c6gd.2xlarge | c6gd.4xlarge | c6gd.8xlarge | c6gd.12xlarge | c6gd.16xlarge | c6gd.metal | c6gn.medium | c6gn.large | c6gn.xlarge | c6gn.2xlarge | c6gn.4xlarge | c6gn.8xlarge | c6gn.12xlarge | c6gn.16xlarge | c6i.large | c6i.xlarge | c6i.2xlarge | c6i.4xlarge | c6i.8xlarge | c6i.12xlarge | c6i.16xlarge | c6i.24xlarge | c6i.32xlarge | c6i.metal | cc1.4xlarge | cc2.8xlarge | cg1.4xlarge | cr1.8xlarge | d2.xlarge | d2.2xlarge | d2.4xlarge | d2.8xlarge | d3.xlarge | d3.2xlarge | d3.4xlarge | d3.8xlarge | d3en.xlarge | d3en.2xlarge | d3en.4xlarge | d3en.6xlarge | d3en.8xlarge | d3en.12xlarge | dl1.24xlarge | f1.2xlarge | f1.4xlarge | f1.16xlarge | g2.2xlarge | g2.8xlarge | g3.4xlarge | g3.8xlarge | g3.16xlarge | g3s.xlarge | g4ad.xlarge | g4ad.2xlarge | g4ad.4xlarge | g4ad.8xlarge | g4ad.16xlarge | g4dn.xlarge | g4dn.2xlarge | g4dn.4xlarge | g4dn.8xlarge | g4dn.12xlarge | g4dn.16xlarge | g4dn.metal | g5.xlarge | g5.2xlarge | g5.4xlarge | g5.8xlarge | g5.12xlarge | g5.16xlarge | g5.24xlarge | g5.48xlarge | g5g.xlarge | g5g.2xlarge | g5g.4xlarge | g5g.8xlarge | g5g.16xlarge | g5g.metal | hi1.4xlarge | hpc6a.48xlarge | hs1.8xlarge | h1.2xlarge | h1.4xlarge | h1.8xlarge | h1.16xlarge | i2.xlarge | i2.2xlarge | i2.4xlarge | i2.8xlarge | i3.large | i3.xlarge | i3.2xlarge | i3.4xlarge | i3.8xlarge | i3.16xlarge | i3.metal | i3en.large | i3en.xlarge | i3en.2xlarge | i3en.3xlarge | i3en.6xlarge | i3en.12xlarge | i3en.24xlarge | i3en.metal | im4gn.large | im4gn.xlarge | im4gn.2xlarge | im4gn.4xlarge | im4gn.8xlarge | im4gn.16xlarge | inf1.xlarge | inf1.2xlarge | inf1.6xlarge | inf1.24xlarge | is4gen.medium | is4gen.large | is4gen.xlarge | is4gen.2xlarge | is4gen.4xlarge | is4gen.8xlarge | m1.small | m1.medium | m1.large | m1.xlarge | m2.xlarge | m2.2xlarge | m2.4xlarge | m3.medium | m3.large | m3.xlarge | m3.2xlarge | m4.large | m4.xlarge | m4.2xlarge | m4.4xlarge | m4.10xlarge | m4.16xlarge | m5.large | m5.xlarge | m5.2xlarge | m5.4xlarge | m5.8xlarge | m5.12xlarge | m5.16xlarge | m5.24xlarge | m5.metal | m5a.large | m5a.xlarge | m5a.2xlarge | m5a.4xlarge | m5a.8xlarge | m5a.12xlarge | m5a.16xlarge | m5a.24xlarge | m5ad.large | m5ad.xlarge | m5ad.2xlarge | m5ad.4xlarge | m5ad.8xlarge | m5ad.12xlarge | m5ad.16xlarge | m5ad.24xlarge | m5d.large | m5d.xlarge | m5d.2xlarge | m5d.4xlarge | m5d.8xlarge | m5d.12xlarge | m5d.16xlarge | m5d.24xlarge | m5d.metal | m5dn.large | m5dn.xlarge | m5dn.2xlarge | m5dn.4xlarge | m5dn.8xlarge | m5dn.12xlarge | m5dn.16xlarge | m5dn.24xlarge | m5dn.metal | m5n.large | m5n.xlarge | m5n.2xlarge | m5n.4xlarge | m5n.8xlarge | m5n.12xlarge | m5n.16xlarge | m5n.24xlarge | m5n.metal | m5zn.large | m5zn.xlarge | m5zn.2xlarge | m5zn.3xlarge | m5zn.6xlarge | m5zn.12xlarge | m5zn.metal | m6a.large | m6a.xlarge | m6a.2xlarge | m6a.4xlarge | m6a.8xlarge | m6a.12xlarge | m6a.16xlarge | m6a.24xlarge | m6a.32xlarge | m6a.48xlarge | m6g.metal | m6g.medium | m6g.large | m6g.xlarge | m6g.2xlarge | m6g.4xlarge | m6g.8xlarge | m6g.12xlarge | m6g.16xlarge | m6gd.metal | m6gd.medium | m6gd.large | m6gd.xlarge | m6gd.2xlarge | m6gd.4xlarge | m6gd.8xlarge | m6gd.12xlarge | m6gd.16xlarge | m6i.large | m6i.xlarge | m6i.2xlarge | m6i.4xlarge | m6i.8xlarge | m6i.12xlarge | m6i.16xlarge | m6i.24xlarge | m6i.32xlarge | m6i.metal | mac1.metal | p2.xlarge | p2.8xlarge | p2.16xlarge | p3.2xlarge | p3.8xlarge | p3.16xlarge | p3dn.24xlarge | p4d.24xlarge | r3.large | r3.xlarge | r3.2xlarge | r3.4xlarge | r3.8xlarge | r4.large | r4.xlarge | r4.2xlarge | r4.4xlarge | r4.8xlarge | r4.16xlarge | r5.large | r5.xlarge | r5.2xlarge | r5.4xlarge | r5.8xlarge | r5.12xlarge | r5.16xlarge | r5.24xlarge | r5.metal | r5a.large | r5a.xlarge | r5a.2xlarge | r5a.4xlarge | r5a.8xlarge | r5a.12xlarge | r5a.16xlarge | r5a.24xlarge | r5ad.large | r5ad.xlarge | r5ad.2xlarge | r5ad.4xlarge | r5ad.8xlarge | r5ad.12xlarge | r5ad.16xlarge | r5ad.24xlarge | r5b.large | r5b.xlarge | r5b.2xlarge | r5b.4xlarge | r5b.8xlarge | r5b.12xlarge | r5b.16xlarge | r5b.24xlarge | r5b.metal | r5d.large | r5d.xlarge | r5d.2xlarge | r5d.4xlarge | r5d.8xlarge | r5d.12xlarge | r5d.16xlarge | r5d.24xlarge | r5d.metal | r5dn.large | r5dn.xlarge | r5dn.2xlarge | r5dn.4xlarge | r5dn.8xlarge | r5dn.12xlarge | r5dn.16xlarge | r5dn.24xlarge | r5dn.metal | r5n.large | r5n.xlarge | r5n.2xlarge | r5n.4xlarge | r5n.8xlarge | r5n.12xlarge | r5n.16xlarge | r5n.24xlarge | r5n.metal | r6g.medium | r6g.large | r6g.xlarge | r6g.2xlarge | r6g.4xlarge | r6g.8xlarge | r6g.12xlarge | r6g.16xlarge | r6g.metal | r6gd.medium | r6gd.large | r6gd.xlarge | r6gd.2xlarge | r6gd.4xlarge | r6gd.8xlarge | r6gd.12xlarge | r6gd.16xlarge | r6gd.metal | r6i.large | r6i.xlarge | r6i.2xlarge | r6i.4xlarge | r6i.8xlarge | r6i.12xlarge | r6i.16xlarge | r6i.24xlarge | r6i.32xlarge | r6i.metal | t1.micro | t2.nano | t2.micro | t2.small | t2.medium | t2.large | t2.xlarge | t2.2xlarge | t3.nano | t3.micro | t3.small | t3.medium | t3.large | t3.xlarge | t3.2xlarge | t3a.nano | t3a.micro | t3a.small | t3a.medium | t3a.large | t3a.xlarge | t3a.2xlarge | t4g.nano | t4g.micro | t4g.small | t4g.medium | t4g.large | t4g.xlarge | t4g.2xlarge | u-6tb1.56xlarge | u-6tb1.112xlarge | u-9tb1.112xlarge | u-12tb1.112xlarge | u-6tb1.metal | u-9tb1.metal | u-12tb1.metal | u-18tb1.metal | u-24tb1.metal | vt1.3xlarge | vt1.6xlarge | vt1.24xlarge | x1.16xlarge | x1.32xlarge | x1e.xlarge | x1e.2xlarge | x1e.4xlarge | x1e.8xlarge | x1e.16xlarge | x1e.32xlarge | x2iezn.2xlarge | x2iezn.4xlarge | x2iezn.6xlarge | x2iezn.8xlarge | x2iezn.12xlarge | x2iezn.metal | x2gd.medium | x2gd.large | x2gd.xlarge | x2gd.2xlarge | x2gd.4xlarge | x2gd.8xlarge | x2gd.12xlarge | x2gd.16xlarge | x2gd.metal | z1d.large | z1d.xlarge | z1d.2xlarge | z1d.3xlarge | z1d.6xlarge | z1d.12xlarge | z1d.metal | x2idn.16xlarge | x2idn.24xlarge | x2idn.32xlarge | x2iedn.xlarge | x2iedn.2xlarge | x2iedn.4xlarge | x2iedn.8xlarge | x2iedn.16xlarge | x2iedn.24xlarge | x2iedn.32xlarge | c6a.large | c6a.xlarge | c6a.2xlarge | c6a.4xlarge | c6a.8xlarge | c6a.12xlarge | c6a.16xlarge | c6a.24xlarge | c6a.32xlarge | c6a.48xlarge | c6a.metal | m6a.metal | i4i.large | i4i.xlarge | i4i.2xlarge | i4i.4xlarge | i4i.8xlarge | i4i.16xlarge | i4i.32xlarge | i4i.metal | x2idn.metal | x2iedn.metal | c7g.medium | c7g.large | c7g.xlarge | c7g.2xlarge | c7g.4xlarge | c7g.8xlarge | c7g.12xlarge | c7g.16xlarge | mac2.metal | c6id.large | c6id.xlarge | c6id.2xlarge | c6id.4xlarge | c6id.8xlarge | c6id.12xlarge | c6id.16xlarge | c6id.24xlarge | c6id.32xlarge | c6id.metal | m6id.large | m6id.xlarge | m6id.2xlarge | m6id.4xlarge | m6id.8xlarge | m6id.12xlarge | m6id.16xlarge | m6id.24xlarge | m6id.32xlarge | m6id.metal | r6id.large | r6id.xlarge | r6id.2xlarge | r6id.4xlarge | r6id.8xlarge | r6id.12xlarge | r6id.16xlarge | r6id.24xlarge | r6id.32xlarge | r6id.metal | r6a.large | r6a.xlarge | r6a.2xlarge | r6a.4xlarge | r6a.8xlarge | r6a.12xlarge | r6a.16xlarge | r6a.24xlarge | r6a.32xlarge | r6a.48xlarge | r6a.metal | p4de.24xlarge | u-3tb1.56xlarge | u-18tb1.112xlarge | u-24tb1.112xlarge | trn1.2xlarge | trn1.32xlarge | hpc6id.32xlarge | c6in.large | c6in.xlarge | c6in.2xlarge | c6in.4xlarge | c6in.8xlarge | c6in.12xlarge | c6in.16xlarge | c6in.24xlarge | c6in.32xlarge | m6in.large | m6in.xlarge | m6in.2xlarge | m6in.4xlarge | m6in.8xlarge | m6in.12xlarge | m6in.16xlarge | m6in.24xlarge | m6in.32xlarge | m6idn.large | m6idn.xlarge | m6idn.2xlarge | m6idn.4xlarge | m6idn.8xlarge | m6idn.12xlarge | m6idn.16xlarge | m6idn.24xlarge | m6idn.32xlarge | r6in.large | r6in.xlarge | r6in.2xlarge | r6in.4xlarge | r6in.8xlarge | r6in.12xlarge | r6in.16xlarge | r6in.24xlarge | r6in.32xlarge | r6idn.large | r6idn.xlarge | r6idn.2xlarge | r6idn.4xlarge | r6idn.8xlarge | r6idn.12xlarge | r6idn.16xlarge | r6idn.24xlarge | r6idn.32xlarge | c7g.metal | m7g.medium | m7g.large | m7g.xlarge | m7g.2xlarge | m7g.4xlarge | m7g.8xlarge | m7g.12xlarge | m7g.16xlarge | m7g.metal | r7g.medium | r7g.large | r7g.xlarge | r7g.2xlarge | r7g.4xlarge | r7g.8xlarge | r7g.12xlarge | r7g.16xlarge | r7g.metal | c6in.metal | m6in.metal | m6idn.metal | r6in.metal | r6idn.metal | inf2.xlarge | inf2.8xlarge | inf2.24xlarge | inf2.48xlarge | trn1n.32xlarge | i4g.large | i4g.xlarge | i4g.2xlarge | i4g.4xlarge | i4g.8xlarge | i4g.16xlarge | hpc7g.4xlarge | hpc7g.8xlarge | hpc7g.16xlarge | c7gn.medium | c7gn.large | c7gn.xlarge | c7gn.2xlarge | c7gn.4xlarge | c7gn.8xlarge | c7gn.12xlarge | c7gn.16xlarge | p5.48xlarge | m7i.large | m7i.xlarge | m7i.2xlarge | m7i.4xlarge | m7i.8xlarge | m7i.12xlarge | m7i.16xlarge | m7i.24xlarge | m7i.48xlarge | m7i-flex.large | m7i-flex.xlarge | m7i-flex.2xlarge | m7i-flex.4xlarge | m7i-flex.8xlarge | m7a.medium | m7a.large | m7a.xlarge | m7a.2xlarge | m7a.4xlarge | m7a.8xlarge | m7a.12xlarge | m7a.16xlarge | m7a.24xlarge | m7a.32xlarge | m7a.48xlarge | m7a.metal-48xl | hpc7a.12xlarge | hpc7a.24xlarge | hpc7a.48xlarge | hpc7a.96xlarge | c7gd.medium | c7gd.large | c7gd.xlarge | c7gd.2xlarge | c7gd.4xlarge | c7gd.8xlarge | c7gd.12xlarge | c7gd.16xlarge | m7gd.medium | m7gd.large | m7gd.xlarge | m7gd.2xlarge | m7gd.4xlarge | m7gd.8xlarge | m7gd.12xlarge | m7gd.16xlarge | r7gd.medium | r7gd.large | r7gd.xlarge | r7gd.2xlarge | r7gd.4xlarge | r7gd.8xlarge | r7gd.12xlarge | r7gd.16xlarge | r7a.medium | r7a.large | r7a.xlarge | r7a.2xlarge | r7a.4xlarge | r7a.8xlarge | r7a.12xlarge | r7a.16xlarge | r7a.24xlarge | r7a.32xlarge | r7a.48xlarge | c7i.large | c7i.xlarge | c7i.2xlarge | c7i.4xlarge | c7i.8xlarge | c7i.12xlarge | c7i.16xlarge | c7i.24xlarge | c7i.48xlarge | mac2-m2pro.metal | r7iz.large | r7iz.xlarge | r7iz.2xlarge | r7iz.4xlarge | r7iz.8xlarge | r7iz.12xlarge | r7iz.16xlarge | r7iz.32xlarge | c7a.medium | c7a.large | c7a.xlarge | c7a.2xlarge | c7a.4xlarge | c7a.8xlarge | c7a.12xlarge | c7a.16xlarge | c7a.24xlarge | c7a.32xlarge | c7a.48xlarge | c7a.metal-48xl | r7a.metal-48xl | r7i.large | r7i.xlarge | r7i.2xlarge | r7i.4xlarge | r7i.8xlarge | r7i.12xlarge | r7i.16xlarge | r7i.24xlarge | r7i.48xlarge | dl2q.24xlarge | mac2-m2.metal | i4i.12xlarge | i4i.24xlarge | c7i.metal-24xl | c7i.metal-48xl | m7i.metal-24xl | m7i.metal-48xl | r7i.metal-24xl | r7i.metal-48xl | r7iz.metal-16xl | r7iz.metal-32xl | c7gd.metal | m7gd.metal | r7gd.metal | g6.xlarge | g6.2xlarge | g6.4xlarge | g6.8xlarge | g6.12xlarge | g6.16xlarge | g6.24xlarge | g6.48xlarge | gr6.4xlarge | gr6.8xlarge | c7i-flex.large | c7i-flex.xlarge | c7i-flex.2xlarge | c7i-flex.4xlarge | c7i-flex.8xlarge | u7i-12tb.224xlarge | u7in-16tb.224xlarge | u7in-24tb.224xlarge | u7in-32tb.224xlarge | u7ib-12tb.224xlarge | c7gn.metal | r8g.medium | r8g.large | r8g.xlarge | r8g.2xlarge | r8g.4xlarge | r8g.8xlarge | r8g.12xlarge | r8g.16xlarge | r8g.24xlarge | r8g.48xlarge | r8g.metal-24xl | r8g.metal-48xl | mac2-m1ultra.metal | g6e.xlarge | g6e.2xlarge | g6e.4xlarge | g6e.8xlarge | g6e.12xlarge | g6e.16xlarge | g6e.24xlarge | g6e.48xlarge | c8g.medium | c8g.large | c8g.xlarge | c8g.2xlarge | c8g.4xlarge | c8g.8xlarge | c8g.12xlarge | c8g.16xlarge | c8g.24xlarge | c8g.48xlarge | c8g.metal-24xl | c8g.metal-48xl | m8g.medium | m8g.large | m8g.xlarge | m8g.2xlarge | m8g.4xlarge | m8g.8xlarge | m8g.12xlarge | m8g.16xlarge | m8g.24xlarge | m8g.48xlarge | m8g.metal-24xl | m8g.metal-48xl | x8g.medium | x8g.large | x8g.xlarge | x8g.2xlarge | x8g.4xlarge | x8g.8xlarge | x8g.12xlarge | x8g.16xlarge | x8g.24xlarge | x8g.48xlarge | x8g.metal-24xl | x8g.metal-48xl | i7ie.large | i7ie.xlarge | i7ie.2xlarge | i7ie.3xlarge | i7ie.6xlarge | i7ie.12xlarge | i7ie.18xlarge | i7ie.24xlarge | i7ie.48xlarge | i8g.large | i8g.xlarge | i8g.2xlarge | i8g.4xlarge | i8g.8xlarge | i8g.12xlarge | i8g.16xlarge | i8g.24xlarge | i8g.metal-24xl | u7i-6tb.112xlarge | u7i-8tb.112xlarge | u7inh-32tb.480xlarge | p5e.48xlarge | p5en.48xlarge | f2.12xlarge | f2.48xlarge | trn2.48xlarge | c7i-flex.12xlarge | c7i-flex.16xlarge | m7i-flex.12xlarge | m7i-flex.16xlarge | i7ie.metal-24xl | i7ie.metal-48xl | i8g.48xlarge | c8gd.medium | c8gd.large | c8gd.xlarge | c8gd.2xlarge | c8gd.4xlarge | c8gd.8xlarge | c8gd.12xlarge | c8gd.16xlarge | c8gd.24xlarge | c8gd.48xlarge | c8gd.metal-24xl | c8gd.metal-48xl | i7i.large | i7i.xlarge | i7i.2xlarge | i7i.4xlarge | i7i.8xlarge | i7i.12xlarge | i7i.16xlarge | i7i.24xlarge | i7i.48xlarge | i7i.metal-24xl | i7i.metal-48xl | p6-b200.48xlarge | m8gd.medium | m8gd.large | m8gd.xlarge | m8gd.2xlarge | m8gd.4xlarge | m8gd.8xlarge | m8gd.12xlarge | m8gd.16xlarge | m8gd.24xlarge | m8gd.48xlarge | m8gd.metal-24xl | m8gd.metal-48xl | r8gd.medium | r8gd.large | r8gd.xlarge | r8gd.2xlarge | r8gd.4xlarge | r8gd.8xlarge | r8gd.12xlarge | r8gd.16xlarge | r8gd.24xlarge | r8gd.48xlarge | r8gd.metal-24xl | r8gd.metal-48xl | c8gn.medium | c8gn.large | c8gn.xlarge | c8gn.2xlarge | c8gn.4xlarge | c8gn.8xlarge | c8gn.12xlarge | c8gn.16xlarge | c8gn.24xlarge | c8gn.48xlarge | c8gn.metal-24xl | c8gn.metal-48xl | f2.6xlarge | p6e-gb200.36xlarge | g6f.large | g6f.xlarge | g6f.2xlarge | g6f.4xlarge | gr6f.4xlarge | p5.4xlarge | r8i.large | r8i.xlarge | r8i.2xlarge | r8i.4xlarge | r8i.8xlarge | r8i.12xlarge | r8i.16xlarge | r8i.24xlarge | r8i.32xlarge | r8i.48xlarge | r8i.96xlarge | r8i.metal-48xl | r8i.metal-96xl | r8i-flex.large | r8i-flex.xlarge | r8i-flex.2xlarge | r8i-flex.4xlarge | r8i-flex.8xlarge | r8i-flex.12xlarge | r8i-flex.16xlarge`
Required: No

 ** KernelId **
The ID of the kernel.
We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see [User provided kernels](https://docs.aws.amazon.com/linux/al2/ug/UserProvidedKernels.html) in the *Amazon Linux 2 User Guide*.
Type: String
Required: No

 ** KeyName **
The name of the key pair. You can create a key pair using [CreateKeyPair](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateKeyPair.html) or [ImportKeyPair](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportKeyPair.html).
If you do not specify a key pair, you can't connect to the instance unless you choose an AMI that is configured to allow users another way to log in.
Type: String
Required: No

 ** LicenseSpecification.N **
The license configurations.
Type: Array of [LaunchTemplateLicenseConfigurationRequest](API_LaunchTemplateLicenseConfigurationRequest.md) objects
Required: No

 ** MaintenanceOptions **
The maintenance options for the instance.
Type: [LaunchTemplateInstanceMaintenanceOptionsRequest](API_LaunchTemplateInstanceMaintenanceOptionsRequest.md) object
Required: No

 ** MetadataOptions **
The metadata options for the instance. For more information, see [Configure the Instance Metadata Service options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html) in the *Amazon EC2 User Guide*.
Type: [LaunchTemplateInstanceMetadataOptionsRequest](API_LaunchTemplateInstanceMetadataOptionsRequest.md) object
Required: No

 ** Monitoring **
The monitoring for the instance.
Type: [LaunchTemplatesMonitoringRequest](API_LaunchTemplatesMonitoringRequest.md) object
Required: No

 ** NetworkInterface.N **
The network interfaces for the instance.
Type: Array of [LaunchTemplateInstanceNetworkInterfaceSpecificationRequest](API_LaunchTemplateInstanceNetworkInterfaceSpecificationRequest.md) objects
Required: No

 ** NetworkPerformanceOptions **
Contains launch template settings to boost network performance for the type of workload that runs on your instance.
Type: [LaunchTemplateNetworkPerformanceOptionsRequest](API_LaunchTemplateNetworkPerformanceOptionsRequest.md) object
Required: No

 ** Operator **
The entity that manages the launch template.
Type: [OperatorRequest](API_OperatorRequest.md) object
Required: No

 ** Placement **
The placement for the instance.
Type: [LaunchTemplatePlacementRequest](API_LaunchTemplatePlacementRequest.md) object
Required: No

 ** PrivateDnsNameOptions **
The options for the instance hostname. The default values are inherited from the subnet.
Type: [LaunchTemplatePrivateDnsNameOptionsRequest](API_LaunchTemplatePrivateDnsNameOptionsRequest.md) object
Required: No

 ** RamDiskId **
The ID of the RAM disk.
We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see [User provided kernels](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedkernels.html) in the *Amazon EC2 User Guide*.
Type: String
Required: No

 ** SecondaryInterface.N **
The secondary interfaces to associate with instances launched from the template.
Type: Array of [LaunchTemplateInstanceSecondaryInterfaceSpecificationRequest](API_LaunchTemplateInstanceSecondaryInterfaceSpecificationRequest.md) objects
Required: No

 ** SecurityGroup.N **
The names of the security groups. For a nondefault VPC, you must use security group IDs instead.
If you specify a network interface, you must specify any security groups as part of the network interface instead of using this parameter.
Type: Array of strings
Required: No

 ** SecurityGroupId.N **
The IDs of the security groups.
If you specify a network interface, you must specify any security groups as part of the network interface instead of using this parameter.
Type: Array of strings
Required: No

 ** TagSpecification.N **
The tags to apply to the resources that are created during instance launch. These tags are not applied to the launch template.
Type: Array of [LaunchTemplateTagSpecificationRequest](API_LaunchTemplateTagSpecificationRequest.md) objects
Required: No

 ** UserData **
The user data to make available to the instance. You must provide base64-encoded text. User data is limited to 16 KB. For more information, see [Run commands when you launch an EC2 instance with user data input](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html) in the *Amazon EC2 User Guide*.
If you are creating the launch template for use with AWS Batch, the user data must be provided in the [MIME multi-part archive format](https://cloudinit.readthedocs.io/en/latest/topics/format.html#mime-multi-part-archive). For more information, see [Amazon EC2 user data in launch templates](https://docs.aws.amazon.com/batch/latest/userguide/launch-templates.html#lt-user-data) in the * AWS Batch User Guide*.
Type: String
Required: No

## See Also
<a name="API_RequestLaunchTemplateData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/RequestLaunchTemplateData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/RequestLaunchTemplateData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/RequestLaunchTemplateData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
