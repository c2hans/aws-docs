---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ProvisioningArtifactPreferences.html
---

# ProvisioningArtifactPreferences
<a name="API_ProvisioningArtifactPreferences"></a>

The user-defined preferences that will be applied during product provisioning, unless overridden by `ProvisioningPreferences` or `UpdateProvisioningPreferences`.

For more information on maximum concurrent accounts and failure tolerance, see [Stack set operation options](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stackset-ops-options) in the * AWS CloudFormation User Guide*.

## Contents
<a name="API_ProvisioningArtifactPreferences_Contents"></a>

 ** StackSetAccounts **   <a name="servicecatalog-Type-ProvisioningArtifactPreferences-StackSetAccounts"></a>
One or more AWS accounts where stack instances are deployed from the stack set. These accounts can be scoped in `ProvisioningPreferences$StackSetAccounts` and `UpdateProvisioningPreferences$StackSetAccounts`.
Applicable only to a `CFN_STACKSET` provisioned product type.
Type: Array of strings
Pattern: `^[0-9]{12}$`
Required: No

 ** StackSetRegions **   <a name="servicecatalog-Type-ProvisioningArtifactPreferences-StackSetRegions"></a>
One or more AWS Regions where stack instances are deployed from the stack set. These Regions can be scoped in `ProvisioningPreferences$StackSetRegions` and `UpdateProvisioningPreferences$StackSetRegions`.
Applicable only to a `CFN_STACKSET` provisioned product type.
Type: Array of strings
Required: No

## See Also
<a name="API_ProvisioningArtifactPreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ProvisioningArtifactPreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ProvisioningArtifactPreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ProvisioningArtifactPreferences)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
