---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_RestoreRequest.html
---

# RestoreRequest
<a name="API_RestoreRequest"></a>

Container for restore job parameters.

## Contents
<a name="API_RestoreRequest_Contents"></a>

 ** Days **   <a name="AmazonS3-Type-RestoreRequest-Days"></a>
Lifetime of the active copy in days. Do not use with restores that specify `OutputLocation`.
The Days element is required for regular restores, and must not be provided for select requests.
Type: Integer
Required: No

 ** Description **   <a name="AmazonS3-Type-RestoreRequest-Description"></a>
The optional description for the job.
Type: String
Required: No

 ** GlacierJobParameters **   <a name="AmazonS3-Type-RestoreRequest-GlacierJobParameters"></a>
S3 Glacier related parameters pertaining to this job. Do not use with restores that specify `OutputLocation`.
Type: [GlacierJobParameters](API_GlacierJobParameters.md) data type
Required: No

 ** OutputLocation **   <a name="AmazonS3-Type-RestoreRequest-OutputLocation"></a>
Describes the location where the restore job's output is stored.
Type: [OutputLocation](API_OutputLocation.md) data type
Required: No

 ** SelectParameters **   <a name="AmazonS3-Type-RestoreRequest-SelectParameters"></a>
Amazon S3 Select is no longer available to new customers. Existing customers of Amazon S3 Select can continue to use the feature as usual. [Learn more](http://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/)
Describes the parameters for Select job types.
Type: [SelectParameters](API_SelectParameters.md) data type
Required: No

 ** Tier **   <a name="AmazonS3-Type-RestoreRequest-Tier"></a>
Retrieval tier at which the restore will be processed.
Type: String
Valid Values: `Standard | Bulk | Expedited`
Required: No

 ** Type **   <a name="AmazonS3-Type-RestoreRequest-Type"></a>
Amazon S3 Select is no longer available to new customers. Existing customers of Amazon S3 Select can continue to use the feature as usual. [Learn more](http://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/)
Type of restore request.
Type: String
Valid Values: `SELECT`
Required: No

## See Also
<a name="API_RestoreRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/RestoreRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/RestoreRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/RestoreRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
