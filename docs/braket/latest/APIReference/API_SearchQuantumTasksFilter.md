---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_SearchQuantumTasksFilter.html
---

# SearchQuantumTasksFilter
<a name="API_SearchQuantumTasksFilter"></a>

A filter used to search for quantum tasks.

## Contents
<a name="API_SearchQuantumTasksFilter_Contents"></a>

 ** name **   <a name="braket-Type-SearchQuantumTasksFilter-name"></a>
The name of the quantum task parameter to filter based on. Filter name can be either `quantumTaskArn`, `deviceArn`, `jobArn`, `status` or `createdAt`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** operator **   <a name="braket-Type-SearchQuantumTasksFilter-operator"></a>
An operator to use for the filter.
Type: String
Valid Values: `LT | LTE | EQUAL | GT | GTE | BETWEEN`
Required: Yes

 ** values **   <a name="braket-Type-SearchQuantumTasksFilter-values"></a>
The values used to filter quantum tasks based on the filter name and operator.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_SearchQuantumTasksFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/SearchQuantumTasksFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/SearchQuantumTasksFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/SearchQuantumTasksFilter)
