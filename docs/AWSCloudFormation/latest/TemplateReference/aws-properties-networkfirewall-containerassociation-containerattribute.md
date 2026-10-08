---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-containerassociation-containerattribute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::ContainerAssociation ContainerAttribute
<a name="aws-properties-networkfirewall-containerassociation-containerattribute"></a>

A key-value filter pair used in container association monitoring configurations to narrow which containers are tracked. The key must match exactly. The value can be an exact value or a wildcard pattern.

## Syntax
<a name="aws-properties-networkfirewall-containerassociation-containerattribute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-containerassociation-containerattribute-syntax.json"></a>

```
{
  "[Key](#cfn-networkfirewall-containerassociation-containerattribute-key)" : {{String}},
  "[Value](#cfn-networkfirewall-containerassociation-containerattribute-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-networkfirewall-containerassociation-containerattribute-syntax.yaml"></a>

```
  [Key](#cfn-networkfirewall-containerassociation-containerattribute-key): {{String}}
  [Value](#cfn-networkfirewall-containerassociation-containerattribute-value): {{String}}
```

## Properties
<a name="aws-properties-networkfirewall-containerassociation-containerattribute-properties"></a>

`Key`  <a name="cfn-networkfirewall-containerassociation-containerattribute-key"></a>
The attribute key to filter on. For Amazon EKS, specify `namespace` to filter by namespace, or specify a Kubernetes label key. For Amazon ECS, specify a container instance attribute name. Keys don't support wildcards.
Valid characters are letters, numbers, spaces, hyphens (`-`), underscores (`_`), periods (`.`), forward slashes (`/`), and colons (`:`).
*Required*: Yes
*Type*: String
*Pattern*: `^\S+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-networkfirewall-containerassociation-containerattribute-value"></a>
The attribute value to match. You can specify an exact value, such as `payments-api`, or a wildcard pattern, such as `payments-*`.
Valid characters are letters, numbers, spaces, hyphens (`-`), underscores (`_`), periods (`.`), forward slashes (`/`), colons (`:`), asterisks (`*`), and backslashes (`\`).
Network Firewall evaluates the value using the following rules:
+ An asterisk (`*`) matches zero or more characters. For example, `payments-*` matches `payments-`, `payments-api`, and `payments-api-v2`, and `*-prod` matches `web-prod`.
+ The pattern must match the entire value. For example, `payments-*` doesn't match `my-payments-api`. To match a value that contains `payments` anywhere, use `*payments*`.
+ Matching is case sensitive. For example, `Payments-*` doesn't match `payments-api`.
+ To match a literal asterisk, escape it with a backslash (`\*`). To match a literal backslash, use `\\`. A backslash followed by any other character matches a literal backslash followed by that character.
+ A wildcard pattern matches only containers that have the attribute. For example, a filter with key `app` and value `*` matches every container that has an `app` label, but doesn't match a container without an `app` label.
+ A value that doesn't contain `*` or `\` matches only that exact value.
A value can contain at most 10 unescaped asterisks. Escaped asterisks (`\*`) don't count toward this limit. A value can't end with a single unescaped backslash.
*Required*: Yes
*Type*: String
*Pattern*: `^\S+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
