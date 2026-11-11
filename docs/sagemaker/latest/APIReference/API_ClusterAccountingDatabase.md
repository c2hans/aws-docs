---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterAccountingDatabase.html
---

# ClusterAccountingDatabase
<a name="API_ClusterAccountingDatabase"></a>

The external MySQL-compatible database that the Slurm accounting daemon (`slurmdbd`) connects to for a SageMaker HyperPod cluster. You provide the database credentials in an AWS Secrets Manager secret instead of in the request.

## Contents
<a name="API_ClusterAccountingDatabase_Contents"></a>

 ** Endpoint **   <a name="sagemaker-Type-ClusterAccountingDatabase-Endpoint"></a>
The hostname or endpoint of the accounting database, such as the endpoint of an Amazon RDS for MySQL or Aurora MySQL database. The database must be reachable from the subnets and security groups that you configure for the cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(?=.{1,255}$)([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)(\.[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)*`
Required: Yes

 ** SecretArn **   <a name="sagemaker-Type-ClusterAccountingDatabase-SecretArn"></a>
The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that contains the user name and password for the accounting database. The database user must be able to create the schema and to read from and write to it.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:secretsmanager:[a-z0-9\-]*:[0-9]{12}:secret:.+`
Required: Yes

 ** Name **   <a name="sagemaker-Type-ClusterAccountingDatabase-Name"></a>
The name of the database schema that stores the Slurm accounting data. The default is `slurm_acct_db_` followed by the cluster ID from the cluster ARN, for example `slurm_acct_db_a1b2c3d4e5f6`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9$_]+`
Required: No

 ** Port **   <a name="sagemaker-Type-ClusterAccountingDatabase-Port"></a>
The port that the accounting database listens on. The default is `3306`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

## See Also
<a name="API_ClusterAccountingDatabase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterAccountingDatabase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterAccountingDatabase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterAccountingDatabase)
