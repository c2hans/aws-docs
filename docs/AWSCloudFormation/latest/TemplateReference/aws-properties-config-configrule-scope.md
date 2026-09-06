---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-config-configrule-scope.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Config::ConfigRule Scope
<a name="aws-properties-config-configrule-scope"></a>

Defines which resources trigger an evaluation for an AWS Config rule. The scope can include one or more resource types, a combination of a tag key and value, or a combination of one resource type and one resource ID. Specify a scope to constrain which resources trigger an evaluation for a rule. Otherwise, evaluations for the rule are triggered when any resource in your recording group changes in configuration.

## Syntax
<a name="aws-properties-config-configrule-scope-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-config-configrule-scope-syntax.json"></a>

```
{
  "[ComplianceResourceId](#cfn-config-configrule-scope-complianceresourceid)" : {{String}},
  "[ComplianceResourceTypes](#cfn-config-configrule-scope-complianceresourcetypes)" : {{[ String, ... ]}},
  "[TagKey](#cfn-config-configrule-scope-tagkey)" : {{String}},
  "[TagValue](#cfn-config-configrule-scope-tagvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-config-configrule-scope-syntax.yaml"></a>

```
  [ComplianceResourceId](#cfn-config-configrule-scope-complianceresourceid): {{String}}
  [ComplianceResourceTypes](#cfn-config-configrule-scope-complianceresourcetypes): {{
    - String}}
  [TagKey](#cfn-config-configrule-scope-tagkey): {{String}}
  [TagValue](#cfn-config-configrule-scope-tagvalue): {{String}}
```

## Properties
<a name="aws-properties-config-configrule-scope-properties"></a>

`ComplianceResourceId`  <a name="cfn-config-configrule-scope-complianceresourceid"></a>
The ID of the only AWS resource that you want to trigger an evaluation for the rule. If you specify a resource ID, you must specify one resource type for `ComplianceResourceTypes`.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `768`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComplianceResourceTypes`  <a name="cfn-config-configrule-scope-complianceresourcetypes"></a>
The resource types of only those AWS resources that you want to trigger an evaluation for the rule. You can only specify one type if you also specify a resource ID for `ComplianceResourceId`.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TagKey`  <a name="cfn-config-configrule-scope-tagkey"></a>
The tag key that is applied to only those AWS resources that you want to trigger an evaluation for the rule.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TagValue`  <a name="cfn-config-configrule-scope-tagvalue"></a>
The tag value applied to only those AWS resources that you want to trigger an evaluation for the rule. If you specify a value for `TagValue`, you must also specify a value for `TagKey`.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-config-configrule-scope--examples"></a>

**Topics**
+ [Multiple Resource Types with Tag-Based Scope](#aws-properties-config-configrule-scope--examples--Multiple_Resource_Types_with_Tag-Based_Scope)
+ [Single Resource Specific Scope](#aws-properties-config-configrule-scope--examples--Single_Resource_Specific_Scope)

### Multiple Resource Types with Tag-Based Scope
<a name="aws-properties-config-configrule-scope--examples--Multiple_Resource_Types_with_Tag-Based_Scope"></a>

This example configures AWS Config to evaluate both Amazon EC2 instances and volumes that are tagged with "`Environment`=`Production`". This is useful when you want to monitor compliance for multiple resource types that share specific tags.

#### YAML
<a name="aws-properties-config-configrule-scope--examples--Multiple_Resource_Types_with_Tag-Based_Scope--yaml"></a>

```
Scope:
  ComplianceResourceTypes:
    - "AWS::EC2::Instance"
    - "AWS::EC2::Volume"
  TagKey: "Environment"
  TagValue: "Production"
```

#### JSON
<a name="aws-properties-config-configrule-scope--examples--Multiple_Resource_Types_with_Tag-Based_Scope--json"></a>

```
{
  "Scope": {
    "ComplianceResourceTypes": [
      "AWS::EC2::Instance",
      "AWS::EC2::Volume"
    ],
    "TagKey": "Environment",
    "TagValue": "Production"
  }
}
```

### Single Resource Specific Scope
<a name="aws-properties-config-configrule-scope--examples--Single_Resource_Specific_Scope"></a>

This example shows how to target a specific Amazon EC2 instance for evaluation using its resource ID. When using `ComplianceResourceId`, you must specify exactly one resource type in `ComplianceResourceTypes`.

#### YAML
<a name="aws-properties-config-configrule-scope--examples--Single_Resource_Specific_Scope--yaml"></a>

```
Scope:
  ComplianceResourceId: "i-1234567890abcdef0"
  ComplianceResourceTypes:
    - "AWS::EC2::Instance"
```

#### JSON
<a name="aws-properties-config-configrule-scope--examples--Single_Resource_Specific_Scope--json"></a>

```
{
  "Scope": {
    "ComplianceResourceId": "i-1234567890abcdef0",
    "ComplianceResourceTypes": [
      "AWS::EC2::Instance"
    ]
  }
}
```
