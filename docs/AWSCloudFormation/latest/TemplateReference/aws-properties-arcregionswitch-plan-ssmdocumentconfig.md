---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-ssmdocumentconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan SsmDocumentConfig
<a name="aws-properties-arcregionswitch-plan-ssmdocumentconfig"></a>

The Systems Manager document to run and the managed nodes to target for a single AWS Region.

## Syntax
<a name="aws-properties-arcregionswitch-plan-ssmdocumentconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-ssmdocumentconfig-syntax.json"></a>

```
{
  "[CrossAccountRole](#cfn-arcregionswitch-plan-ssmdocumentconfig-crossaccountrole)" : {{String}},
  "[DocumentArn](#cfn-arcregionswitch-plan-ssmdocumentconfig-documentarn)" : {{String}},
  "[DocumentVersion](#cfn-arcregionswitch-plan-ssmdocumentconfig-documentversion)" : {{String}},
  "[ExternalId](#cfn-arcregionswitch-plan-ssmdocumentconfig-externalid)" : {{String}},
  "[Parameters](#cfn-arcregionswitch-plan-ssmdocumentconfig-parameters)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Targets](#cfn-arcregionswitch-plan-ssmdocumentconfig-targets)" : {{[ SsmTarget, ... ]}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-ssmdocumentconfig-syntax.yaml"></a>

```
  [CrossAccountRole](#cfn-arcregionswitch-plan-ssmdocumentconfig-crossaccountrole): {{String}}
  [DocumentArn](#cfn-arcregionswitch-plan-ssmdocumentconfig-documentarn): {{String}}
  [DocumentVersion](#cfn-arcregionswitch-plan-ssmdocumentconfig-documentversion): {{String}}
  [ExternalId](#cfn-arcregionswitch-plan-ssmdocumentconfig-externalid): {{String}}
  [Parameters](#cfn-arcregionswitch-plan-ssmdocumentconfig-parameters): {{
    {{Key}}: {{Value}}}}
  [Targets](#cfn-arcregionswitch-plan-ssmdocumentconfig-targets): {{
    - SsmTarget}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-ssmdocumentconfig-properties"></a>

`CrossAccountRole`  <a name="cfn-arcregionswitch-plan-ssmdocumentconfig-crossaccountrole"></a>
The cross-account role for the configuration.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DocumentArn`  <a name="cfn-arcregionswitch-plan-ssmdocumentconfig-documentarn"></a>
The Amazon Resource Name (ARN) of the Systems Manager document to run.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z0-9\-]+:ssm:[a-z0-9\-]+:([0-9]{12})?:document/[a-zA-Z0-9_.\-]+$`
*Minimum*: `20`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DocumentVersion`  <a name="cfn-arcregionswitch-plan-ssmdocumentconfig-documentversion"></a>
The version of the Systems Manager document to run for this Region. When you omit it, Systems Manager runs the document's default version.
*Required*: No
*Type*: String
*Pattern*: `^([$]LATEST|[$]DEFAULT|[1-9][0-9]*)$`
*Minimum*: `1`
*Maximum*: `8`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExternalId`  <a name="cfn-arcregionswitch-plan-ssmdocumentconfig-externalid"></a>
The external ID (secret key) for the configuration.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Parameters`  <a name="cfn-arcregionswitch-plan-ssmdocumentconfig-parameters"></a>
The parameters that are passed to this Region's Systems Manager document. You set parameters for each document, so each Region can run its document with its own parameters.
*Required*: No
*Type*: Object of Array
*Pattern*: `.+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Targets`  <a name="cfn-arcregionswitch-plan-ssmdocumentconfig-targets"></a>
The target filters that Systems Manager resolves to managed nodes when the command runs. To target specific managed nodes, use the `InstanceIds` key. You can specify up to five target filters.
*Required*: Yes
*Type*: Array of [SsmTarget](aws-properties-arcregionswitch-plan-ssmtarget.md)
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
