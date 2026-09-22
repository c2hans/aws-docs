---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-infrastructureconfiguration-placement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::InfrastructureConfiguration Placement
<a name="aws-properties-imagebuilder-infrastructureconfiguration-placement"></a>

By default, EC2 instances run on shared tenancy hardware. This means that multiple AWS accounts might share the same physical hardware. When you use dedicated hardware, the physical server that hosts your instances is dedicated to your AWS account. Instance placement settings contain the details for the physical hardware where instances that Image Builder launches during image creation will run.

## Syntax
<a name="aws-properties-imagebuilder-infrastructureconfiguration-placement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-infrastructureconfiguration-placement-syntax.json"></a>

```
{
  "[AvailabilityZone](#cfn-imagebuilder-infrastructureconfiguration-placement-availabilityzone)" : {{String}},
  "[HostId](#cfn-imagebuilder-infrastructureconfiguration-placement-hostid)" : {{String}},
  "[HostResourceGroupArn](#cfn-imagebuilder-infrastructureconfiguration-placement-hostresourcegrouparn)" : {{String}},
  "[Tenancy](#cfn-imagebuilder-infrastructureconfiguration-placement-tenancy)" : {{String}}
}
```

### YAML
<a name="aws-properties-imagebuilder-infrastructureconfiguration-placement-syntax.yaml"></a>

```
  [AvailabilityZone](#cfn-imagebuilder-infrastructureconfiguration-placement-availabilityzone): {{String}}
  [HostId](#cfn-imagebuilder-infrastructureconfiguration-placement-hostid): {{String}}
  [HostResourceGroupArn](#cfn-imagebuilder-infrastructureconfiguration-placement-hostresourcegrouparn): {{String}}
  [Tenancy](#cfn-imagebuilder-infrastructureconfiguration-placement-tenancy): {{String}}
```

## Properties
<a name="aws-properties-imagebuilder-infrastructureconfiguration-placement-properties"></a>

`AvailabilityZone`  <a name="cfn-imagebuilder-infrastructureconfiguration-placement-availabilityzone"></a>
The Availability Zone where your build and test instances will launch.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HostId`  <a name="cfn-imagebuilder-infrastructureconfiguration-placement-hostid"></a>
The ID of the Dedicated Host on which build and test instances run. This only applies if `tenancy` is `host`.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HostResourceGroupArn`  <a name="cfn-imagebuilder-infrastructureconfiguration-placement-hostresourcegrouparn"></a>
The Amazon Resource Name (ARN) of the host resource group in which to launch build and test instances. This only applies if `tenancy` is `host`.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tenancy`  <a name="cfn-imagebuilder-infrastructureconfiguration-placement-tenancy"></a>
The tenancy of the instance. An instance with a tenancy of `dedicated` runs on single-tenant hardware. An instance with a tenancy of `host` runs on a Dedicated Host.
If tenancy is set to `host`, then you can optionally specify one target for placement – either host ID or host resource group ARN. If automatic placement is enabled for your host, and you don't specify any placement target, Amazon EC2 will try to find an available host for your build and test instances.
*Required*: No
*Type*: String
*Allowed values*: `default | dedicated | host`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
