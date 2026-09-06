---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_ControlOperationSummary.html
---

# ControlOperationSummary
<a name="API_ControlOperationSummary"></a>

A summary of information about the specified control operation.

## Contents
<a name="API_ControlOperationSummary_Contents"></a>

 ** controlIdentifier **   <a name="controltower-Type-ControlOperationSummary-controlIdentifier"></a>
The `controlIdentifier` of a control.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: No

 ** enabledControlIdentifier **   <a name="controltower-Type-ControlOperationSummary-enabledControlIdentifier"></a>
The `controlIdentifier` of an enabled control.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: No

 ** endTime **   <a name="controltower-Type-ControlOperationSummary-endTime"></a>
The time at which the control operation was completed.
Type: Timestamp
Required: No

 ** operationIdentifier **   <a name="controltower-Type-ControlOperationSummary-operationIdentifier"></a>
The unique identifier of a control operation.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** operationType **   <a name="controltower-Type-ControlOperationSummary-operationType"></a>
The type of operation.
Type: String
Valid Values: `ENABLE_CONTROL | DISABLE_CONTROL | UPDATE_ENABLED_CONTROL | RESET_ENABLED_CONTROL`
Required: No

 ** startTime **   <a name="controltower-Type-ControlOperationSummary-startTime"></a>
The time at which a control operation began.
Type: Timestamp
Required: No

 ** status **   <a name="controltower-Type-ControlOperationSummary-status"></a>
The status of the specified control operation.
Type: String
Valid Values: `SUCCEEDED | FAILED | IN_PROGRESS`
Required: No

 ** statusMessage **   <a name="controltower-Type-ControlOperationSummary-statusMessage"></a>
A speficic message displayed as part of the control status.
Type: String
Required: No

 ** targetIdentifier **   <a name="controltower-Type-ControlOperationSummary-targetIdentifier"></a>
The unique identifier of the target of a control operation.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: No

## See Also
<a name="API_ControlOperationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/ControlOperationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/ControlOperationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/ControlOperationSummary)
