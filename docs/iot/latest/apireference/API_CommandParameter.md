---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CommandParameter.html
---

# CommandParameter
<a name="API_CommandParameter"></a>

A map of key-value pairs that describe the command.

## Contents
<a name="API_CommandParameter_Contents"></a>

 ** name **   <a name="iot-Type-CommandParameter-name"></a>
The name of a specific parameter used in a command and command execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 192.
Pattern: `^[.$a-zA-Z0-9_-]+$`
Required: Yes

 ** defaultValue **   <a name="iot-Type-CommandParameter-defaultValue"></a>
The default value used to describe the command. This is the value assumed by the parameter if no other value is assigned to it.
Type: [CommandParameterValue](API_CommandParameterValue.md) object
Required: No

 ** description **   <a name="iot-Type-CommandParameter-description"></a>
The description of the command parameter.
Type: String
Length Constraints: Maximum length of 2028.
Pattern: `[^\p{C}]*`
Required: No

 ** type **   <a name="iot-Type-CommandParameter-type"></a>
The type of the command parameter.
Type: String
Valid Values: `STRING | INTEGER | DOUBLE | LONG | UNSIGNEDLONG | BOOLEAN | BINARY`
Required: No

 ** value **   <a name="iot-Type-CommandParameter-value"></a>
Parameter value that overrides the default value, if set.
Type: [CommandParameterValue](API_CommandParameterValue.md) object
Required: No

 ** valueConditions **   <a name="iot-Type-CommandParameter-valueConditions"></a>
The list of conditions that a command parameter value must satisfy to create a command execution.
Type: Array of [CommandParameterValueCondition](API_CommandParameterValueCondition.md) objects
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_CommandParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CommandParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CommandParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CommandParameter)
