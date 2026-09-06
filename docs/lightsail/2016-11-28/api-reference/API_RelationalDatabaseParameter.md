---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_RelationalDatabaseParameter.html
---

# RelationalDatabaseParameter
<a name="API_RelationalDatabaseParameter"></a>

Describes the parameters of a database.

## Contents
<a name="API_RelationalDatabaseParameter_Contents"></a>

 ** allowedValues **   <a name="Lightsail-Type-RelationalDatabaseParameter-allowedValues"></a>
Specifies the valid range of values for the parameter.
Type: String
Required: No

 ** applyMethod **   <a name="Lightsail-Type-RelationalDatabaseParameter-applyMethod"></a>
Indicates when parameter updates are applied.
Can be `immediate` or `pending-reboot`.
Type: String
Required: No

 ** applyType **   <a name="Lightsail-Type-RelationalDatabaseParameter-applyType"></a>
Specifies the engine-specific parameter type.
Type: String
Required: No

 ** dataType **   <a name="Lightsail-Type-RelationalDatabaseParameter-dataType"></a>
Specifies the valid data type for the parameter.
Type: String
Required: No

 ** description **   <a name="Lightsail-Type-RelationalDatabaseParameter-description"></a>
Provides a description of the parameter.
Type: String
Required: No

 ** isModifiable **   <a name="Lightsail-Type-RelationalDatabaseParameter-isModifiable"></a>
A Boolean value indicating whether the parameter can be modified.
Type: Boolean
Required: No

 ** parameterName **   <a name="Lightsail-Type-RelationalDatabaseParameter-parameterName"></a>
Specifies the name of the parameter.
Type: String
Required: No

 ** parameterValue **   <a name="Lightsail-Type-RelationalDatabaseParameter-parameterValue"></a>
Specifies the value of the parameter.
Type: String
Required: No

## See Also
<a name="API_RelationalDatabaseParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/RelationalDatabaseParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/RelationalDatabaseParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/RelationalDatabaseParameter)
