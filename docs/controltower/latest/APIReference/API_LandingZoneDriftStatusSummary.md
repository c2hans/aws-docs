---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_LandingZoneDriftStatusSummary.html
---

# LandingZoneDriftStatusSummary
<a name="API_LandingZoneDriftStatusSummary"></a>

The drift status summary of the landing zone.

If the landing zone differs from the expected configuration, it is defined to be in a state of drift. You can repair this drift by resetting the landing zone.

## Contents
<a name="API_LandingZoneDriftStatusSummary_Contents"></a>

 ** status **   <a name="controltower-Type-LandingZoneDriftStatusSummary-status"></a>
The drift status of the landing zone.
Valid values:
+  `DRIFTED`: The landing zone deployed in this configuration does not match the configuration that AWS Control Tower expected.
+  `IN_SYNC`: The landing zone deployed in this configuration matches the configuration that AWS Control Tower expected.
Type: String
Valid Values: `DRIFTED | IN_SYNC`
Required: No

## See Also
<a name="API_LandingZoneDriftStatusSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/LandingZoneDriftStatusSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/LandingZoneDriftStatusSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/LandingZoneDriftStatusSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
