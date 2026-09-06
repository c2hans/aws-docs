---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ValidationEnum.html
---

# ValidationEnum
<a name="API_ValidationEnum"></a>

Defines enumeration validation for attribute values. Allows specifying a list of permitted values and whether custom values beyond the enumerated list are allowed.

## Contents
<a name="API_ValidationEnum_Contents"></a>

 ** Strict **   <a name="connect-Type-ValidationEnum-Strict"></a>
Boolean that defaults to false. When true, only values specified in the enum list are allowed. When false, custom values beyond the enumerated list are permitted.
Type: Boolean
Required: No

 ** Values **   <a name="connect-Type-ValidationEnum-Values"></a>
A list of predefined values that are allowed for this attribute. These values are always permitted regardless of the Strict setting.
Type: Array of strings
Required: No

## See Also
<a name="API_ValidationEnum_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ValidationEnum)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ValidationEnum)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ValidationEnum)
