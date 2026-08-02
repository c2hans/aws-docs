---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_TargetFailure.html
---

# TargetFailure
<a name="API_TargetFailure"></a>

Describes a target failure.

## Contents
<a name="API_TargetFailure_Contents"></a>

 ** failureCode **   <a name="vpclattice-Type-TargetFailure-failureCode"></a>
The failure code.
Type: String
Required: No

 ** failureMessage **   <a name="vpclattice-Type-TargetFailure-failureMessage"></a>
The failure message.
Type: String
Required: No

 ** id **   <a name="vpclattice-Type-TargetFailure-id"></a>
The ID of the target. If the target group type is `INSTANCE`, this is an instance ID. If the target group type is `IP`, this is an IP address. If the target group type is `LAMBDA`, this is the ARN of a Lambda function. If the target group type is `ALB`, this is the ARN of an Application Load Balancer.
Type: String
Required: No

 ** port **   <a name="vpclattice-Type-TargetFailure-port"></a>
The port on which the target is listening. This parameter doesn't apply if the target is a Lambda function.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

## See Also
<a name="API_TargetFailure_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/TargetFailure)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/TargetFailure)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/TargetFailure)
