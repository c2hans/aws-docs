---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Validation.html
---

# Validation
<a name="API_Validation"></a>

Defines validation rules for data table attribute values. Based on JSON Schema Draft 2020-12 with additional Connect-specific validations. Validation rules ensure data integrity and consistency across the data table.

## Contents
<a name="API_Validation_Contents"></a>

 ** Enum **   <a name="connect-Type-Validation-Enum"></a>
Defines enumeration constraints for attribute values. Can specify a list of allowed values and whether custom values are permitted beyond the enumerated list.
Type: [ValidationEnum](API_ValidationEnum.md) object
Required: No

 ** ExclusiveMaximum **   <a name="connect-Type-Validation-ExclusiveMaximum"></a>
The largest exclusive numeric value for NUMBER value type. Can be provided alongside Maximum where both operate independently. Must be greater than ExclusiveMinimum and Minimum. Applies to NUMBER and values within NUMBER\_LIST.
Type: Double
Required: No

 ** ExclusiveMinimum **   <a name="connect-Type-Validation-ExclusiveMinimum"></a>
The smallest exclusive numeric value for NUMBER value type. Can be provided alongside Minimum where both operate independently. Must be less than ExclusiveMaximum and Maximum. Applies to NUMBER and values within NUMBER\_LIST.
Type: Double
Required: No

 ** IgnoreCase **   <a name="connect-Type-Validation-IgnoreCase"></a>
Boolean that defaults to false. Applies to text lists and text primary attributes. When true, enforces case-insensitive uniqueness for primary attributes and allows case-insensitive lookups.
Type: Boolean
Required: No

 ** Maximum **   <a name="connect-Type-Validation-Maximum"></a>
The largest inclusive numeric value for NUMBER value type. Can be provided alongside ExclusiveMaximum where both operate independently. Must be greater than or equal to Minimum and greater than ExclusiveMinimum. Applies to NUMBER and values within NUMBER\_LIST.
Type: Double
Required: No

 ** MaxLength **   <a name="connect-Type-Validation-MaxLength"></a>
The maximum number of characters a text value can contain. Applies to TEXT value type and values within a TEXT\_LIST. Must be greater than or equal to MinLength.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** MaxValues **   <a name="connect-Type-Validation-MaxValues"></a>
The maximum number of values in a list. Must be an integer greater than or equal to 0 and greater than or equal to MinValues. Applies to all list types.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** Minimum **   <a name="connect-Type-Validation-Minimum"></a>
The smallest inclusive numeric value for NUMBER value type. Cannot be provided when ExclusiveMinimum is also provided. Must be less than or equal to Maximum and less than ExclusiveMaximum. Applies to NUMBER and values within NUMBER\_LIST.
Type: Double
Required: No

 ** MinLength **   <a name="connect-Type-Validation-MinLength"></a>
The minimum number of characters a text value can contain. Applies to TEXT value type and values within a TEXT\_LIST. Must be less than or equal to MaxLength.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** MinValues **   <a name="connect-Type-Validation-MinValues"></a>
The minimum number of values in a list. Must be an integer greater than or equal to 0 and less than or equal to MaxValues. Applies to all list types.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** MultipleOf **   <a name="connect-Type-Validation-MultipleOf"></a>
Specifies that numeric values must be multiples of this number. Must be greater than 0. The result of dividing a value by this multiple must result in an integer. Applies to NUMBER and values within NUMBER\_LIST.
Type: Double
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_Validation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/Validation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/Validation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/Validation)
