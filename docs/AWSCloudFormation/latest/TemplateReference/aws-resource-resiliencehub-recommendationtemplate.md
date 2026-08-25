---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-resiliencehub-recommendationtemplate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHub::RecommendationTemplate
<a name="aws-resource-resiliencehub-recommendationtemplate"></a>

Defines a recommendation template created with the CreateRecommendationTemplate action.

## Syntax
<a name="aws-resource-resiliencehub-recommendationtemplate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-resiliencehub-recommendationtemplate-syntax.json"></a>

```
{
  "Type" : "AWS::ResilienceHub::RecommendationTemplate",
  "Properties" : {
      "[AssessmentArn](#cfn-resiliencehub-recommendationtemplate-assessmentarn)" : {{String}},
      "[Format](#cfn-resiliencehub-recommendationtemplate-format)" : {{String}},
      "[Name](#cfn-resiliencehub-recommendationtemplate-name)" : {{String}},
      "[RecommendationTypes](#cfn-resiliencehub-recommendationtemplate-recommendationtypes)" : {{[ String, ... ]}},
      "[Tags](#cfn-resiliencehub-recommendationtemplate-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-resiliencehub-recommendationtemplate-syntax.yaml"></a>

```
Type: AWS::ResilienceHub::RecommendationTemplate
Properties:
  [AssessmentArn](#cfn-resiliencehub-recommendationtemplate-assessmentarn): {{String}}
  [Format](#cfn-resiliencehub-recommendationtemplate-format): {{String}}
  [Name](#cfn-resiliencehub-recommendationtemplate-name): {{String}}
  [RecommendationTypes](#cfn-resiliencehub-recommendationtemplate-recommendationtypes): {{
    - String}}
  [Tags](#cfn-resiliencehub-recommendationtemplate-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-resiliencehub-recommendationtemplate-properties"></a>

`AssessmentArn`  <a name="cfn-resiliencehub-recommendationtemplate-assessmentarn"></a>
Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app-assessment/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *AWS General Reference* guide.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Format`  <a name="cfn-resiliencehub-recommendationtemplate-format"></a>
Format of the recommendation template.
CfnJson
The template is CloudFormation JSON.
CfnYaml
The template is CloudFormation YAML.
*Required*: Yes
*Type*: String
*Allowed values*: `CfnYaml | CfnJson`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-resiliencehub-recommendationtemplate-name"></a>
Name for the recommendation template.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9][A-Za-z0-9_\-]{1,59}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RecommendationTypes`  <a name="cfn-resiliencehub-recommendationtemplate-recommendationtypes"></a>
An array of strings that specify the recommendation template type or types.
Alarm
The template is an AlarmRecommendation template.
Sop
The template is a SopRecommendation template.
Test
The template is a TestRecommendation template.
*Required*: Yes
*Type*: Array of String
*Allowed values*: `Alarm | Sop | Test`
*Minimum*: `1`
*Maximum*: `4`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-resiliencehub-recommendationtemplate-tags"></a>
Tags assigned to the resource. A tag is a label that you assign to an AWS resource. Each tag consists of a key/value pair.
*Required*: No
*Type*: Array of [Tag](aws-properties-resiliencehub-recommendationtemplate-tag.md)
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-resiliencehub-recommendationtemplate-return-values"></a>

### Ref
<a name="aws-resource-resiliencehub-recommendationtemplate-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-resiliencehub-recommendationtemplate-return-values-fn--getatt"></a>

####
<a name="aws-resource-resiliencehub-recommendationtemplate-return-values-fn--getatt-fn--getatt"></a>

`AppArn`  <a name="AppArn-fn::getatt"></a>
Amazon Resource Name (ARN) of the AWS Resilience Hub application. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *AWS General Reference* guide.

`RecommendationTemplateArn`  <a name="RecommendationTemplateArn-fn::getatt"></a>
Amazon Resource Name (ARN) for the recommendation template.

`Status`  <a name="Status-fn::getatt"></a>
Status of the action.
