---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ReadIamConnectionMetadata.html
---

# ReadIamConnectionMetadata
<a name="API_ReadIamConnectionMetadata"></a>

Read-only metadata for IAM-based connections, containing role and source ARN information.

## Contents
<a name="API_ReadIamConnectionMetadata_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** RoleArn **   <a name="QS-Type-ReadIamConnectionMetadata-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role to assume for authentication.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** SourceArn **   <a name="QS-Type-ReadIamConnectionMetadata-SourceArn"></a>
The Amazon Resource Name (ARN) of the source resource for IAM authentication.
Type: String
Required: Yes

## See Also
<a name="API_ReadIamConnectionMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ReadIamConnectionMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ReadIamConnectionMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ReadIamConnectionMetadata)
