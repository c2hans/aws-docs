---
source_url: https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_DeploymentFilter.html
---

# DeploymentFilter
<a name="API_DeploymentFilter"></a>

A filter name and value pair that is used to return more specific results from a describe operation. Filters can be used to match a set of resources by specific criteria.

## Contents
<a name="API_DeploymentFilter_Contents"></a>

 ** name **   <a name="launchwizard-Type-DeploymentFilter-name"></a>
The name of the filter. Filter names are case-sensitive.
Type: String
Valid Values: `WORKLOAD_NAME | DEPLOYMENT_STATUS`
Required: No

 ** values **   <a name="launchwizard-Type-DeploymentFilter-values"></a>
The filter values. Filter values are case-sensitive. If you specify multiple values for a filter, the values are joined with an `OR`, and the request returns all results that match any of the specified values.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*(^(([A-Za-z])+([0-9A-Za-z\-\_])+)$).*`
Required: No

## See Also
<a name="API_DeploymentFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/launch-wizard-2018-05-10/DeploymentFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/launch-wizard-2018-05-10/DeploymentFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/launch-wizard-2018-05-10/DeploymentFilter)
