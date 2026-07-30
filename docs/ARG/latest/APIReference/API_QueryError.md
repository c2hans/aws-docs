---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_QueryError.html
---

# QueryError
<a name="API_QueryError"></a>

A two-part error structure that can occur in `ListGroupResources` or `SearchResources`.

## Contents
<a name="API_QueryError_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ErrorCode **   <a name="ARG-Type-QueryError-ErrorCode"></a>
Specifies the error code that was raised.
Type: String
Valid Values: `CLOUDFORMATION_STACK_INACTIVE | CLOUDFORMATION_STACK_NOT_EXISTING | CLOUDFORMATION_STACK_UNASSUMABLE_ROLE | RESOURCE_TYPE_NOT_SUPPORTED`
Required: No

 ** Message **   <a name="ARG-Type-QueryError-Message"></a>
A message that explains the `ErrorCode`.
Type: String
Required: No

## See Also
<a name="API_QueryError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/QueryError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/QueryError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/QueryError)
