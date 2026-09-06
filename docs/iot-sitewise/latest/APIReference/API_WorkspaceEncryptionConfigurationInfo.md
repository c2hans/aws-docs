---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_WorkspaceEncryptionConfigurationInfo.html
---

# WorkspaceEncryptionConfigurationInfo
<a name="API_WorkspaceEncryptionConfigurationInfo"></a>

Contains the encryption configuration information for a workspace.

## Contents
<a name="API_WorkspaceEncryptionConfigurationInfo_Contents"></a>

 ** encryptionType **   <a name="iotsitewise-Type-WorkspaceEncryptionConfigurationInfo-encryptionType"></a>
The type of encryption used for the workspace.
Type: String
Valid Values: `SITEWISE_DEFAULT_ENCRYPTION | KMS_BASED_ENCRYPTION`
Required: Yes

 ** kmsKeyArn **   <a name="iotsitewise-Type-WorkspaceEncryptionConfigurationInfo-kmsKeyArn"></a>
The key ARN of the AWS KMS key used for AWS KMS encryption if `encryptionType` is `KMS_BASED_ENCRYPTION`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`
Required: No

## See Also
<a name="API_WorkspaceEncryptionConfigurationInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/WorkspaceEncryptionConfigurationInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/WorkspaceEncryptionConfigurationInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/WorkspaceEncryptionConfigurationInfo)
