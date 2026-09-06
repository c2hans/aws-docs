---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_TargetGroupConfig.html
---

# TargetGroupConfig
<a name="API_TargetGroupConfig"></a>

Describes the configuration of a target group.

For more information, see [Target groups](https://docs.aws.amazon.com/vpc-lattice/latest/ug/target-groups.html) in the *Amazon VPC Lattice User Guide*.

## Contents
<a name="API_TargetGroupConfig_Contents"></a>

 ** healthCheck **   <a name="vpclattice-Type-TargetGroupConfig-healthCheck"></a>
The health check configuration. Not supported if the target group type is `LAMBDA` or `ALB`.
Type: [HealthCheckConfig](API_HealthCheckConfig.md) object
Required: No

 ** ipAddressType **   <a name="vpclattice-Type-TargetGroupConfig-ipAddressType"></a>
The type of IP address used for the target group. Supported only if the target group type is `IP`. The default is `IPV4`.
Type: String
Valid Values: `IPV4 | IPV6`
Required: No

 ** lambdaEventStructureVersion **   <a name="vpclattice-Type-TargetGroupConfig-lambdaEventStructureVersion"></a>
The version of the event structure that your Lambda function receives. Supported only if the target group type is `LAMBDA`. The default is `V1`.
Type: String
Valid Values: `V1 | V2`
Required: No

 ** port **   <a name="vpclattice-Type-TargetGroupConfig-port"></a>
The port on which the targets are listening. For HTTP, the default is 80. For HTTPS, the default is 443. Not supported if the target group type is `LAMBDA`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

 ** protocol **   <a name="vpclattice-Type-TargetGroupConfig-protocol"></a>
The protocol to use for routing traffic to the targets. The default is the protocol of the target group. Not supported if the target group type is `LAMBDA`.
Type: String
Valid Values: `HTTP | HTTPS | TCP`
Required: No

 ** protocolVersion **   <a name="vpclattice-Type-TargetGroupConfig-protocolVersion"></a>
The protocol version. The default is `HTTP1`. Not supported if the target group type is `LAMBDA`.
Type: String
Valid Values: `HTTP1 | HTTP2 | GRPC`
Required: No

 ** vpcIdentifier **   <a name="vpclattice-Type-TargetGroupConfig-vpcIdentifier"></a>
The ID of the VPC. Not supported if the target group type is `LAMBDA`.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 50.
Pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`
Required: No

## See Also
<a name="API_TargetGroupConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/TargetGroupConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/TargetGroupConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/TargetGroupConfig)
