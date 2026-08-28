---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_PropertyValue.html
---

# PropertyValue
<a name="API_PropertyValue"></a>

An object that contains information about a value for a time series property.

## Contents
<a name="API_PropertyValue_Contents"></a>

 ** value **   <a name="tm-Type-PropertyValue-value"></a>
An object that specifies a value for a time series property.
Type: [DataValue](API_DataValue.md) object
Required: Yes

 ** time **   <a name="tm-Type-PropertyValue-time"></a>
ISO8601 DateTime of a value for a time series property.
The time for when the property value was recorded in ISO 8601 format: *YYYY-MM-DDThh:mm:ss[.SSSSSSSSS][Z/±HH:mm]*.
+  *[YYYY]*: year
+  *[MM]*: month
+  *[DD]*: day
+  *[hh]*: hour
+  *[mm]*: minute
+  *[ss]*: seconds
+  *[.SSSSSSSSS]*: additional precision, where precedence is maintained. For example: [.573123] is equal to 573123000 nanoseconds.
+  *Z*: default timezone UTC
+  *± HH:mm*: time zone offset in Hours and Minutes.
 *Required sub-fields*: YYYY-MM-DDThh:mm:ss and [Z/±HH:mm]
Type: String
Length Constraints: Minimum length of 20. Maximum length of 35.
Required: No

 ** timestamp **   <a name="tm-Type-PropertyValue-timestamp"></a>
 *This member has been deprecated.*
The timestamp of a value for a time series property.
Type: Timestamp
Required: No

## See Also
<a name="API_PropertyValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/PropertyValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/PropertyValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/PropertyValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
