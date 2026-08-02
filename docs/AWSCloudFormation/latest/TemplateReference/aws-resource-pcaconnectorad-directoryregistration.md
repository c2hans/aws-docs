---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-pcaconnectorad-directoryregistration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCAConnectorAD::DirectoryRegistration
<a name="aws-resource-pcaconnectorad-directoryregistration"></a>

Creates a directory registration that authorizes communication between AWS Private CA and an Active Directory

## Syntax
<a name="aws-resource-pcaconnectorad-directoryregistration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-pcaconnectorad-directoryregistration-syntax.json"></a>

```
{
  "Type" : "AWS::PCAConnectorAD::DirectoryRegistration",
  "Properties" : {
      "[DirectoryId](#cfn-pcaconnectorad-directoryregistration-directoryid)" : {{String}},
      "[Tags](#cfn-pcaconnectorad-directoryregistration-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-pcaconnectorad-directoryregistration-syntax.yaml"></a>

```
Type: AWS::PCAConnectorAD::DirectoryRegistration
Properties:
  [DirectoryId](#cfn-pcaconnectorad-directoryregistration-directoryid): {{String}}
  [Tags](#cfn-pcaconnectorad-directoryregistration-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-pcaconnectorad-directoryregistration-properties"></a>

`DirectoryId`  <a name="cfn-pcaconnectorad-directoryregistration-directoryid"></a>
The identifier of the Active Directory.
*Required*: Yes
*Type*: String
*Pattern*: `^d-[0-9a-f]{10}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-pcaconnectorad-directoryregistration-tags"></a>
Metadata assigned to a directory registration consisting of a key-value pair.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-pcaconnectorad-directoryregistration-return-values"></a>

### Fn::GetAtt
<a name="aws-resource-pcaconnectorad-directoryregistration-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-pcaconnectorad-directoryregistration-return-values-fn--getatt-fn--getatt"></a>

`DirectoryRegistrationArn`  <a name="DirectoryRegistrationArn-fn::getatt"></a>
 The Amazon Resource Name (ARN) that was returned when you called [CreateDirectoryRegistration](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html) .
