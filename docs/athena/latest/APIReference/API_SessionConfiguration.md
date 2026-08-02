---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_SessionConfiguration.html
---

# SessionConfiguration
<a name="API_SessionConfiguration"></a>

Contains session configuration information.

## Contents
<a name="API_SessionConfiguration_Contents"></a>

 ** EncryptionConfiguration **   <a name="athena-Type-SessionConfiguration-EncryptionConfiguration"></a>
If query and calculation results are encrypted in Amazon S3, indicates the encryption option used (for example, `SSE_KMS` or `CSE_KMS`) and key information.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object
Required: No

 ** ExecutionRole **   <a name="athena-Type-SessionConfiguration-ExecutionRole"></a>
The ARN of the execution role used to access user resources for Spark sessions and Identity Center enabled workgroups. This property applies only to Spark enabled workgroups and Identity Center enabled workgroups.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
Required: No

 ** IdleTimeoutSeconds **   <a name="athena-Type-SessionConfiguration-IdleTimeoutSeconds"></a>
The idle timeout in seconds for the session.
Type: Long
Required: No

 ** SessionIdleTimeoutInMinutes **   <a name="athena-Type-SessionConfiguration-SessionIdleTimeoutInMinutes"></a>
The idle timeout in seconds for the session.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 480.
Required: No

 ** WorkingDirectory **   <a name="athena-Type-SessionConfiguration-WorkingDirectory"></a>
The Amazon S3 location that stores information for the notebook.
Type: String
Required: No

## See Also
<a name="API_SessionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/SessionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/SessionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/SessionConfiguration)
