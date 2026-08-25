---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cases-case.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cases::Case
<a name="aws-resource-cases-case"></a>

**Note**
If you provide a value for `PerformedBy.UserArn`, you must also have the [connect:DescribeUser](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html) permission on the user ARN that you provide.

Creates a case in the specified Cases domain. Case system and custom fields are taken as an array id/value pairs with a declared data types.

When creating a case from a template that has tag propagation configurations, the specified tags are automatically applied to the case.

The following field is always required when creating a case:
+  `title`

The following field may be required depending on the template configuration:
+ `customer_id` - Required only if the template's `requiredFields` list includes `customer_id`. When required, provide the full customer profile ARN in this format: `arn:aws:profile:your_AWS_Region:your_AWS_account_ID:domains/your_profiles_domain_name/profiles/profile_ID`. When not required, the field is optional and can be omitted, added, changed, or removed after case creation.

## Syntax
<a name="aws-resource-cases-case-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cases-case-syntax.json"></a>

```
{
  "Type" : "AWS::Cases::Case",
  "Properties" : {
      "[CustomerId](#cfn-cases-case-customerid)" : {{String}},
      "[DomainId](#cfn-cases-case-domainid)" : {{String}},
      "[Tags](#cfn-cases-case-tags)" : {{[ Tag, ... ]}},
      "[TemplateId](#cfn-cases-case-templateid)" : {{String}},
      "[Title](#cfn-cases-case-title)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-cases-case-syntax.yaml"></a>

```
Type: AWS::Cases::Case
Properties:
  [CustomerId](#cfn-cases-case-customerid): {{String}}
  [DomainId](#cfn-cases-case-domainid): {{String}}
  [Tags](#cfn-cases-case-tags): {{
    - Tag}}
  [TemplateId](#cfn-cases-case-templateid): {{String}}
  [Title](#cfn-cases-case-title): {{String}}
```

## Properties
<a name="aws-resource-cases-case-properties"></a>

`CustomerId`  <a name="cfn-cases-case-customerid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Maximum*: `4100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DomainId`  <a name="cfn-cases-case-domainid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-cases-case-tags"></a>
A map of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-cases-case-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateId`  <a name="cfn-cases-case-templateid"></a>
A unique identifier of a template.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Title`  <a name="cfn-cases-case-title"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Maximum*: `4100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cases-case-return-values"></a>

### Ref
<a name="aws-resource-cases-case-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-cases-case-return-values-fn--getatt"></a>

####
<a name="aws-resource-cases-case-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CaseId`  <a name="CaseId-fn::getatt"></a>
A unique identifier of the case.
