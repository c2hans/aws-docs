---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rds-dbinstance-certificatedetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RDS::DBInstance CertificateDetails
<a name="aws-properties-rds-dbinstance-certificatedetails"></a>

The details of the DB instance’s server certificate.

For more information, see [Using SSL/TLS to encrypt a connection to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html) in the *Amazon RDS User Guide* and [ Using SSL/TLS to encrypt a connection to a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html) in the *Amazon Aurora User Guide*.

## Syntax
<a name="aws-properties-rds-dbinstance-certificatedetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rds-dbinstance-certificatedetails-syntax.json"></a>

```
{
  "[CAIdentifier](#cfn-rds-dbinstance-certificatedetails-caidentifier)" : {{String}},
  "[ValidTill](#cfn-rds-dbinstance-certificatedetails-validtill)" : {{String}}
}
```

### YAML
<a name="aws-properties-rds-dbinstance-certificatedetails-syntax.yaml"></a>

```
  [CAIdentifier](#cfn-rds-dbinstance-certificatedetails-caidentifier): {{String}}
  [ValidTill](#cfn-rds-dbinstance-certificatedetails-validtill): {{String}}
```

## Properties
<a name="aws-properties-rds-dbinstance-certificatedetails-properties"></a>

`CAIdentifier`  <a name="cfn-rds-dbinstance-certificatedetails-caidentifier"></a>
The CA identifier of the CA certificate used for the DB instance's server certificate.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValidTill`  <a name="cfn-rds-dbinstance-certificatedetails-validtill"></a>
The expiration date of the DB instance’s server certificate.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
