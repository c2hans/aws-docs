---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-voice-id_ServerSideEncryptionConfiguration.html
---

# ServerSideEncryptionConfiguration
<a name="API_connect-voice-id_ServerSideEncryptionConfiguration"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

The configuration containing information about the customer managed key used for encrypting customer data.

## Contents
<a name="API_connect-voice-id_ServerSideEncryptionConfiguration_Contents"></a>

 ** KmsKeyId **   <a name="connect-Type-connect-voice-id_ServerSideEncryptionConfiguration-KmsKeyId"></a>
The identifier of the KMS key to use to encrypt data stored by Voice ID. Voice ID doesn't support asymmetric customer managed keys.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## See Also
<a name="API_connect-voice-id_ServerSideEncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/voice-id-2021-09-27/ServerSideEncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/voice-id-2021-09-27/ServerSideEncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/voice-id-2021-09-27/ServerSideEncryptionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
