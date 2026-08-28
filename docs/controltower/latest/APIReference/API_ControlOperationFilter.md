---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_ControlOperationFilter.html
---

# ControlOperationFilter
<a name="API_ControlOperationFilter"></a>

A filter object that lets you call `ListControlOperations` with a specific filter.

## Contents
<a name="API_ControlOperationFilter_Contents"></a>

 ** controlIdentifiers **   <a name="controltower-Type-ControlOperationFilter-controlIdentifiers"></a>
The set of `controlIdentifier` returned by the filter.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: No

 ** controlOperationTypes **   <a name="controltower-Type-ControlOperationFilter-controlOperationTypes"></a>
The set of `ControlOperation` objects returned by the filter.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `ENABLE_CONTROL | DISABLE_CONTROL | UPDATE_ENABLED_CONTROL | RESET_ENABLED_CONTROL`
Required: No

 ** enabledControlIdentifiers **   <a name="controltower-Type-ControlOperationFilter-enabledControlIdentifiers"></a>
The set `controlIdentifier` of enabled controls selected by the filter.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: No

 ** statuses **   <a name="controltower-Type-ControlOperationFilter-statuses"></a>
Lists the status of control operations.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `SUCCEEDED | FAILED | IN_PROGRESS`
Required: No

 ** targetIdentifiers **   <a name="controltower-Type-ControlOperationFilter-targetIdentifiers"></a>
The set of `targetIdentifier` objects returned by the filter.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: No

## See Also
<a name="API_ControlOperationFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/ControlOperationFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/ControlOperationFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/ControlOperationFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
