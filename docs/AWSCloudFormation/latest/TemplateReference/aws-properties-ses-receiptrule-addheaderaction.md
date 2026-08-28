---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-receiptrule-addheaderaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::ReceiptRule AddHeaderAction
<a name="aws-properties-ses-receiptrule-addheaderaction"></a>

When included in a receipt rule, this action adds a header to the received email.

For information about adding a header using a receipt rule, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-receipt-rules-console-walkthrough.html).

## Syntax
<a name="aws-properties-ses-receiptrule-addheaderaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-receiptrule-addheaderaction-syntax.json"></a>

```
{
  "[HeaderName](#cfn-ses-receiptrule-addheaderaction-headername)" : {{String}},
  "[HeaderValue](#cfn-ses-receiptrule-addheaderaction-headervalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-receiptrule-addheaderaction-syntax.yaml"></a>

```
  [HeaderName](#cfn-ses-receiptrule-addheaderaction-headername): {{String}}
  [HeaderValue](#cfn-ses-receiptrule-addheaderaction-headervalue): {{String}}
```

## Properties
<a name="aws-properties-ses-receiptrule-addheaderaction-properties"></a>

`HeaderName`  <a name="cfn-ses-receiptrule-addheaderaction-headername"></a>
The name of the header to add to the incoming message. The name must contain at least one character, and can contain up to 50 characters. It consists of alphanumeric (`a–z, A–Z, 0–9`) characters and dashes.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HeaderValue`  <a name="cfn-ses-receiptrule-addheaderaction-headervalue"></a>
The content to include in the header. This value can contain up to 2048 characters. It can't contain newline (`\n`) or carriage return (`\r`) characters.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
