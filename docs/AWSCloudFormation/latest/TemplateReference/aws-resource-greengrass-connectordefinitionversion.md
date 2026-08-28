---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-greengrass-connectordefinitionversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Greengrass::ConnectorDefinitionVersion
<a name="aws-resource-greengrass-connectordefinitionversion"></a>

The `AWS::Greengrass::ConnectorDefinitionVersion` resource represents a connector definition version for AWS IoT Greengrass. A connector definition version contains a list of connectors.

**Note**
To create a connector definition version, you must specify the ID of the connector definition that you want to associate with the version. For information about creating a connector definition, see [`AWS::Greengrass::ConnectorDefinition`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinition.html).
After you create a connector definition version that contains the connectors you want to deploy, you must add it to your group version. For more information, see [`AWS::Greengrass::Group`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html).

## Syntax
<a name="aws-resource-greengrass-connectordefinitionversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-greengrass-connectordefinitionversion-syntax.json"></a>

```
{
  "Type" : "AWS::Greengrass::ConnectorDefinitionVersion",
  "Properties" : {
      "[ConnectorDefinitionId](#cfn-greengrass-connectordefinitionversion-connectordefinitionid)" : {{String}},
      "[Connectors](#cfn-greengrass-connectordefinitionversion-connectors)" : {{[ Connector, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-greengrass-connectordefinitionversion-syntax.yaml"></a>

```
Type: AWS::Greengrass::ConnectorDefinitionVersion
Properties:
  [ConnectorDefinitionId](#cfn-greengrass-connectordefinitionversion-connectordefinitionid): {{String}}
  [Connectors](#cfn-greengrass-connectordefinitionversion-connectors): {{
    - Connector}}
```

## Properties
<a name="aws-resource-greengrass-connectordefinitionversion-properties"></a>

`ConnectorDefinitionId`  <a name="cfn-greengrass-connectordefinitionversion-connectordefinitionid"></a>
The ID of the connector definition associated with this version. This value is a GUID.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Connectors`  <a name="cfn-greengrass-connectordefinitionversion-connectors"></a>
The connectors in this version. Only one instance of a given connector can be added to the connector definition version at a time.
*Required*: Yes
*Type*: Array of [Connector](aws-properties-greengrass-connectordefinitionversion-connector.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-greengrass-connectordefinitionversion-return-values"></a>

### Ref
<a name="aws-resource-greengrass-connectordefinitionversion-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the connector definition version, such as `arn:aws:greengrass:us-east-1:123456789012:/greengrass/definition/connectors/1234a5b6-78cd-901e-2fgh-3i45j6k178l9/versions/9876ac30-4bdb-4f9d-95af-b5fdb66be1a2`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-greengrass-connectordefinitionversion-return-values-fn--getatt"></a>

## Examples
<a name="aws-resource-greengrass-connectordefinitionversion--examples"></a>

### Connector Definition Version Snippet
<a name="aws-resource-greengrass-connectordefinitionversion--examples--Connector_Definition_Version_Snippet"></a>

The following snippet defines connector definition and connector definition version resources. The connector definition version references the connector definition and contains a connector.

For an example of a complete template, see the [`AWS::Greengrass::Group`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html) resource.

#### JSON
<a name="aws-resource-greengrass-connectordefinitionversion--examples--Connector_Definition_Version_Snippet--json"></a>

```
"TestConnectorDefinition": {
    "Type": "AWS::Greengrass::ConnectorDefinition",
    "Properties": {
        "Name": "DemoTestConnectorDefinition"
    }
},
"TestConnectorDefinitionVersion": {
    "Type": "AWS::Greengrass::ConnectorDefinitionVersion",
    "Properties": {
        "ConnectorDefinitionId": {
            "Ref": "TestConnectorDefinition"
        },
        "Connectors": [
            {
                "Id": "Connector1",
                "ConnectorArn": {
                    "Fn::Join": [
                        ":",
                        [
                            "arn:aws:greengrass",
                            {
                                "Ref": "AWS::Region"
                            },
                            ":/connectors/SNS/versions/1"
                        ]
                    ]
                },
                "Parameters": {
                    "DefaultSNSArn": {
                        "Fn::Join": [
                            ":",
                            [
                                "arn:aws:sns",
                                {
                                    "Ref": "AWS::Region"
                                },
                                {
                                    "Ref": "AWS::AccountId"
                                },
                                "defaultSns"
                            ]
                        ]
                    }
                }
            }
        ]
    }
}
```

#### YAML
<a name="aws-resource-greengrass-connectordefinitionversion--examples--Connector_Definition_Version_Snippet--yaml"></a>

```
TestConnectorDefinition:
  Type: 'AWS::Greengrass::ConnectorDefinition'
  Properties:
    Name: DemoTestConnectorDefinition
TestConnectorDefinitionVersion:
  Type: 'AWS::Greengrass::ConnectorDefinitionVersion'
  Properties:
    ConnectorDefinitionId: !Ref TestConnectorDefinition
    Connectors:
      - Id: Connector1
        ConnectorArn: !Join
          - ':'
          - - 'arn:aws:greengrass'
            - !Ref 'AWS::Region'
            - ':/connectors/SNS/versions/1'
        Parameters:
          DefaultSNSArn: !Join
            - ':'
            - - 'arn:aws:sns'
              - !Ref 'AWS::Region'
              - !Ref 'AWS::AccountId'
              - defaultSns
```

## See also
<a name="aws-resource-greengrass-connectordefinitionversion--seealso"></a>
+ [CreateConnectorDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/createconnectordefinitionversion-post.html) in the * AWS IoT Greengrass Version 1 API Reference *
+  [AWS IoT Greengrass Version 1 Developer Guide](https://docs.aws.amazon.com/greengrass/v1/developerguide/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
