---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_Parameter.html
---

# Parameter
<a name="API_Parameter"></a>

A value such as an Amazon Resource Name (ARN) or an Amazon Simple Notification Service topic entered in an extension when invoked. Parameter values are specified in an extension association. For more information about extensions, see [Extending workflows](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html) in the * AWS AppConfig User Guide*.

## Contents
<a name="API_Parameter_Contents"></a>

 ** Description **   <a name="appconfig-Type-Parameter-Description"></a>
Information about the parameter.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** Dynamic **   <a name="appconfig-Type-Parameter-Dynamic"></a>
Indicates whether this parameter's value can be supplied at the extension's action point instead of during extension association. Dynamic parameters can't be marked `Required`.
Type: Boolean
Required: No

 ** Required **   <a name="appconfig-Type-Parameter-Required"></a>
A parameter value must be specified in the extension association.
Type: Boolean
Required: No

## See Also
<a name="API_Parameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/Parameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/Parameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/Parameter)
