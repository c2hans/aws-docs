---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_AssociationFilter.html
---

# AssociationFilter
<a name="API_AssociationFilter"></a>

Describes a filter.

## Contents
<a name="API_AssociationFilter_Contents"></a>

 ** key **   <a name="systemsmanager-Type-AssociationFilter-key"></a>
The name of the filter.
 `InstanceId` has been deprecated.
Type: String
Valid Values: `InstanceId | Name | AssociationId | AssociationStatusName | LastExecutedBefore | LastExecutedAfter | AssociationName | ResourceGroupName | CloudConnectorId`
Required: Yes

 ** value **   <a name="systemsmanager-Type-AssociationFilter-value"></a>
The filter value.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

## See Also
<a name="API_AssociationFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/AssociationFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/AssociationFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/AssociationFilter)
