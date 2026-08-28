---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-events-connection-connectionhttpparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Events::Connection ConnectionHttpParameters
<a name="aws-properties-events-connection-connectionhttpparameters"></a>

Any additional parameters for the connection.

## Syntax
<a name="aws-properties-events-connection-connectionhttpparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-events-connection-connectionhttpparameters-syntax.json"></a>

```
{
  "[BodyParameters](#cfn-events-connection-connectionhttpparameters-bodyparameters)" : {{[ Parameter, ... ]}},
  "[HeaderParameters](#cfn-events-connection-connectionhttpparameters-headerparameters)" : {{[ Parameter, ... ]}},
  "[QueryStringParameters](#cfn-events-connection-connectionhttpparameters-querystringparameters)" : {{[ Parameter, ... ]}}
}
```

### YAML
<a name="aws-properties-events-connection-connectionhttpparameters-syntax.yaml"></a>

```
  [BodyParameters](#cfn-events-connection-connectionhttpparameters-bodyparameters): {{
    - Parameter}}
  [HeaderParameters](#cfn-events-connection-connectionhttpparameters-headerparameters): {{
    - Parameter}}
  [QueryStringParameters](#cfn-events-connection-connectionhttpparameters-querystringparameters): {{
    - Parameter}}
```

## Properties
<a name="aws-properties-events-connection-connectionhttpparameters-properties"></a>

`BodyParameters`  <a name="cfn-events-connection-connectionhttpparameters-bodyparameters"></a>
Any additional body string parameters for the connection.
*Required*: No
*Type*: Array of [Parameter](aws-properties-events-connection-parameter.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HeaderParameters`  <a name="cfn-events-connection-connectionhttpparameters-headerparameters"></a>
Any additional header parameters for the connection.
*Required*: No
*Type*: Array of [Parameter](aws-properties-events-connection-parameter.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryStringParameters`  <a name="cfn-events-connection-connectionhttpparameters-querystringparameters"></a>
Any additional query string parameters for the connection.
*Required*: No
*Type*: Array of [Parameter](aws-properties-events-connection-parameter.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
