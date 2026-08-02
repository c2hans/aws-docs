---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_OcsfFindingFilters.html
---

# OcsfFindingFilters
<a name="API_OcsfFindingFilters"></a>

Specifies the filtering criteria for security findings using OCSF.

## Contents
<a name="API_OcsfFindingFilters_Contents"></a>

 ** CompositeFilters **   <a name="securityhub-Type-OcsfFindingFilters-CompositeFilters"></a>
Enables the creation of complex filtering conditions by combining filter criteria.
Type: Array of [CompositeFilter](API_CompositeFilter.md) objects
Required: No

 ** CompositeOperator **   <a name="securityhub-Type-OcsfFindingFilters-CompositeOperator"></a>
The logical operators used to combine the filtering on multiple `CompositeFilters`.
Type: String
Valid Values: `AND | OR`
Required: No

## See Also
<a name="API_OcsfFindingFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/OcsfFindingFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/OcsfFindingFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/OcsfFindingFilters)
