---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DryRunConfigOutput.html
---

# DryRunConfigOutput
<a name="API_DryRunConfigOutput"></a>

Returns the dry run configurations set for a canary.

## Contents
<a name="API_DryRunConfigOutput_Contents"></a>

 ** DryRunId **   <a name="synthetics-Type-DryRunConfigOutput-DryRunId"></a>
The DryRunId associated with an existing canary’s dry run. You can use this DryRunId to retrieve information about the dry run.
Type: String
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** LastDryRunExecutionStatus **   <a name="synthetics-Type-DryRunConfigOutput-LastDryRunExecutionStatus"></a>
Returns the last execution status for a canary's dry run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_DryRunConfigOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/DryRunConfigOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/DryRunConfigOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/DryRunConfigOutput)
