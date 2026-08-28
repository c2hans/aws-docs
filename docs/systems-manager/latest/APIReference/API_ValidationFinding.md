---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ValidationFinding.html
---

# ValidationFinding
<a name="API_ValidationFinding"></a>

A validation finding from a cloud connector validation check.

## Contents
<a name="API_ValidationFinding_Contents"></a>

 ** Code **   <a name="systemsmanager-Type-ValidationFinding-Code"></a>
A code that identifies the specific validation finding.
Type: String
Valid Values: `TargetInaccessible | TargetUnusable | TargetStateWarning | AwsRoleAssumptionFailed | WebIdentityTokenFailed | OutboundWebIdentityFederationDisabled | ProviderCredentialCreationFailed | TenantSummary | SubscriptionAccessible`
Required: No

 ** Message **   <a name="systemsmanager-Type-ValidationFinding-Message"></a>
A message that describes the validation finding.
Type: String
Required: No

 ** ProviderMessage **   <a name="systemsmanager-Type-ValidationFinding-ProviderMessage"></a>
A message from the third-party cloud provider related to the validation finding.
Type: String
Required: No

 ** Scope **   <a name="systemsmanager-Type-ValidationFinding-Scope"></a>
The scope of the validation finding, identifying the specific resource affected.
Type: [ValidationFindingScope](API_ValidationFindingScope.md) object
Required: No

 ** Type **   <a name="systemsmanager-Type-ValidationFinding-Type"></a>
The type of the validation finding.
Type: String
Valid Values: `INFO | WARN | ERROR`
Required: No

## See Also
<a name="API_ValidationFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ValidationFinding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ValidationFinding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ValidationFinding)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
