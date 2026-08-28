---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-gamelift-location.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::Location
<a name="aws-resource-gamelift-location"></a>

The AWS::GameLift::Location resource creates a custom location for use in an Anywhere fleet.

## Syntax
<a name="aws-resource-gamelift-location-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-gamelift-location-syntax.json"></a>

```
{
  "Type" : "AWS::GameLift::Location",
  "Properties" : {
      "[LocationName](#cfn-gamelift-location-locationname)" : {{String}},
      "[Tags](#cfn-gamelift-location-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-gamelift-location-syntax.yaml"></a>

```
Type: AWS::GameLift::Location
Properties:
  [LocationName](#cfn-gamelift-location-locationname): {{String}}
  [Tags](#cfn-gamelift-location-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-gamelift-location-properties"></a>

`LocationName`  <a name="cfn-gamelift-location-locationname"></a>
A descriptive name for the custom location.
*Required*: Yes
*Type*: String
*Pattern*: `^custom-[A-Za-z0-9\-]+`
*Minimum*: `8`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-gamelift-location-tags"></a>
A list of labels to assign to the new resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management, and cost allocation. For more information, see [ Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *AWS General Rareference*.
*Required*: No
*Type*: Array of [Tag](aws-properties-gamelift-location-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-gamelift-location-return-values"></a>

### Ref
<a name="aws-resource-gamelift-location-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the custom location ID, such as `arn:aws:gamelift:[region]::location/location-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-gamelift-location-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-gamelift-location-return-values-fn--getatt-fn--getatt"></a>

`LocationArn`  <a name="LocationArn-fn::getatt"></a>
A unique identifier for the custom location. For example, `arn:aws:gamelift:[region]::location/location-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`.

## See also
<a name="aws-resource-gamelift-location--seealso"></a>
+ [ Create GameLift resources using Amazon CloudFront](https://docs.aws.amazon.com/gamelift/latest/developerguide/resources-cloudformation.html) in the *Amazon GameLift Developer Guide*
+ [ Create an Amazon GameLift Anywhere fleet](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-anywhere.html) in the *Amazon GameLift Developer Guide*
+ [ CreateLocation](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateLocation.html) in the *Amazon GameLift API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
