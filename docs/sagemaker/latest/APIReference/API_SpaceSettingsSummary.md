---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SpaceSettingsSummary.html
---

# SpaceSettingsSummary
<a name="API_SpaceSettingsSummary"></a>

Specifies summary information about the space settings.

## Contents
<a name="API_SpaceSettingsSummary_Contents"></a>

 ** AppType **   <a name="sagemaker-Type-SpaceSettingsSummary-AppType"></a>
The type of app created within the space.
Type: String
Valid Values: `JupyterServer | KernelGateway | DetailedProfiler | TensorBoard | CodeEditor | JupyterLab | RStudioServerPro | RSessionGateway | Canvas`
Required: No

 ** RemoteAccess **   <a name="sagemaker-Type-SpaceSettingsSummary-RemoteAccess"></a>
A setting that enables or disables remote access for a SageMaker space. When enabled, this allows you to connect to the remote space from your local IDE.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** SpaceStorageSettings **   <a name="sagemaker-Type-SpaceSettingsSummary-SpaceStorageSettings"></a>
The storage settings for a space.
Type: [SpaceStorageSettings](API_SpaceStorageSettings.md) object
Required: No

## See Also
<a name="API_SpaceSettingsSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/SpaceSettingsSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/SpaceSettingsSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/SpaceSettingsSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
