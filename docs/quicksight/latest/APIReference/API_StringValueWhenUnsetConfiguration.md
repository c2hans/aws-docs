---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_StringValueWhenUnsetConfiguration.html
---

# StringValueWhenUnsetConfiguration
<a name="API_StringValueWhenUnsetConfiguration"></a>

The configuration that defines the default value of a `String` parameter when a value has not been set.

## Contents
<a name="API_StringValueWhenUnsetConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CustomValue **   <a name="QS-Type-StringValueWhenUnsetConfiguration-CustomValue"></a>
A custom value that's used when the value of a parameter isn't set.
Type: String
Required: No

 ** ValueWhenUnsetOption **   <a name="QS-Type-StringValueWhenUnsetConfiguration-ValueWhenUnsetOption"></a>
The built-in options for default values. The value can be one of the following:
+  `RECOMMENDED`: The recommended value.
+  `NULL`: The `NULL` value.
Type: String
Valid Values: `RECOMMENDED_VALUE | NULL`
Required: No

## See Also
<a name="API_StringValueWhenUnsetConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/StringValueWhenUnsetConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/StringValueWhenUnsetConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/StringValueWhenUnsetConfiguration)
