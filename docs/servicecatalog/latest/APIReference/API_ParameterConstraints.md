---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ParameterConstraints.html
---

# ParameterConstraints
<a name="API_ParameterConstraints"></a>

The constraints that the administrator has put on the parameter.

## Contents
<a name="API_ParameterConstraints_Contents"></a>

 ** AllowedPattern **   <a name="servicecatalog-Type-ParameterConstraints-AllowedPattern"></a>
A regular expression that represents the patterns that allow for `String` types. The pattern must match the entire parameter value provided.
Type: String
Required: No

 ** AllowedValues **   <a name="servicecatalog-Type-ParameterConstraints-AllowedValues"></a>
The values that the administrator has allowed for the parameter.
Type: Array of strings
Required: No

 ** ConstraintDescription **   <a name="servicecatalog-Type-ParameterConstraints-ConstraintDescription"></a>
A string that explains a constraint when the constraint is violated. For example, without a constraint description, a parameter that has an allowed pattern of `[A-Za-z0-9]+` displays the following error message when the user specifies an invalid value:
 `Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+`
By adding a constraint description, such as must only contain letters (uppercase and lowercase) and numbers, you can display the following customized error message:
 `Malformed input-Parameter MyParameter must only contain uppercase and lowercase letters and numbers.`
Type: String
Required: No

 ** MaxLength **   <a name="servicecatalog-Type-ParameterConstraints-MaxLength"></a>
An integer value that determines the largest number of characters you want to allow for `String` types.
Type: String
Required: No

 ** MaxValue **   <a name="servicecatalog-Type-ParameterConstraints-MaxValue"></a>
A numeric value that determines the largest numeric value you want to allow for `Number` types.
Type: String
Required: No

 ** MinLength **   <a name="servicecatalog-Type-ParameterConstraints-MinLength"></a>
An integer value that determines the smallest number of characters you want to allow for `String` types.
Type: String
Required: No

 ** MinValue **   <a name="servicecatalog-Type-ParameterConstraints-MinValue"></a>
A numeric value that determines the smallest numeric value you want to allow for `Number` types.
Type: String
Required: No

## See Also
<a name="API_ParameterConstraints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ParameterConstraints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ParameterConstraints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ParameterConstraints)
