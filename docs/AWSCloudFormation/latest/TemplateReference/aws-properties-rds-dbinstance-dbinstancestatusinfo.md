---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rds-dbinstance-dbinstancestatusinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RDS::DBInstance DBInstanceStatusInfo
<a name="aws-properties-rds-dbinstance-dbinstancestatusinfo"></a>

Provides a list of status information for a DB instance.

## Syntax
<a name="aws-properties-rds-dbinstance-dbinstancestatusinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rds-dbinstance-dbinstancestatusinfo-syntax.json"></a>

```
{
  "[Message](#cfn-rds-dbinstance-dbinstancestatusinfo-message)" : {{String}},
  "[Normal](#cfn-rds-dbinstance-dbinstancestatusinfo-normal)" : {{Boolean}},
  "[Status](#cfn-rds-dbinstance-dbinstancestatusinfo-status)" : {{String}},
  "[StatusType](#cfn-rds-dbinstance-dbinstancestatusinfo-statustype)" : {{String}}
}
```

### YAML
<a name="aws-properties-rds-dbinstance-dbinstancestatusinfo-syntax.yaml"></a>

```
  [Message](#cfn-rds-dbinstance-dbinstancestatusinfo-message): {{String}}
  [Normal](#cfn-rds-dbinstance-dbinstancestatusinfo-normal): {{Boolean}}
  [Status](#cfn-rds-dbinstance-dbinstancestatusinfo-status): {{String}}
  [StatusType](#cfn-rds-dbinstance-dbinstancestatusinfo-statustype): {{String}}
```

## Properties
<a name="aws-properties-rds-dbinstance-dbinstancestatusinfo-properties"></a>

`Message`  <a name="cfn-rds-dbinstance-dbinstancestatusinfo-message"></a>
Details of the error if there is an error for the instance. If the instance isn't in an error state, this value is blank.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Normal`  <a name="cfn-rds-dbinstance-dbinstancestatusinfo-normal"></a>
Indicates whether the instance is operating normally (TRUE) or is in an error state (FALSE).
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-rds-dbinstance-dbinstancestatusinfo-status"></a>
The status of the DB instance. For a StatusType of read replica, the values can be replicating, replication stop point set, replication stop point reached, error, stopped, or terminated.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatusType`  <a name="cfn-rds-dbinstance-dbinstancestatusinfo-statustype"></a>
This value is currently "read replication."
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
