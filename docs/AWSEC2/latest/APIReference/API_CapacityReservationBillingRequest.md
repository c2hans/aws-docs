---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CapacityReservationBillingRequest.html
---

# CapacityReservationBillingRequest
<a name="API_CapacityReservationBillingRequest"></a>

Information about a request to assign billing of the unused capacity of a Capacity Reservation.

## Contents
<a name="API_CapacityReservationBillingRequest_Contents"></a>

 ** capacityReservationId **
The ID of the Capacity Reservation.
Type: String
Required: No

 ** capacityReservationInfo **
Information about the Capacity Reservation.
Type: [CapacityReservationInfo](API_CapacityReservationInfo.md) object
Required: No

 ** lastUpdateTime **
The date and time, in UTC time format, at which the request was initiated.
Type: Timestamp
Required: No

 ** requestedBy **
The ID of the AWS account that initiated the request.
Type: String
Required: No

 ** status **
The status of the request. For more information, see [ View billing assignment requests for a shared Amazon EC2 Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/view-billing-transfers.html).
Type: String
Valid Values: `pending | accepted | rejected | cancelled | revoked | expired`
Required: No

 ** statusMessage **
Information about the status.
Type: String
Required: No

 ** unusedReservationBillingOwnerId **
The ID of the AWS account to which the request was sent.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

## See Also
<a name="API_CapacityReservationBillingRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CapacityReservationBillingRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CapacityReservationBillingRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CapacityReservationBillingRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
