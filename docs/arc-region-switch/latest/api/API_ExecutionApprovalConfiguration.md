---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ExecutionApprovalConfiguration.html
---

# ExecutionApprovalConfiguration
<a name="API_ExecutionApprovalConfiguration"></a>

Configuration for approval steps in a Region switch plan execution. Approval steps require manual intervention before the execution can proceed.

## Contents
<a name="API_ExecutionApprovalConfiguration_Contents"></a>

 ** approvalRole **   <a name="regionswitch-Type-ExecutionApprovalConfiguration-approvalRole"></a>
The IAM approval role for the configuration.
Type: String
Required: Yes

 ** timeoutMinutes **   <a name="regionswitch-Type-ExecutionApprovalConfiguration-timeoutMinutes"></a>
The timeout value specified for the configuration.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_ExecutionApprovalConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/ExecutionApprovalConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/ExecutionApprovalConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/ExecutionApprovalConfiguration)
