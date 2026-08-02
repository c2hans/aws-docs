---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_CapacityProvider.html
---

# CapacityProvider
<a name="API_CapacityProvider"></a>

A capacity provider manages compute resources for Lambda functions.

## Contents
<a name="API_CapacityProvider_Contents"></a>

 ** CapacityProviderArn **   <a name="lambda-Type-CapacityProvider-CapacityProviderArn"></a>
The Amazon Resource Name (ARN) of the capacity provider.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `arn:aws[a-zA-Z-]*:lambda:[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:capacity-provider:[a-zA-Z0-9-_]+`
Required: Yes

 ** PermissionsConfig **   <a name="lambda-Type-CapacityProvider-PermissionsConfig"></a>
The permissions configuration for the capacity provider.
Type: [CapacityProviderPermissionsConfig](API_CapacityProviderPermissionsConfig.md) object
Required: Yes

 ** State **   <a name="lambda-Type-CapacityProvider-State"></a>
The current state of the capacity provider.
Type: String
Valid Values: `Pending | Active | Failed | Deleting`
Required: Yes

 ** VpcConfig **   <a name="lambda-Type-CapacityProvider-VpcConfig"></a>
The VPC configuration for the capacity provider.
Type: [CapacityProviderVpcConfig](API_CapacityProviderVpcConfig.md) object
Required: Yes

 ** CapacityProviderScalingConfig **   <a name="lambda-Type-CapacityProvider-CapacityProviderScalingConfig"></a>
The scaling configuration for the capacity provider.
Type: [CapacityProviderScalingConfig](API_CapacityProviderScalingConfig.md) object
Required: No

 ** InstanceRequirements **   <a name="lambda-Type-CapacityProvider-InstanceRequirements"></a>
The instance requirements for compute resources managed by the capacity provider.
Type: [InstanceRequirements](API_InstanceRequirements.md) object
Required: No

 ** KmsKeyArn **   <a name="lambda-Type-CapacityProvider-KmsKeyArn"></a>
The ARN of the KMS key used to encrypt the capacity provider's resources.
Type: String
Pattern: `(arn:(aws[a-zA-Z-]*)?:[a-z0-9-.]+:.*)|()`
Required: No

 ** LastModified **   <a name="lambda-Type-CapacityProvider-LastModified"></a>
The date and time when the capacity provider was last modified.
Type: String
Required: No

 ** PropagateTags **   <a name="lambda-Type-CapacityProvider-PropagateTags"></a>
Configuration for tag propagation to managed resources launched by the capacity provider.
Type: [PropagateTags](API_PropagateTags.md) object
Required: No

 ** TelemetryConfig **   <a name="lambda-Type-CapacityProvider-TelemetryConfig"></a>
The telemetry configuration for the capacity provider, including logging settings.
Type: [CapacityProviderTelemetryConfig](API_CapacityProviderTelemetryConfig.md) object
Required: No

## See Also
<a name="API_CapacityProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/CapacityProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/CapacityProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/CapacityProvider)
