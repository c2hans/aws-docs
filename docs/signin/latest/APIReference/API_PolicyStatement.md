---
source_url: https://docs.aws.amazon.com/signin/latest/APIReference/API_PolicyStatement.html
---

# PolicyStatement
<a name="API_PolicyStatement"></a>

An individual statement within the AWS Sign-In resource-based policy.

## Contents
<a name="API_PolicyStatement_Contents"></a>

 ** action **   <a name="signin-Type-PolicyStatement-action"></a>
The actions the statement controls.
Type: Array of strings
Required: No

 ** condition **   <a name="signin-Type-PolicyStatement-condition"></a>
The condition block that scopes when the statement applies.
Type: String to string to array of strings map map
Required: No

 ** effect **   <a name="signin-Type-PolicyStatement-effect"></a>
The effect of the statement, either `Allow` or `Deny`.
Type: String
Required: No

 ** principal **   <a name="signin-Type-PolicyStatement-principal"></a>
The principal the statement applies to.
Type: String to string map
Required: No

 ** resource **   <a name="signin-Type-PolicyStatement-resource"></a>
The resource the statement applies to.
Type: String
Required: No

## See Also
<a name="API_PolicyStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signincontrolplane-2022-07-26/PolicyStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signincontrolplane-2022-07-26/PolicyStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signincontrolplane-2022-07-26/PolicyStatement)
