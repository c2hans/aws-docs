---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appstream-stackfleetassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppStream::StackFleetAssociation
<a name="aws-resource-appstream-stackfleetassociation"></a>

The `AWS::AppStream::StackFleetAssociation` resource associates the specified fleet with the specified stack for Amazon WorkSpaces Applications.

## Syntax
<a name="aws-resource-appstream-stackfleetassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-appstream-stackfleetassociation-syntax.json"></a>

```
{
  "Type" : "AWS::AppStream::StackFleetAssociation",
  "Properties" : {
      "[FleetName](#cfn-appstream-stackfleetassociation-fleetname)" : {{String}},
      "[StackName](#cfn-appstream-stackfleetassociation-stackname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-appstream-stackfleetassociation-syntax.yaml"></a>

```
Type: AWS::AppStream::StackFleetAssociation
Properties:
  [FleetName](#cfn-appstream-stackfleetassociation-fleetname): {{String}}
  [StackName](#cfn-appstream-stackfleetassociation-stackname): {{String}}
```

## Properties
<a name="aws-resource-appstream-stackfleetassociation-properties"></a>

`FleetName`  <a name="cfn-appstream-stackfleetassociation-fleetname"></a>
The name of the fleet.
To associate a fleet with a stack, you must specify a dependency on the fleet resource. For more information, see [DependsOn Attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StackName`  <a name="cfn-appstream-stackfleetassociation-stackname"></a>
The name of the stack.
To associate a fleet with a stack, you must specify a dependency on the stack resource. For more information, see [DependsOn Attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-resource-appstream-stackfleetassociation--seealso"></a>
+ [AssociateFleet](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_AssociateFleet.html) in the *Amazon WorkSpaces Applications API Reference*
