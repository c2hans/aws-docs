---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_SoftwareFilters.html
---

# SoftwareFilters
<a name="API_SoftwareFilters"></a>

Enables filtering of software packages and the resources that contain them.

## Contents
<a name="API_SoftwareFilters_Contents"></a>

 ** CompositeFilters **   <a name="securityhub-Type-SoftwareFilters-CompositeFilters"></a>
A collection of complex filtering conditions that can be applied to software packages.
Type: Array of [SoftwareCompositeFilter](API_SoftwareCompositeFilter.md) objects
Required: No

 ** CompositeOperator **   <a name="securityhub-Type-SoftwareFilters-CompositeOperator"></a>
The logical operator used to combine multiple filter conditions in the structure.
Type: String
Valid Values: `AND | OR`
Required: No

## See Also
<a name="API_SoftwareFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/SoftwareFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/SoftwareFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/SoftwareFilters)
