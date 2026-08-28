---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-pipes-pipe.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe
<a name="aws-resource-pipes-pipe"></a>

Specifies a pipe. Amazon EventBridge Pipes connect event sources to targets and reduces the need for specialized knowledge and integration code.

**Note**
As an aid to help you jumpstart developing CloudFormation templates, the EventBridge console enables you to create templates from the existing pipes in your account. For more information, see [Generate an CloudFormation template from EventBridge Pipes](https://docs.aws.amazon.com/eventbridge/latest/userguide/pipes-generate-template.html) in the *Amazon EventBridge User Guide*.

## Syntax
<a name="aws-resource-pipes-pipe-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-pipes-pipe-syntax.json"></a>

```
{
  "Type" : "AWS::Pipes::Pipe",
  "Properties" : {
      "[Description](#cfn-pipes-pipe-description)" : {{String}},
      "[DesiredState](#cfn-pipes-pipe-desiredstate)" : {{String}},
      "[Enrichment](#cfn-pipes-pipe-enrichment)" : {{String}},
      "[EnrichmentParameters](#cfn-pipes-pipe-enrichmentparameters)" : {{PipeEnrichmentParameters}},
      "[KmsKeyIdentifier](#cfn-pipes-pipe-kmskeyidentifier)" : {{String}},
      "[LogConfiguration](#cfn-pipes-pipe-logconfiguration)" : {{PipeLogConfiguration}},
      "[Name](#cfn-pipes-pipe-name)" : {{String}},
      "[RoleArn](#cfn-pipes-pipe-rolearn)" : {{String}},
      "[Source](#cfn-pipes-pipe-source)" : {{String}},
      "[SourceParameters](#cfn-pipes-pipe-sourceparameters)" : {{PipeSourceParameters}},
      "[Tags](#cfn-pipes-pipe-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Target](#cfn-pipes-pipe-target)" : {{String}},
      "[TargetParameters](#cfn-pipes-pipe-targetparameters)" : {{PipeTargetParameters}}
    }
}
```

### YAML
<a name="aws-resource-pipes-pipe-syntax.yaml"></a>

```
Type: AWS::Pipes::Pipe
Properties:
  [Description](#cfn-pipes-pipe-description): {{String}}
  [DesiredState](#cfn-pipes-pipe-desiredstate): {{String}}
  [Enrichment](#cfn-pipes-pipe-enrichment): {{String}}
  [EnrichmentParameters](#cfn-pipes-pipe-enrichmentparameters): {{
    PipeEnrichmentParameters}}
  [KmsKeyIdentifier](#cfn-pipes-pipe-kmskeyidentifier): {{String}}
  [LogConfiguration](#cfn-pipes-pipe-logconfiguration): {{
    PipeLogConfiguration}}
  [Name](#cfn-pipes-pipe-name): {{String}}
  [RoleArn](#cfn-pipes-pipe-rolearn): {{String}}
  [Source](#cfn-pipes-pipe-source): {{String}}
  [SourceParameters](#cfn-pipes-pipe-sourceparameters): {{
    PipeSourceParameters}}
  [Tags](#cfn-pipes-pipe-tags): {{
    {{Key}}: {{Value}}}}
  [Target](#cfn-pipes-pipe-target): {{String}}
  [TargetParameters](#cfn-pipes-pipe-targetparameters): {{
    PipeTargetParameters}}
```

## Properties
<a name="aws-resource-pipes-pipe-properties"></a>

`Description`  <a name="cfn-pipes-pipe-description"></a>
A description of the pipe.
*Required*: No
*Type*: String
*Pattern*: `^.*$`
*Minimum*: `0`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DesiredState`  <a name="cfn-pipes-pipe-desiredstate"></a>
The state the pipe should be in.
*Required*: No
*Type*: String
*Allowed values*: `RUNNING | STOPPED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enrichment`  <a name="cfn-pipes-pipe-enrichment"></a>
The ARN of the enrichment resource.
*Required*: No
*Type*: String
*Pattern*: `^$|arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-]+):([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1})?:(\d{12})?:(.+)$`
*Minimum*: `0`
*Maximum*: `1600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnrichmentParameters`  <a name="cfn-pipes-pipe-enrichmentparameters"></a>
The parameters required to set up enrichment on your pipe.
*Required*: No
*Type*: [PipeEnrichmentParameters](aws-properties-pipes-pipe-pipeenrichmentparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyIdentifier`  <a name="cfn-pipes-pipe-kmskeyidentifier"></a>
The identifier of the AWS KMS customer managed key for EventBridge to use, if you choose to use a customer managed key to encrypt pipe data. The identifier can be the key Amazon Resource Name (ARN), KeyId, key alias, or key alias ARN.
To update a pipe that is using the default AWS owned key to use a customer managed key instead, or update a pipe that is using a customer managed key to use a different customer managed key, specify a customer managed key identifier.
To update a pipe that is using a customer managed key to use the default AWS owned key, specify an empty string.
For more information, see [Managing keys](https://docs.aws.amazon.com/kms/latest/developerguide/getting-started.html) in the *AWS Key Management Service Developer Guide*.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogConfiguration`  <a name="cfn-pipes-pipe-logconfiguration"></a>
The logging configuration settings for the pipe.
*Required*: No
*Type*: [PipeLogConfiguration](aws-properties-pipes-pipe-pipelogconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-pipes-pipe-name"></a>
The name of the pipe.
*Required*: No
*Type*: String
*Pattern*: `^[\.\-_A-Za-z0-9]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-pipes-pipe-rolearn"></a>
The ARN of the role that allows the pipe to send data to the target.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z0-9+=,.@\-_/]+$`
*Minimum*: `1`
*Maximum*: `1600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-pipes-pipe-source"></a>
The ARN of the source resource.
*Required*: Yes
*Type*: String
*Pattern*: `^smk://(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9]):[0-9]{1,5}|arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-]+):([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1})?:(\d{12})?:(.+)$`
*Minimum*: `1`
*Maximum*: `1600`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceParameters`  <a name="cfn-pipes-pipe-sourceparameters"></a>
The parameters required to set up a source for your pipe.
*Required*: No
*Type*: [PipeSourceParameters](aws-properties-pipes-pipe-pipesourceparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-pipes-pipe-tags"></a>
The list of key-value pairs to associate with the pipe.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Target`  <a name="cfn-pipes-pipe-target"></a>
The ARN of the target resource.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-]+):([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1})?:(\d{12})?:(.+)$`
*Minimum*: `1`
*Maximum*: `1600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetParameters`  <a name="cfn-pipes-pipe-targetparameters"></a>
The parameters required to set up a target for your pipe.
For more information about pipe target parameters, including how to use dynamic path parameters, see [Target parameters](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-event-target.html) in the *Amazon EventBridge User Guide*.
*Required*: No
*Type*: [PipeTargetParameters](aws-properties-pipes-pipe-pipetargetparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-pipes-pipe-return-values"></a>

### Ref
<a name="aws-resource-pipes-pipe-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the pipe that was created by the request.

### Fn::GetAtt
<a name="aws-resource-pipes-pipe-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-pipes-pipe-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the pipe.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The time the pipe was created.

`CurrentState`  <a name="CurrentState-fn::getatt"></a>
The state the pipe is in.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
When the pipe was last updated, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).

`StateReason`  <a name="StateReason-fn::getatt"></a>
The reason the pipe is in its current state.

## Examples
<a name="aws-resource-pipes-pipe--examples"></a>

**Topics**
+ [Create a Pipe with an enrichment](#aws-resource-pipes-pipe--examples--Create_a_Pipe_with_an_enrichment)
+ [Create a pipe with an event filter](#aws-resource-pipes-pipe--examples--Create_a_pipe_with_an_event_filter)

### Create a Pipe with an enrichment
<a name="aws-resource-pipes-pipe--examples--Create_a_Pipe_with_an_enrichment"></a>

Create a Pipe with an Amazon SQS source, an API Gateway enrichment, and a Step Functions state machine target.

#### JSON
<a name="aws-resource-pipes-pipe--examples--Create_a_Pipe_with_an_enrichment--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "TestPipe": {
      "Type": "AWS::Pipes::Pipe",
      "Properties": {
        "Name": "PipeCfnExample",
        "RoleArn": "arn:aws:iam::123456789123:role/Pipe-Dev-All-Targets-Dummy-Execution-Role",
        "Source": "arn:aws:sqs:us-east-1:123456789123:pipeDemoSource",
        "Enrichment": "arn:aws:execute-api:us-east-1:123456789123:53eo2i89p9/*/POST/pets",
        "Target": "arn:aws:states:us-east-1:123456789123:stateMachine:PipeTargetStateMachine"
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-pipes-pipe--examples--Create_a_Pipe_with_an_enrichment--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  TestPipe:
    Type: AWS::Pipes::Pipe
    Properties:
      Name:  PipeCfnExample
      RoleArn: arn:aws:iam::123456789123:role/Pipe-Dev-All-Targets-Dummy-Execution-Role
      Source: arn:aws:sqs:us-east-1:123456789123:pipeDemoSource
      Enrichment: arn:aws:execute-api:us-east-1:123456789123:53eo2i89p9/*/POST/pets
      Target: arn:aws:states:us-east-1:123456789123:stateMachine:PipeTargetStateMachine
```

