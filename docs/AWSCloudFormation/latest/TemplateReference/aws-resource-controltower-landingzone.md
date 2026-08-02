---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-controltower-landingzone.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ControlTower::LandingZone
<a name="aws-resource-controltower-landingzone"></a>

Creates a new landing zone. This API call starts an asynchronous operation that creates and configures a landing zone, based on the parameters specified in the manifest JSON file.

## Syntax
<a name="aws-resource-controltower-landingzone-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-controltower-landingzone-syntax.json"></a>

```
{
  "Type" : "AWS::ControlTower::LandingZone",
  "Properties" : {
      "[Manifest](#cfn-controltower-landingzone-manifest)" : {{}},
      "[RemediationTypes](#cfn-controltower-landingzone-remediationtypes)" : {{[ String, ... ]}},
      "[Tags](#cfn-controltower-landingzone-tags)" : {{[ Tag, ... ]}},
      "[Version](#cfn-controltower-landingzone-version)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-controltower-landingzone-syntax.yaml"></a>

```
Type: AWS::ControlTower::LandingZone
Properties:
  [Manifest](#cfn-controltower-landingzone-manifest): {{
    }}
  [RemediationTypes](#cfn-controltower-landingzone-remediationtypes): {{
    - String}}
  [Tags](#cfn-controltower-landingzone-tags): {{
    - Tag}}
  [Version](#cfn-controltower-landingzone-version): {{String}}
```

## Properties
<a name="aws-resource-controltower-landingzone-properties"></a>

`Manifest`  <a name="cfn-controltower-landingzone-manifest"></a>
The landing zone manifest JSON text file that specifies the landing zone configurations.
*Required*: Yes
*Type*:
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RemediationTypes`  <a name="cfn-controltower-landingzone-remediationtypes"></a>
The types of remediation actions configured for the landing zone, such as automatic drift correction or compliance enforcement.
*Required*: No
*Type*: Array of String
*Allowed values*: `INHERITANCE_DRIFT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-controltower-landingzone-tags"></a>
Tags to be applied to the landing zone.
*Required*: No
*Type*: Array of [Tag](aws-properties-controltower-landingzone-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Version`  <a name="cfn-controltower-landingzone-version"></a>
The landing zone's current deployed version.
*Required*: Yes
*Type*: String
*Pattern*: `\d+.\d+`
*Minimum*: `3`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-controltower-landingzone-return-values"></a>

### Ref
<a name="aws-resource-controltower-landingzone-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the **LandingZoneIdentifier**. For example:

 `"LandingZoneIdentifier": "arn:aws:controltower:us-west-2:123456789012:landingzone/1A2B3C4D5E6F7G8H`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-controltower-landingzone-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type.

####
<a name="aws-resource-controltower-landingzone-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the landing zone.

`DriftStatus`  <a name="DriftStatus-fn::getatt"></a>
The drift status of the landing zone.

`LandingZoneIdentifier`  <a name="LandingZoneIdentifier-fn::getatt"></a>
The unique identifier of the landing zone.

`LatestAvailableVersion`  <a name="LatestAvailableVersion-fn::getatt"></a>
The latest available version of the landing zone.

`Status`  <a name="Status-fn::getatt"></a>
The landing zone deployment status. One of `ACTIVE`, `PROCESSING`, `FAILED`.
