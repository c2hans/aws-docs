---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cases-domain.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cases::Domain
<a name="aws-resource-cases-domain"></a>

Creates a domain, which is a container for all case data, such as cases, fields, templates and layouts. Each Connect Customer instance can be associated with only one Cases domain.

**Important**
This will not associate your connect instance to Cases domain. Instead, use the Connect Customer [CreateIntegrationAssociation](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateIntegrationAssociation.html) API. You need specific IAM permissions to successfully associate the Cases domain. For more information, see [Onboard to Cases](https://docs.aws.amazon.com/connect/latest/adminguide/required-permissions-iam-cases.html#onboard-cases-iam).

## Syntax
<a name="aws-resource-cases-domain-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cases-domain-syntax.json"></a>

```
{
  "Type" : "AWS::Cases::Domain",
  "Properties" : {
      "[Name](#cfn-cases-domain-name)" : {{String}},
      "[Tags](#cfn-cases-domain-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cases-domain-syntax.yaml"></a>

```
Type: AWS::Cases::Domain
Properties:
  [Name](#cfn-cases-domain-name): {{String}}
  [Tags](#cfn-cases-domain-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cases-domain-properties"></a>

`Name`  <a name="cfn-cases-domain-name"></a>
The name of the domain.
*Required*: Yes
*Type*: String
*Pattern*: `^.*[\S]$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: Updates are not supported.

`Tags`  <a name="cfn-cases-domain-tags"></a>
An array of key-value pairs to apply to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-cases-domain-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cases-domain-return-values"></a>

### Ref
<a name="aws-resource-cases-domain-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the domain. For example:

 `arn:aws:cases:us-west-2:123456789012:domain/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cases-domain-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cases-domain-return-values-fn--getatt-fn--getatt"></a>

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
The timestamp when the Cases domain was created.

`DomainArn`  <a name="DomainArn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the Cases domain.

`DomainId`  <a name="DomainId-fn::getatt"></a>
The unique identifier of the Cases domain.

`DomainStatus`  <a name="DomainStatus-fn::getatt"></a>
The status of the Cases domain.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
