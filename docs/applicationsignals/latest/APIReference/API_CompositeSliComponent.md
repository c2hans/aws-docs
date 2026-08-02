---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_CompositeSliComponent.html
---

# CompositeSliComponent
<a name="API_CompositeSliComponent"></a>

Identifies a single operation to include in a composite SLI for a service-level SLO. Used as an element of the `Components` list in `CompositeSliConfig`.

## Contents
<a name="API_CompositeSliComponent_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** OperationName **   <a name="applicationsignals-Type-CompositeSliComponent-OperationName"></a>
The name of the operation to include in the composite SLI.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_CompositeSliComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/CompositeSliComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/CompositeSliComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/CompositeSliComponent)
