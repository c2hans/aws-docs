---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_FindingFilter.html
---

# FindingFilter
<a name="API_FindingFilter"></a>

This data type is used as a request parameter in the [ListFindings](API_ListFindings.md) action.

## Contents
<a name="API_FindingFilter_Contents"></a>

 ** agentIds **   <a name="Inspector-Type-FindingFilter-agentIds"></a>
For a record to match a filter, one of the values that is specified for this data type property must be the exact match of the value of the **agentId** property of the [Finding](API_Finding.md) data type.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 99 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** attributes **   <a name="Inspector-Type-FindingFilter-attributes"></a>
For a record to match a filter, the list of values that are specified for this data type property must be contained in the list of values of the **attributes** property of the [Finding](API_Finding.md) data type.
Type: Array of [Attribute](API_Attribute.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** autoScalingGroups **   <a name="Inspector-Type-FindingFilter-autoScalingGroups"></a>
For a record to match a filter, one of the values that is specified for this data type property must be the exact match of the value of the **autoScalingGroup** property of the [Finding](API_Finding.md) data type.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** creationTimeRange **   <a name="Inspector-Type-FindingFilter-creationTimeRange"></a>
The time range during which the finding is generated.
Type: [TimestampRange](API_TimestampRange.md) object
Required: No

 ** ruleNames **   <a name="Inspector-Type-FindingFilter-ruleNames"></a>
For a record to match a filter, one of the values that is specified for this data type property must be the exact match of the value of the **ruleName** property of the [Finding](API_Finding.md) data type.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Maximum length of 1000.
Required: No

 ** rulesPackageArns **   <a name="Inspector-Type-FindingFilter-rulesPackageArns"></a>
For a record to match a filter, one of the values that is specified for this data type property must be the exact match of the value of the **rulesPackageArn** property of the [Finding](API_Finding.md) data type.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

 ** severities **   <a name="Inspector-Type-FindingFilter-severities"></a>
For a record to match a filter, one of the values that is specified for this data type property must be the exact match of the value of the **severity** property of the [Finding](API_Finding.md) data type.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Valid Values: `Low | Medium | High | Informational | Undefined`
Required: No

 ** userAttributes **   <a name="Inspector-Type-FindingFilter-userAttributes"></a>
For a record to match a filter, the value that is specified for this data type property must be contained in the list of values of the **userAttributes** property of the [Finding](API_Finding.md) data type.
Type: Array of [Attribute](API_Attribute.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_FindingFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/FindingFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/FindingFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/FindingFilter)
