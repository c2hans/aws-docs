---
source_url: https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_ManagedResourceSummary.html
---

# ManagedResourceSummary
<a name="API_ManagedResourceSummary"></a>

A complex structure for a managed resource in an AWS account with information about zonal shifts and autoshifts.

You can start a zonal shift in ARC for a managed resource to temporarily move traffic for the resource away from an Availability Zone in an AWS Region. You can also configure zonal autoshift for a managed resource.

**Note**
At this time, managed resources are Amazon EC2 Auto Scaling groups, Amazon Elastic Kubernetes Service, Network Load Balancers, and Application Load Balancer.

## Contents
<a name="API_ManagedResourceSummary_Contents"></a>

 ** availabilityZones **   <a name="zonalshift-Type-ManagedResourceSummary-availabilityZones"></a>
The Availability Zones that a resource is deployed in.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 20.
Required: Yes

 ** appliedWeights **   <a name="zonalshift-Type-ManagedResourceSummary-appliedWeights"></a>
A collection of key-value pairs that indicate whether resources are active in Availability Zones or not. The key name is the Availability Zone where the resource is deployed. The value is 1 or 0.
Type: String to float map
Key Length Constraints: Minimum length of 0. Maximum length of 20.
Valid Range: Minimum value of 0.0. Maximum value of 1.0.
Required: No

 ** arn **   <a name="zonalshift-Type-ManagedResourceSummary-arn"></a>
The Amazon Resource Name (ARN) for the managed resource.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.
Pattern: `arn:.*`
Required: No

 ** autoshifts **   <a name="zonalshift-Type-ManagedResourceSummary-autoshifts"></a>
An array of the autoshifts that have been completed for a resource.
Type: Array of [AutoshiftInResource](API_AutoshiftInResource.md) objects
Required: No

 ** name **   <a name="zonalshift-Type-ManagedResourceSummary-name"></a>
The name of the managed resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** practiceRunStatus **   <a name="zonalshift-Type-ManagedResourceSummary-practiceRunStatus"></a>
This status tracks whether a practice run configuration exists for a resource. When you configure a practice run for a resource so that a practice run configuration exists, ARC sets this value to `ENABLED`. If a you have not configured a practice run for the resource, or delete a practice run configuration, ARC sets the value to `DISABLED`.
ARC updates this status; you can't set a practice run status to `ENABLED` or `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** zonalAutoshiftStatus **   <a name="zonalshift-Type-ManagedResourceSummary-zonalAutoshiftStatus"></a>
The status of autoshift for a resource. When you configure zonal autoshift for a resource, you can set the value of the status to `ENABLED` or `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** zonalShifts **   <a name="zonalshift-Type-ManagedResourceSummary-zonalShifts"></a>
An array of the zonal shifts for a resource.
Type: Array of [ZonalShiftInResource](API_ZonalShiftInResource.md) objects
Required: No

## See Also
<a name="API_ManagedResourceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-zonal-shift-2022-10-30/ManagedResourceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-zonal-shift-2022-10-30/ManagedResourceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-zonal-shift-2022-10-30/ManagedResourceSummary)
