---
source_url: https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_AutoshiftInResource.html
---

# AutoshiftInResource
<a name="API_AutoshiftInResource"></a>

A complex structure that lists an autoshift that is currently active for a managed resource and information about the autoshift.

For more information, see [How zonal autoshift and practice runs work](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.html) in the Amazon Application Recovery Controller Developer Guide.

## Contents
<a name="API_AutoshiftInResource_Contents"></a>

 ** appliedStatus **   <a name="zonalshift-Type-AutoshiftInResource-appliedStatus"></a>
The `appliedStatus` field specifies which application traffic shift is in effect for a resource when there is more than one active traffic shift. There can be more than one application traffic shift in progress at the same time - that is, practice run zonal shifts, customer-initiated zonal shifts, or an autoshift. The `appliedStatus` field for a shift that is in progress for a resource can have one of two values: `APPLIED` or `NOT_APPLIED`. The zonal shift or autoshift that is currently in effect for the resource has an `appliedStatus` set to `APPLIED`.
The overall principle for precedence is that zonal shifts that you start as a customer take precedence autoshifts, which take precedence over practice runs. That is, customer-initiated zonal shifts > autoshifts > practice run zonal shifts.
For more information, see [How zonal autoshift and practice runs work](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.html) in the Amazon Application Recovery Controller Developer Guide.
Type: String
Valid Values: `APPLIED | NOT_APPLIED`
Required: Yes

 ** awayFrom **   <a name="zonalshift-Type-AutoshiftInResource-awayFrom"></a>
The Availability Zone (for example, `use1-az1`) that traffic is shifted away from for a resource, when AWS starts an autoshift. Until the autoshift ends, traffic for the resource is instead directed to other Availability Zones in the AWS Region. An autoshift can end for a resource, for example, when AWS ends the autoshift for the Availability Zone or when you disable zonal autoshift for the resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20.
Required: Yes

 ** startTime **   <a name="zonalshift-Type-AutoshiftInResource-startTime"></a>
The time (UTC) when the autoshift started.
Type: Timestamp
Required: Yes

## See Also
<a name="API_AutoshiftInResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-zonal-shift-2022-10-30/AutoshiftInResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-zonal-shift-2022-10-30/AutoshiftInResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-zonal-shift-2022-10-30/AutoshiftInResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-zonal-shift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
