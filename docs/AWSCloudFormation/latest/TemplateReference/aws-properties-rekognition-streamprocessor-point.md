---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rekognition-streamprocessor-point.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Rekognition::StreamProcessor Point
<a name="aws-properties-rekognition-streamprocessor-point"></a>

The X and Y coordinates of a point on an image or video frame. The X and Y values are ratios of the overall image size or video resolution. For example, if the input image is 700x200 and the values are X=0.5 and Y=0.25, then the point is at the (350,50) pixel coordinate on the image.

An array of `Point` objects, `Polygon`, is returned by [DetectText](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectText) and by [DetectCustomLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectCustomLabels) or used to define regions of interest in Amazon Rekognition Video operations such as `CreateStreamProcessor`. `Polygon` represents a fine-grained polygon around a detected item. For more information, see [Geometry](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_Geometry).

## Syntax
<a name="aws-properties-rekognition-streamprocessor-point-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rekognition-streamprocessor-point-syntax.json"></a>

```
{
  "[X](#cfn-rekognition-streamprocessor-point-x)" : {{Number}},
  "[Y](#cfn-rekognition-streamprocessor-point-y)" : {{Number}}
}
```

### YAML
<a name="aws-properties-rekognition-streamprocessor-point-syntax.yaml"></a>

```
  [X](#cfn-rekognition-streamprocessor-point-x): {{Number}}
  [Y](#cfn-rekognition-streamprocessor-point-y): {{Number}}
```

## Properties
<a name="aws-properties-rekognition-streamprocessor-point-properties"></a>

`X`  <a name="cfn-rekognition-streamprocessor-point-x"></a>
The value of the X coordinate for a point on a `Polygon`.
*Required*: Yes
*Type*: Number
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Y`  <a name="cfn-rekognition-streamprocessor-point-y"></a>
The value of the Y coordinate for a point on a `Polygon`.
*Required*: Yes
*Type*: Number
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
