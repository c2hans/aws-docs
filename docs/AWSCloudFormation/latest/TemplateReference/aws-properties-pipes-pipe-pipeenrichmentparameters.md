---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-pipeenrichmentparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe PipeEnrichmentParameters
<a name="aws-properties-pipes-pipe-pipeenrichmentparameters"></a>

The parameters required to set up enrichment on your pipe.

## Syntax
<a name="aws-properties-pipes-pipe-pipeenrichmentparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-pipeenrichmentparameters-syntax.json"></a>

```
{
  "[HttpParameters](#cfn-pipes-pipe-pipeenrichmentparameters-httpparameters)" : {{PipeEnrichmentHttpParameters}},
  "[InputTemplate](#cfn-pipes-pipe-pipeenrichmentparameters-inputtemplate)" : {{String}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-pipeenrichmentparameters-syntax.yaml"></a>

```
  [HttpParameters](#cfn-pipes-pipe-pipeenrichmentparameters-httpparameters): {{
    PipeEnrichmentHttpParameters}}
  [InputTemplate](#cfn-pipes-pipe-pipeenrichmentparameters-inputtemplate): {{String}}
```

## Properties
<a name="aws-properties-pipes-pipe-pipeenrichmentparameters-properties"></a>

`HttpParameters`  <a name="cfn-pipes-pipe-pipeenrichmentparameters-httpparameters"></a>
Contains the HTTP parameters to use when the target is a API Gateway REST endpoint or EventBridge ApiDestination.
If you specify an API Gateway REST API or EventBridge ApiDestination as a target, you can use this parameter to specify headers, path parameters, and query string keys/values as part of your target invoking request. If you're using ApiDestinations, the corresponding Connection can also have these values configured. In case of any conflicting keys, values from the Connection take precedence.
*Required*: No
*Type*: [PipeEnrichmentHttpParameters](aws-properties-pipes-pipe-pipeenrichmenthttpparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputTemplate`  <a name="cfn-pipes-pipe-pipeenrichmentparameters-inputtemplate"></a>
Valid JSON text passed to the enrichment. In this case, nothing from the event itself is passed to the enrichment. For more information, see [The JavaScript Object Notation (JSON) Data Interchange Format](http://www.rfc-editor.org/rfc/rfc7159.txt).
To remove an input template, specify an empty string.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `8192`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
