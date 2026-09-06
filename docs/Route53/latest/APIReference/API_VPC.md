---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_VPC.html
---

# VPC
<a name="API_VPC"></a>

(Private hosted zones only) A complex type that contains information about an Amazon VPC.

If you associate a private hosted zone with an Amazon VPC when you make a [CreateHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHostedZone.html) request, the following parameters are also required.

## Contents
<a name="API_VPC_Contents"></a>

 ** VPCId **   <a name="Route53-Type-VPC-VPCId"></a>
(Private hosted zones only) The ID of an Amazon VPC.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** VPCRegion **   <a name="Route53-Type-VPC-VPCRegion"></a>
(Private hosted zones only) The region that an Amazon VPC was created in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `us-east-1 | us-east-2 | us-west-1 | us-west-2 | eu-west-1 | eu-west-2 | eu-west-3 | eu-central-1 | eu-central-2 | ap-east-1 | me-south-1 | us-gov-west-1 | us-gov-east-1 | us-iso-east-1 | us-iso-west-1 | us-isob-east-1 | me-central-1 | ap-southeast-1 | ap-southeast-2 | ap-southeast-3 | ap-south-1 | ap-south-2 | ap-northeast-1 | ap-northeast-2 | ap-northeast-3 | eu-north-1 | sa-east-1 | ca-central-1 | cn-north-1 | cn-northwest-1 | af-south-1 | eu-south-1 | eu-south-2 | ap-southeast-4 | il-central-1 | ca-west-1 | ap-southeast-5 | mx-central-1 | us-isof-south-1 | us-isof-east-1 | ap-southeast-7 | ap-east-2 | eu-isoe-west-1 | ap-southeast-6 | us-isob-west-1`
Required: No

## See Also
<a name="API_VPC_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/VPC)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/VPC)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/VPC)
