---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CapacityReservationTarget.html
---

# CapacityReservationTarget
<a name="API_CapacityReservationTarget"></a>

 The target for the Capacity Reservation. Specify Capacity Reservations IDs or Capacity Reservation resource group ARNs.

## Contents
<a name="API_CapacityReservationTarget_Contents"></a>

 ** CapacityReservationIds.member.N **
 The Capacity Reservation IDs to launch instances into.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9\-_\/]+`
Required: No

 ** CapacityReservationResourceGroupArns.member.N **
 The resource group ARNs of the Capacity Reservation to launch instances into.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_CapacityReservationTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/CapacityReservationTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/CapacityReservationTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/CapacityReservationTarget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
