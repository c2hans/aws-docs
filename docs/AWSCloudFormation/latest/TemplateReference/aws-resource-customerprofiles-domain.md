---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-customerprofiles-domain.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::Domain
<a name="aws-resource-customerprofiles-domain"></a>

Specifies an Amazon Connect Customer Profiles Domain.

## Syntax
<a name="aws-resource-customerprofiles-domain-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-customerprofiles-domain-syntax.json"></a>

```
{
  "Type" : "AWS::CustomerProfiles::Domain",
  "Properties" : {
      "[DataStore](#cfn-customerprofiles-domain-datastore)" : {{DataStore}},
      "[DeadLetterQueueUrl](#cfn-customerprofiles-domain-deadletterqueueurl)" : {{String}},
      "[DefaultEncryptionKey](#cfn-customerprofiles-domain-defaultencryptionkey)" : {{String}},
      "[DefaultExpirationDays](#cfn-customerprofiles-domain-defaultexpirationdays)" : {{Integer}},
      "[DomainName](#cfn-customerprofiles-domain-domainname)" : {{String}},
      "[Matching](#cfn-customerprofiles-domain-matching)" : {{Matching}},
      "[RuleBasedMatching](#cfn-customerprofiles-domain-rulebasedmatching)" : {{RuleBasedMatching}},
      "[Tags](#cfn-customerprofiles-domain-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-customerprofiles-domain-syntax.yaml"></a>

```
Type: AWS::CustomerProfiles::Domain
Properties:
  [DataStore](#cfn-customerprofiles-domain-datastore): {{
    DataStore}}
  [DeadLetterQueueUrl](#cfn-customerprofiles-domain-deadletterqueueurl): {{String}}
  [DefaultEncryptionKey](#cfn-customerprofiles-domain-defaultencryptionkey): {{String}}
  [DefaultExpirationDays](#cfn-customerprofiles-domain-defaultexpirationdays): {{Integer}}
  [DomainName](#cfn-customerprofiles-domain-domainname): {{String}}
  [Matching](#cfn-customerprofiles-domain-matching): {{
    Matching}}
  [RuleBasedMatching](#cfn-customerprofiles-domain-rulebasedmatching): {{
    RuleBasedMatching}}
  [Tags](#cfn-customerprofiles-domain-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-customerprofiles-domain-properties"></a>

`DataStore`  <a name="cfn-customerprofiles-domain-datastore"></a>
Property description not available.
*Required*: No
*Type*: [DataStore](aws-properties-customerprofiles-domain-datastore.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeadLetterQueueUrl`  <a name="cfn-customerprofiles-domain-deadletterqueueurl"></a>
The URL of the SQS dead letter queue, which is used for reporting errors associated with ingesting data from third party applications. You must set up a policy on the `DeadLetterQueue` for the `SendMessage` operation to enable Amazon Connect Customer Profiles to send messages to the `DeadLetterQueue`.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultEncryptionKey`  <a name="cfn-customerprofiles-domain-defaultencryptionkey"></a>
The default encryption key, which is an AWS managed key, is used when no specific type of encryption key is specified. It is used to encrypt all data before it is placed in permanent or semi-permanent storage.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultExpirationDays`  <a name="cfn-customerprofiles-domain-defaultexpirationdays"></a>
The default number of days until the data within the domain expires.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1098`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainName`  <a name="cfn-customerprofiles-domain-domainname"></a>
The unique name of the domain.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Matching`  <a name="cfn-customerprofiles-domain-matching"></a>
The process of matching duplicate profiles.
*Required*: No
*Type*: [Matching](aws-properties-customerprofiles-domain-matching.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleBasedMatching`  <a name="cfn-customerprofiles-domain-rulebasedmatching"></a>
The process of matching duplicate profiles using Rule-Based matching.
*Required*: No
*Type*: [RuleBasedMatching](aws-properties-customerprofiles-domain-rulebasedmatching.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-customerprofiles-domain-tags"></a>
The tags used to organize, track, or control access for this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-customerprofiles-domain-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-customerprofiles-domain-return-values"></a>

### Ref
<a name="aws-resource-customerprofiles-domain-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the DomainName of the domain.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-customerprofiles-domain-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-customerprofiles-domain-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp of when the domain was created.

`LastUpdatedAt`  <a name="LastUpdatedAt-fn::getatt"></a>
The timestamp of when the domain was most recently edited.

`RuleBasedMatching.Status`  <a name="RuleBasedMatching.Status-fn::getatt"></a>
Property description not available.

## Examples
<a name="aws-resource-customerprofiles-domain--examples"></a>

The following example creates a Domain.

###
<a name="aws-resource-customerprofiles-domain--examples--"></a>

#### YAML
<a name="aws-resource-customerprofiles-domain--examples----yaml"></a>

```
Type: "AWS::CustomerProfiles::Domain"
Properties:
    DomainName: "ExampleDomain"
    DefaultEncryptionKey: "arn:aws:kms:us-east-1:123456789012:key/1988472d-6b77-4bb6-ae39-efce5EXAMPLE"
    DeadLetterQueueUrl: "arn:aws:sqs:us-east-1:123456789012:DLQName"
    DefaultExpirationDays: 6
```

#### JSON
<a name="aws-resource-customerprofiles-domain--examples----json"></a>

```
"Type": "AWS::CustomerProfiles::Domain",
"Properties": {
    "DomainName": "ExampleDomain",
    "DefaultEncryptionKey": "arn:aws:kms:us-east-1:123456789012:key/1988472d-6b77-4bb6-ae39-efce5EXAMPLE",
    "DeadLetterQueueUrl": "arn:aws:sqs:us-east-1:123456789012:DLQName",
    "DefaultExpirationDays": 6
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
