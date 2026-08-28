---
source_url: https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_ZonalShiftInResource.html
---

# ZonalShiftInResource
<a name="API_ZonalShiftInResource"></a>

A complex structure that lists the zonal shifts for a managed resource and their statuses for the resource.

## Contents
<a name="API_ZonalShiftInResource_Contents"></a>

 ** appliedStatus **   <a name="zonalshift-Type-ZonalShiftInResource-appliedStatus"></a>
The `appliedStatus` field specifies which application traffic shift is in effect for a resource when there is more than one active traffic shift. There can be more than one application traffic shift in progress at the same time - that is, practice run zonal shifts, customer-initiated zonal shifts, or an autoshift. The `appliedStatus` field for a shift that is in progress for a resource can have one of two values: `APPLIED` or `NOT_APPLIED`. The zonal shift or autoshift that is currently in effect for the resource has an `appliedStatus` set to `APPLIED`.
The overall principle for precedence is that zonal shifts that you start as a customer take precedence autoshifts, which take precedence over practice runs. That is, customer-initiated zonal shifts > autoshifts > practice run zonal shifts.
For more information, see [How zonal autoshift and practice runs work](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.html) in the Amazon Application Recovery Controller Developer Guide.
Type: String
Valid Values: `APPLIED | NOT_APPLIED`
Required: Yes

 ** awayFrom **   <a name="zonalshift-Type-ZonalShiftInResource-awayFrom"></a>
The Availability Zone (for example, `use1-az1`) that traffic is moved away from for a resource when you start a zonal shift. Until the zonal shift expires or you cancel it, traffic for the resource is instead moved to other Availability Zones in the AWS Region.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20.
Required: Yes

 ** comment **   <a name="zonalshift-Type-ZonalShiftInResource-comment"></a>
A comment that you enter for a customer-initiated zonal shift. Only the latest comment is retained; no comment history is maintained. That is, a new comment overwrites any existing comment string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: Yes

 ** expiryTime **   <a name="zonalshift-Type-ZonalShiftInResource-expiryTime"></a>
The expiry time (expiration time) for a customer-initiated zonal shift. A zonal shift is temporary and must be set to expire when you start the zonal shift. You can initially set a zonal shift to expire in a maximum of three days (72 hours). However, you can update a zonal shift to set a new expiration at any time.
When you start a zonal shift, you specify how long you want it to be active, which ARC converts to an expiry time (expiration time). You can cancel a zonal shift when you're ready to restore traffic to the Availability Zone, or just wait for it to expire. Or you can update the zonal shift to specify another length of time to expire in.
Type: Timestamp
Required: Yes

 ** resourceIdentifier **   <a name="zonalshift-Type-ZonalShiftInResource-resourceIdentifier"></a>
The identifier for the resource to include in a zonal shift. The identifier is the Amazon Resource Name (ARN) for the resource.
Amazon Application Recovery Controller currently supports enabling the following resources for zonal shift and zonal autoshift:
+  [Amazon EC2 Auto Scaling groups](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.ec2-auto-scaling-groups.html)
+  [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.eks.html)
+  [Application Load Balancer](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.app-load-balancers.html)
+  [Network Load Balancer](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.network-load-balancers.html)
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.
Required: Yes

 ** startTime **   <a name="zonalshift-Type-ZonalShiftInResource-startTime"></a>
The time (UTC) when the zonal shift starts.
Type: Timestamp
Required: Yes

 ** zonalShiftId **   <a name="zonalshift-Type-ZonalShiftInResource-zonalShiftId"></a>
The identifier of a zonal shift.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 36.
Pattern: `[A-Za-z0-9-]+`
Required: Yes

 ** practiceRunOutcome **   <a name="zonalshift-Type-ZonalShiftInResource-practiceRunOutcome"></a>
The outcome, or end state, returned for a practice run. The following values can be returned:
+  **PENDING:** Outcome value when a practice run is in progress.
+  **SUCCEEDED:** Outcome value when the outcome alarm specified for the practice run configuration does not go into an `ALARM` state during the practice run, and the practice run was not interrupted before it completed the expected 30 minute zonal shift.
+  **INTERRUPTED:** Outcome value when the practice run was stopped before the expected 30 minute zonal shift duration, or there was another problem with the practice run that created an inconclusive outcome.
+  **FAILED:** Outcome value when the outcome alarm specified for the practice run configuration goes into an `ALARM` state during the practice run, and the practice run was not interrupted before it completed.
+  **CAPACITY\_CHECK\_FAILED:** The check for balanced capacity across Availability Zones for your load balancing and Auto Scaling group resources failed.
For more information about practice run outcomes, see [ Considerations when you configure zonal autoshift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.configure.html) in the Amazon Application Recovery Controller Developer Guide.
Type: String
Valid Values: `FAILED | INTERRUPTED | PENDING | SUCCEEDED | CAPACITY_CHECK_FAILED`
Required: No

 ** shiftType **   <a name="zonalshift-Type-ZonalShiftInResource-shiftType"></a>
Defines the zonal shift type.
Type: String
Valid Values: `ZONAL_SHIFT | PRACTICE_RUN | FIS_EXPERIMENT | ZONAL_AUTOSHIFT`
Required: No

## See Also
<a name="API_ZonalShiftInResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-zonal-shift-2022-10-30/ZonalShiftInResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-zonal-shift-2022-10-30/ZonalShiftInResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-zonal-shift-2022-10-30/ZonalShiftInResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-zonal-shift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
