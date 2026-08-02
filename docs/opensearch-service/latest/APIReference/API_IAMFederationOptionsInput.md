---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_IAMFederationOptionsInput.html
---

# IAMFederationOptionsInput
<a name="API_IAMFederationOptionsInput"></a>

Input parameters for configuring IAM identity federation settings.

## Contents
<a name="API_IAMFederationOptionsInput_Contents"></a>

 ** Enabled **   <a name="opensearchservice-Type-IAMFederationOptionsInput-Enabled"></a>
Specifies whether IAM identity federation is enabled for the OpenSearch domain.
Type: Boolean
Required: No

 ** RolesKey **   <a name="opensearchservice-Type-IAMFederationOptionsInput-RolesKey"></a>
The key in the SAML assertion that contains the user's role information.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^(null|[A-Za-z][A-Za-z0-9_.:/=+\-@]*)$`
Required: No

 ** SubjectKey **   <a name="opensearchservice-Type-IAMFederationOptionsInput-SubjectKey"></a>
The key in the SAML assertion that contains the user's subject identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^(null|[A-Za-z][A-Za-z0-9_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_IAMFederationOptionsInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/IAMFederationOptionsInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/IAMFederationOptionsInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/IAMFederationOptionsInput)
