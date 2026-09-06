---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ServiceActionSummary.html
---

# ServiceActionSummary
<a name="API_ServiceActionSummary"></a>

Detailed information about the self-service action.

## Contents
<a name="API_ServiceActionSummary_Contents"></a>

 ** DefinitionType **   <a name="servicecatalog-Type-ServiceActionSummary-DefinitionType"></a>
The self-service action definition type. For example, `SSM_AUTOMATION`.
Type: String
Valid Values: `SSM_AUTOMATION`
Required: No

 ** Description **   <a name="servicecatalog-Type-ServiceActionSummary-Description"></a>
The self-service action description.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** Id **   <a name="servicecatalog-Type-ServiceActionSummary-Id"></a>
The self-service action identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** Name **   <a name="servicecatalog-Type-ServiceActionSummary-Name"></a>
The self-service action name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9_\-.]*`
Required: No

## See Also
<a name="API_ServiceActionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ServiceActionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ServiceActionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ServiceActionSummary)
