---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnabledBaselineSummary.html
---

# EnabledBaselineSummary
<a name="API_EnabledBaselineSummary"></a>

Returns a summary of information about an `EnabledBaseline` object.

## Contents
<a name="API_EnabledBaselineSummary_Contents"></a>

 ** arn **   <a name="controltower-Type-EnabledBaselineSummary-arn"></a>
The ARN of the `EnabledBaseline` resource
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: Yes

 ** baselineIdentifier **   <a name="controltower-Type-EnabledBaselineSummary-baselineIdentifier"></a>
The specific baseline that is enabled as part of the `EnabledBaseline` resource.
Type: String
Required: Yes

 ** statusSummary **   <a name="controltower-Type-EnabledBaselineSummary-statusSummary"></a>
The deployment summary of an `EnabledControl` or `EnabledBaseline` resource.
Type: [EnablementStatusSummary](API_EnablementStatusSummary.md) object
Required: Yes

 ** targetIdentifier **   <a name="controltower-Type-EnabledBaselineSummary-targetIdentifier"></a>
The target upon which the baseline is enabled.
Type: String
Required: Yes

 ** baselineVersion **   <a name="controltower-Type-EnabledBaselineSummary-baselineVersion"></a>
The enabled version of the baseline.
Type: String
Required: No

 ** driftStatusSummary **   <a name="controltower-Type-EnabledBaselineSummary-driftStatusSummary"></a>
The drift status of the enabled baseline.
Type: [EnabledBaselineDriftStatusSummary](API_EnabledBaselineDriftStatusSummary.md) object
Required: No

 ** parentIdentifier **   <a name="controltower-Type-EnabledBaselineSummary-parentIdentifier"></a>
An ARN that represents an object returned by `ListEnabledBaseline`, to describe an enabled baseline.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: No

## See Also
<a name="API_EnabledBaselineSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/EnabledBaselineSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/EnabledBaselineSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/EnabledBaselineSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
