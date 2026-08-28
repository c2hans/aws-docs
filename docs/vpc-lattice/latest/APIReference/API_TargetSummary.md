---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_TargetSummary.html
---

# TargetSummary
<a name="API_TargetSummary"></a>

Summary information about a target.

## Contents
<a name="API_TargetSummary_Contents"></a>

 ** id **   <a name="vpclattice-Type-TargetSummary-id"></a>
The ID of the target. If the target group type is `INSTANCE`, this is an instance ID. If the target group type is `IP`, this is an IP address. If the target group type is `LAMBDA`, this is the ARN of a Lambda function. If the target type is `ALB`, this is the ARN of an Application Load Balancer.
Type: String
Required: No

 ** port **   <a name="vpclattice-Type-TargetSummary-port"></a>
The port on which the target is listening.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

 ** reasonCode **   <a name="vpclattice-Type-TargetSummary-reasonCode"></a>
The code for why the target status is what it is.
Type: String
Required: No

 ** status **   <a name="vpclattice-Type-TargetSummary-status"></a>
The status of the target.
+  `DRAINING`: The target is being deregistered. No new connections are sent to this target while current connections are being drained. The default draining time is 1 minute.
+  `UNAVAILABLE`: Health checks are unavailable for the target group.
+  `HEALTHY`: The target is healthy.
+  `UNHEALTHY`: The target is unhealthy.
+  `INITIAL`: Initial health checks on the target are being performed.
+  `UNUSED`: Target group is not used in a service.
Type: String
Valid Values: `DRAINING | UNAVAILABLE | HEALTHY | UNHEALTHY | INITIAL | UNUSED`
Required: No

## See Also
<a name="API_TargetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/TargetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/TargetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/TargetSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
