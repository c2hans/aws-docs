---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-pcaconnectorscep-challenge.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCAConnectorSCEP::Challenge
<a name="aws-resource-pcaconnectorscep-challenge"></a>

For general-purpose connectors. Creates a *challenge password* for the specified connector. The SCEP protocol uses a challenge password to authenticate a request before issuing a certificate from a certificate authority (CA). Your SCEP clients include the challenge password as part of their certificate request to Connector for SCEP. To retrieve the connector Amazon Resource Names (ARNs) for the connectors in your account, call [ListConnectors](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_ListConnectors.html).

To create additional challenge passwords for the connector, call `CreateChallenge` again. We recommend frequently rotating your challenge passwords.

## Syntax
<a name="aws-resource-pcaconnectorscep-challenge-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-pcaconnectorscep-challenge-syntax.json"></a>

```
{
  "Type" : "AWS::PCAConnectorSCEP::Challenge",
  "Properties" : {
      "[ConnectorArn](#cfn-pcaconnectorscep-challenge-connectorarn)" : {{String}},
      "[Tags](#cfn-pcaconnectorscep-challenge-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-pcaconnectorscep-challenge-syntax.yaml"></a>

```
Type: AWS::PCAConnectorSCEP::Challenge
Properties:
  [ConnectorArn](#cfn-pcaconnectorscep-challenge-connectorarn): {{String}}
  [Tags](#cfn-pcaconnectorscep-challenge-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-pcaconnectorscep-challenge-properties"></a>

`ConnectorArn`  <a name="cfn-pcaconnectorscep-challenge-connectorarn"></a>
The Amazon Resource Name (ARN) of the connector.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[a-z]+)*:pca-connector-scep:[a-z]+(-[a-z]+)+-[1-9]\d*:\d{12}:connector\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}$`
*Minimum*: `5`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-pcaconnectorscep-challenge-tags"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-pcaconnectorscep-challenge-return-values"></a>

### Ref
<a name="aws-resource-pcaconnectorscep-challenge-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-pcaconnectorscep-challenge-return-values-fn--getatt"></a>

####
<a name="aws-resource-pcaconnectorscep-challenge-return-values-fn--getatt-fn--getatt"></a>

`ChallengeArn`  <a name="ChallengeArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the challenge.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
