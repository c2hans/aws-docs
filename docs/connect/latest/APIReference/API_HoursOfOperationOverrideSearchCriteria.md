---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_HoursOfOperationOverrideSearchCriteria.html
---

# HoursOfOperationOverrideSearchCriteria
<a name="API_HoursOfOperationOverrideSearchCriteria"></a>

The search criteria to be used to return hours of operations overrides.

## Contents
<a name="API_HoursOfOperationOverrideSearchCriteria_Contents"></a>

 ** AndConditions **   <a name="connect-Type-HoursOfOperationOverrideSearchCriteria-AndConditions"></a>
A list of conditions which would be applied together with an AND condition.
Type: Array of [HoursOfOperationOverrideSearchCriteria](#API_HoursOfOperationOverrideSearchCriteria) objects
Required: No

 ** DateCondition **   <a name="connect-Type-HoursOfOperationOverrideSearchCriteria-DateCondition"></a>
A leaf node condition which can be used to specify a date condition.
Type: [DateCondition](API_DateCondition.md) object
Required: No

 ** OrConditions **   <a name="connect-Type-HoursOfOperationOverrideSearchCriteria-OrConditions"></a>
A list of conditions which would be applied together with an OR condition.
Type: Array of [HoursOfOperationOverrideSearchCriteria](#API_HoursOfOperationOverrideSearchCriteria) objects
Required: No

 ** StringCondition **   <a name="connect-Type-HoursOfOperationOverrideSearchCriteria-StringCondition"></a>
A leaf node condition which can be used to specify a string condition.
Type: [StringCondition](API_StringCondition.md) object
Required: No

## See Also
<a name="API_HoursOfOperationOverrideSearchCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/HoursOfOperationOverrideSearchCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/HoursOfOperationOverrideSearchCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/HoursOfOperationOverrideSearchCriteria)
