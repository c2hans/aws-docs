---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_IdMappingWorkflowOutputSource.html
---

# IdMappingWorkflowOutputSource
<a name="API_IdMappingWorkflowOutputSource"></a>

The output source for the ID mapping workflow.

## Contents
<a name="API_IdMappingWorkflowOutputSource_Contents"></a>

 ** outputS3Path **   <a name="API-Type-IdMappingWorkflowOutputSource-outputS3Path"></a>
The S3 path to which AWS Entity Resolution will write the output table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`
Required: Yes

 ** KMSArn **   <a name="API-Type-IdMappingWorkflowOutputSource-KMSArn"></a>
Customer AWS KMS ARN for encryption at rest. If not provided, system will use an AWS Entity Resolution managed KMS key.
Type: String
Pattern: `arn:aws:kms:.*:[0-9]+:.*`
Required: No

## See Also
<a name="API_IdMappingWorkflowOutputSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/IdMappingWorkflowOutputSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/IdMappingWorkflowOutputSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/IdMappingWorkflowOutputSource)
