---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_Target.html
---

# Target
<a name="API_Target"></a>

Describes a target.

## Contents
<a name="API_Target_Contents"></a>

 ** id **   <a name="vpclattice-Type-Target-id"></a>
The ID of the target. If the target group type is `INSTANCE`, this is an instance ID. If the target group type is `IP`, this is an IP address. If the target group type is `LAMBDA`, this is the ARN of a Lambda function. If the target group type is `ALB`, this is the ARN of an Application Load Balancer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

 ** port **   <a name="vpclattice-Type-Target-port"></a>
The port on which the target is listening. For HTTP, the default is 80. For HTTPS, the default is 443.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

## See Also
<a name="API_Target_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/Target)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/Target)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/Target)
