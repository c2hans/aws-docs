---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVerifiedAccessTrustProvider.html
---

# CreateVerifiedAccessTrustProvider
<a name="API_CreateVerifiedAccessTrustProvider"></a>

A trust provider is a third-party entity that creates, maintains, and manages identity information for users and devices. When an application request is made, the identity information sent by the trust provider is evaluated by Verified Access before allowing or denying the application request.

## Request Parameters
<a name="API_CreateVerifiedAccessTrustProvider_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **Description**
A description for the Verified Access trust provider.
Type: String
Required: No

 **DeviceOptions**
The options for a device-based trust provider. This parameter is required when the provider type is `device`.
Type: [CreateVerifiedAccessTrustProviderDeviceOptions](API_CreateVerifiedAccessTrustProviderDeviceOptions.md) object
Required: No

 **DeviceTrustProviderType**
The type of device-based trust provider. This parameter is required when the provider type is `device`.
Type: String
Valid Values: `jamf | crowdstrike | jumpcloud`
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **NativeApplicationOidcOptions**
The OpenID Connect (OIDC) options.
Type: [CreateVerifiedAccessNativeApplicationOidcOptions](API_CreateVerifiedAccessNativeApplicationOidcOptions.md) object
Required: No

 **OidcOptions**
The options for a OpenID Connect-compatible user-identity trust provider. This parameter is required when the provider type is `user`.
Type: [CreateVerifiedAccessTrustProviderOidcOptions](API_CreateVerifiedAccessTrustProviderOidcOptions.md) object
Required: No

 **PolicyReferenceName**
The identifier to be used when working with policy rules.
Type: String
Required: Yes

 **SseSpecification**
The options for server side encryption.
Type: [VerifiedAccessSseSpecificationRequest](API_VerifiedAccessSseSpecificationRequest.md) object
Required: No

 **TagSpecification.N**
The tags to assign to the Verified Access trust provider.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **TrustProviderType**
The type of trust provider.
Type: String
Valid Values: `user | device`
Required: Yes

 **UserTrustProviderType**
The type of user-based trust provider. This parameter is required when the provider type is `user`.
Type: String
Valid Values: `iam-identity-center | oidc`
Required: No

## Response Elements
<a name="API_CreateVerifiedAccessTrustProvider_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **verifiedAccessTrustProvider**
Details about the Verified Access trust provider.
Type: [VerifiedAccessTrustProvider](API_VerifiedAccessTrustProvider.md) object

## Errors
<a name="API_CreateVerifiedAccessTrustProvider_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateVerifiedAccessTrustProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateVerifiedAccessTrustProvider)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateVerifiedAccessTrustProvider)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateVerifiedAccessTrustProvider)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateVerifiedAccessTrustProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateVerifiedAccessTrustProvider)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateVerifiedAccessTrustProvider)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateVerifiedAccessTrustProvider)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateVerifiedAccessTrustProvider)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateVerifiedAccessTrustProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateVerifiedAccessTrustProvider)
