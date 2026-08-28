---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_VMScannerState.html
---

# VMScannerState
<a name="API_VMScannerState"></a>

The state of the Amazon Inspector VM scanner.

## Contents
<a name="API_VMScannerState_Contents"></a>

 ** activated **   <a name="inspector2-Type-VMScannerState-activated"></a>
Whether the VM scanner is activated.
Type: Boolean
Required: No

 ** activatedAt **   <a name="inspector2-Type-VMScannerState-activatedAt"></a>
The date and time the VM scanner was activated.
Type: Timestamp
Required: No

 ** status **   <a name="inspector2-Type-VMScannerState-status"></a>
The status of the VM scanner.
Type: String
Valid Values: `SUCCESS | PENDING | FAILED`
Required: No

## See Also
<a name="API_VMScannerState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/VMScannerState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/VMScannerState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/VMScannerState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
