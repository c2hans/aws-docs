---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_RemediationConfiguration.html
---

# RemediationConfiguration
<a name="API_RemediationConfiguration"></a>

An object that represents the details about the remediation configuration that includes the remediation action, parameters, and data to execute the action.

## Contents
<a name="API_RemediationConfiguration_Contents"></a>

 ** ConfigRuleName **   <a name="config-Type-RemediationConfiguration-ConfigRuleName"></a>
The name of the AWS Config rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

 ** TargetId **   <a name="config-Type-RemediationConfiguration-TargetId"></a>
Target ID is the name of the SSM document.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** TargetType **   <a name="config-Type-RemediationConfiguration-TargetType"></a>
The type of the target. Target executes remediation. For example, SSM document.
Type: String
Valid Values: `SSM_DOCUMENT`
Required: Yes

 ** Arn **   <a name="config-Type-RemediationConfiguration-Arn"></a>
Amazon Resource Name (ARN) of remediation configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** Automatic **   <a name="config-Type-RemediationConfiguration-Automatic"></a>
The remediation is triggered automatically.
Type: Boolean
Required: No

 ** CreatedByService **   <a name="config-Type-RemediationConfiguration-CreatedByService"></a>
Name of the service that owns the service-linked rule, if applicable.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** ExecutionControls **   <a name="config-Type-RemediationConfiguration-ExecutionControls"></a>
An ExecutionControls object.
Type: [ExecutionControls](API_ExecutionControls.md) object
Required: No

 ** MaximumAutomaticAttempts **   <a name="config-Type-RemediationConfiguration-MaximumAutomaticAttempts"></a>
The maximum number of failed attempts for auto-remediation. If you do not select a number, the default is 5.
For example, if you specify MaximumAutomaticAttempts as 5 with RetryAttemptSeconds as 50 seconds, AWS Config will put a RemediationException on your behalf for the failing resource after the 5th failed attempt within 50 seconds.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** Parameters **   <a name="config-Type-RemediationConfiguration-Parameters"></a>
An object of the RemediationParameterValue.
Type: String to [RemediationParameterValue](API_RemediationParameterValue.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 25 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** ResourceType **   <a name="config-Type-RemediationConfiguration-ResourceType"></a>
The type of a resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** RetryAttemptSeconds **   <a name="config-Type-RemediationConfiguration-RetryAttemptSeconds"></a>
Time window to determine whether or not to add a remediation exception to prevent infinite remediation attempts. If `MaximumAutomaticAttempts` remediation attempts have been made under `RetryAttemptSeconds`, a remediation exception will be added to the resource. If you do not select a number, the default is 60 seconds.
For example, if you specify `RetryAttemptSeconds` as 50 seconds and `MaximumAutomaticAttempts` as 5, AWS Config will run auto-remediations 5 times within 50 seconds before adding a remediation exception to the resource.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 2678000.
Required: No

 ** TargetVersion **   <a name="config-Type-RemediationConfiguration-TargetVersion"></a>
Version of the target. For example, version of the SSM document.
If you make backward incompatible changes to the SSM document, you must call PutRemediationConfiguration API again to ensure the remediations can run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_RemediationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/RemediationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/RemediationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/RemediationConfiguration)
