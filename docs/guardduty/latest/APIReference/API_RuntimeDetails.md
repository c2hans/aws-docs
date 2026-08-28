---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_RuntimeDetails.html
---

# RuntimeDetails
<a name="API_RuntimeDetails"></a>

Information about the process and any required context values for a specific finding.

## Contents
<a name="API_RuntimeDetails_Contents"></a>

 ** context **   <a name="guardduty-Type-RuntimeDetails-context"></a>
Additional information about the suspicious activity.
Type: [RuntimeContext](API_RuntimeContext.md) object
Required: No

 ** process **   <a name="guardduty-Type-RuntimeDetails-process"></a>
Information about the observed process.
Type: [ProcessDetails](API_ProcessDetails.md) object
Required: No

## See Also
<a name="API_RuntimeDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/RuntimeDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/RuntimeDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/RuntimeDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
