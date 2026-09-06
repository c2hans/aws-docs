---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_StepParameterChunks.html
---

# StepParameterChunks
<a name="API_StepParameterChunks"></a>

Defines how a step parameter range should be divided into chunks.

## Contents
<a name="API_StepParameterChunks_Contents"></a>

 ** defaultTaskCount **   <a name="deadlinecloud-Type-StepParameterChunks-defaultTaskCount"></a>
The number of tasks to combine into a single chunk by default.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2147483647.
Required: Yes

 ** rangeConstraint **   <a name="deadlinecloud-Type-StepParameterChunks-rangeConstraint"></a>
Specifies whether the chunked ranges must be contiguous or can have gaps between them.
Type: String
Valid Values: `CONTIGUOUS | NONCONTIGUOUS`
Required: Yes

 ** targetRuntimeSeconds **   <a name="deadlinecloud-Type-StepParameterChunks-targetRuntimeSeconds"></a>
The number of seconds to aim for when forming chunks.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

## See Also
<a name="API_StepParameterChunks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/StepParameterChunks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/StepParameterChunks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/StepParameterChunks)
