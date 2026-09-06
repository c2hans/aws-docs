---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_OperationSummary.html
---

# OperationSummary
<a name="API_OperationSummary"></a>

A complex type that contains information about an operation that matches the criteria that you specified in a [ListOperations](https://docs.aws.amazon.com/cloud-map/latest/api/API_ListOperations.html) request.

## Contents
<a name="API_OperationSummary_Contents"></a>

 ** Id **   <a name="cloudmap-Type-OperationSummary-Id"></a>
The ID for an operation.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** Status **   <a name="cloudmap-Type-OperationSummary-Status"></a>
The status of the operation. Values include the following:
+  **SUBMITTED**: This is the initial state immediately after you submit a request.
+  **PENDING**: AWS Cloud Map is performing the operation.
+  **SUCCESS**: The operation succeeded.
+  **FAIL**: The operation failed. For the failure reason, see `ErrorMessage`.
Type: String
Valid Values: `SUBMITTED | PENDING | SUCCESS | FAIL`
Required: No

## See Also
<a name="API_OperationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/OperationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/OperationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/OperationSummary)
