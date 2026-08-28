---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_AzureScopeConfiguration.html
---

# AzureScopeConfiguration
<a name="API_AzureScopeConfiguration"></a>

The scope of Azure resources that Amazon Inspector scans, defined separately for VM, container image, and serverless scanning. Returned as part of a connector's configuration.

## Contents
<a name="API_AzureScopeConfiguration_Contents"></a>

 ** containerImageScanning **   <a name="inspector2-Type-AzureScopeConfiguration-containerImageScanning"></a>
The scope configuration for container image scanning.
Type: [ScopeConfiguration](API_ScopeConfiguration.md) object
Required: No

 ** serverlessScanning **   <a name="inspector2-Type-AzureScopeConfiguration-serverlessScanning"></a>
The scope configuration for serverless scanning.
Type: [ScopeConfiguration](API_ScopeConfiguration.md) object
Required: No

 ** vmScanning **   <a name="inspector2-Type-AzureScopeConfiguration-vmScanning"></a>
The scope configuration for VM scanning.
Type: [ScopeConfiguration](API_ScopeConfiguration.md) object
Required: No

## See Also
<a name="API_AzureScopeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/AzureScopeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/AzureScopeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/AzureScopeConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
