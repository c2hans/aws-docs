---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rds-dbinstance-endpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RDS::DBInstance Endpoint
<a name="aws-properties-rds-dbinstance-endpoint"></a>

This data type represents the information you need to connect to an Amazon RDS DB instance. This data type is used as a response element in the following actions:
+  `CreateDBInstance`
+  `DescribeDBInstances`
+  `DeleteDBInstance`

For the data structure that represents Amazon Aurora DB cluster endpoints, see `DBClusterEndpoint`.

## Syntax
<a name="aws-properties-rds-dbinstance-endpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rds-dbinstance-endpoint-syntax.json"></a>

```
{
  "[Address](#cfn-rds-dbinstance-endpoint-address)" : {{String}},
  "[HostedZoneId](#cfn-rds-dbinstance-endpoint-hostedzoneid)" : {{String}},
  "[Port](#cfn-rds-dbinstance-endpoint-port)" : {{String}}
}
```

### YAML
<a name="aws-properties-rds-dbinstance-endpoint-syntax.yaml"></a>

```
  [Address](#cfn-rds-dbinstance-endpoint-address): {{String}}
  [HostedZoneId](#cfn-rds-dbinstance-endpoint-hostedzoneid): {{String}}
  [Port](#cfn-rds-dbinstance-endpoint-port): {{String}}
```

## Properties
<a name="aws-properties-rds-dbinstance-endpoint-properties"></a>

`Address`  <a name="cfn-rds-dbinstance-endpoint-address"></a>
Specifies the DNS address of the DB instance.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HostedZoneId`  <a name="cfn-rds-dbinstance-endpoint-hostedzoneid"></a>
Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-rds-dbinstance-endpoint-port"></a>
Specifies the port that the database engine is listening on.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
