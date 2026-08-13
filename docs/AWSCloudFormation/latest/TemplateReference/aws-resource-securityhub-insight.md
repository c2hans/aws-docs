---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-securityhub-insight.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::Insight
<a name="aws-resource-securityhub-insight"></a>

The `AWS::SecurityHub::Insight` resource creates a custom insight in AWS Security Hub CSPM. An insight is a collection of findings that relate to a security issue that requires attention or remediation. For more information, see [Insights in AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-insights.html) in the *AWS Security Hub CSPM User Guide*.

Tags aren't supported for this resource.

## Syntax
<a name="aws-resource-securityhub-insight-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-securityhub-insight-syntax.json"></a>

```
{
  "Type" : "AWS::SecurityHub::Insight",
  "Properties" : {
      "[Filters](#cfn-securityhub-insight-filters)" : {{AwsSecurityFindingFilters}},
      "[GroupByAttribute](#cfn-securityhub-insight-groupbyattribute)" : {{String}},
      "[Name](#cfn-securityhub-insight-name)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-securityhub-insight-syntax.yaml"></a>

```
Type: AWS::SecurityHub::Insight
Properties:
  [Filters](#cfn-securityhub-insight-filters): {{
    AwsSecurityFindingFilters}}
  [GroupByAttribute](#cfn-securityhub-insight-groupbyattribute): {{String}}
  [Name](#cfn-securityhub-insight-name): {{String}}
```

## Properties
<a name="aws-resource-securityhub-insight-properties"></a>

`Filters`  <a name="cfn-securityhub-insight-filters"></a>
One or more attributes used to filter the findings included in the insight. The insight only includes findings that match the criteria defined in the filters. You can filter by up to ten finding attributes. For each attribute, you can provide up to 20 filter values.
*Required*: Yes
*Type*: [AwsSecurityFindingFilters](aws-properties-securityhub-insight-awssecurityfindingfilters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GroupByAttribute`  <a name="cfn-securityhub-insight-groupbyattribute"></a>
The grouping attribute for the insight's findings. Indicates how to group the matching findings, and identifies the type of item that the insight applies to. For example, if an insight is grouped by resource identifier, then the insight produces a list of resource identifiers.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-securityhub-insight-name"></a>
The name of a Security Hub CSPM insight.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-securityhub-insight-return-values"></a>

### Ref
<a name="aws-resource-securityhub-insight-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of a Security Hub CSPM insight. For example, `arn:aws:securityhub:us-west-1:123456789012:insight/123456789012/custom/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-securityhub-insight-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-securityhub-insight-return-values-fn--getatt-fn--getatt"></a>

`InsightArn`  <a name="InsightArn-fn::getatt"></a>
The ARN of a Security Hub CSPM insight.

## Examples
<a name="aws-resource-securityhub-insight--examples"></a>

### Creating a Security Hub CSPM insight
<a name="aws-resource-securityhub-insight--examples--Creating_a_insight"></a>

The following example creates a custom Security Hub CSPM insight. The insight includes findings that match the specified filters.

#### JSON
<a name="aws-resource-securityhub-insight--examples--Creating_a_insight--json"></a>

```
{
    "Description": "Example template to create a Security Hub insight",
    "Resources": {
        "SecurityHubInsight": {
            "Type": "AWS::SecurityHub::Insight",
            "Properties": {
                "Name": "Example insight name",
                "GroupByAttribute": "ResourceId",
                "Filters": {
                   "CompanyName": [
                       {
                           "Comparison": "EQUALS",
                           "Value": "AWS"
                       }
                   ],
                   "CreatedAt": [
                       {
                           "DateRange": {
                               "Unit": "DAYS",
                               "Value": 5
                           }
                       }
                   ],
                   "Criticality": [
                       {
                           "Gte": 50,
                           "Lte": 95
                       }
                   ],
                   "Id": [
                       {
                           "Comparison": "EQUALS",
                           "Value": "example-id"
                       }
                   ],
                   "RecordState": [
                       {
                           "Comparison": "EQUALS",
                           "Value": "ACTIVE"
                       }
                   ],
                   "ResourceTags": [
                       {
                           "Comparison": "EQUALS",
                           "Key": "department",
                           "Value": "security"
                       },
                       {
                           "Comparison": "EQUALS",
                           "Key": "department",
                           "Value": "operations"
                       }
                   ],
                   "SeverityLabel": [
                       {
                           "Comparison": "EQUALS",
                           "Value": "LOW"
                       },
                       {
                           "Comparison": "EQUALS",
                           "Value": "HIGH"
                       }
                   ],
                   "UpdatedAt": [
                       {
                           "Start": "2023-04-25T17:05:54.832Z",
                           "End": "2023-05-25T17:05:54.832Z"
                       }
                   ]
                }
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-securityhub-insight--examples--Creating_a_insight--yaml"></a>

```
Description: Example template to create a Security Hub insight
Resources:
  SecurityHubInsight:
    Type: "AWS::SecurityHub::Insight"
    Properties:
      Name: "Example insight name"
      GroupByAttribute: "ResourceId"
      Filters:
        CompanyName:
          - Comparison: EQUALS
            Value: AWS
        CreatedAt:
          - DateRange:
              Unit: DAYS
              Value: 5
        Criticality:
          - Gte: 50
            Lte: 95
        Id:
          - Comparison: EQUALS
            Value: example-id
        RecordState:
          - Comparison: EQUALS
            Value: ACTIVE
        ResourceTags:
          - Comparison: EQUALS
            Key: department
            Value: security
          - Comparison: EQUALS
            Key: department
            Value: operations
        SeverityLabel:
          - Comparison: EQUALS
            Value: LOW
          - Comparison: EQUALS
            Value: HIGH
        UpdatedAt:
          - Start: "2023-04-25T17:05:54.832Z"
            End: "2023-05-25T17:05:54.832Z"
```
