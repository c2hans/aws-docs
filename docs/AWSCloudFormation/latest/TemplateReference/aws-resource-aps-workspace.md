---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-aps-workspace.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::APS::Workspace
<a name="aws-resource-aps-workspace"></a>

An Amazon Managed Service for Prometheus workspace is a logical and isolated Prometheus server dedicated to ingesting, storing, and querying your Prometheus-compatible metrics.

## Syntax
<a name="aws-resource-aps-workspace-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-aps-workspace-syntax.json"></a>

```
{
  "Type" : "AWS::APS::Workspace",
  "Properties" : {
      "[AlertManagerDefinition](#cfn-aps-workspace-alertmanagerdefinition)" : {{String}},
      "[Alias](#cfn-aps-workspace-alias)" : {{String}},
      "[KmsKeyArn](#cfn-aps-workspace-kmskeyarn)" : {{String}},
      "[LoggingConfiguration](#cfn-aps-workspace-loggingconfiguration)" : {{LoggingConfiguration}},
      "[QueryLoggingConfiguration](#cfn-aps-workspace-queryloggingconfiguration)" : {{QueryLoggingConfiguration}},
      "[Tags](#cfn-aps-workspace-tags)" : {{[ Tag, ... ]}},
      "[WorkspaceConfiguration](#cfn-aps-workspace-workspaceconfiguration)" : {{WorkspaceConfiguration}}
    }
}
```

### YAML
<a name="aws-resource-aps-workspace-syntax.yaml"></a>

```
Type: AWS::APS::Workspace
Properties:
  [AlertManagerDefinition](#cfn-aps-workspace-alertmanagerdefinition): {{String}}
  [Alias](#cfn-aps-workspace-alias): {{String}}
  [KmsKeyArn](#cfn-aps-workspace-kmskeyarn): {{String}}
  [LoggingConfiguration](#cfn-aps-workspace-loggingconfiguration): {{
    LoggingConfiguration}}
  [QueryLoggingConfiguration](#cfn-aps-workspace-queryloggingconfiguration): {{
    QueryLoggingConfiguration}}
  [Tags](#cfn-aps-workspace-tags): {{
    - Tag}}
  [WorkspaceConfiguration](#cfn-aps-workspace-workspaceconfiguration): {{
    WorkspaceConfiguration}}
```

## Properties
<a name="aws-resource-aps-workspace-properties"></a>

`AlertManagerDefinition`  <a name="cfn-aps-workspace-alertmanagerdefinition"></a>
The alert manager definition, a YAML configuration for the alert manager in your Amazon Managed Service for Prometheus workspace.
For details about the alert manager definition, see [Creating an alert manager configuration files](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-alertmanager-config.html) in the *Amazon Managed Service for Prometheus User Guide*.
The following example shows part of a CloudFormation YAML file with an embedded alert manager definition (following the `- |-`).

