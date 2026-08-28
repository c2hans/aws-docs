---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-sqlhastandbydetectedinstance.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::SqlHaStandbyDetectedInstance
<a name="aws-resource-ec2-sqlhastandbydetectedinstance"></a>

Specifies an Amazon EC2 instance for SQL Server High Availability standby detection monitoring. Once enabled, AWS monitors the metadata for the instance to determine whether it is an active or standby node in a SQL Server High Availability cluster. If the instance is determined to be a standby failover node, AWS automatically applies SQL Server licensing fee waiver for this instance.

To register an instance, it must be running a Windows SQL Server license-included AMI and have the AWS Systems Manager agent installed and running. Only Windows Server 2019 and later and SQL Server (Standard and Enterprise editions) 2017 and later are supported. For more information, see [ Prerequisites for using SQL Server High Availability instance standby detection](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/prerequisites-and-requirements.html).

## Syntax
<a name="aws-resource-ec2-sqlhastandbydetectedinstance-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-sqlhastandbydetectedinstance-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::SqlHaStandbyDetectedInstance",
  "Properties" : {
      "[InstanceId](#cfn-ec2-sqlhastandbydetectedinstance-instanceid)" : {{String}},
      "[SqlServerCredentials](#cfn-ec2-sqlhastandbydetectedinstance-sqlservercredentials)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-sqlhastandbydetectedinstance-syntax.yaml"></a>

```
Type: AWS::EC2::SqlHaStandbyDetectedInstance
Properties:
  [InstanceId](#cfn-ec2-sqlhastandbydetectedinstance-instanceid): {{String}}
  [SqlServerCredentials](#cfn-ec2-sqlhastandbydetectedinstance-sqlservercredentials): {{String}}
```

## Properties
<a name="aws-resource-ec2-sqlhastandbydetectedinstance-properties"></a>

`InstanceId`  <a name="cfn-ec2-sqlhastandbydetectedinstance-instanceid"></a>
The ID of the SQL Server High Availability instance.
*Required*: Yes
*Type*: String
*Pattern*: `^i-[0-9a-f]{8,17}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SqlServerCredentials`  <a name="cfn-ec2-sqlhastandbydetectedinstance-sqlservercredentials"></a>
The ARN of the AWS Secrets Manager secret containing the SQL Server access credentials for the SQL Server High Availability instance. If not specified, deafult local user credentials will be used by the AWS Systems Manager agent.
*Required*: No
*Type*: String
*Pattern*: `^(?=.{20,2048}$)arn:aws[a-z-]*:secretsmanager:[a-z0-9-]+:\d{12}:secret:[a-zA-Z0-9/_+=.@-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-sqlhastandbydetectedinstance-return-values"></a>

### Ref
<a name="aws-resource-ec2-sqlhastandbydetectedinstance-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the SQL Server High Availability instance.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-sqlhastandbydetectedinstance-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-sqlhastandbydetectedinstance-return-values-fn--getatt-fn--getatt"></a>

`HaStatus`  <a name="HaStatus-fn::getatt"></a>
The SQL Server High Availability status of the instance. Valid values are:
+ `processing` - The SQL Server High Availability status for the SQL Server High Availability instance is being updated.
+ `active` - The SQL Server High Availability instance is an active node in an SQL Server High Availability cluster.
+ `standby` - The SQL Server High Availability instance is a standby failover node in an SQL Server High Availability cluster.
+ `invalid` - An error occurred due to misconfigured permissions, or unable to dertemine SQL Server High Availability status for the SQL Server High Availability instance.

`LastUpdatedTime`  <a name="LastUpdatedTime-fn::getatt"></a>
The date and time when the instance's SQL Server High Availability status was last updated, in the ISO 8601 format in the UTC time zone (`YYYY-MM-DDThh:mm:ss.sssZ`).

`SqlServerLicenseUsage`  <a name="SqlServerLicenseUsage-fn::getatt"></a>
The license type for the SQL Server license. Valid values include:
+ `full` - The SQL Server High Availability instance is using a full SQL Server license.
+ `waived` - The SQL Server High Availability instance is waived from the SQL Server license.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
