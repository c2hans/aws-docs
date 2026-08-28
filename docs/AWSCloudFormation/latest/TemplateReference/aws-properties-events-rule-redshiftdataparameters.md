---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-events-rule-redshiftdataparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Events::Rule RedshiftDataParameters
<a name="aws-properties-events-rule-redshiftdataparameters"></a>

These are custom parameters to be used when the target is a Amazon Redshift cluster to invoke the Amazon Redshift Data API ExecuteStatement based on EventBridge events.

## Syntax
<a name="aws-properties-events-rule-redshiftdataparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-events-rule-redshiftdataparameters-syntax.json"></a>

```
{
  "[Database](#cfn-events-rule-redshiftdataparameters-database)" : {{String}},
  "[DbUser](#cfn-events-rule-redshiftdataparameters-dbuser)" : {{String}},
  "[SecretManagerArn](#cfn-events-rule-redshiftdataparameters-secretmanagerarn)" : {{String}},
  "[Sql](#cfn-events-rule-redshiftdataparameters-sql)" : {{String}},
  "[Sqls](#cfn-events-rule-redshiftdataparameters-sqls)" : {{[ String, ... ]}},
  "[StatementName](#cfn-events-rule-redshiftdataparameters-statementname)" : {{String}},
  "[WithEvent](#cfn-events-rule-redshiftdataparameters-withevent)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-events-rule-redshiftdataparameters-syntax.yaml"></a>

```
  [Database](#cfn-events-rule-redshiftdataparameters-database): {{String}}
  [DbUser](#cfn-events-rule-redshiftdataparameters-dbuser): {{String}}
  [SecretManagerArn](#cfn-events-rule-redshiftdataparameters-secretmanagerarn): {{String}}
  [Sql](#cfn-events-rule-redshiftdataparameters-sql): {{String}}
  [Sqls](#cfn-events-rule-redshiftdataparameters-sqls): {{
    - String}}
  [StatementName](#cfn-events-rule-redshiftdataparameters-statementname): {{String}}
  [WithEvent](#cfn-events-rule-redshiftdataparameters-withevent): {{Boolean}}
```

## Properties
<a name="aws-properties-events-rule-redshiftdataparameters-properties"></a>

`Database`  <a name="cfn-events-rule-redshiftdataparameters-database"></a>
The name of the database. Required when authenticating using temporary credentials.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DbUser`  <a name="cfn-events-rule-redshiftdataparameters-dbuser"></a>
The database user name. Required when authenticating using temporary credentials.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretManagerArn`  <a name="cfn-events-rule-redshiftdataparameters-secretmanagerarn"></a>
The name or ARN of the secret that enables access to the database. Required when authenticating using AWS Secrets Manager.
*Required*: No
*Type*: String
*Pattern*: `(^arn:aws([a-z]|\-)*:secretsmanager:[a-z0-9-.]+:.*)|(\$(\.[\w_-]+(\[(\d+|\*)\])*)*)`
*Minimum*: `1`
*Maximum*: `1600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Sql`  <a name="cfn-events-rule-redshiftdataparameters-sql"></a>
The SQL statement text to run.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `100000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Sqls`  <a name="cfn-events-rule-redshiftdataparameters-sqls"></a>
One or more SQL statements to run. The SQL statements are run as a single transaction. They run serially in the order of the array. Subsequent SQL statements don't start until the previous statement in the array completes. If any SQL statement fails, then because they are run as one transaction, all work is rolled back.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `40`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatementName`  <a name="cfn-events-rule-redshiftdataparameters-statementname"></a>
The name of the SQL statement. You can name the SQL statement when you create it to identify the query.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WithEvent`  <a name="cfn-events-rule-redshiftdataparameters-withevent"></a>
Indicates whether to send an event back to EventBridge after the SQL statement runs.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
