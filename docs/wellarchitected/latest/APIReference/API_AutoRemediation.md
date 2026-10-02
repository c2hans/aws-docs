---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_AutoRemediation.html
---

# AutoRemediation
<a name="API_AutoRemediation"></a>

The per-resource auto-remediation for a single affected resource. Represents one AWS Systems Manager (SSM) runbook execution that targets the resource. Present only when the resource's check is backed by an SSM automation runbook.

## Contents
<a name="API_AutoRemediation_Contents"></a>

 ** cliCommand **   <a name="wellarchitected-Type-AutoRemediation-cliCommand"></a>
The AWS CLI command that triggers the same SSM runbook execution for this resource. You can copy and run this command as-is.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** deepLink **   <a name="wellarchitected-Type-AutoRemediation-deepLink"></a>
A deep link to the SSM runbook execution page in the AWS Management Console for this resource, with the execution parameters prefilled.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_AutoRemediation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/AutoRemediation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/AutoRemediation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/AutoRemediation)
