---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_VpcDNSTarget.html
---

# VpcDNSTarget
<a name="API_VpcDNSTarget"></a>

DNS Target record for a custom domain of this Amazon VPC.

## Contents
<a name="API_VpcDNSTarget_Contents"></a>

 ** DomainName **   <a name="apprunner-Type-VpcDNSTarget-DomainName"></a>
The domain name of your target DNS that is associated with the Amazon VPC.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9*.-]{1,255}`
Required: No

 ** VpcId **   <a name="apprunner-Type-VpcDNSTarget-VpcId"></a>
The ID of the Amazon VPC that is associated with the custom domain name of the target DNS.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 51200.
Pattern: `.*`
Required: No

 ** VpcIngressConnectionArn **   <a name="apprunner-Type-VpcDNSTarget-VpcIngressConnectionArn"></a>
The Amazon Resource Name (ARN) of the VPC Ingress Connection that is associated with your service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: No

## See Also
<a name="API_VpcDNSTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/VpcDNSTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/VpcDNSTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/VpcDNSTarget)
