---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-ssis-etl/implement.html
---

# Implementation phase
<a name="implement"></a>

Migration that follows the big bang or phased approach requires new development and testing. The AWS Schema Conversion Tool (AWS SCT) can automatically generate AWS Glue jobs from SSIS packages. This reduces the migration time and effort significantly. Or, you can use AWS Glue Studio for graphical interface-based development, or build Spark libraries that you can run on either AWS Glue or Amazon EMR.

The following sections provide useful pointers for using AWS SCT, AWS Glue, and Amazon EMR.

## AWS SCT
<a name="sct"></a>

The following screen illustration shows an AWS Glue job script that was converted by AWS SCT.

![AWS Glue job script converted by AWS SCT](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-ssis-etl/images/guide-img/ae5b08b7-f641-4524-9650-6ac5a0f71dd9/images/ee349bd8-f30d-48ed-b169-3f89a4b77935.png)

AWS SCT can convert SSIS packages to AWS Glue jobs in bulk. You can edit the script to update existing logic or to add new logic, based on your new design. We recommend that you follow the naming conventions in the AWS SCT converted scripts to customize the scripts. For more information, see [Converting SSIS to AWS Glue using AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP-converting-aws-glue-ssis.html) in the AWS SCT documentation.

## AWS Glue
<a name="glue"></a>

AWS Glue Studio provides a graphical interface and a development experience that's similar to SSIS, as illustrated in the following screen.

![AWS Glue Studio UI](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-ssis-etl/images/guide-img/ae5b08b7-f641-4524-9650-6ac5a0f71dd9/images/c8a26ced-2605-443e-a528-42f458fc01f8.png)

If you prefer not to use a graphical interface, you can also run your custom scripts with the required Python libraries from the AWS Glue console. For more information, see [Providing your own custom scripts](https://docs.aws.amazon.com/glue/latest/dg/console-custom-created.html) in the AWS Glue documentation.

AWS Glue provides a set of built-in transforms for processing your data. These are similar to SSIS data flow transformations. Follow these best practices when you migrate your SSIS ETL jobs by using AWS Glue:
+ Prepare a mapping from AWS Glue transforms to the equivalent SSIS transformations.
+ If your transformations cannot be mapped to AWS Glue transforms, build them by using a Python or Scala custom script.
+ For custom logging (such as rows read, rows written, or bad records), use custom scripts in addition to [Amazon CloudWatch](https://docs.aws.amazon.com/glue/latest/dg/logging-and-monitoring.html).
+ Add a [development endpoint](https://docs.aws.amazon.com/glue/latest/dg/add-dev-endpoint.html) to develop and debug custom scripts locally.

## Amazon EMR
<a name="emr"></a>

You can run custom scripts (written in Python or Scala) or compiled Python libraries in Amazon EMR clusters, as with AWS Glue. Follow these best practices:
+ Start with memory optimized instance types while creating Amazon EMR clusters with the Spark framework. (SSIS uses memory buffers.)
+ Build generic Python methods that are equivalent to each SSIS task or transformation. For example, in the following illustration, a method that takes two dataframes as input produces a third dataframe that has matching records from the two dataframes as output. This works as a [merge join](https://learn.microsoft.com/en-us/sql/integration-services/data-flow/transformations/merge-join-transformation) transformation.

![Sample Python merge function for SSIS tasks](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-ssis-etl/images/guide-img/ae5b08b7-f641-4524-9650-6ac5a0f71dd9/images/33366daf-7f94-49e4-8a77-1776665f385d.png)

## Testing
<a name="test"></a>

A testing framework is required to validate the completeness and correctness of data. This framework should cover all the existing scenarios and any improvements you made while migrating your jobs to AWS.
+ Completeness validation:
  + All jobs are migrated to their target state.
  + All functionality is migrated in each job.
  + All types of logs are available, including job execution details, error messages, bad records, and row counts.
+ Correctness validation:
  + The quality of data is consistent in the existing and new environments.
  + All columns of all tables match, or tables are improved on AWS.
  + All audit and logging information match.

You should also verify that the performance of your migrated jobs matches the performance of your existing jobs.
