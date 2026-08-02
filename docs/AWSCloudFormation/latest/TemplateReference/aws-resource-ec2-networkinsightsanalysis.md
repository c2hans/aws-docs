---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-networkinsightsanalysis.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::NetworkInsightsAnalysis
<a name="aws-resource-ec2-networkinsightsanalysis"></a>

Specifies a network insights analysis.

## Syntax
<a name="aws-resource-ec2-networkinsightsanalysis-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-networkinsightsanalysis-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::NetworkInsightsAnalysis",
  "Properties" : {
      "[AdditionalAccounts](#cfn-ec2-networkinsightsanalysis-additionalaccounts)" : {{[ String, ... ]}},
      "[FilterInArns](#cfn-ec2-networkinsightsanalysis-filterinarns)" : {{[ String, ... ]}},
      "[FilterOutArns](#cfn-ec2-networkinsightsanalysis-filteroutarns)" : {{[ String, ... ]}},
      "[NetworkInsightsPathId](#cfn-ec2-networkinsightsanalysis-networkinsightspathid)" : {{String}},
      "[Tags](#cfn-ec2-networkinsightsanalysis-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ec2-networkinsightsanalysis-syntax.yaml"></a>

```
Type: AWS::EC2::NetworkInsightsAnalysis
Properties:
  [AdditionalAccounts](#cfn-ec2-networkinsightsanalysis-additionalaccounts): {{
    - String}}
  [FilterInArns](#cfn-ec2-networkinsightsanalysis-filterinarns): {{
    - String}}
  [FilterOutArns](#cfn-ec2-networkinsightsanalysis-filteroutarns): {{
    - String}}
  [NetworkInsightsPathId](#cfn-ec2-networkinsightsanalysis-networkinsightspathid): {{String}}
  [Tags](#cfn-ec2-networkinsightsanalysis-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ec2-networkinsightsanalysis-properties"></a>

`AdditionalAccounts`  <a name="cfn-ec2-networkinsightsanalysis-additionalaccounts"></a>
The member accounts that contain resources that the path can traverse.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterInArns`  <a name="cfn-ec2-networkinsightsanalysis-filterinarns"></a>
The Amazon Resource Names (ARN) of the resources that the path must traverse.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FilterOutArns`  <a name="cfn-ec2-networkinsightsanalysis-filteroutarns"></a>
The Amazon Resource Names (ARN) of the resources that the path must ignore.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkInsightsPathId`  <a name="cfn-ec2-networkinsightsanalysis-networkinsightspathid"></a>
The ID of the path.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ec2-networkinsightsanalysis-tags"></a>
The tags to apply.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-networkinsightsanalysis-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-networkinsightsanalysis-return-values"></a>

### Ref
<a name="aws-resource-ec2-networkinsightsanalysis-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the network insights analysis.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-networkinsightsanalysis-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-networkinsightsanalysis-return-values-fn--getatt-fn--getatt"></a>

`AlternatePathHints`  <a name="AlternatePathHints-fn::getatt"></a>
Potential intermediate components.

`Explanations`  <a name="Explanations-fn::getatt"></a>
The explanations. For more information, see [Reachability Analyzer explanation codes](https://docs.aws.amazon.com/vpc/latest/reachability/explanation-codes.html).

`ForwardPathComponents`  <a name="ForwardPathComponents-fn::getatt"></a>
The components in the path from source to destination.

`NetworkInsightsAnalysisArn`  <a name="NetworkInsightsAnalysisArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the network insights analysis.

`NetworkInsightsAnalysisId`  <a name="NetworkInsightsAnalysisId-fn::getatt"></a>
The ID of the network insights analysis.

`NetworkPathFound`  <a name="NetworkPathFound-fn::getatt"></a>
Indicates whether the destination is reachable from the source.

`ReturnPathComponents`  <a name="ReturnPathComponents-fn::getatt"></a>
The components in the path from destination to source.

`StartDate`  <a name="StartDate-fn::getatt"></a>
The time the analysis started.

`Status`  <a name="Status-fn::getatt"></a>
The status of the network insights analysis.

`StatusMessage`  <a name="StatusMessage-fn::getatt"></a>
The status message, if the status is `failed`.

`SuggestedAccounts`  <a name="SuggestedAccounts-fn::getatt"></a>
The IDs of potential intermediate accounts.
