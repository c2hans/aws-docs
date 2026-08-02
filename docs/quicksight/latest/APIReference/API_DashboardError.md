---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DashboardError.html
---

# DashboardError
<a name="API_DashboardError"></a>

Dashboard error.

## Contents
<a name="API_DashboardError_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Message **   <a name="QS-Type-DashboardError-Message"></a>
Message.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Type **   <a name="QS-Type-DashboardError-Type"></a>
Type.
Type: String
Valid Values: `ACCESS_DENIED | SOURCE_NOT_FOUND | DATA_SET_NOT_FOUND | INTERNAL_FAILURE | PARAMETER_VALUE_INCOMPATIBLE | PARAMETER_TYPE_INVALID | PARAMETER_NOT_FOUND | COLUMN_TYPE_MISMATCH | COLUMN_GEOGRAPHIC_ROLE_MISMATCH | COLUMN_REPLACEMENT_MISSING`
Required: No

 ** ViolatedEntities **   <a name="QS-Type-DashboardError-ViolatedEntities"></a>
Lists the violated entities that caused the dashboard error.
Type: Array of [Entity](API_Entity.md) objects
Array Members: Maximum number of 200 items.
Required: No

## See Also
<a name="API_DashboardError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DashboardError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DashboardError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DashboardError)