```
  Workspace:
    Type: AWS::APS::Workspace
    ....
    Properties:
      ....
      AlertManagerDefinition:
        Fn::Sub:
          - |-
            alertmanager_config: |
              templates:
                - 'default_template'
              route:
                receiver: example-sns
              receivers:
                - name: example-sns
                  sns_configs:
                    - topic_arn: 'arn:aws:sns:${AWS::Region}:${AWS::AccountId}:${TopicName}'
          -
```
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Alias`  <a name="cfn-aps-workspace-alias"></a>
The alias that is assigned to this workspace to help identify it. It does not need to be unique.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-aps-workspace-kmskeyarn"></a>
(optional) The ARN for a customer managed AWS KMS key to use for encrypting data within your workspace. For more information about using your own key in your workspace, see [Encryption at rest](https://docs.aws.amazon.com/prometheus/latest/userguide/encryption-at-rest-Amazon-Service-Prometheus.html) in the *Amazon Managed Service for Prometheus User Guide*.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[-a-z]*:kms:[-a-z0-9]+:[0-9]{12}:key/.+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LoggingConfiguration`  <a name="cfn-aps-workspace-loggingconfiguration"></a>
Contains information about the logging configuration for the workspace.
*Required*: No
*Type*: [LoggingConfiguration](aws-properties-aps-workspace-loggingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryLoggingConfiguration`  <a name="cfn-aps-workspace-queryloggingconfiguration"></a>
The definition of logging configuration in an Amazon Managed Service for Prometheus workspace.
*Required*: No
*Type*: [QueryLoggingConfiguration](aws-properties-aps-workspace-queryloggingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-aps-workspace-tags"></a>
The list of tag keys and values that are associated with the workspace.
*Required*: No
*Type*: Array of [Tag](aws-properties-aps-workspace-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkspaceConfiguration`  <a name="cfn-aps-workspace-workspaceconfiguration"></a>
Use this structure to define label sets and the ingestion limits for time series that match label sets, and to specify the retention period of the workspace.
*Required*: No
*Type*: [WorkspaceConfiguration](aws-properties-aps-workspace-workspaceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-aps-workspace-return-values"></a>

### Ref
<a name="aws-resource-aps-workspace-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name. For example:

 `{ "Ref": "Id" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-aps-workspace-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-aps-workspace-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the workspace. For example, `arn:aws:aps:<region>:123456789012:workspace/ws-example1-1234-abcd-5678-ef90abcd1234`.

`PrometheusEndpoint`  <a name="PrometheusEndpoint-fn::getatt"></a>
The Prometheus endpoint available for this workspace. For example, `https://aps-workspaces.<region>.amazonaws.com/workspaces/ws-example1-1234-abcd-5678-ef90abcd1234/api/v1/`.

`WorkspaceId`  <a name="WorkspaceId-fn::getatt"></a>
The unique ID for the workspace. For example, `ws-example1-1234-abcd-5678-ef90abcd1234`.

## Examples
<a name="aws-resource-aps-workspace--examples"></a>

**Topics**
+ [Amazon Managed Service for Prometheus workspace example](#aws-resource-aps-workspace--examples--Amazon_Managed_Service_for_Prometheus_workspace_example)
+ [Amazon Managed Service for Prometheus logging configuration example](#aws-resource-aps-workspace--examples--Amazon_Managed_Service_for_Prometheus_logging_configuration_example)

### Amazon Managed Service for Prometheus workspace example
<a name="aws-resource-aps-workspace--examples--Amazon_Managed_Service_for_Prometheus_workspace_example"></a>

The following example creates an Amazon Managed Service for Prometheus workspace with an alias and one tag.

#### JSON
<a name="aws-resource-aps-workspace--examples--Amazon_Managed_Service_for_Prometheus_workspace_example--json"></a>

```
{ "Resources": { "APSWorkspace": { "Type":
                "AWS::APS::Workspace", "Properties": { "Alias": "TestWorkspace" "Tags": [ { "Key":
                "BusinessPurpose", "Value": "LoadTesting" } ] } } } }
```

#### YAML
<a name="aws-resource-aps-workspace--examples--Amazon_Managed_Service_for_Prometheus_workspace_example--yaml"></a>

```
Resources: APSWorkspace: Type: AWS::APS::Workspace Properties:
                Alias: TestWorkspace Tags: - Key: BusinessPurpose Value: LoadTesting
```

### Amazon Managed Service for Prometheus logging configuration example
<a name="aws-resource-aps-workspace--examples--Amazon_Managed_Service_for_Prometheus_logging_configuration_example"></a>

The following example creates a new workspace and sets a new logging configuration. You must replace the `LogGroupArn` with a valid ARN for your system.

#### JSON
<a name="aws-resource-aps-workspace--examples--Amazon_Managed_Service_for_Prometheus_logging_configuration_example--json"></a>

```
{ "Resources": { "APSWorkspace": { "Type":
                "AWS::APS::Workspace", "Properties": { "Alias": "TestWorkspace",
                "LoggingConfiguration": { "LogGroupArn":
                "arn:aws:logs:{region}:{account}:log-group:test-log-group:*" }, "Tags": [ { "Key":
                "BusinessPurpose", "Value": "LoadTesting" } ] } } } }
```

#### YAML
<a name="aws-resource-aps-workspace--examples--Amazon_Managed_Service_for_Prometheus_logging_configuration_example--yaml"></a>

```
Resources: APSWorkspace: Type: AWS::APS::Workspace Properties:
                Alias: TestWorkspace LoggingConfiguration: LogGroupArn:
                "arn:aws:logs:{region}:{account}:log-group:test-log-group:*" Tags: - Key:
                BusinessPurpose Value: LoadTesting
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
