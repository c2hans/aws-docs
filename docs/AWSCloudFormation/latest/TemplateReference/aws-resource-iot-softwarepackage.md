---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-softwarepackage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::SoftwarePackage
<a name="aws-resource-iot-softwarepackage"></a>

Use the `AWS::IoT::SoftwarePackage` resource to create a software package.

For information about working with software packages, see [AWS IoT Device Management Software Package Catalog](https://docs.aws.amazon.com/iot/latest/developerguide/software-package-catalog.html) and [Creating a software package and package version](https://docs.aws.amazon.com/iot/latest/developerguide/creating-package-and-version.html) in the *AWS IoT Developer Guide*. See also, [CreatePackage](https://docs.aws.amazon.com/iot/latest/apireference/API_CreatePackage.html) in the *API Guide*.

## Syntax
<a name="aws-resource-iot-softwarepackage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iot-softwarepackage-syntax.json"></a>

```
{
  "Type" : "AWS::IoT::SoftwarePackage",
  "Properties" : {
      "[Description](#cfn-iot-softwarepackage-description)" : {{String}},
      "[PackageName](#cfn-iot-softwarepackage-packagename)" : {{String}},
      "[Tags](#cfn-iot-softwarepackage-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-iot-softwarepackage-syntax.yaml"></a>

```
Type: AWS::IoT::SoftwarePackage
Properties:
  [Description](#cfn-iot-softwarepackage-description): {{String}}
  [PackageName](#cfn-iot-softwarepackage-packagename): {{String}}
  [Tags](#cfn-iot-softwarepackage-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-iot-softwarepackage-properties"></a>

`Description`  <a name="cfn-iot-softwarepackage-description"></a>
A summary of the package being created. This can be used to outline the package's contents or purpose.
*Required*: No
*Type*: String
*Pattern*: `^[^\p{C}]+$`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PackageName`  <a name="cfn-iot-softwarepackage-packagename"></a>
The name of the new software package.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_.]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-iot-softwarepackage-tags"></a>
Metadata that can be used to manage the package.
*Required*: No
*Type*: Array of [Tag](aws-properties-iot-softwarepackage-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-iot-softwarepackage-return-values"></a>

### Ref
<a name="aws-resource-iot-softwarepackage-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the software package name. For example:

```
{ "Ref": "MyPackage" }
```

Response:

```
package-name
```

For a stack named MyStack, a value that is similar to the following is returned:

```
MyStack-MySoftwarePackage-AB1CDEFGHIJK
```

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-iot-softwarepackage-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

For example:

```
{ "GetAtt": "MySoftwarePackage.PackageArn" }
```

####
<a name="aws-resource-iot-softwarepackage-return-values-fn--getatt-fn--getatt"></a>

`PackageArn`  <a name="PackageArn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the package.

## Examples
<a name="aws-resource-iot-softwarepackage--examples"></a>

The following example declares a software package and the values of its attributes.

###
<a name="aws-resource-iot-softwarepackage--examples--"></a>

#### JSON
<a name="aws-resource-iot-softwarepackage--examples----json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "MySoftwarePackage": {
      "Type": "AWS::IoT::SoftwarePackage",
      "Properties": {
        "PackageName": "Package",
        "Description": "description",
        "Tags": [
          {
            "Key": "TagKey",
            "Value": "TagValue"
          }
        ]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-iot-softwarepackage--examples----yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  MySoftwarePackage:
    Type: AWS::IoT::SoftwarePackage
    Properties:
      PackageName: "Package"
      Description: "description"
      Tags:
        - Key: "TagKey"
          Value: "TagValue"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
