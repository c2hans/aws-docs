---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-cluster-clusteraccountingdatabase.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Cluster ClusterAccountingDatabase
<a name="aws-properties-sagemaker-cluster-clusteraccountingdatabase"></a>

The external MySQL-compatible database that the Slurm accounting daemon (`slurmdbd`) connects to for a SageMaker HyperPod cluster. You provide the database credentials in an AWS Secrets Manager secret instead of in the request.

## Syntax
<a name="aws-properties-sagemaker-cluster-clusteraccountingdatabase-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-cluster-clusteraccountingdatabase-syntax.json"></a>

```
{
  "[Endpoint](#cfn-sagemaker-cluster-clusteraccountingdatabase-endpoint)" : {{String}},
  "[Name](#cfn-sagemaker-cluster-clusteraccountingdatabase-name)" : {{String}},
  "[Port](#cfn-sagemaker-cluster-clusteraccountingdatabase-port)" : {{Integer}},
  "[SecretArn](#cfn-sagemaker-cluster-clusteraccountingdatabase-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-cluster-clusteraccountingdatabase-syntax.yaml"></a>

```
  [Endpoint](#cfn-sagemaker-cluster-clusteraccountingdatabase-endpoint): {{String}}
  [Name](#cfn-sagemaker-cluster-clusteraccountingdatabase-name): {{String}}
  [Port](#cfn-sagemaker-cluster-clusteraccountingdatabase-port): {{Integer}}
  [SecretArn](#cfn-sagemaker-cluster-clusteraccountingdatabase-secretarn): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-cluster-clusteraccountingdatabase-properties"></a>

`Endpoint`  <a name="cfn-sagemaker-cluster-clusteraccountingdatabase-endpoint"></a>
The hostname or endpoint of the accounting database, such as the endpoint of an Amazon RDS for MySQL or Aurora MySQL database. The database must be reachable from the subnets and security groups that you configure for the cluster.
*Required*: Yes
*Type*: String
*Pattern*: `^(?=.{1,255}$)([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)(\.[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-sagemaker-cluster-clusteraccountingdatabase-name"></a>
The name of the database schema that stores the Slurm accounting data. The default is `slurm_acct_db_` followed by the cluster ID from the cluster ARN, for example `slurm_acct_db_a1b2c3d4e5f6`.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9$_]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-sagemaker-cluster-clusteraccountingdatabase-port"></a>
The port that the accounting database listens on. The default is `3306`.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretArn`  <a name="cfn-sagemaker-cluster-clusteraccountingdatabase-secretarn"></a>
The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that contains the user name and password for the accounting database. The database user must be able to create the schema and to read from and write to it.
*Required*: Yes
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
