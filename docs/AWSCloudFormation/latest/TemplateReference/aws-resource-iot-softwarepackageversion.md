---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-softwarepackageversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::SoftwarePackageVersion
<a name="aws-resource-iot-softwarepackageversion"></a>

Use the `AWS::IoT::SoftwarePackageVersion` resource to create a software package version.

For information about working with software package versions, see [AWS IoT Device ManagementSoftware Package Catalog](https://docs.aws.amazon.com/iot/latest/developerguide/software-package-catalog.html) and [Creating a software package and package version](https://docs.aws.amazon.com/iot/latest/developerguide/creating-package-and-version.html) in the *AWS IoT Developer Guide*. See also, [CreatePackageVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_CreatePackageVersion.html) in the *API Guide*.

**Note**
The associated software package must exist before the package version is created. If you create a software package and package version in the same CloudFormation template, set the software package as a [dependency](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html) of the package version. If they are created out of sequence, you will receive an error.
Package versions and created in a `draft` state, for more information, see [Package version lifecycle](https://docs.aws.amazon.com/iot/latest/developerguide/preparing-to-use-software-package-catalog.html#package-version-lifecycle). To change the package version state after it’s created, use the [UpdatePackageVersionAPI](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdatePackageVersion.html) command.

## Syntax
<a name="aws-resource-iot-softwarepackageversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iot-softwarepackageversion-syntax.json"></a>

```
{
  "Type" : "AWS::IoT::SoftwarePackageVersion",
  "Properties" : {
      "[Artifact](#cfn-iot-softwarepackageversion-artifact)" : {{PackageVersionArtifact}},
      "[Attributes](#cfn-iot-softwarepackageversion-attributes)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Description](#cfn-iot-softwarepackageversion-description)" : {{String}},
      "[PackageName](#cfn-iot-softwarepackageversion-packagename)" : {{String}},
      "[Recipe](#cfn-iot-softwarepackageversion-recipe)" : {{String}},
      "[Sbom](#cfn-iot-softwarepackageversion-sbom)" : {{Sbom}},
      "[Tags](#cfn-iot-softwarepackageversion-tags)" : {{[ Tag, ... ]}},
      "[VersionName](#cfn-iot-softwarepackageversion-versionname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-iot-softwarepackageversion-syntax.yaml"></a>

```
Type: AWS::IoT::SoftwarePackageVersion
Properties:
  [Artifact](#cfn-iot-softwarepackageversion-artifact): {{
    PackageVersionArtifact}}
  [Attributes](#cfn-iot-softwarepackageversion-attributes): {{
    {{Key}}: {{Value}}}}
  [Description](#cfn-iot-softwarepackageversion-description): {{String}}
  [PackageName](#cfn-iot-softwarepackageversion-packagename): {{String}}
  [Recipe](#cfn-iot-softwarepackageversion-recipe): {{String}}
  [Sbom](#cfn-iot-softwarepackageversion-sbom): {{
    Sbom}}
  [Tags](#cfn-iot-softwarepackageversion-tags): {{
    - Tag}}
  [VersionName](#cfn-iot-softwarepackageversion-versionname): {{String}}
```

## Properties
<a name="aws-resource-iot-softwarepackageversion-properties"></a>

`Artifact`  <a name="cfn-iot-softwarepackageversion-artifact"></a>
Property description not available.
*Required*: No
*Type*: [PackageVersionArtifact](aws-properties-iot-softwarepackageversion-packageversionartifact.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Attributes`  <a name="cfn-iot-softwarepackageversion-attributes"></a>
Metadata that can be used to define a package version’s configuration. For example, the S3 file location, configuration options that are being sent to the device or fleet.
The combined size of all the attributes on a package version is limited to 3KB.
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z0-9:_-]+$`
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-iot-softwarepackageversion-description"></a>
A summary of the package version being created. This can be used to outline the package's contents or purpose.
*Required*: No
*Type*: String
*Pattern*: `^[^\p{C}]+$`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PackageName`  <a name="cfn-iot-softwarepackageversion-packagename"></a>
The name of the associated software package.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_.]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Recipe`  <a name="cfn-iot-softwarepackageversion-recipe"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Sbom`  <a name="cfn-iot-softwarepackageversion-sbom"></a>
Property description not available.
*Required*: No
*Type*: [Sbom](aws-properties-iot-softwarepackageversion-sbom.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-iot-softwarepackageversion-tags"></a>
Metadata that can be used to manage the package version.
*Required*: No
*Type*: Array of [Tag](aws-properties-iot-softwarepackageversion-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VersionName`  <a name="cfn-iot-softwarepackageversion-versionname"></a>
The name of the new package version.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_.]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-iot-softwarepackageversion-return-values"></a>

### Ref
<a name="aws-resource-iot-softwarepackageversion-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the software package name and package version. For example:

```
{ "Ref": "MyPackageVersion" }
```

Response:

```
package-name|version-name
```

For a stack named MyStack, a value that is similar to the following is returned:

```
MyStack-MyPackageVersion-AB1CDEFGHIJK
```

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-iot-softwarepackageversion-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

For example:

```
{ "GetAtt": "MySoftwarePackageVersion.PackageVersionArn" }
```

####
<a name="aws-resource-iot-softwarepackageversion-return-values-fn--getatt-fn--getatt"></a>

`ErrorReason`  <a name="ErrorReason-fn::getatt"></a>
Error reason for a package version failure during creation or update.

`PackageVersionArn`  <a name="PackageVersionArn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the package.

`SbomValidationStatus`  <a name="SbomValidationStatus-fn::getatt"></a>
Property description not available.

`Status`  <a name="Status-fn::getatt"></a>
The status of the package version. For more information, see [Package version lifecycle](https://docs.aws.amazon.com/iot/latest/developerguide/preparing-to-use-software-package-catalog.html#package-version-lifecycle).

## Examples
<a name="aws-resource-iot-softwarepackageversion--examples"></a>

The following example declares a package version and the values of its attributes.

###
<a name="aws-resource-iot-softwarepackageversion--examples--"></a>

#### JSON
<a name="aws-resource-iot-softwarepackageversion--examples----json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "MyPackageVersion": {
      "Type": "AWS::IoT::SoftwarePackageVersion",
      "Properties": {
        "PackageName": "PackageName",
        "VersionName": "1.0.0",
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
<a name="aws-resource-iot-softwarepackageversion--examples----yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  MyPackageVersion:
    Type: AWS::IoT::SoftwarePackageVersion
    Properties:
      PackageName: "PackageName"
      VersionName: "1.0.0"
      Description: "description"
      Tags:
        - Key: "TagKey"
          Value: "TagValue"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
