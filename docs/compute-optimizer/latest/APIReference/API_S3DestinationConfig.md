---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_S3DestinationConfig.html
---

# S3DestinationConfig
<a name="API_S3DestinationConfig"></a>

Describes the destination Amazon Simple Storage Service (Amazon S3) bucket name and key prefix for a recommendations export job.

You must create the destination Amazon S3 bucket for your recommendations export before you create the export job. Compute Optimizer does not create the S3 bucket for you. After you create the S3 bucket, ensure that it has the required permission policy to allow Compute Optimizer to write the export file to it. If you plan to specify an object prefix when you create the export job, you must include the object prefix in the policy that you add to the S3 bucket. For more information, see [Amazon S3 Bucket Policy for Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/create-s3-bucket-policy-for-compute-optimizer.html) in the *Compute Optimizer User Guide*.

## Contents
<a name="API_S3DestinationConfig_Contents"></a>

 ** bucket **   <a name="computeoptimizer-Type-S3DestinationConfig-bucket"></a>
The name of the Amazon S3 bucket to use as the destination for an export job.
Type: String
Required: No

 ** keyPrefix **   <a name="computeoptimizer-Type-S3DestinationConfig-keyPrefix"></a>
The Amazon S3 bucket prefix for an export job.
Type: String
Required: No

## See Also
<a name="API_S3DestinationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/S3DestinationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/S3DestinationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/S3DestinationConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
