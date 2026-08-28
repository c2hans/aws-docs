---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_EncryptionConfiguration.html
---

# EncryptionConfiguration
<a name="API_EncryptionConfiguration"></a>

Settings to configure server-side encryption.

 For additional control over security, you can encrypt your data using a **customer-managed key** for Step Functions state machines and activities. You can configure a symmetric AWS KMS key and data key reuse period when creating or updating a **State Machine**, and when creating an **Activity**. The execution history and state machine definition will be encrypted with the key applied to the State Machine. Activity inputs will be encrypted with the key applied to the Activity.

**Note**
 Step Functions automatically enables encryption at rest using AWS owned keys at no charge. However, AWS KMS charges apply when using a customer managed key. For more information about pricing, see [AWS Key Management Service pricing](https://aws.amazon.com/kms/pricing/).

For more information on AWS KMS, see [What is AWS Key Management Service?](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)

## Contents
<a name="API_EncryptionConfiguration_Contents"></a>

 ** type **   <a name="StepFunctions-Type-EncryptionConfiguration-type"></a>
Encryption type
Type: String
Valid Values: `AWS_OWNED_KEY | CUSTOMER_MANAGED_KMS_KEY`
Required: Yes

 ** kmsDataKeyReusePeriodSeconds **   <a name="StepFunctions-Type-EncryptionConfiguration-kmsDataKeyReusePeriodSeconds"></a>
Maximum duration that Step Functions will reuse data keys. When the period expires, Step Functions will call `GenerateDataKey`. Only applies to customer managed keys.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 900.
Required: No

 ** kmsKeyId **   <a name="StepFunctions-Type-EncryptionConfiguration-kmsKeyId"></a>
An alias, alias ARN, key ID, or key ARN of a symmetric encryption AWS KMS key to encrypt data. To specify a AWS KMS key in a different AWS account, you must use the key ARN or alias ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_EncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/EncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/EncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/EncryptionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Step Functions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query step-functions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
