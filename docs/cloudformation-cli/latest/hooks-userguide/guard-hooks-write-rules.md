---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/guard-hooks-write-rules.html
---

# Write Guard rules to evaluate resources for Guard Hooks
<a name="guard-hooks-write-rules"></a>

AWS CloudFormation Guard is an open-source and general purpose domain specific language (DSL) you can use to author policy-as-code. This topic explains how to use Guard to author example rules which can be run in the Guard Hook to automatically evaluate CloudFormation and AWS Cloud Control API operations. It will also focus on the different types of inputs available to your Guard rules depending on when your Guard Hook runs. A Guard Hook can be configured to run during the following types of operations:
+ Resource operations
+ Stack operations
+ Change set operations

For more information on writing Guard rules, see [Writing AWS CloudFormation Guard rules](https://docs.aws.amazon.com/cfn-guard/latest/ug/writing-rules.html)

**Topics**
+ [Resource operation Guard rules](#guard-hooks-write-rules-resource-operations)
+ [Stack operation Guard rules](#guard-hooks-write-rules-stack-operations)
+ [Change set operation Guard rules](#guard-hooks-write-rules-change-set-operations)

## Resource operation Guard rules
<a name="guard-hooks-write-rules-resource-operations"></a>

Any time you create, update, or delete a resource, that's considered a resource operation. As an example, if you run update a CloudFormation stack that creates a new resource, you have completed a resource operation. When you create, update or delete a resource using Cloud Control API, that is also considered a resource operation. You can configure your Guard Hook to target `RESOURCE` and `CLOUD_CONTROL` operations in the `TargetOperations` configuration for your Hook. When your Guard Hook evaluates a resource operation, the Guard engine evaluates a resource input.

**Topics**
+ [Guard resource input syntax](#guard-hooks-write-rules-resource-operations-input)
+ [Example Guard resource operation input](#guard-hooks-write-rules-resource-operations-example)
+ [Guard rules for resource changes](#guard-hooks-rules-resource-changes)

### Guard resource input syntax
<a name="guard-hooks-write-rules-resource-operations-input"></a>

The Guard resource input is the data that's made available to your Guard rules to evaluate.

The following is an example shape of a resource input:

```
HookContext:
  AWSAccountID: String
  StackId: String
  HookTypeName: String
  HookTypeVersion: String
  InvocationPoint: [CREATE_PRE_PROVISION, UPDATE_PRE_PROVISION, DELETE_PRE_PROVISION]
  TargetName: String
  TargetType: RESOURCE
  TargetLogicalId: String
  ChangeSetId: String
Resources:
  {ResourceLogicalID}:
    ResourceType: {ResourceType}
    ResourceProperties:
        {ResourceProperties}
Previous:
  ResourceLogicalID:
    ResourceType: {ResourceType}
    ResourceProperties:
        {PreviousResourceProperties}
```

`HookContext`  <a name="guard-hook-resource-hookcontext"></a>
`AWSAccountID`  <a name="guard-hook-resource-awsaccountid"></a>
The ID of the AWS account containing the resource being evaluated.
`StackId`  <a name="guard-hook-resource-stackid"></a>
The stack ID of the CloudFormation stack that is part of the resource operation. This is empty if the caller is Cloud Control API.
`HookTypeName`  <a name="guard-hook-resource-hooktypename"></a>
The name of the Hook that's running.
`HookTypeVersion`  <a name="guard-hook-resource-hooktypeversion"></a>
The version of the Hook that is running.
`InvocationPoint`  <a name="guard-hook-resource-invocationpoint"></a>
The exact point in the provisioning logic where the Hook runs.
*Valid values*: (`CREATE_PRE_PROVISION` \| `UPDATE_PRE_PROVISION` \| `DELETE_PRE_PROVISION`)
`TargetName`  <a name="guard-hook-resource-targetname"></a>
The target type being evaluated, for example, `AWS::S3::Bucket`.
`TargetType`  <a name="guard-hook-resource-targettype"></a>
The target type being evaluated, for example `AWS::S3::Bucket`. For resources provisioned with Cloud Control API, this value will be `RESOURCE`.
`TargetLogicalId`  <a name="guard-hook-resource-targetlogicalid"></a>
The `TargetLogicalId` of the resource being evaluated. If the origin of the Hook is CloudFormation, this will be the logical ID (also known as logical name) of the resource. If the origin of the Hook is Cloud Control API, this will be a constructed value.
`ChangeSetId`  <a name="guard-hook-resource-changesetid"></a>
The change set ID that was executed to cause the Hook invocation. This value is empty if the resource change was initiated by Cloud Control API, or the `create-stack`, `update-stack`, or `delete-stack` operations.

`Resources`  <a name="guard-hook-resource-resources"></a>
`ResourceLogicalID`  <a name="guard-hook-resource-current-resourcelogicalid"></a>
When the operation is initiated by CloudFormation, the `ResourceLogicalID` is the logical ID of the resource in the CloudFormation template.
When the operation's initiated by Cloud Control API, the `ResourceLogicalID` is a combination of the resource type, name, operation ID, and request ID.
`ResourceType`  <a name="guard-hook-resource-current-resourcetype"></a>
The type name of the resource (example: `AWS::S3::Bucket`).
`ResourceProperties`  <a name="guard-hook-resource-current-resourceproperties"></a>
The proposed properties of the resource being modified. When the Guard Hook is running against the CloudFormation resource changes, any functions, parameters, and transforms will be fully resolved. If the resource is being deleted, this value will be empty.

`Previous`  <a name="guard-hook-resource-previous"></a>
`ResourceLogicalID`  <a name="guard-hook-resource-previous-resourcelogicalid"></a>
When the operation is initiated by CloudFormation, the `ResourceLogicalID` is the logical ID of the resource in the CloudFormation template.
When the operation's initiated by Cloud Control API, the `ResourceLogicalID` is a combination of the resource type, name, operation ID, and request ID.
`ResourceType`  <a name="guard-hook-resource-previous-resourcetype"></a>
The type name of the resource (example: `AWS::S3::Bucket`).
`ResourceProperties`  <a name="guard-hook-resource-previous-resourceproperties"></a>
The current properties associated with the resource being modified. If the resource is being deleted, this value will be empty.

### Example Guard resource operation input
<a name="guard-hooks-write-rules-resource-operations-example"></a>

The following example input shows a Guard Hook that will receive the definition of the `AWS::S3::Bucket` resource to update. This is the data available to Guard for evaluation.

```
HookContext:
  AwsAccountId: "123456789012"
  StackId: "arn:aws:cloudformation:us-west-2:123456789012:stack/MyStack/1a2345b6-0000-00a0-a123-00abc0abc000"
  HookTypeName: org::s3policy::hook
  HookTypeVersion: "00001"
  InvocationPoint: UPDATE_PRE_PROVISION
  TargetName: AWS::S3::Bucket
  TargetType: RESOURCE
  TargetLogicalId: MyS3Bucket
  ChangeSetId: ""
Resources:
  MyS3Bucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: {{amzn-s3-demo-bucket}}
      ObjectLockEnabled: true
Previous:
  MyS3Bucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: {{amzn-s3-demo-bucket}}
      ObjectLockEnabled: false
```

To see all of the properties available for the resource type, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html).

### Guard rules for resource changes
<a name="guard-hooks-rules-resource-changes"></a>

When a Guard Hook evaluates resource changes, it starts by downloading all the rules configured with the Hook. These rules are then evaluated against the resource input. The Hook will fail if any rules fail their evaluation. If there are no failures, the Hook will pass.

The following example is a Guard rule that evaluates if the `ObjectLockEnabled` property is `true` for any `AWS::S3::Bucket` resource types.

```
let s3_buckets_default_lock_enabled = Resources.*[ Type == 'AWS::S3::Bucket']

rule S3_BUCKET_DEFAULT_LOCK_ENABLED when %s3_buckets_default_lock_enabled !empty {
  %s3_buckets_default_lock_enabled.Properties.ObjectLockEnabled exists
  %s3_buckets_default_lock_enabled.Properties.ObjectLockEnabled == true
  <<
    Violation: S3 Bucket ObjectLockEnabled must be set to true.
    Fix: Set the S3 property ObjectLockEnabled parameter to true.
  >>
}
```

When this rule runs against the following input, it will fail since the `ObjectLockEnabled` property isn't set to `true`.

```
Resources:
  MyS3Bucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: {{amzn-s3-demo-bucket}}
      ObjectLockEnabled: false
```

When this rule runs against the following input, it will pass since the `ObjectLockEnabled` is set to `true`.

```
Resources:
  MyS3Bucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: {{amzn-s3-demo-bucket}}
      ObjectLockEnabled: true
```

When a Hook fails, the rules which failed will be propagated back to CloudFormation or Cloud Control API. If a logging bucket has been configured for the Guard Hook, additional rule feedback will be provided there. This additional feedback includes the `Violation` and `Fix` information.

## Stack operation Guard rules
<a name="guard-hooks-write-rules-stack-operations"></a>

When a CloudFormation stack is created, updated, or deleted, you can configure your Guard Hook to start by evaluating the new template and potentially block the stack operation from proceeding. You can configure your Guard Hook to target `STACK` operations in the `TargetOperations` configuration for your Hook.

**Topics**
+ [Guard stack input syntax](#guard-hooks-write-rules-stack-operations-input)
+ [Example Guard stack operation input](#guard-hooks-write-rules-stack-operations-example)
+ [Guard rules for stack changes](#guard-hooks-rules-stack-changes)

### Guard stack input syntax
<a name="guard-hooks-write-rules-stack-operations-input"></a>

The input for Guard stack operations provides the whole CloudFormation template for your Guard rules to evaluate.

The following is an example shape of a stack input:

```
HookContext:
  AWSAccountID: String
  StackId: String
  HookTypeName: String
  HookTypeVersion: String
  InvocationPoint: [CREATE_PRE_PROVISION, UPDATE_PRE_PROVISION, DELETE_PRE_PROVISION]
  TargetName: String
  TargetType:STACK
  ChangeSetId: String
{Proposed CloudFormation Template}
Previous:
    {CloudFormation Template}
```

`HookContext`  <a name="guard-hook-stack-hookcontext"></a>
`AWSAccountID`  <a name="guard-hook-stack-awsaccountid"></a>
The ID of the AWS account containing the resource.
`StackId`  <a name="guard-hook-stack-stackid"></a>
The stack ID of the CloudFormation stack that is part of the stack operation.
`HookTypeName`  <a name="guard-hook-stack-hooktypename"></a>
The name of the Hook that's running.
`HookTypeVersion`  <a name="guard-hook-stack-hooktypeversion"></a>
The version of the Hook that is running.
`InvocationPoint`  <a name="guard-hook-stack-invocationpoint"></a>
The exact point in the provisioning logic where the Hook runs.
*Valid values*: (`CREATE_PRE_PROVISION` \| `UPDATE_PRE_PROVISION` \| `DELETE_PRE_PROVISION`)
`TargetName`  <a name="guard-hook-stack-targetname"></a>
The name of the stack being evaluated.
`TargetType`  <a name="guard-hook-stack-targettype"></a>
This value will be `STACK` when running as a stack-level Hook.
`ChangeSetId`  <a name="guard-hook-stack-changesetid"></a>
The change set ID that was executed to cause the Hook invocation. This value is empty if the stack operation was initiated by a `create-stack`, `update-stack`, or `delete-stack` operation.

`Proposed CloudFormation Template`  <a name="guard-hook-stack-template-current-template"></a>
The full CloudFormation template value that was passed to CloudFormation `create-stack` or `update-stack` operations. This includes things like the `Resources`, `Outputs`, and `Properties`. It can be a JSON or YAML string depending on what was provided to CloudFormation.
In `delete-stack` operations, this value will be empty.

`Previous`  <a name="guard-hook-stack-template-previous-template"></a>
The last successfully deployed CloudFormation template. This value is empty if the stack is being created or deleted.
In `delete-stack` operations, this value will be empty.

**Note**
The templates provided are what is passed into `create` or `update` stack operations. When deleting a stack, no template values are provided.

### Example Guard stack operation input
<a name="guard-hooks-write-rules-stack-operations-example"></a>

The following example input shows a Guard Hook that will receive a full template and the previously deployed template. The template in this example is using the JSON format.

```
HookContext:
  AwsAccountId: 123456789012
  StackId: "arn:aws:cloudformation:us-west-2:123456789012:stack/MyStack/1a2345b6-0000-00a0-a123-00abc0abc000"
  HookTypeName: org::templatechecker::hook
  HookTypeVersion: "00001"
  InvocationPoint: UPDATE_PRE_PROVISION
  TargetName: MyStack
  TargetType: CHANGE_SET
  TargetLogicalId: arn:aws:cloudformation:us-west-2:123456789012:changeSet/SampleChangeSet/1a2345b6-0000-00a0-a123-00abc0abc000
  ChangeSetId: arn:aws:cloudformation:us-west-2:123456789012:changeSet/SampleChangeSet/1a2345b6-0000-00a0-a123-00abc0abc000
Resources: {
   "S3Bucket": {
        "Type": "AWS::S3::Bucket",
        "Properties": {
           "BucketEncryption": {
               "ServerSideEncryptionConfiguration": [
                {"ServerSideEncryptionByDefault":
                    {"SSEAlgorithm": "aws:kms",
                      "KMSMasterKeyID": "KMS-KEY-ARN" },
                      "BucketKeyEnabled": true }
                ]
           }
        }
}
Previous: {
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "S3Bucket": {
            "Type": "AWS::S3::Bucket",
            "Properties": {}
        }
    }
}
```

### Guard rules for stack changes
<a name="guard-hooks-rules-stack-changes"></a>

When a Guard Hook evaluates stack changes, it starts by downloading all the rules configured with the Hook. These rules are then evaluated against the resource input. The Hook will fail if any rules fail their evaluation. If there are no failures, the Hook will pass.

The following example is a Guard rule that evaluates if there are any `AWS::S3::Bucket` resource types containing a property called `BucketEncryption`, with the `SSEAlgorithm` set to either `aws:kms` or `AES256`.

```
let s3_buckets_s3_default_encryption = Resources.*[ Type == 'AWS::S3::Bucket']

rule S3_DEFAULT_ENCRYPTION_KMS when %s3_buckets_s3_default_encryption !empty {
  %s3_buckets_s3_default_encryption.Properties.BucketEncryption exists
  %s3_buckets_s3_default_encryption.Properties.BucketEncryption.ServerSideEncryptionConfiguration[*].ServerSideEncryptionByDefault.SSEAlgorithm in ["aws:kms","AES256"]
  <<
    Violation: S3 Bucket default encryption must be set.
    Fix: Set the S3 Bucket property BucketEncryption.ServerSideEncryptionConfiguration.ServerSideEncryptionByDefault.SSEAlgorithm to either "aws:kms" or "AES256"
  >>
}
```

When the rule runs against the following template, it will `fail`.

```
AWSTemplateFormatVersion: 2010-09-09
Description: S3 bucket without default encryption
Resources:
  EncryptedS3Bucket:
    Type: 'AWS::S3::Bucket'
    Properties:
      BucketName: !Sub 'encryptedbucket-${AWS::Region}-${AWS::AccountId}'
```

When the rule runs against the following template, it will `pass`.

```
AWSTemplateFormatVersion: 2010-09-09
Description: S3 bucket with default encryption using SSE-KMS with an S3 Bucket Key
Resources:
  EncryptedS3Bucket:
    Type: 'AWS::S3::Bucket'
    Properties:
      BucketName: !Sub 'encryptedbucket-${AWS::Region}-${AWS::AccountId}'
      BucketEncryption:
        ServerSideEncryptionConfiguration:
          - ServerSideEncryptionByDefault:
              SSEAlgorithm: 'aws:kms'
              KMSMasterKeyID: KMS-KEY-ARN
            BucketKeyEnabled: true
```

## Change set operation Guard rules
<a name="guard-hooks-write-rules-change-set-operations"></a>

When a CloudFormation change set is created, you can configure your Guard Hook to evaluate the template and changes proposed in the change set to block the change set execution.

**Topics**
+ [Guard change set input syntax](#guard-hooks-write-rules-change-set-operations-input)
+ [Example Guard change set operation input](#guard-hooks-write-rules-change-set-operations-example)
+ [Guard rule for change set operations](#guard-hooks-rules-change-set-operations)

### Guard change set input syntax
<a name="guard-hooks-write-rules-change-set-operations-input"></a>

The Guard change set input is the data that's made available to your Guard rules to evaluate.

The following is an example shape of a change set input:

```
HookContext:
  AWSAccountID: String
  StackId: String
  HookTypeName: String
  HookTypeVersion: String
  InvocationPoint: [CREATE_PRE_PROVISION, UPDATE_PRE_PROVISION, DELETE_PRE_PROVISION]
  TargetName: CHANGE_SET
  TargetType:CHANGE_SET
  TargetLogicalId:ChangeSet ID
  ChangeSetId: String
{Proposed CloudFormation Template}
Previous:
  {CloudFormation Template}
Changes: [{ResourceChange}]
```

The `ResourceChange` model syntax is:

```
logicalResourceId: String
resourceType: String
action: CREATE, UPDATE, DELETE
lineNumber: Number
beforeContext: JSON String
afterContext: JSON String
```

`HookContext`  <a name="guard-hook-change-set-hookcontext"></a>
`AWSAccountID`  <a name="guard-hook-change-set-awsaccountid"></a>
The ID of the AWS account containing the resource.
`StackId`  <a name="guard-hook-change-set-stackid"></a>
The stack ID of the CloudFormation stack that is part of the stack operation.
`HookTypeName`  <a name="guard-hook-change-set-hooktypename"></a>
The name of the Hook that's running.
`HookTypeVersion`  <a name="guard-hook-change-set-hooktypeversion"></a>
The version of the Hook that is running.
`InvocationPoint`  <a name="guard-hook-change-set-invocationpoint"></a>
The exact point in the provisioning logic where the Hook runs.
*Valid values*: (`CREATE_PRE_PROVISION` \| `UPDATE_PRE_PROVISION` \| `DELETE_PRE_PROVISION`)
`TargetName`  <a name="guard-hook-change-set-targetname"></a>
The name of the stack being evaluated.
`TargetType`  <a name="guard-hook-change-set-targettype"></a>
This value will be `CHANGE_SET` when running as a change set-level Hook.
`TargetLogicalId`  <a name="guard-hook-change-set-targetlogicalid"></a>
This value will be the ARN of the change set.
`ChangeSetId`  <a name="guard-hook-change-set-changesetid"></a>
The change set ID that was executed to cause the Hook invocation. This value is empty if the stack operation was initiated by a `create-stack`, `update-stack`, or `delete-stack` operation.

`Proposed CloudFormation Template`  <a name="guard-hook-change-set-current-template"></a>
The full CloudFormation template that was provided to a `create-change-set` operation. It can be a JSON or YAML string depending on what was provided to CloudFormation.

`Previous`  <a name="guard-hook-change-set-previous-template"></a>
The last successfully deployed CloudFormation template. This value is empty if the stack is being created or deleted.

`Changes`  <a name="guard-hook-change-set-changes"></a>
The `Changes` model. This lists the resource changes.

Changes
logicalResourceId  <a name="guard-hook-change-set-change-logicalresourceid"></a>
The logical resource name of the changed resource.
resourceType  <a name="guard-hook-change-set-change-resourcetype"></a>
The resource type that will be changed.
action  <a name="guard-hook-change-set-change-action"></a>
The type of operation being performed on the resource.
*Valid values*: (`CREATE` \| `UPDATE` \| `DELETE`)
lineNumber  <a name="guard-hook-change-set-change-linenumber"></a>
The line number in the template associated with the change.
beforeContext  <a name="guard-hook-change-set-change-beforecontext"></a>
A JSON string of properties of the resource before the change:

```
{"properties": {"property1": "value"}}
```
afterContext  <a name="guard-hook-change-set-change-aftercontext"></a>
A JSON string of properties of the resource after the change:

```
{"properties": {"property1": "new value"}}
```

### Example Guard change set operation input
<a name="guard-hooks-write-rules-change-set-operations-example"></a>

The following example input shows a Guard Hook that will receive a full template, the previously deployed template, and a list of resource changes. The template in this example is using the JSON format.

```
HookContext:
  AwsAccountId: "00000000"
  StackId: MyStack
  HookTypeName: org::templatechecker::hook
  HookTypeVersion: "00001"
  InvocationPoint: UPDATE_PRE_PROVISION
  TargetName: my-example-stack
  TargetType:STACK
  TargetLogicalId: arn...:changeSet/change-set
  ChangeSetId: ""
Resources: {
    "S3Bucket": {
       "Type": "AWS::S3::Bucket",
       "Properties": {
           "BucketName": "{{amzn-s3-demo-bucket}}",
           "VersioningConfiguration":{
              "Status": "Enabled"
            }
         }
    }
Previous: {
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "S3Bucket": {
            "Type": "AWS::S3::Bucket",
            "Properties": {
                "BucketName": "{{amzn-s3-demo-bucket}}",
                "VersioningConfiguration":{
                  "Status": "Suspended"
                }
            }
        }
    }
}
Changes: [
  {
    "logicalResourceId": "S3Bucket",
    "resourceType": "AWS::S3::Bucket",
    "action": "UPDATE",
    "lineNumber": 5,
    "beforeContext": "{\"Properties\":{\"VersioningConfiguration\":{\"Status\":\"Suspended\"}}}",
    "afterContext": "{\"Properties\":{\"VersioningConfiguration\":{\"Status\":\"Enabled\"}}}"
  }
]
```

### Guard rule for change set operations
<a name="guard-hooks-rules-change-set-operations"></a>

The following example is a Guard rule that evaluates changes to Amazon S3 buckets, and ensures that `VersionConfiguration` is not disabled.

```
let s3_buckets_changing = Changes[resourceType == 'AWS::S3::Bucket']

rule S3_VERSIONING_STAY_ENABLED when %s3_buckets_changing !empty {
    let afterContext = json_parse(%s3_buckets_changing.afterContext)
    when %afterContext.Properties.VersioningConfiguration.Status !empty {
        %afterContext.Properties.VersioningConfiguration.Status == 'Enabled'
    }
}
```
