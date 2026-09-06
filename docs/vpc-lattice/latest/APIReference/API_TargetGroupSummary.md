---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_TargetGroupSummary.html
---

# TargetGroupSummary
<a name="API_TargetGroupSummary"></a>

Summary information about a target group.

For more information, see [Target groups](https://docs.aws.amazon.com/vpc-lattice/latest/ug/target-groups.html) in the *Amazon VPC Lattice User Guide*.

## Contents
<a name="API_TargetGroupSummary_Contents"></a>

 ** arn **   <a name="vpclattice-Type-TargetGroupSummary-arn"></a>
The ARN (Amazon Resource Name) of the target group.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:targetgroup/tg-[0-9a-z]{17}`
Required: No

 ** createdAt **   <a name="vpclattice-Type-TargetGroupSummary-createdAt"></a>
The date and time that the target group was created, in ISO-8601 format.
Type: Timestamp
Required: No

 ** id **   <a name="vpclattice-Type-TargetGroupSummary-id"></a>
The ID of the target group.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `tg-[0-9a-z]{17}`
Required: No

 ** ipAddressType **   <a name="vpclattice-Type-TargetGroupSummary-ipAddressType"></a>
The type of IP address used for the target group. The possible values are `IPV4` and `IPV6`. This is an optional parameter. If not specified, the default is `IPV4`.
Type: String
Valid Values: `IPV4 | IPV6`
Required: No

 ** lambdaEventStructureVersion **   <a name="vpclattice-Type-TargetGroupSummary-lambdaEventStructureVersion"></a>
The version of the event structure that your Lambda function receives. Supported only if the target group type is `LAMBDA`.
Type: String
Valid Values: `V1 | V2`
Required: No

 ** lastUpdatedAt **   <a name="vpclattice-Type-TargetGroupSummary-lastUpdatedAt"></a>
The date and time that the target group was last updated, in ISO-8601 format.
Type: Timestamp
Required: No

 ** name **   <a name="vpclattice-Type-TargetGroupSummary-name"></a>
The name of the target group.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `(?!tg-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`
Required: No

 ** port **   <a name="vpclattice-Type-TargetGroupSummary-port"></a>
The port of the target group.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

 ** protocol **   <a name="vpclattice-Type-TargetGroupSummary-protocol"></a>
The protocol of the target group.
Type: String
Valid Values: `HTTP | HTTPS | TCP`
Required: No

 ** serviceArns **   <a name="vpclattice-Type-TargetGroupSummary-serviceArns"></a>
The Amazon Resource Names (ARNs) of the service.
Type: Array of strings
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}`
Required: No

 ** status **   <a name="vpclattice-Type-TargetGroupSummary-status"></a>
The status.
Type: String
Valid Values: `CREATE_IN_PROGRESS | ACTIVE | DELETE_IN_PROGRESS | CREATE_FAILED | DELETE_FAILED`
Required: No

 ** type **   <a name="vpclattice-Type-TargetGroupSummary-type"></a>
The target group type.
Type: String
Valid Values: `IP | LAMBDA | INSTANCE | ALB`
Required: No

 ** vpcIdentifier **   <a name="vpclattice-Type-TargetGroupSummary-vpcIdentifier"></a>
The ID of the VPC of the target group.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 50.
Pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`
Required: No

## See Also
<a name="API_TargetGroupSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/TargetGroupSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/TargetGroupSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/TargetGroupSummary)
