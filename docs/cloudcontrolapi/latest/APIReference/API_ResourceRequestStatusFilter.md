---
source_url: https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_ResourceRequestStatusFilter.html
---

# ResourceRequestStatusFilter
<a name="API_ResourceRequestStatusFilter"></a>

The filter criteria to use in determining the requests returned.

## Contents
<a name="API_ResourceRequestStatusFilter_Contents"></a>

 ** Operations **   <a name="ccapi-Type-ResourceRequestStatusFilter-Operations"></a>
The operation types to include in the filter.
Type: Array of strings
Valid Values: `CREATE | DELETE | UPDATE`
Required: No

 ** OperationStatuses **   <a name="ccapi-Type-ResourceRequestStatusFilter-OperationStatuses"></a>
The operation statuses to include in the filter.
+  `PENDING`: The operation has been requested, but not yet initiated.
+  `IN_PROGRESS`: The operation is in progress.
+  `SUCCESS`: The operation completed.
+  `FAILED`: The operation failed.
+  `CANCEL_IN_PROGRESS`: The operation is in the process of being canceled.
+  `CANCEL_COMPLETE`: The operation has been canceled.
Type: Array of strings
Valid Values: `PENDING | IN_PROGRESS | SUCCESS | FAILED | CANCEL_IN_PROGRESS | CANCEL_COMPLETE`
Required: No

## See Also
<a name="API_ResourceRequestStatusFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudcontrol-2021-09-30/ResourceRequestStatusFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudcontrol-2021-09-30/ResourceRequestStatusFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudcontrol-2021-09-30/ResourceRequestStatusFilter)
