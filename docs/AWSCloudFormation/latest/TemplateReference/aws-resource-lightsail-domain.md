---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lightsail-domain.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lightsail::Domain
<a name="aws-resource-lightsail-domain"></a>

Describes a domain where you are storing recordsets.

## Syntax
<a name="aws-resource-lightsail-domain-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lightsail-domain-syntax.json"></a>

```
{
  "Type" : "AWS::Lightsail::Domain",
  "Properties" : {
      "[DomainEntries](#cfn-lightsail-domain-domainentries)" : {{[ DomainEntry, ... ]}},
      "[DomainName](#cfn-lightsail-domain-domainname)" : {{String}},
      "[Tags](#cfn-lightsail-domain-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-lightsail-domain-syntax.yaml"></a>

```
Type: AWS::Lightsail::Domain
Properties:
  [DomainEntries](#cfn-lightsail-domain-domainentries): {{
    - DomainEntry}}
  [DomainName](#cfn-lightsail-domain-domainname): {{String}}
  [Tags](#cfn-lightsail-domain-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-lightsail-domain-properties"></a>

`DomainEntries`  <a name="cfn-lightsail-domain-domainentries"></a>
An array of key-value pairs containing information about the domain entries.
*Required*: No
*Type*: Array of [DomainEntry](aws-properties-lightsail-domain-domainentry.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainName`  <a name="cfn-lightsail-domain-domainname"></a>
The fully qualified domain name in the certificate request.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-lightsail-domain-tags"></a>
The tag keys and optional values for the resource. For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags).
*Required*: No
*Type*: Array of [Tag](aws-properties-lightsail-domain-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-lightsail-domain-return-values"></a>

### Ref
<a name="aws-resource-lightsail-domain-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-lightsail-domain-return-values-fn--getatt"></a>

####
<a name="aws-resource-lightsail-domain-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the domain recordset (`arn:aws:lightsail:global:123456789101:Domain/824cede0-abc7-4f84-8dbc-12345EXAMPLE`).

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date when the domain recordset was created.

`ResourceType`  <a name="ResourceType-fn::getatt"></a>
The resource type.

`SupportCode`  <a name="SupportCode-fn::getatt"></a>
The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
