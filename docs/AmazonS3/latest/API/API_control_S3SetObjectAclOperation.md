---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3SetObjectAclOperation.html
---

# S3SetObjectAclOperation
<a name="API_control_S3SetObjectAclOperation"></a>

Contains the configuration parameters for a PUT Object ACL operation. S3 Batch Operations passes every object to the underlying `PutObjectAcl` API operation. For more information about the parameters for this operation, see [PutObjectAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectPUTacl.html).

## Contents
<a name="API_control_S3SetObjectAclOperation_Contents"></a>

 ** AccessControlPolicy **   <a name="AmazonS3-Type-control_S3SetObjectAclOperation-AccessControlPolicy"></a>

Type: [S3AccessControlPolicy](API_control_S3AccessControlPolicy.md) data type
Required: No

## See Also
<a name="API_control_S3SetObjectAclOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/S3SetObjectAclOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/S3SetObjectAclOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/S3SetObjectAclOperation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
