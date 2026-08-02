---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_ImportTaskFilter.html
---

# ImportTaskFilter
<a name="API_ImportTaskFilter"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

A name-values pair of elements you can use to filter the results when querying your import tasks. Currently, wildcards are not supported for filters.

**Note**
When filtering by import status, all other filter values are ignored.

## Contents
<a name="API_ImportTaskFilter_Contents"></a>

 ** name **   <a name="DiscServ-Type-ImportTaskFilter-name"></a>
The name, status, or import task ID for a specific import task.
Type: String
Valid Values: `IMPORT_TASK_ID | STATUS | NAME | FILE_CLASSIFICATION`
Required: No

 ** values **   <a name="DiscServ-Type-ImportTaskFilter-values"></a>
An array of strings that you can provide to match against a specific name, status, or import task ID to filter the results for your import task queries.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_ImportTaskFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/ImportTaskFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/ImportTaskFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/ImportTaskFilter)
