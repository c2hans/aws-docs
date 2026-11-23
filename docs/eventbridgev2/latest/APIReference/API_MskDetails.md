---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_MskDetails.html
---

# MskDetails

Values EventBridge manages for a subscriber that targets an Amazon MSK cluster.

## Contents
<a name="API_MskDetails_Contents"></a>

 ** ConnectivityState **   <a name="eventbridgev2-Type-MskDetails-ConnectivityState"></a>
Provisioning state of the connectivity EventBridge sets up to the cluster. Distinct from the subscriber's State, which the customer controls.
Type: String
Valid Values: `PROVISIONING | PROVISION_FAILED | ACTIVE`
Required: No

 ** StateReason **   <a name="eventbridgev2-Type-MskDetails-StateReason"></a>
Why provisioning failed. Present only when ConnectivityState is PROVISION\_FAILED.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** VpcConnectionArn **   <a name="eventbridgev2-Type-MskDetails-VpcConnectionArn"></a>
ARN of the VPC connection EventBridge uses to reach the cluster. Present only for PRIVATE connectivity, once the connection exists. It is the connection the cluster owner sees through the MSK ListClientVpcConnections API.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Required: No

## See Also
<a name="API_MskDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/MskDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/MskDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/MskDetails)
