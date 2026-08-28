---
source_url: https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_AutoshiftSummary.html
---

# AutoshiftSummary
<a name="API_AutoshiftSummary"></a>

Information about an autoshift. AWS starts an autoshift to temporarily move traffic for a resource away from an Availability Zone in an AWS Region when AWS determines that there's an issue in the Availability Zone that could potentially affect customers. You can configure zonal autoshift in ARC for managed resources in your AWS account in a Region. Supported AWS resources are automatically registered with ARC.

Autoshifts are temporary. When the Availability Zone recovers, AWS ends the autoshift, and traffic for the resource is no longer directed to the other Availability Zones in the Region.

You can stop an autoshift for a resource by disabling zonal autoshift.

## Contents
<a name="API_AutoshiftSummary_Contents"></a>

 ** awayFrom **   <a name="zonalshift-Type-AutoshiftSummary-awayFrom"></a>
The Availability Zone (for example, `use1-az1`) that traffic is shifted away from for a resource when AWS starts an autoshift. Until the autoshift ends, traffic for the resource is instead directed to other Availability Zones in the AWS Region. An autoshift can end for a resource, for example, when AWS ends the autoshift for the Availability Zone or when you disable zonal autoshift for the resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20.
Required: Yes

 ** startTime **   <a name="zonalshift-Type-AutoshiftSummary-startTime"></a>
The time (in UTC) when the autoshift started.
Type: Timestamp
Required: Yes

 ** status **   <a name="zonalshift-Type-AutoshiftSummary-status"></a>
The status for an autoshift.
Type: String
Valid Values: `ACTIVE | COMPLETED`
Required: Yes

 ** endTime **   <a name="zonalshift-Type-AutoshiftSummary-endTime"></a>
The time (in UTC) when the autoshift ended.
Type: Timestamp
Required: No

## See Also
<a name="API_AutoshiftSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-zonal-shift-2022-10-30/AutoshiftSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-zonal-shift-2022-10-30/AutoshiftSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-zonal-shift-2022-10-30/AutoshiftSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-zonal-shift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
