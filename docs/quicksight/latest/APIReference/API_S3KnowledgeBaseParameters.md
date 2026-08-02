---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_S3KnowledgeBaseParameters.html
---

# S3KnowledgeBaseParameters
<a name="API_S3KnowledgeBaseParameters"></a>

The parameters that are required to connect to a S3 Knowledge Base data source.

## Contents
<a name="API_S3KnowledgeBaseParameters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BucketUrl **   <a name="QS-Type-S3KnowledgeBaseParameters-BucketUrl"></a>
The URL of the S3 bucket that contains the knowledge base data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** MetadataFilesLocation **   <a name="QS-Type-S3KnowledgeBaseParameters-MetadataFilesLocation"></a>
The location of metadata files within the S3 bucket that describe the structure and content of the knowledge base.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** RoleArn **   <a name="QS-Type-S3KnowledgeBaseParameters-RoleArn"></a>
Use the `RoleArn` structure to override an account-wide role for a specific S3 Knowledge Base data source. For example, say an account administrator has turned off all S3 access with an account-wide role. The administrator can then use `RoleArn` to bypass the account-wide role and allow S3 access for the single S3 Knowledge Base data source that is specified in the structure, even if the account-wide role forbidding S3 access is still active.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

## See Also
<a name="API_S3KnowledgeBaseParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/S3KnowledgeBaseParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/S3KnowledgeBaseParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/S3KnowledgeBaseParameters)
