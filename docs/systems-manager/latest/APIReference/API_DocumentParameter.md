---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DocumentParameter.html
---

# DocumentParameter
<a name="API_DocumentParameter"></a>

Parameters specified in a Systems Manager document that run on the server when the command is run.

## Contents
<a name="API_DocumentParameter_Contents"></a>

 ** DefaultValue **   <a name="systemsmanager-Type-DocumentParameter-DefaultValue"></a>
If specified, the default values for the parameters. Parameters without a default value are required. Parameters with a default value are optional.
Type: String
Required: No

 ** Description **   <a name="systemsmanager-Type-DocumentParameter-Description"></a>
A description of what the parameter does, how to use it, the default value, and whether or not the parameter is optional.
Type: String
Required: No

 ** Name **   <a name="systemsmanager-Type-DocumentParameter-Name"></a>
The name of the parameter.
Type: String
Required: No

 ** Type **   <a name="systemsmanager-Type-DocumentParameter-Type"></a>
The type of parameter. The type can be either String or StringList.
Type: String
Valid Values: `String | StringList`
Required: No

## See Also
<a name="API_DocumentParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DocumentParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DocumentParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DocumentParameter)
