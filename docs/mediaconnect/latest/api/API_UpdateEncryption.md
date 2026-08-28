---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateEncryption.html
---

# UpdateEncryption
<a name="API_UpdateEncryption"></a>

 Information about the encryption of the flow.

## Contents
<a name="API_UpdateEncryption_Contents"></a>

 ** algorithm **   <a name="mediaconnect-Type-UpdateEncryption-algorithm"></a>
 The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
Type: String
Valid Values: `aes128 | aes192 | aes256`
Required: No

 ** constantInitializationVector **   <a name="mediaconnect-Type-UpdateEncryption-constantInitializationVector"></a>
 A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
Type: String
Required: No

 ** deviceId **   <a name="mediaconnect-Type-UpdateEncryption-deviceId"></a>
 The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
Type: String
Required: No

 ** keyType **   <a name="mediaconnect-Type-UpdateEncryption-keyType"></a>
 The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
Type: String
Valid Values: `speke | static-key | srt-password`
Required: No

 ** region **   <a name="mediaconnect-Type-UpdateEncryption-region"></a>
 The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
Type: String
Required: No

 ** resourceId **   <a name="mediaconnect-Type-UpdateEncryption-resourceId"></a>
 An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
Type: String
Required: No

 ** roleArn **   <a name="mediaconnect-Type-UpdateEncryption-roleArn"></a>
 The ARN of the role that you created during setup (when you set up MediaConnect as a trusted entity).
Type: String
Required: No

 ** secretArn **   <a name="mediaconnect-Type-UpdateEncryption-secretArn"></a>
 The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
Type: String
Required: No

 ** url **   <a name="mediaconnect-Type-UpdateEncryption-url"></a>
 The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.
Type: String
Required: No

## See Also
<a name="API_UpdateEncryption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/UpdateEncryption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/UpdateEncryption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/UpdateEncryption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
