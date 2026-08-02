---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_Filter.html
---

# Filter
<a name="API_Filter"></a>

Use filters to return a subset of resources. You can define filters for specific parameters, such as the resource status.

## Contents
<a name="API_Filter_Contents"></a>

 ** resourceArns **   <a name="omics-Type-Filter-resourceArns"></a>
Filter based on the Amazon Resource Number (ARN) of the resource. You can specify up to 10 values.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** status **   <a name="omics-Type-Filter-status"></a>
Filter based on the resource status. You can specify up to 10 values.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Valid Values: `PENDING | ACTIVATING | ACTIVE | DELETING | DELETED | FAILED`
Required: No

 ** type **   <a name="omics-Type-Filter-type"></a>
The type of resources to be filtered. You can specify one or more of the resource types.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Valid Values: `VARIANT_STORE | ANNOTATION_STORE | WORKFLOW`
Required: No

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/Filter)
