---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Workforce.html
---

# Workforce
<a name="API_Workforce"></a>

A single private workforce, which is automatically created when you create your first private work team. You can create one private work force in each AWS Region. By default, any workforce-related API operation used in a specific region will apply to the workforce created in that region. To learn how to create a private workforce, see [Create a Private Workforce](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-create-private.html).

## Contents
<a name="API_Workforce_Contents"></a>

 ** WorkforceArn **   <a name="sagemaker-Type-Workforce-WorkforceArn"></a>
The Amazon Resource Name (ARN) of the private workforce.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:workforce/.*`
Required: Yes

 ** WorkforceName **   <a name="sagemaker-Type-Workforce-WorkforceName"></a>
The name of the private workforce.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9\-]){0,62}`
Required: Yes

 ** CognitoConfig **   <a name="sagemaker-Type-Workforce-CognitoConfig"></a>
The configuration of an Amazon Cognito workforce. A single Cognito workforce is created using and corresponds to a single [ Amazon Cognito user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html).
Type: [CognitoConfig](API_CognitoConfig.md) object
Required: No

 ** CreateDate **   <a name="sagemaker-Type-Workforce-CreateDate"></a>
The date that the workforce is created.
Type: Timestamp
Required: No

 ** FailureReason **   <a name="sagemaker-Type-Workforce-FailureReason"></a>
The reason your workforce failed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

 ** IpAddressType **   <a name="sagemaker-Type-Workforce-IpAddressType"></a>
The IP address type you specify - either `IPv4` only or `dualstack` (`IPv4` and `IPv6`) - to support your labeling workforce.
Type: String
Valid Values: `ipv4 | dualstack`
Required: No

 ** LastUpdatedDate **   <a name="sagemaker-Type-Workforce-LastUpdatedDate"></a>
The most recent date that [UpdateWorkforce](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateWorkforce.html) was used to successfully add one or more IP address ranges ([CIDRs](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html)) to a private workforce's allow list.
Type: Timestamp
Required: No

 ** OidcConfig **   <a name="sagemaker-Type-Workforce-OidcConfig"></a>
The configuration of an OIDC Identity Provider (IdP) private workforce.
Type: [OidcConfigForResponse](API_OidcConfigForResponse.md) object
Required: No

 ** SourceIpConfig **   <a name="sagemaker-Type-Workforce-SourceIpConfig"></a>
A list of one to ten IP address ranges ([CIDRs](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html)) to be added to the workforce allow list. By default, a workforce isn't restricted to specific IP addresses.
Type: [SourceIpConfig](API_SourceIpConfig.md) object
Required: No

 ** Status **   <a name="sagemaker-Type-Workforce-Status"></a>
The status of your workforce.
Type: String
Valid Values: `Initializing | Updating | Deleting | Failed | Active`
Required: No

 ** SubDomain **   <a name="sagemaker-Type-Workforce-SubDomain"></a>
The subdomain for your OIDC Identity Provider.
Type: String
Required: No

 ** WorkforceVpcConfig **   <a name="sagemaker-Type-Workforce-WorkforceVpcConfig"></a>
The configuration of a VPC workforce.
Type: [WorkforceVpcConfigResponse](API_WorkforceVpcConfigResponse.md) object
Required: No

## See Also
<a name="API_Workforce_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/Workforce)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/Workforce)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/Workforce)