### Create a pipe with an event filter
<a name="aws-resource-pipes-pipe--examples--Create_a_pipe_with_an_event_filter"></a>

The following example:
+ Provisions a DynamoDB table and associated data stream to act as the pipe source, and a Amazon SQS queue for the pipe target.
+ Provisions an IAM execution role for the pipe that defines the necessary permissions to access both the source and target.
+ Creates a pipe that connects the DynamoDB stream source to the Amazon SQS queue target.
+ Within the pipe, defines an event filter with an event pattern that selects events where `eventname` is `INSERT` or `MODIFY`.

**Note**
Be aware that you will be billed for the AWS resources used if you create a stack from this template.

#### JSON
<a name="aws-resource-pipes-pipe--examples--Create_a_pipe_with_an_event_filter--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",

 "Description" : "EventBridge Pipe template example. Provisions a pipe, along with a DynamoDB stream as the pipe source and an SQS queue as the pipe target. Also provisions an execution role that contains the necessary permissions to access both the source and target. Once provisioned, the pipe receives events from the DynamoDB data stream, applies a filter, and sends matching events on to an SQS Queue. You will be billed for the Amazon resources used if you create a stack from this template.",

  "Parameters" : {
    "SourceTableName" : {
      "Type" : "String",
      "Default" : "pipe-example-source",
      "Description" : "Specify the name of the table to provision as the pipe source, or accept the default."
    },
  "TargetQueueName" : {
    "Type" : "String",
    "Default" : "pipe-example-target",
    "Description" : "Specify the name of the queue to provision as the pipe target, or accept the default."
  },
    "PipeName" : {
      "Type" : "String",
      "Default" : "pipe-with-filtering-example",
      "Description" : "Specify the name of the table to provision as the pipe source, or accept the default."
    }
},
  "Resources": {
    "PipeSourceDynamoDBTable": {
      "Type": "AWS::DynamoDB::Table",
      "Properties": {
        "AttributeDefinitions": [{
            "AttributeName": "Album",
            "AttributeType": "S"
          },
          {
            "AttributeName": "Artist",
            "AttributeType": "S"
          }

        ],
        "KeySchema": [{
            "AttributeName": "Album",
            "KeyType": "HASH"

          },
          {
            "AttributeName": "Artist",
            "KeyType": "RANGE"
          }
        ],
        "ProvisionedThroughput": {
          "ReadCapacityUnits": 10,
          "WriteCapacityUnits": 10
        },
        "StreamSpecification": {
          "StreamViewType": "NEW_AND_OLD_IMAGES"
        },
        "TableName": { "Ref" : "SourceTableName" }
      }
    },
    "PipeTargetQueue": {
      "Type": "AWS::SQS::Queue",
      "Properties": {
        "QueueName": { "Ref" : "TargetQueueName" }
      }
    },
    "PipeTutorialPipeRole": {
      "Type": "AWS::IAM::Role",
      "Properties": {
        "AssumeRolePolicyDocument": {
          "Version": "2012-10-17"		 	 	 ,
          "Statement": [{
            "Effect": "Allow",
            "Principal": {
              "Service": "pipes.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
              "StringLike": {
                "aws:SourceArn": {
	"Fn::Join": [
		"",
                [
                  "arn:",
                  { "Ref": "AWS::Partition" },
                  ":pipes:",
                  { "Ref": "AWS::Region" },
                  ":",
                  { "Ref": "AWS::AccountId" },
                  ":pipe/",
                  { "Ref": "PipeName" }
               ]
	]
       },
                "aws:SourceAccount": { "Ref" : "AWS::AccountId" }
              }
            }
          }]
        },
        "Description" : "EventBridge Pipe template example. Execution role that grants the pipe the permissions necessary to send events to the specified pipe.",
        "Path": "/",
        "Policies": [{
            "PolicyName": "SourcePermissions",
            "PolicyDocument": {
              "Version": "2012-10-17"		 	 	 ,
              "Statement": [{
                "Effect": "Allow",
                "Action": [
                  "dynamodb:DescribeStream",
                  "dynamodb:GetRecords",
                  "dynamodb:GetShardIterator",
                  "dynamodb:ListStreams"
                ],
                "Resource": [
                  { "Fn::GetAtt" : [ "PipeSourceDynamoDBTable", "StreamArn" ] }
                ]
              }]
            }
          },
          {
            "PolicyName": "TargetPermissions",
            "PolicyDocument": {
              "Version": "2012-10-17"		 	 	 ,
              "Statement": [{
                "Effect": "Allow",
                "Action": [
                  "sqs:SendMessage"
                ],
                "Resource": [
                  { "Fn::GetAtt" : [ "PipeTargetQueue", "Arn" ] }
                ]
              }]
            }
          }
        ]
      }
  },
    "PipeWithFiltering": {
      "Type": "AWS::Pipes::Pipe",
      "Properties": {
        "Description" : "EventBridge Pipe template example. Pipe that receives events from a DynamoDB stream, applies a filter, and sends matching events on to an SQS Queue.",
        "Name": { "Ref" : "PipeName" },
        "RoleArn": {"Fn::GetAtt" : ["PipeTutorialPipeRole", "Arn"] },
        "Source": { "Fn::GetAtt" : [ "PipeSourceDynamoDBTable", "StreamArn" ] },
        "SourceParameters": {
          "DynamoDBStreamParameters" : {
            "StartingPosition" : "LATEST"
         },
        "FilterCriteria" : {
          "Filters" : [ {
            "Pattern" : "{ \"eventName\": [\"INSERT\", \"MODIFY\"] }"
         }]
        }
        },
        "Target": { "Fn::GetAtt" : [ "PipeTargetQueue", "Arn" ] }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-pipes-pipe--examples--Create_a_pipe_with_an_event_filter--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Description: >-
  EventBridge Pipe template example. Provisions a pipe, along with a DynamoDB
  stream as the pipe source and an SQS queue as the pipe target. Also provisions
  an execution role that contains the necessary permissions to access both the
  source and target. Once provisioned, the pipe receives events from the
  DynamoDB data stream, applies a filter, and sends matching events on to an SQS
  Queue. You will be billed for the Amazon resources used if you create a stack
  from this template.
Parameters:
  SourceTableName:
    Type: String
    Default: pipe-example-source
    Description: >-
      Specify the name of the table to provision as the pipe source, or accept
      the default.
  TargetQueueName:
    Type: String
    Default: pipe-example-target
    Description: >-
      Specify the name of the queue to provision as the pipe target, or accept
      the default.
  PipeName:
    Type: String
    Default: pipe-with-filtering-example
    Description: >-
      Specify the name of the table to provision as the pipe source, or accept
      the default.
Resources:
  PipeSourceDynamoDBTable:
    Type: 'AWS::DynamoDB::Table'
    Properties:
      AttributeDefinitions:
        - AttributeName: Album
          AttributeType: S
        - AttributeName: Artist
          AttributeType: S
      KeySchema:
        - AttributeName: Album
          KeyType: HASH
        - AttributeName: Artist
          KeyType: RANGE
      ProvisionedThroughput:
        ReadCapacityUnits: 10
        WriteCapacityUnits: 10
      StreamSpecification:
        StreamViewType: NEW_AND_OLD_IMAGES
      TableName:
        Ref: SourceTableName
  PipeTargetQueue:
    Type: 'AWS::SQS::Queue'
    Properties:
      QueueName:
        Ref: TargetQueueName
  PipeTutorialPipeRole:
    Type: 'AWS::IAM::Role'
    Properties:
      AssumeRolePolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal:
              Service: pipes.amazonaws.com
            Action: 'sts:AssumeRole'
            Condition:
              StringLike:
                'aws:SourceArn':
                  'Fn::Join':
                    - ''
                    - - 'arn:'
                      - Ref: 'AWS::Partition'
                      - ':pipes:'
                      - Ref: 'AWS::Region'
                      - ':'
                      - Ref: 'AWS::AccountId'
                      - ':pipe/'
                      - Ref: PipeName
                'aws:SourceAccount':
                  Ref: 'AWS::AccountId'
      Description: >-
        EventBridge Pipe template example. Execution role that grants the pipe
        the permissions necessary to send events to the specified pipe.
      Path: /
      Policies:
        - PolicyName: SourcePermissions
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action:
                  - 'dynamodb:DescribeStream'
                  - 'dynamodb:GetRecords'
                  - 'dynamodb:GetShardIterator'
                  - 'dynamodb:ListStreams'
                Resource:
                  - 'Fn::GetAtt':
                      - PipeSourceDynamoDBTable
                      - StreamArn
        - PolicyName: TargetPermissions
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action:
                  - 'sqs:SendMessage'
                Resource:
                  - 'Fn::GetAtt':
                      - PipeTargetQueue
                      - Arn
  PipeWithFiltering:
    Type: 'AWS::Pipes::Pipe'
    Properties:
      Description: >-
        EventBridge Pipe template example. Pipe that receives events from a
        DynamoDB stream, applies a filter, and sends matching events on to an
        SQS Queue.
      Name:
        Ref: PipeName
      RoleArn:
        'Fn::GetAtt':
          - PipeTutorialPipeRole
          - Arn
      Source:
        'Fn::GetAtt':
          - PipeSourceDynamoDBTable
          - StreamArn
      SourceParameters:
        DynamoDBStreamParameters:
          StartingPosition: LATEST
        FilterCriteria:
          Filters:
            - Pattern: '{ "eventName": ["INSERT", "MODIFY"] }'
      Target:
        'Fn::GetAtt':
          - PipeTargetQueue
          - Arn
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
