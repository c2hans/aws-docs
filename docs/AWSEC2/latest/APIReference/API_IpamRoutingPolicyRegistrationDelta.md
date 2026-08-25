---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IpamRoutingPolicyRegistrationDelta.html
---

# IpamRoutingPolicyRegistrationDelta
<a name="API_IpamRoutingPolicyRegistrationDelta"></a>

Contains information about a routing policy registration change, including the changes applied and their publication state.

## Contents
<a name="API_IpamRoutingPolicyRegistrationDelta_Contents"></a>

 ** deltaId **
The unique identifier of the delta.
Type: String
Required: No

 ** deltaJson **
The JSON specification describing the changes applied in this delta.
Type: String
Required: No

 ** state **
The state of the delta. Valid values: `pending` \| `published` \| `failed`.
Type: String
Valid Values: `pending | published | failed`
Required: No

 ** stateMessage **
A message describing the current state, including error information if the delta failed.
Type: String
Required: No

## See Also
<a name="API_IpamRoutingPolicyRegistrationDelta_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IpamRoutingPolicyRegistrationDelta)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IpamRoutingPolicyRegistrationDelta)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IpamRoutingPolicyRegistrationDelta)
