---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ResourceConflict.html
---

# ResourceConflict
<a name="API_ResourceConflict"></a>

Contains information about a resource conflict.

## Contents
<a name="API_ResourceConflict_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** resourceId **   <a name="verifiedpermissions-Type-ResourceConflict-resourceId"></a>
The unique identifier of the resource involved in a conflict.
Type: String
Required: Yes

 ** resourceType **   <a name="verifiedpermissions-Type-ResourceConflict-resourceType"></a>
The type of the resource involved in a conflict.
Type: String
Valid Values: `IDENTITY_SOURCE | POLICY_STORE | POLICY | POLICY_TEMPLATE | SCHEMA | POLICY_STORE_ALIAS`
Required: Yes

## See Also
<a name="API_ResourceConflict_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/ResourceConflict)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/ResourceConflict)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/ResourceConflict)
