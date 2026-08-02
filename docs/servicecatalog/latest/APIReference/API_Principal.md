---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_Principal.html
---

# Principal
<a name="API_Principal"></a>

Information about a principal.

## Contents
<a name="API_Principal_Contents"></a>

 ** PrincipalARN **   <a name="servicecatalog-Type-Principal-PrincipalARN"></a>
The ARN of the principal (user, role, or group). This field allows for an ARN with no `accountID`, with or without wildcard characters if the `PrincipalType` is an `IAM_PATTERN`.
For more information, review [associate-principal-with-portfolio](https://docs.aws.amazon.com/cli/latest/reference/servicecatalog/associate-principal-with-portfolio.html#options) in the AWS CLI Command Reference.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** PrincipalType **   <a name="servicecatalog-Type-Principal-PrincipalType"></a>
The principal type. The supported value is `IAM` if you use a fully defined ARN, or `IAM_PATTERN` if you use an ARN with no `accountID`, with or without wildcard characters.
Type: String
Valid Values: `IAM | IAM_PATTERN`
Required: No

## See Also
<a name="API_Principal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/Principal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/Principal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/Principal)
