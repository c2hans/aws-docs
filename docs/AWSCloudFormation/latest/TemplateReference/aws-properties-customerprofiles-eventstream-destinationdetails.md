---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-eventstream-destinationdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::EventStream DestinationDetails
<a name="aws-properties-customerprofiles-eventstream-destinationdetails"></a>

Details regarding the Kinesis stream.

## Syntax
<a name="aws-properties-customerprofiles-eventstream-destinationdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-eventstream-destinationdetails-syntax.json"></a>

```
{
  "[Status](#cfn-customerprofiles-eventstream-destinationdetails-status)" : {{String}},
  "[Uri](#cfn-customerprofiles-eventstream-destinationdetails-uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-eventstream-destinationdetails-syntax.yaml"></a>

```
  [Status](#cfn-customerprofiles-eventstream-destinationdetails-status): {{String}}
  [Uri](#cfn-customerprofiles-eventstream-destinationdetails-uri): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-eventstream-destinationdetails-properties"></a>

`Status`  <a name="cfn-customerprofiles-eventstream-destinationdetails-status"></a>
The status of enabling the Kinesis stream as a destination for export.
*Required*: Yes
*Type*: String
*Allowed values*: `HEALTHY | UNHEALTHY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Uri`  <a name="cfn-customerprofiles-eventstream-destinationdetails-uri"></a>
The StreamARN of the destination to deliver profile events to. For example, arn:aws:kinesis:region:account-id:stream/stream-name.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
