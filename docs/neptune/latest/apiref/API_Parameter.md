---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_Parameter.html
---

# Parameter
<a name="API_Parameter"></a>

Specifies a parameter.

## Contents
<a name="API_Parameter_Contents"></a>

 ** AllowedValues **
Specifies the valid range of values for the parameter.
Type: String
Required: No

 ** ApplyMethod **
Indicates when to apply parameter updates.
Type: String
Valid Values: `immediate | pending-reboot`
Required: No

 ** ApplyType **
Specifies the engine specific parameters type.
Type: String
Required: No

 ** DataType **
Specifies the valid data type for the parameter.
Type: String
Required: No

 ** Description **
Provides a description of the parameter.
Type: String
Required: No

 ** IsModifiable **
 Indicates whether (`true`) or not (`false`) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.
Type: Boolean
Required: No

 ** MinimumEngineVersion **
The earliest engine version to which the parameter can apply.
Type: String
Required: No

 ** ParameterName **
Specifies the name of the parameter.
Type: String
Required: No

 ** ParameterValue **
Specifies the value of the parameter.
Type: String
Required: No

 ** Source **
Indicates the source of the parameter value.
Type: String
Required: No

## See Also
<a name="API_Parameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/Parameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/Parameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/Parameter)
