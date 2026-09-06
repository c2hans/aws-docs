---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_ListServiceInstancesFilter.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# ListServiceInstancesFilter
<a name="API_ListServiceInstancesFilter"></a>

A filtering criterion to scope down the result list of the [ListServiceInstances](API_ListServiceInstances.md) action.

## Contents
<a name="API_ListServiceInstancesFilter_Contents"></a>

 ** key **   <a name="proton-Type-ListServiceInstancesFilter-key"></a>
The name of a filtering criterion.
Type: String
Valid Values: `name | deploymentStatus | templateName | serviceName | deployedTemplateVersionStatus | environmentName | lastDeploymentAttemptedAtBefore | lastDeploymentAttemptedAtAfter | createdAtBefore | createdAtAfter`
Required: No

 ** value **   <a name="proton-Type-ListServiceInstancesFilter-value"></a>
A value to filter by.
With the date/time keys (`*At{Before,After}`), the value is a valid [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339.html) string with no UTC offset and with an optional fractional precision (for example, `1985-04-12T23:20:50.52Z`).
Type: String
Required: No

## See Also
<a name="API_ListServiceInstancesFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/ListServiceInstancesFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/ListServiceInstancesFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/ListServiceInstancesFilter)
