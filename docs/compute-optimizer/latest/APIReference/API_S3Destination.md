---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_S3Destination.html
---

# S3Destination
<a name="API_S3Destination"></a>

Describes the destination Amazon Simple Storage Service (Amazon S3) bucket name and object keys of a recommendations export file, and its associated metadata file.

## Contents
<a name="API_S3Destination_Contents"></a>

 ** bucket **   <a name="computeoptimizer-Type-S3Destination-bucket"></a>
The name of the Amazon S3 bucket used as the destination of an export file.
Type: String
Required: No

 ** key **   <a name="computeoptimizer-Type-S3Destination-key"></a>
The Amazon S3 bucket key of an export file.
The key uniquely identifies the object, or export file, in the S3 bucket.
Type: String
Required: No

 ** metadataKey **   <a name="computeoptimizer-Type-S3Destination-metadataKey"></a>
The Amazon S3 bucket key of a metadata file.
The key uniquely identifies the object, or metadata file, in the S3 bucket.
Type: String
Required: No

## See Also
<a name="API_S3Destination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/S3Destination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/S3Destination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/S3Destination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
