---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_RLSPolicyAttachment.html
---

# RLSPolicyAttachment
<a name="API_RLSPolicyAttachment"></a>

A structure that describes the attachment of a row-level security policy to a resource for a principal.

## Contents
<a name="API_RLSPolicyAttachment_Contents"></a>

 ** CatalogId **   <a name="lakeformation-Type-RLSPolicyAttachment-CatalogId"></a>
The identifier for the Data Catalog that contains the attachment. By default, the account ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Condition **   <a name="lakeformation-Type-RLSPolicyAttachment-Condition"></a>
A Lake Formation condition, which applies to the row-level security policy attachment and contains an expression.
Type: [Condition](API_Condition.md) object
Required: No

 ** DefaultRLSPolicy **   <a name="lakeformation-Type-RLSPolicyAttachment-DefaultRLSPolicy"></a>
Indicates whether this attachment is the default row-level security policy for the resource.
Type: Boolean
Required: No

 ** PolicyName **   <a name="lakeformation-Type-RLSPolicyAttachment-PolicyName"></a>
The name of the attached row-level security policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Principal **   <a name="lakeformation-Type-RLSPolicyAttachment-Principal"></a>
The principal to which the attached policy applies.
Type: [DataLakePrincipal](API_DataLakePrincipal.md) object
Required: No

 ** Resource **   <a name="lakeformation-Type-RLSPolicyAttachment-Resource"></a>
The resource to which the policy is attached.
Type: [Resource](API_Resource.md) object
Required: No

## See Also
<a name="API_RLSPolicyAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/RLSPolicyAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/RLSPolicyAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/RLSPolicyAttachment)
