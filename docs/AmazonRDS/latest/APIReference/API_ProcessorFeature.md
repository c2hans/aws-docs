---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ProcessorFeature.html
---

# ProcessorFeature
<a name="API_ProcessorFeature"></a>

Contains the processor features of a DB instance class.

To specify the number of CPU cores, use the `coreCount` feature name for the `Name` parameter. To specify the number of threads per core, use the `threadsPerCore` feature name for the `Name` parameter.

You can set the processor features of the DB instance class for a DB instance when you call one of the following actions:
+  `CreateDBInstance`
+  `ModifyDBInstance`
+  `RestoreDBInstanceFromDBSnapshot`
+  `RestoreDBInstanceFromS3`
+  `RestoreDBInstanceToPointInTime`

You can view the valid processor values for a particular instance class by calling the `DescribeOrderableDBInstanceOptions` action and specifying the instance class for the `DBInstanceClass` parameter.

In addition, you can use the following actions for DB instance class processor information:
+  `DescribeDBInstances`
+  `DescribeDBSnapshots`
+  `DescribeValidDBInstanceModifications`

If you call `DescribeDBInstances`, `ProcessorFeature` returns non-null values only if the following conditions are met:
+ You are accessing an Oracle or SQL Server DB instance.
+ Your Oracle or SQL Server DB instance class supports configuring the number of CPU cores and threads per core.
+ The current number CPU cores and threads is set to a non-default value.

For more information, see [ Configuring the processor for a DB instance class in RDS for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html#USER_ConfigureProcessor), [ Optimizing your RDS for SQL Server CPU](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Concepts.General.OptimizeCPU.html), and [DB instance classes](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html) in the *Amazon RDS User Guide. *

## Contents
<a name="API_ProcessorFeature_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **
The name of the processor feature. Valid names are `coreCount` and `threadsPerCore`.
Type: String
Required: No

 ** Value **
The value of a processor feature.
Type: String
Required: No

## See Also
<a name="API_ProcessorFeature_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ProcessorFeature)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ProcessorFeature)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ProcessorFeature)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
