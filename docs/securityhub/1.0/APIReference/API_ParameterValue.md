---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ParameterValue.html
---

# ParameterValue
<a name="API_ParameterValue"></a>

 An object that includes the data type of a security control parameter and its current value.

## Contents
<a name="API_ParameterValue_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Boolean **   <a name="securityhub-Type-ParameterValue-Boolean"></a>
 A control parameter that is a boolean.
Type: Boolean
Required: No

 ** Double **   <a name="securityhub-Type-ParameterValue-Double"></a>
 A control parameter that is a double.
Type: Double
Required: No

 ** Enum **   <a name="securityhub-Type-ParameterValue-Enum"></a>
 A control parameter that is an enum.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EnumList **   <a name="securityhub-Type-ParameterValue-EnumList"></a>
 A control parameter that is a list of enums.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** Integer **   <a name="securityhub-Type-ParameterValue-Integer"></a>
 A control parameter that is an integer.
Type: Integer
Required: No

 ** IntegerList **   <a name="securityhub-Type-ParameterValue-IntegerList"></a>
 A control parameter that is a list of integers.
Type: Array of integers
Required: No

 ** String **   <a name="securityhub-Type-ParameterValue-String"></a>
 A control parameter that is a string.
Type: String
Pattern: `.*\S.*`
Required: No

 ** StringList **   <a name="securityhub-Type-ParameterValue-StringList"></a>
 A control parameter that is a list of strings.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_ParameterValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ParameterValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ParameterValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ParameterValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
