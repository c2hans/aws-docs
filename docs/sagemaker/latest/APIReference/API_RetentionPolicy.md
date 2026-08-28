---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_RetentionPolicy.html
---

# RetentionPolicy
<a name="API_RetentionPolicy"></a>

The retention policy for data stored on an Amazon Elastic File System volume.

## Contents
<a name="API_RetentionPolicy_Contents"></a>

 ** HomeEfsFileSystem **   <a name="sagemaker-Type-RetentionPolicy-HomeEfsFileSystem"></a>
The default is `Retain`, which specifies to keep the data stored on the Amazon EFS volume.
Specify `Delete` to delete the data stored on the Amazon EFS volume.
Type: String
Valid Values: `Retain | Delete`
Required: No

## See Also
<a name="API_RetentionPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/RetentionPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/RetentionPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/RetentionPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
