---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iot-jobs-data_CommandParameterValue.html
---

# CommandParameterValue
<a name="API_iot-jobs-data_CommandParameterValue"></a>

The list of values used to describe a specific command parameter.

## Contents
<a name="API_iot-jobs-data_CommandParameterValue_Contents"></a>

 ** B **   <a name="iot-Type-iot-jobs-data_CommandParameterValue-B"></a>
An attribute of type Boolean. For example:
 `"BOOL": true`
Type: Boolean
Required: No

 ** BIN **   <a name="iot-Type-iot-jobs-data_CommandParameterValue-BIN"></a>
An attribute of type Binary.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1.
Required: No

 ** D **   <a name="iot-Type-iot-jobs-data_CommandParameterValue-D"></a>
An attribute of type Double (Sixty-Four Bits).
Type: Double
Required: No

 ** I **   <a name="iot-Type-iot-jobs-data_CommandParameterValue-I"></a>
An attribute of type Integer (Thirty-Two Bits).
Type: Integer
Required: No

 ** L **   <a name="iot-Type-iot-jobs-data_CommandParameterValue-L"></a>
An attribute of type Long.
Type: Long
Required: No

 ** S **   <a name="iot-Type-iot-jobs-data_CommandParameterValue-S"></a>
An attribute of type String. For example:
 `"S": "Hello"`
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** UL **   <a name="iot-Type-iot-jobs-data_CommandParameterValue-UL"></a>
An attribute of type Unsigned Long.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `^[0-9]*$`
Required: No

## See Also
<a name="API_iot-jobs-data_CommandParameterValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-jobs-data-2017-09-29/CommandParameterValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-jobs-data-2017-09-29/CommandParameterValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-jobs-data-2017-09-29/CommandParameterValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
