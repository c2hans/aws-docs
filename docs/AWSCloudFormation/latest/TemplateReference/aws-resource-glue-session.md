---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-session.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Session
<a name="aws-resource-glue-session"></a>

The period in which a remote Spark runtime environment is running.

## Syntax
<a name="aws-resource-glue-session-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-glue-session-syntax.json"></a>

```
{
  "Type" : "AWS::Glue::Session",
  "Properties" : {
      "[Command](#cfn-glue-session-command)" : {{SessionCommand}},
      "[Connections](#cfn-glue-session-connections)" : {{ConnectionsList}},
      "[DefaultArguments](#cfn-glue-session-defaultarguments)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Description](#cfn-glue-session-description)" : {{String}},
      "[GlueVersion](#cfn-glue-session-glueversion)" : {{String}},
      "[Id](#cfn-glue-session-id)" : {{String}},
      "[IdleTimeout](#cfn-glue-session-idletimeout)" : {{Integer}},
      "[MaxCapacity](#cfn-glue-session-maxcapacity)" : {{Number}},
      "[NumberOfWorkers](#cfn-glue-session-numberofworkers)" : {{Integer}},
      "[RequestOrigin](#cfn-glue-session-requestorigin)" : {{String}},
      "[Role](#cfn-glue-session-role)" : {{String}},
      "[SecurityConfiguration](#cfn-glue-session-securityconfiguration)" : {{String}},
      "[Tags](#cfn-glue-session-tags)" : {{[ Tag, ... ]}},
      "[Timeout](#cfn-glue-session-timeout)" : {{Integer}},
      "[WorkerType](#cfn-glue-session-workertype)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-glue-session-syntax.yaml"></a>

```
Type: AWS::Glue::Session
Properties:
  [Command](#cfn-glue-session-command): {{
    SessionCommand}}
  [Connections](#cfn-glue-session-connections): {{
    ConnectionsList}}
  [DefaultArguments](#cfn-glue-session-defaultarguments): {{
    {{Key}}: {{Value}}}}
  [Description](#cfn-glue-session-description): {{String}}
  [GlueVersion](#cfn-glue-session-glueversion): {{String}}
  [Id](#cfn-glue-session-id): {{String}}
  [IdleTimeout](#cfn-glue-session-idletimeout): {{Integer}}
  [MaxCapacity](#cfn-glue-session-maxcapacity): {{Number}}
  [NumberOfWorkers](#cfn-glue-session-numberofworkers): {{Integer}}
  [RequestOrigin](#cfn-glue-session-requestorigin): {{String}}
  [Role](#cfn-glue-session-role): {{String}}
  [SecurityConfiguration](#cfn-glue-session-securityconfiguration): {{String}}
  [Tags](#cfn-glue-session-tags): {{
    - Tag}}
  [Timeout](#cfn-glue-session-timeout): {{Integer}}
  [WorkerType](#cfn-glue-session-workertype): {{String}}
```

## Properties
<a name="aws-resource-glue-session-properties"></a>

`Command`  <a name="cfn-glue-session-command"></a>
The command object.See SessionCommand.
*Required*: Yes
*Type*: [SessionCommand](aws-properties-glue-session-sessioncommand.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Connections`  <a name="cfn-glue-session-connections"></a>
The number of connections used for the session.
*Required*: No
*Type*: [ConnectionsList](aws-properties-glue-session-connectionslist.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DefaultArguments`  <a name="cfn-glue-session-defaultarguments"></a>
A map array of key-value pairs. Max is 75 pairs.
*Required*: No
*Type*: Object of String
*Pattern*: `^[.\-_A-Za-z0-9]+$`
*Minimum*: `0`
*Maximum*: `4096`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-glue-session-description"></a>
The description of the session.
*Required*: No
*Type*: String
*Pattern*: `^[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*$`
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`GlueVersion`  <a name="cfn-glue-session-glueversion"></a>
The AWS Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The GlueVersion must be greater than 2.0.
*Required*: No
*Type*: String
*Pattern*: `^(\w+\.)+\w+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Id`  <a name="cfn-glue-session-id"></a>
The ID of the session.
*Required*: Yes
*Type*: String
*Pattern*: `^[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IdleTimeout`  <a name="cfn-glue-session-idletimeout"></a>
The number of minutes when idle before the session times out.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxCapacity`  <a name="cfn-glue-session-maxcapacity"></a>
The number of AWS Glue data processing units (DPUs) that can be allocated when the job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB memory.
*Required*: No
*Type*: Number
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NumberOfWorkers`  <a name="cfn-glue-session-numberofworkers"></a>
The number of workers of a defined `WorkerType` to use for the session.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RequestOrigin`  <a name="cfn-glue-session-requestorigin"></a>
The origin of the request.
*Required*: No
*Type*: String
*Pattern*: `^[.\-_A-Za-z0-9]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Role`  <a name="cfn-glue-session-role"></a>
The name or Amazon Resource Name (ARN) of the IAM role associated with the Session.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[^:]*:iam::[0-9]*:role/.+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityConfiguration`  <a name="cfn-glue-session-securityconfiguration"></a>
The name of the SecurityConfiguration structure to be used with the session.
*Required*: No
*Type*: String
*Pattern*: `^[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-glue-session-tags"></a>
The map of key value pairs (tags) belonging to the session.
*Required*: No
*Type*: Array of [Tag](aws-properties-glue-session-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Timeout`  <a name="cfn-glue-session-timeout"></a>
 The number of minutes before session times out. Default for Spark ETL jobs is 48 hours (2880 minutes). Consult the documentation for other job types.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`WorkerType`  <a name="cfn-glue-session-workertype"></a>
The type of predefined worker that is allocated when a session runs. Accepts a value of `G.1X`, `G.2X`, `G.4X`, or `G.8X` for Spark sessions. Accepts the value `Z.2X` for Ray sessions.
*Required*: No
*Type*: String
*Allowed values*: `Standard | G.1X | G.2X | G.025X | G.4X | G.8X | Z.2X`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-glue-session-return-values"></a>

### Ref
<a name="aws-resource-glue-session-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-glue-session-return-values-fn--getatt"></a>

####
<a name="aws-resource-glue-session-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreatedOn`  <a name="CreatedOn-fn::getatt"></a>
The time and date when the session was created.

`Progress`  <a name="Progress-fn::getatt"></a>
The code execution progress of the session.

`Status`  <a name="Status-fn::getatt"></a>
The session status.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
