---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-redshift-cluster-loggingproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Redshift::Cluster LoggingProperties
<a name="aws-properties-redshift-cluster-loggingproperties"></a>

Specifies logging information, such as queries and connection attempts, for the specified Amazon Redshift cluster.

## Syntax
<a name="aws-properties-redshift-cluster-loggingproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-redshift-cluster-loggingproperties-syntax.json"></a>

```
{
  "[BucketName](#cfn-redshift-cluster-loggingproperties-bucketname)" : {{String}},
  "[LogDestinationType](#cfn-redshift-cluster-loggingproperties-logdestinationtype)" : {{String}},
  "[LogExports](#cfn-redshift-cluster-loggingproperties-logexports)" : {{[ String, ... ]}},
  "[S3KeyPrefix](#cfn-redshift-cluster-loggingproperties-s3keyprefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-redshift-cluster-loggingproperties-syntax.yaml"></a>

```
  [BucketName](#cfn-redshift-cluster-loggingproperties-bucketname): {{String}}
  [LogDestinationType](#cfn-redshift-cluster-loggingproperties-logdestinationtype): {{String}}
  [LogExports](#cfn-redshift-cluster-loggingproperties-logexports): {{
    - String}}
  [S3KeyPrefix](#cfn-redshift-cluster-loggingproperties-s3keyprefix): {{String}}
```

## Properties
<a name="aws-properties-redshift-cluster-loggingproperties-properties"></a>

`BucketName`  <a name="cfn-redshift-cluster-loggingproperties-bucketname"></a>
The name of an existing S3 bucket where the log files are to be stored.
Constraints:
+ Must be in the same region as the cluster
+ The cluster must have read bucket and put object permissions
*Required*: No
*Type*: String
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogDestinationType`  <a name="cfn-redshift-cluster-loggingproperties-logdestinationtype"></a>
The log destination type. An enum with possible values of `s3` and `cloudwatch`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogExports`  <a name="cfn-redshift-cluster-loggingproperties-logexports"></a>
The collection of exported log types. Possible values are `connectionlog`, `useractivitylog`, and `userlog`.
*Required*: No
*Type*: Array of String
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3KeyPrefix`  <a name="cfn-redshift-cluster-loggingproperties-s3keyprefix"></a>
The prefix applied to the log file names.
Valid characters are any letter from any language, any whitespace character, any numeric character, and the following characters: underscore (`_`), period (`.`), colon (`:`), slash (`/`), equal (`=`), plus (`+`), backslash (`\`), hyphen (`-`), at symbol (`@`).
*Required*: No
*Type*: String
*Pattern*: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
