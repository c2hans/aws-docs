---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ExecutionEnvironmentVariables.html
---

# ExecutionEnvironmentVariables
<a name="API_ExecutionEnvironmentVariables"></a>

Environment variables provided as input for a pipeline execution.

## Contents
<a name="API_ExecutionEnvironmentVariables_Contents"></a>

 ** computeNodes **   <a name="iotsitewise-Type-ExecutionEnvironmentVariables-computeNodes"></a>
Per-compute-node environment variable overrides. Each entry maps a compute node name to its environment variable overrides.
Type: String to string to string map map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `[a-zA-Z0-9_-]+`
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `(?!(?i)AWS_)[a-zA-Z_][a-zA-Z0-9_]*`
Value Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** global **   <a name="iotsitewise-Type-ExecutionEnvironmentVariables-global"></a>
Global environment variables that apply to all compute nodes in the pipeline execution.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `(?!(?i)AWS_)[a-zA-Z_][a-zA-Z0-9_]*`
Value Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_ExecutionEnvironmentVariables_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ExecutionEnvironmentVariables)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ExecutionEnvironmentVariables)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ExecutionEnvironmentVariables)
