---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-athena-session.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Athena::Session
<a name="aws-resource-athena-session"></a>

<a name="aws-resource-athena-session-description"></a>The `AWS::Athena::Session` resource Property description not available. for Athena.

## Syntax
<a name="aws-resource-athena-session-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-athena-session-syntax.json"></a>

```
{
  "Type" : "AWS::Athena::Session",
  "Properties" : {
      "[EngineConfiguration](#cfn-athena-session-engineconfiguration)" : {{EngineConfiguration}},
      "[ExecutionRole](#cfn-athena-session-executionrole)" : {{String}},
      "[WorkGroup](#cfn-athena-session-workgroup)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-athena-session-syntax.yaml"></a>

```
Type: AWS::Athena::Session
Properties:
  [EngineConfiguration](#cfn-athena-session-engineconfiguration): {{
    EngineConfiguration}}
  [ExecutionRole](#cfn-athena-session-executionrole): {{String}}
  [WorkGroup](#cfn-athena-session-workgroup): {{String}}
```

## Properties
<a name="aws-resource-athena-session-properties"></a>

`EngineConfiguration`  <a name="cfn-athena-session-engineconfiguration"></a>
The engine configuration for the workgroup, which includes the minimum/maximum number of Data Processing Units (DPU) that queries should use when running in provisioned capacity. If not specified, Athena uses default values (Default value for min is 4 and for max is Minimum of 124 and allocated DPUs).
To specify DPU values for PC queries the WG containing EngineConfiguration should have the following values: The name of the Classifications should be `athena-query-engine-properties`, with the only allowed properties as `max-dpu-count` and `min-dpu-count`.
*Required*: Yes
*Type*: [EngineConfiguration](aws-properties-athena-session-engineconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExecutionRole`  <a name="cfn-athena-session-executionrole"></a>
The ARN of the execution role used to access user resources for Spark sessions and Identity Center enabled workgroups. This property applies only to Spark enabled workgroups and Identity Center enabled workgroups.
*Required*: No
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`WorkGroup`  <a name="cfn-athena-session-workgroup"></a>
A workgroup, which contains a name, description, creation time, state, and other configuration, listed under WorkGroup$Configuration. Each workgroup enables you to isolate queries for you or your group of users from other queries in the same account, to configure the query results location and the encryption configuration (known as workgroup settings), to enable sending query metrics to Amazon CloudWatch, and to establish per-query data usage control limits for all queries in a workgroup. The workgroup settings override is specified in `EnforceWorkGroupConfiguration` (true/false) in the `WorkGroupConfiguration`. See WorkGroupConfiguration$EnforceWorkGroupConfiguration.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9._-]{1,128}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-athena-session-return-values"></a>

### Ref
<a name="aws-resource-athena-session-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-athena-session-return-values-fn--getatt"></a>

####
<a name="aws-resource-athena-session-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`EngineVersion`  <a name="EngineVersion-fn::getatt"></a>
The engine version used by the session (for example, `PySpark engine version 3`).

`SessionId`  <a name="SessionId-fn::getatt"></a>
The session ID.
