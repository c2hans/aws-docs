---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_RetrievalFilterConfiguration.html
---

# RetrievalFilterConfiguration
<a name="API_amazon-q-connect_RetrievalFilterConfiguration"></a>

Configuration for filtering content during retrieval operations.

## Contents
<a name="API_amazon-q-connect_RetrievalFilterConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** andAll **   <a name="connect-Type-amazon-q-connect_RetrievalFilterConfiguration-andAll"></a>
Filter configuration that requires all conditions to be met.
Type: Array of [RetrievalFilterConfiguration](#API_amazon-q-connect_RetrievalFilterConfiguration) objects
Array Members: Minimum number of 2 items.
Required: No

 ** equals **   <a name="connect-Type-amazon-q-connect_RetrievalFilterConfiguration-equals"></a>
Filter configuration for exact equality matching.
Type: [FilterAttribute](API_amazon-q-connect_FilterAttribute.md) object
Required: No

 ** greaterThan **   <a name="connect-Type-amazon-q-connect_RetrievalFilterConfiguration-greaterThan"></a>
Filter configuration for greater than comparison.
Type: [FilterAttribute](API_amazon-q-connect_FilterAttribute.md) object
Required: No

 ** greaterThanOrEquals **   <a name="connect-Type-amazon-q-connect_RetrievalFilterConfiguration-greaterThanOrEquals"></a>
Filter configuration for greater than or equal comparison.
Type: [FilterAttribute](API_amazon-q-connect_FilterAttribute.md) object
Required: No

 ** in **   <a name="connect-Type-amazon-q-connect_RetrievalFilterConfiguration-in"></a>
Filter configuration for membership in a set of values.
Type: [FilterAttribute](API_amazon-q-connect_FilterAttribute.md) object
Required: No

 ** lessThan **   <a name="connect-Type-amazon-q-connect_RetrievalFilterConfiguration-lessThan"></a>
Filter configuration for less than comparison.
Type: [FilterAttribute](API_amazon-q-connect_FilterAttribute.md) object
Required: No

 ** lessThanOrEquals **   <a name="connect-Type-amazon-q-connect_RetrievalFilterConfiguration-lessThanOrEquals"></a>
Filter configuration for less than or equal comparison.
Type: [FilterAttribute](API_amazon-q-connect_FilterAttribute.md) object
Required: No

 ** listContains **   <a name="connect-Type-amazon-q-connect_RetrievalFilterConfiguration-listContains"></a>
Filter configuration for checking if a list contains a value.
Type: [FilterAttribute](API_amazon-q-connect_FilterAttribute.md) object
Required: No

 ** notEquals **   <a name="connect-Type-amazon-q-connect_RetrievalFilterConfiguration-notEquals"></a>
Filter configuration for inequality matching.
Type: [FilterAttribute](API_amazon-q-connect_FilterAttribute.md) object
Required: No

 ** notIn **   <a name="connect-Type-amazon-q-connect_RetrievalFilterConfiguration-notIn"></a>
Filter configuration for exclusion from a set of values.
Type: [FilterAttribute](API_amazon-q-connect_FilterAttribute.md) object
Required: No

 ** orAll **   <a name="connect-Type-amazon-q-connect_RetrievalFilterConfiguration-orAll"></a>
Filter configuration where any condition can be met.
Type: Array of [RetrievalFilterConfiguration](#API_amazon-q-connect_RetrievalFilterConfiguration) objects
Array Members: Minimum number of 2 items.
Required: No

 ** startsWith **   <a name="connect-Type-amazon-q-connect_RetrievalFilterConfiguration-startsWith"></a>
Filter configuration for prefix matching.
Type: [FilterAttribute](API_amazon-q-connect_FilterAttribute.md) object
Required: No

 ** stringContains **   <a name="connect-Type-amazon-q-connect_RetrievalFilterConfiguration-stringContains"></a>
Filter configuration for substring matching.
Type: [FilterAttribute](API_amazon-q-connect_FilterAttribute.md) object
Required: No

## See Also
<a name="API_amazon-q-connect_RetrievalFilterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/RetrievalFilterConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/RetrievalFilterConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/RetrievalFilterConfiguration)
