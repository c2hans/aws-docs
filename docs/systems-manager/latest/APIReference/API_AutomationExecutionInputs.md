---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_AutomationExecutionInputs.html
---

# AutomationExecutionInputs
<a name="API_AutomationExecutionInputs"></a>

Information about the optional inputs that can be specified for an automation execution preview.

## Contents
<a name="API_AutomationExecutionInputs_Contents"></a>

 ** Parameters **   <a name="systemsmanager-Type-AutomationExecutionInputs-Parameters"></a>
Information about parameters that can be specified for the preview operation.
Type: String to array of strings map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** TargetLocations **   <a name="systemsmanager-Type-AutomationExecutionInputs-TargetLocations"></a>
Information about the AWS Regions and AWS accounts targeted by the Automation execution preview operation.
Type: Array of [TargetLocation](API_TargetLocation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** TargetLocationsURL **   <a name="systemsmanager-Type-AutomationExecutionInputs-TargetLocationsURL"></a>
A publicly accessible URL for a file that contains the `TargetLocations` body. Currently, only files in presigned Amazon S3 buckets are supported.
Type: String
Pattern: `^https:\/\/[-a-zA-Z0-9@:%._\+~#=]{1,253}\.s3(\.[a-z\d-]{9,16})?\.amazonaws\.com\/.{1,2000}`
Required: No

 ** TargetMaps **   <a name="systemsmanager-Type-AutomationExecutionInputs-TargetMaps"></a>
A key-value mapping of document parameters to target resources. Both Targets and TargetMaps can't be specified together.
Type: Array of string to array of strings maps
Array Members: Minimum number of 0 items. Maximum number of 300 items.
Map Entries: Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** TargetParameterName **   <a name="systemsmanager-Type-AutomationExecutionInputs-TargetParameterName"></a>
The name of the parameter used as the target resource for the rate-controlled execution. Required if you specify targets.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** Targets **   <a name="systemsmanager-Type-AutomationExecutionInputs-Targets"></a>
Information about the resources that would be included in the actual runbook execution, if it were to be run. Both Targets and TargetMaps can't be specified together.
Type: Array of [Target](API_Target.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

## See Also
<a name="API_AutomationExecutionInputs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/AutomationExecutionInputs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/AutomationExecutionInputs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/AutomationExecutionInputs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
