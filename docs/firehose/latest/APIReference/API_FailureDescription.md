---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_FailureDescription.html
---

# FailureDescription
<a name="API_FailureDescription"></a>

Provides details in case one of the following operations fails due to an error related to KMS: [CreateDeliveryStream](API_CreateDeliveryStream.md), [DeleteDeliveryStream](API_DeleteDeliveryStream.md), [StartDeliveryStreamEncryption](API_StartDeliveryStreamEncryption.md), [StopDeliveryStreamEncryption](API_StopDeliveryStreamEncryption.md).

## Contents
<a name="API_FailureDescription_Contents"></a>

 ** Details **   <a name="Firehose-Type-FailureDescription-Details"></a>
A message providing details about the error that caused the failure.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^(?!\s*$).+`
Required: Yes

 ** Type **   <a name="Firehose-Type-FailureDescription-Type"></a>
The type of error that caused the failure.
Type: String
Valid Values: `VPC_ENDPOINT_SERVICE_NAME_NOT_FOUND | VPC_INTERFACE_ENDPOINT_SERVICE_ACCESS_DENIED | RETIRE_KMS_GRANT_FAILED | CREATE_KMS_GRANT_FAILED | KMS_ACCESS_DENIED | DISABLED_KMS_KEY | INVALID_KMS_KEY | KMS_KEY_NOT_FOUND | KMS_OPT_IN_REQUIRED | CREATE_ENI_FAILED | DELETE_ENI_FAILED | SUBNET_NOT_FOUND | SECURITY_GROUP_NOT_FOUND | ENI_ACCESS_DENIED | SUBNET_ACCESS_DENIED | SECURITY_GROUP_ACCESS_DENIED | UNKNOWN_ERROR`
Required: Yes

## See Also
<a name="API_FailureDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/FailureDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/FailureDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/FailureDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
