---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_BaselineOperation.html
---

# BaselineOperation
<a name="API_BaselineOperation"></a>

An object of shape `BaselineOperation`, returning details about the specified `Baseline` operation ID.

## Contents
<a name="API_BaselineOperation_Contents"></a>

 ** endTime **   <a name="controltower-Type-BaselineOperation-endTime"></a>
The end time of the operation (if applicable), in ISO 8601 format.
Type: Timestamp
Required: No

 ** operationIdentifier **   <a name="controltower-Type-BaselineOperation-operationIdentifier"></a>
The identifier of the specified operation.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** operationType **   <a name="controltower-Type-BaselineOperation-operationType"></a>
An enumerated type (`enum`) with possible values of `ENABLE_BASELINE`, `DISABLE_BASELINE`, `UPDATE_ENABLED_BASELINE`, or `RESET_ENABLED_BASELINE`.
Type: String
Valid Values: `ENABLE_BASELINE | DISABLE_BASELINE | UPDATE_ENABLED_BASELINE | RESET_ENABLED_BASELINE`
Required: No

 ** startTime **   <a name="controltower-Type-BaselineOperation-startTime"></a>
The start time of the operation, in ISO 8601 format.
Type: Timestamp
Required: No

 ** status **   <a name="controltower-Type-BaselineOperation-status"></a>
An enumerated type (`enum`) with possible values of `SUCCEEDED`, `FAILED`, or `IN_PROGRESS`.
Type: String
Valid Values: `SUCCEEDED | FAILED | IN_PROGRESS`
Required: No

 ** statusMessage **   <a name="controltower-Type-BaselineOperation-statusMessage"></a>
A status message that gives more information about the operation's status, if applicable.
Type: String
Required: No

## See Also
<a name="API_BaselineOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/BaselineOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/BaselineOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/BaselineOperation)
