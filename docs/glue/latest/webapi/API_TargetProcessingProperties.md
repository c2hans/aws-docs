---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_TargetProcessingProperties.html
---

# TargetProcessingProperties
<a name="API_TargetProcessingProperties"></a>

The resource properties associated with the integration target.

## Contents
<a name="API_TargetProcessingProperties_Contents"></a>

 ** ConnectionName **   <a name="Glue-Type-TargetProcessingProperties-ConnectionName"></a>
The AWS Glue network connection to configure the AWS Glue job running in the customer VPC.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** EventBusArn **   <a name="Glue-Type-TargetProcessingProperties-EventBusArn"></a>
The ARN of an Eventbridge event bus to receive the integration status notification.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** KmsArn **   <a name="Glue-Type-TargetProcessingProperties-KmsArn"></a>
The ARN of the KMS key used for encryption.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** RoleArn **   <a name="Glue-Type-TargetProcessingProperties-RoleArn"></a>
The IAM role to access the AWS Glue database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_TargetProcessingProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/TargetProcessingProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/TargetProcessingProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/TargetProcessingProperties)
