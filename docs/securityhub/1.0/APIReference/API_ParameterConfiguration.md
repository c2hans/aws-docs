---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ParameterConfiguration.html
---

# ParameterConfiguration
<a name="API_ParameterConfiguration"></a>

 An object that provides the current value of a security control parameter and identifies whether it has been customized.

## Contents
<a name="API_ParameterConfiguration_Contents"></a>

 ** ValueType **   <a name="securityhub-Type-ParameterConfiguration-ValueType"></a>
 Identifies whether a control parameter uses a custom user-defined value or subscribes to the default AWS Security Hub CSPM behavior.
When `ValueType` is set equal to `DEFAULT`, the default behavior can be a specific Security Hub CSPM default value, or the default behavior can be to ignore a specific parameter. When `ValueType` is set equal to `DEFAULT`, Security Hub CSPM ignores user-provided input for the `Value` field.
When `ValueType` is set equal to `CUSTOM`, the `Value` field can't be empty.
Type: String
Valid Values: `DEFAULT | CUSTOM`
Required: Yes

 ** Value **   <a name="securityhub-Type-ParameterConfiguration-Value"></a>
 The current value of a control parameter.
Type: [ParameterValue](API_ParameterValue.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_ParameterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ParameterConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ParameterConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ParameterConfiguration)
