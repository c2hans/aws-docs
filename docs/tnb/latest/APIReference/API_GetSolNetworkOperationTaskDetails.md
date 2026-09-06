---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolNetworkOperationTaskDetails.html
---

# GetSolNetworkOperationTaskDetails
<a name="API_GetSolNetworkOperationTaskDetails"></a>

Gets the details of a network operation.

A network operation is any operation that is done to your network, such as network instance instantiation or termination.

## Contents
<a name="API_GetSolNetworkOperationTaskDetails_Contents"></a>

 ** taskContext **   <a name="TNB-Type-GetSolNetworkOperationTaskDetails-taskContext"></a>
Context for the network operation task.
Type: String to string map
Required: No

 ** taskEndTime **   <a name="TNB-Type-GetSolNetworkOperationTaskDetails-taskEndTime"></a>
Task end time.
Type: Timestamp
Required: No

 ** taskErrorDetails **   <a name="TNB-Type-GetSolNetworkOperationTaskDetails-taskErrorDetails"></a>
Task error details.
Type: [ErrorInfo](API_ErrorInfo.md) object
Required: No

 ** taskName **   <a name="TNB-Type-GetSolNetworkOperationTaskDetails-taskName"></a>
Task name.
Type: String
Required: No

 ** taskStartTime **   <a name="TNB-Type-GetSolNetworkOperationTaskDetails-taskStartTime"></a>
Task start time.
Type: Timestamp
Required: No

 ** taskStatus **   <a name="TNB-Type-GetSolNetworkOperationTaskDetails-taskStatus"></a>
Task status.
Type: String
Valid Values: `SCHEDULED | STARTED | IN_PROGRESS | COMPLETED | ERROR | SKIPPED | CANCELLED`
Required: No

## See Also
<a name="API_GetSolNetworkOperationTaskDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/GetSolNetworkOperationTaskDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/GetSolNetworkOperationTaskDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/GetSolNetworkOperationTaskDetails)
