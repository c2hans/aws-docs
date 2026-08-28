---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-devicefarm-instanceprofile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DeviceFarm::InstanceProfile
<a name="aws-resource-devicefarm-instanceprofile"></a>

Creates a profile that can be applied to one or more private fleet device instances.

## Syntax
<a name="aws-resource-devicefarm-instanceprofile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-devicefarm-instanceprofile-syntax.json"></a>

```
{
  "Type" : "AWS::DeviceFarm::InstanceProfile",
  "Properties" : {
      "[Description](#cfn-devicefarm-instanceprofile-description)" : {{String}},
      "[ExcludeAppPackagesFromCleanup](#cfn-devicefarm-instanceprofile-excludeapppackagesfromcleanup)" : {{[ String, ... ]}},
      "[Name](#cfn-devicefarm-instanceprofile-name)" : {{String}},
      "[PackageCleanup](#cfn-devicefarm-instanceprofile-packagecleanup)" : {{Boolean}},
      "[RebootAfterUse](#cfn-devicefarm-instanceprofile-rebootafteruse)" : {{Boolean}},
      "[Tags](#cfn-devicefarm-instanceprofile-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-devicefarm-instanceprofile-syntax.yaml"></a>

```
Type: AWS::DeviceFarm::InstanceProfile
Properties:
  [Description](#cfn-devicefarm-instanceprofile-description): {{String}}
  [ExcludeAppPackagesFromCleanup](#cfn-devicefarm-instanceprofile-excludeapppackagesfromcleanup): {{
    - String}}
  [Name](#cfn-devicefarm-instanceprofile-name): {{String}}
  [PackageCleanup](#cfn-devicefarm-instanceprofile-packagecleanup): {{Boolean}}
  [RebootAfterUse](#cfn-devicefarm-instanceprofile-rebootafteruse): {{Boolean}}
  [Tags](#cfn-devicefarm-instanceprofile-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-devicefarm-instanceprofile-properties"></a>

`Description`  <a name="cfn-devicefarm-instanceprofile-description"></a>
The description of the instance profile.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `16384`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExcludeAppPackagesFromCleanup`  <a name="cfn-devicefarm-instanceprofile-excludeapppackagesfromcleanup"></a>
An array of strings containing the list of app packages that should not be cleaned up from the device after a test run completes.
The list of packages is considered only if you set `packageCleanup` to `true`.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-devicefarm-instanceprofile-name"></a>
The name of the instance profile.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PackageCleanup`  <a name="cfn-devicefarm-instanceprofile-packagecleanup"></a>
When set to `true`, Device Farm removes app packages after a test run. The default value is `false` for private devices.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RebootAfterUse`  <a name="cfn-devicefarm-instanceprofile-rebootafteruse"></a>
When set to `true`, Device Farm reboots the instance after a test run. The default value is `true`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-devicefarm-instanceprofile-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html) in the *AWS CloudFormation guide*.
*Required*: No
*Type*: Array of [Tag](aws-properties-devicefarm-instanceprofile-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-devicefarm-instanceprofile-return-values"></a>

### Ref
<a name="aws-resource-devicefarm-instanceprofile-return-values-ref"></a>

Not supported for this resource.

### Fn::GetAtt
<a name="aws-resource-devicefarm-instanceprofile-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-devicefarm-instanceprofile-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the instance profile. See [Amazon resource names](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *General Reference guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
