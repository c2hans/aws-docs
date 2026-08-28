---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_OperationFilter.html
---

# OperationFilter
<a name="API_OperationFilter"></a>

A complex type that lets you select the operations that you want to list.

## Contents
<a name="API_OperationFilter_Contents"></a>

 ** Name **   <a name="cloudmap-Type-OperationFilter-Name"></a>
Specify the operations that you want to get:
+  **NAMESPACE\_ID**: Gets operations related to specified namespaces.
+  **SERVICE\_ID**: Gets operations related to specified services.
+  **STATUS**: Gets operations based on the status of the operations: `SUBMITTED`, `PENDING`, `SUCCEED`, or `FAIL`.
+  **TYPE**: Gets specified types of operation.
+  **UPDATE\_DATE**: Gets operations that changed status during a specified date/time range.
Type: String
Valid Values: `NAMESPACE_ID | SERVICE_ID | STATUS | TYPE | UPDATE_DATE`
Required: Yes

 ** Values **   <a name="cloudmap-Type-OperationFilter-Values"></a>
Specify values that are applicable to the value that you specify for `Name`:
+  **NAMESPACE\_ID**: Specify one namespace ID.
+  **SERVICE\_ID**: Specify one service ID.
+  **STATUS**: Specify one or more statuses: `SUBMITTED`, `PENDING`, `SUCCEED`, or `FAIL`.
+  **TYPE**: Specify one or more of the following types: `CREATE_NAMESPACE`, `DELETE_NAMESPACE`, `UPDATE_SERVICE`, `REGISTER_INSTANCE`, or `DEREGISTER_INSTANCE`.
+  **UPDATE\_DATE**: Specify a start date and an end date in Unix date/time format and Coordinated Universal Time (UTC). The start date must be the first value.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** Condition **   <a name="cloudmap-Type-OperationFilter-Condition"></a>
The operator that you want to use to determine whether an operation matches the specified value. Valid values for condition include:
+  `EQ`: When you specify `EQ` for the condition, you can specify only one value. `EQ` is supported for `NAMESPACE_ID`, `SERVICE_ID`, `STATUS`, and `TYPE`. `EQ` is the default condition and can be omitted.
+  `IN`: When you specify `IN` for the condition, you can specify a list of one or more values. `IN` is supported for `STATUS` and `TYPE`. An operation must match one of the specified values to be returned in the response.
+  `BETWEEN`: Specify a start date and an end date in Unix date/time format and Coordinated Universal Time (UTC). The start date must be the first value. `BETWEEN` is supported for `UPDATE_DATE`.
Type: String
Valid Values: `EQ | IN | BETWEEN | BEGINS_WITH`
Required: No

## See Also
<a name="API_OperationFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/OperationFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/OperationFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/OperationFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Map. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloud-map` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
