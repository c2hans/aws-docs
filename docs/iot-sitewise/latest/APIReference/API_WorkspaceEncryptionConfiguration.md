---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_WorkspaceEncryptionConfiguration.html
---

# WorkspaceEncryptionConfiguration
<a name="API_WorkspaceEncryptionConfiguration"></a>

Contains the encryption configuration for a workspace.

## Contents
<a name="API_WorkspaceEncryptionConfiguration_Contents"></a>

 ** encryptionType **   <a name="iotsitewise-Type-WorkspaceEncryptionConfiguration-encryptionType"></a>
The encryption scheme for the workspace. `SITEWISE_DEFAULT_ENCRYPTION` encrypts data with the AWS IoT SiteWise default key. `KMS_BASED_ENCRYPTION` encrypts data with the customer managed AWS KMS key identified by `kmsKeyId`.
Type: String
Valid Values: `SITEWISE_DEFAULT_ENCRYPTION | KMS_BASED_ENCRYPTION`
Required: Yes

 ** kmsKeyId **   <a name="iotsitewise-Type-WorkspaceEncryptionConfiguration-kmsKeyId"></a>
The customer managed AWS KMS key used when `encryptionType` is `KMS_BASED_ENCRYPTION`. Accepts a key ID, key ARN, or key alias. Required for `KMS_BASED_ENCRYPTION`; must be omitted for `SITEWISE_DEFAULT_ENCRYPTION`. After a workspace's customer managed key configuration becomes active, the key can't be changed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_WorkspaceEncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/WorkspaceEncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/WorkspaceEncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/WorkspaceEncryptionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
