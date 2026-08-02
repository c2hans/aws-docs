---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelSpotFleetRequestsSuccessItem.html
---

# CancelSpotFleetRequestsSuccessItem
<a name="API_CancelSpotFleetRequestsSuccessItem"></a>

Describes a Spot Fleet request that was successfully canceled.

## Contents
<a name="API_CancelSpotFleetRequestsSuccessItem_Contents"></a>

 ** currentSpotFleetRequestState **
The current state of the Spot Fleet request.
Type: String
Valid Values: `submitted | active | cancelled | failed | cancelled_running | cancelled_terminating | modifying`
Required: No

 ** previousSpotFleetRequestState **
The previous state of the Spot Fleet request.
Type: String
Valid Values: `submitted | active | cancelled | failed | cancelled_running | cancelled_terminating | modifying`
Required: No

 ** spotFleetRequestId **
The ID of the Spot Fleet request.
Type: String
Required: No

## See Also
<a name="API_CancelSpotFleetRequestsSuccessItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CancelSpotFleetRequestsSuccessItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CancelSpotFleetRequestsSuccessItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CancelSpotFleetRequestsSuccessItem)
