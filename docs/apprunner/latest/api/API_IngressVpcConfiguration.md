---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_IngressVpcConfiguration.html
---

# IngressVpcConfiguration
<a name="API_IngressVpcConfiguration"></a>

The configuration of your VPC and the associated VPC endpoint. The VPC endpoint is an AWS PrivateLink resource that allows access to your App Runner services from within an Amazon VPC.

## Contents
<a name="API_IngressVpcConfiguration_Contents"></a>

 ** VpcEndpointId **   <a name="apprunner-Type-IngressVpcConfiguration-VpcEndpointId"></a>
The ID of the VPC endpoint that your App Runner service connects to.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 51200.
Pattern: `.*`
Required: No

 ** VpcId **   <a name="apprunner-Type-IngressVpcConfiguration-VpcId"></a>
The ID of the VPC that is used for the VPC endpoint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 51200.
Pattern: `.*`
Required: No

## See Also
<a name="API_IngressVpcConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/IngressVpcConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/IngressVpcConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/IngressVpcConfiguration)
