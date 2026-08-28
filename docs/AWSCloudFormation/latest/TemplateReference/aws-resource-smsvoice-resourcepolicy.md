---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-smsvoice-resourcepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SMSVOICE::ResourcePolicy
<a name="aws-resource-smsvoice-resourcepolicy"></a>

Attaches a resource-based policy to a AWS End User Messaging SMS resource(phone number, sender Id, phone poll, or opt-out list) that is used for sharing the resource. A shared resource can be a Pool, Opt-out list, Sender Id, or Phone number. For more information about resource-based policies, see [Working with shared resources](https://docs.aws.amazon.com/sms-voice/latest/userguide/shared-resources.html) in the *AWS End User Messaging SMS User Guide*.

## Syntax
<a name="aws-resource-smsvoice-resourcepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-smsvoice-resourcepolicy-syntax.json"></a>

```
{
  "Type" : "AWS::SMSVOICE::ResourcePolicy",
  "Properties" : {
      "[PolicyDocument](#cfn-smsvoice-resourcepolicy-policydocument)" : {{Json}},
      "[ResourceArn](#cfn-smsvoice-resourcepolicy-resourcearn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-smsvoice-resourcepolicy-syntax.yaml"></a>

```
Type: AWS::SMSVOICE::ResourcePolicy
Properties:
  [PolicyDocument](#cfn-smsvoice-resourcepolicy-policydocument): {{Json}}
  [ResourceArn](#cfn-smsvoice-resourcepolicy-resourcearn): {{String}}
```

## Properties
<a name="aws-resource-smsvoice-resourcepolicy-properties"></a>

`PolicyDocument`  <a name="cfn-smsvoice-resourcepolicy-policydocument"></a>
The JSON formatted resource-based policy to attach.
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceArn`  <a name="cfn-smsvoice-resourcepolicy-resourcearn"></a>
The Amazon Resource Name (ARN) of the AWS End User Messaging SMS resource attached to the resource-based policy.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:\S+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-smsvoice-resourcepolicy-return-values"></a>

### Ref
<a name="aws-resource-smsvoice-resourcepolicy-return-values-ref"></a>

 When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns `ResourceArn`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
