---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ServiceGroup.html
---

# ServiceGroup
<a name="API_ServiceGroup"></a>

A structure that represents a logical grouping of services based on shared attributes such as business unit, environment, or entry point.

## Contents
<a name="API_ServiceGroup_Contents"></a>

 ** GroupIdentifier **   <a name="applicationsignals-Type-ServiceGroup-GroupIdentifier"></a>
A unique identifier for this grouping attribute value, used for filtering and API operations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** GroupName **   <a name="applicationsignals-Type-ServiceGroup-GroupName"></a>
The name of the grouping attribute, such as `BusinessUnit` or `Environment`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** GroupSource **   <a name="applicationsignals-Type-ServiceGroup-GroupSource"></a>
The source of the grouping attribute, such as `TAG`, `OTEL`, or `DEFAULT`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** GroupValue **   <a name="applicationsignals-Type-ServiceGroup-GroupValue"></a>
The value of the grouping attribute for this service, such as `Payments` or `Production`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## See Also
<a name="API_ServiceGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/ServiceGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/ServiceGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/ServiceGroup)
