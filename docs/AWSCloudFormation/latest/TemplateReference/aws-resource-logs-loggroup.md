---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-logs-loggroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::LogGroup
<a name="aws-resource-logs-loggroup"></a>

The `AWS::Logs::LogGroup` resource specifies a log group. A log group defines common properties for log streams, such as their retention and access control rules. Each log stream must belong to one log group.

You can create up to 1,000,000 log groups per Region per account. You must use the following guidelines when naming a log group:
+ Log group names must be unique within a Region for an AWS account.
+ Log group names can be between 1 and 512 characters long.
+ Log group names consist of the following characters: a-z, A-Z, 0-9, '\_' (underscore), '-' (hyphen), '/' (forward slash), and '.' (period).

## Syntax
<a name="aws-resource-logs-loggroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-logs-loggroup-syntax.json"></a>

```
{
  "Type" : "AWS::Logs::LogGroup",
  "Properties" : {
      "[BearerTokenAuthenticationEnabled](#cfn-logs-loggroup-bearertokenauthenticationenabled)" : {{Boolean}},
      "[DataProtectionPolicy](#cfn-logs-loggroup-dataprotectionpolicy)" : {{Json}},
      "[DeletionProtectionEnabled](#cfn-logs-loggroup-deletionprotectionenabled)" : {{Boolean}},
      "[FieldIndexPolicies](#cfn-logs-loggroup-fieldindexpolicies)" : {{[ {{{Key}}: {{Value}}, ...}, ... ]}},
      "[KmsKeyId](#cfn-logs-loggroup-kmskeyid)" : {{String}},
      "[LogGroupClass](#cfn-logs-loggroup-loggroupclass)" : {{String}},
      "[LogGroupName](#cfn-logs-loggroup-loggroupname)" : {{String}},
      "[ResourcePolicyDocument](#cfn-logs-loggroup-resourcepolicydocument)" : {{Json}},
      "[RetentionInDays](#cfn-logs-loggroup-retentionindays)" : {{Integer}},
      "[Tags](#cfn-logs-loggroup-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-logs-loggroup-syntax.yaml"></a>

```
Type: AWS::Logs::LogGroup
Properties:
  [BearerTokenAuthenticationEnabled](#cfn-logs-loggroup-bearertokenauthenticationenabled): {{Boolean}}
  [DataProtectionPolicy](#cfn-logs-loggroup-dataprotectionpolicy): {{Json}}
  [DeletionProtectionEnabled](#cfn-logs-loggroup-deletionprotectionenabled): {{Boolean}}
  [FieldIndexPolicies](#cfn-logs-loggroup-fieldindexpolicies): {{
    -
    {{Key}}: {{Value}}}}
  [KmsKeyId](#cfn-logs-loggroup-kmskeyid): {{String}}
  [LogGroupClass](#cfn-logs-loggroup-loggroupclass): {{String}}
  [LogGroupName](#cfn-logs-loggroup-loggroupname): {{String}}
  [ResourcePolicyDocument](#cfn-logs-loggroup-resourcepolicydocument): {{Json}}
  [RetentionInDays](#cfn-logs-loggroup-retentionindays): {{Integer}}
  [Tags](#cfn-logs-loggroup-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-logs-loggroup-properties"></a>

`BearerTokenAuthenticationEnabled`  <a name="cfn-logs-loggroup-bearertokenauthenticationenabled"></a>
Indicates whether bearer token authentication is enabled for this log group. When enabled, bearer token authentication is allowed on operations until it is explicitly disabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataProtectionPolicy`  <a name="cfn-logs-loggroup-dataprotectionpolicy"></a>
Creates a data protection policy and assigns it to the log group. A data protection policy can help safeguard sensitive data that's ingested by the log group by auditing and masking the sensitive log data. When a user who does not have permission to view masked data views a log event that includes masked data, the sensitive data is replaced by asterisks.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeletionProtectionEnabled`  <a name="cfn-logs-loggroup-deletionprotectionenabled"></a>
Indicates whether deletion protection is enabled for this log group. When enabled, deletion protection blocks all deletion operations until it is explicitly disabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldIndexPolicies`  <a name="cfn-logs-loggroup-fieldindexpolicies"></a>
Creates or updates a *field index policy* for the specified log group. Only log groups in the Standard log class support field index policies. For more information about log classes, see [Log classes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html).
You can use field index policies to create *field indexes* on fields found in log events in the log group. Creating field indexes lowers the costs for CloudWatch Logs Insights queries that reference those field indexes, because these queries attempt to skip the processing of log events that are known to not match the indexed field. Good fields to index are fields that you often need to query for and fields that have high cardinality of values Common examples of indexes include request ID, session ID, userID, and instance IDs. For more information, see [Create field indexes to improve query performance and reduce costs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing.html).
Currently, this array supports only one field index policy object.
*Required*: No
*Type*: Array of Object
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyId`  <a name="cfn-logs-loggroup-kmskeyid"></a>
The Amazon Resource Name (ARN) of the AWS KMS key to use when encrypting log data.
To associate an AWS KMS key with the log group, specify the ARN of that KMS key here. If you do so, ingested data is encrypted using this key. This association is stored as long as the data encrypted with the KMS key is still within CloudWatch Logs. This enables CloudWatch Logs to decrypt this data whenever it is requested.
If you attempt to associate a KMS key with the log group but the KMS key doesn't exist or is deactivated, you will receive an `InvalidParameterException` error.
Log group data is always encrypted in CloudWatch Logs. If you omit this key, the encryption does not use AWS KMS. For more information, see [ Encrypt log data in CloudWatch Logs using AWS Key Management Service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html)
*Required*: No
*Type*: String
*Pattern*: `^arn:[a-z0-9-]+:kms:[a-z0-9-]+:\d{12}:(key|alias)/.+\Z`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogGroupClass`  <a name="cfn-logs-loggroup-loggroupclass"></a>
Specifies the log group class for this log group. There are two classes:
+ The `Standard` log class supports all CloudWatch Logs features.
+ The `Infrequent Access` log class supports a subset of CloudWatch Logs features and incurs lower costs.
For details about the features supported by each class, see [Log classes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html)
*Required*: No
*Type*: String
*Allowed values*: `STANDARD | INFREQUENT_ACCESS | DELIVERY`
*Update requires*: Updates are not supported.

`LogGroupName`  <a name="cfn-logs-loggroup-loggroupname"></a>
The name of the log group. If you don't specify a name, AWS CloudFormation generates a unique ID for the log group.
*Required*: No
*Type*: String
*Pattern*: `^[.\-_/#A-Za-z0-9]{1,512}\Z`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourcePolicyDocument`  <a name="cfn-logs-loggroup-resourcepolicydocument"></a>
Creates or updates a resource policy for the specified log group that allows other services to put log events to this account. A LogGroup can have 1 resource policy.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RetentionInDays`  <a name="cfn-logs-loggroup-retentionindays"></a>
The number of days to retain the log events in the specified log group. Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1096, 1827, 2192, 2557, 2922, 3288, and 3653.
To set a log group so that its log events do not expire, do not specify this property.
*Required*: No
*Type*: Integer
*Allowed values*: `1 | 3 | 5 | 7 | 14 | 30 | 60 | 90 | 120 | 150 | 180 | 365 | 400 | 545 | 731 | 1096 | 1827 | 2192 | 2557 | 2922 | 3288 | 3653`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-logs-loggroup-tags"></a>
An array of key-value pairs to apply to the log group.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-logs-loggroup-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-logs-loggroup-return-values"></a>

### Ref
<a name="aws-resource-logs-loggroup-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-logs-loggroup-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-logs-loggroup-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the log group, such as `arn:aws:logs:us-west-1:123456789012:log-group:/mystack-testgroup-12ABC1AB12A1:*`

## Examples
<a name="aws-resource-logs-loggroup--examples"></a>

**Topics**
+ [Create a log group](#aws-resource-logs-loggroup--examples--Create_a_log_group)
+ [Create a log group with a data protection policy](#aws-resource-logs-loggroup--examples--Create_a_log_group_with_a_data_protection_policy)
+ [Create a log group with a field index policy](#aws-resource-logs-loggroup--examples--Create_a_log_group_with_a_field_index_policy)

### Create a log group
<a name="aws-resource-logs-loggroup--examples--Create_a_log_group"></a>

The following example creates a log group that retains events for seven days.

#### JSON
<a name="aws-resource-logs-loggroup--examples--Create_a_log_group--json"></a>

```
"myLogGroup": {
    "Type": "AWS::Logs::LogGroup",
    "Properties": {
        "RetentionInDays": 7
    }
}
```

#### YAML
<a name="aws-resource-logs-loggroup--examples--Create_a_log_group--yaml"></a>

```
myLogGroup:
  Type: AWS::Logs::LogGroup
  Properties:
    RetentionInDays: 7
```

### Create a log group with a data protection policy
<a name="aws-resource-logs-loggroup--examples--Create_a_log_group_with_a_data_protection_policy"></a>

The following example creates a log group that uses a data protection policy to mask email addresses, and send audit findings to CloudWatch Logs, Firehose, and Amazon S3.

#### JSON
<a name="aws-resource-logs-loggroup--examples--Create_a_log_group_with_a_data_protection_policy--json"></a>

```
"TestLogGroupDescription": {
  "Type": "AWS::Logs::LogGroup",
  "Properties": {
      "LogGroupName": "my-log-group",
      "DataProtectionPolicy": {
          "Name": "data-protection-policy",
          "Description": "test description",
          "Version": "2021-06-01",
          "Statement": [{
                  "Sid": "audit-policy test",
                  "DataIdentifier": [
                      "arn:aws:dataprotection::aws:data-identifier/EmailAddress",
                      "arn:aws:dataprotection::aws:data-identifier/DriversLicense-US"
                  ],
                  "Operation": {
                      "Audit": {
                          "FindingsDestination": {
                              "CloudWatchLogs": {
                                  "LogGroup": "EXISTING_LOG_GROUP_IN_YOUR_ACCOUNT"
                              },
                              "Firehose": {
                                  "DeliveryStream": "EXISTING_STREAM_IN_YOUR_ACCOUNT"
                              },
                              "S3": {
                                  "Bucket": "EXISTING_BUCKET"
                              }
                          }
                      }
                  }
              },
              {
                  "Sid": "redact-policy",
                  "DataIdentifier": [
                      "arn:aws:dataprotection::aws:data-identifier/EmailAddress",
                      "arn:aws:dataprotection::aws:data-identifier/DriversLicense-US"
                  ],
                  "Operation": {
                      "Deidentify": {
                          "MaskConfig": {}
                      }
                  }
              }
          ]
      }
  }
}
```

#### YAML
<a name="aws-resource-logs-loggroup--examples--Create_a_log_group_with_a_data_protection_policy--yaml"></a>

```
TestLogGroupDescription:
  Type: AWS::Logs::LogGroup
  Properties:
    LogGroupName: my-log-group
    DataProtectionPolicy:
      Name: data-protection-policy
      Description: test description
      Version: '2021-06-01'
      Statement:
      - Sid: audit-policy test
        DataIdentifier:
        - arn:aws:dataprotection::aws:data-identifier/EmailAddress
        - arn:aws:dataprotection::aws:data-identifier/DriversLicense-US
        Operation:
          Audit:
            FindingsDestination:
              CloudWatchLogs:
                LogGroup: EXISTING_LOG_GROUP_IN_YOUR_ACCOUNT
              Firehose:
                DeliveryStream: EXISTING_STREAM_IN_YOUR_ACCOUNT
              S3:
                Bucket: EXISTING_BUCKET
      - Sid: redact-policy
        DataIdentifier:
        - arn:aws:dataprotection::aws:data-identifier/EmailAddress
        - arn:aws:dataprotection::aws:data-identifier/DriversLicense-US
        Operation:
          Deidentify:
            MaskConfig: {}
```

### Create a log group with a field index policy
<a name="aws-resource-logs-loggroup--examples--Create_a_log_group_with_a_field_index_policy"></a>

The following example creates a log group that uses a field index policy to index the `RequestId` and `TransactionId` fields in log events.

#### JSON
<a name="aws-resource-logs-loggroup--examples--Create_a_log_group_with_a_field_index_policy--json"></a>

```
"TestFieldIndexingLogGroup": {
    "Type": "AWS::Logs::LogGroup",
    "Properties": {
        "LogGroupName": "my-log-group",
        "FieldIndexPolicies": [{
            "Fields": [
                "RequestId",
                "TransactionId"
            ]
        }]
    }
}
```

#### YAML
<a name="aws-resource-logs-loggroup--examples--Create_a_log_group_with_a_field_index_policy--yaml"></a>

```
TestFieldIndexingLogGroup:
  Type: AWS::Logs::LogGroup
  Properties:
    LogGroupName: my-log-group
    FieldIndexPolicies:
        - Fields:
            - RequestId
            - TransactionId
```
