---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_TimestreamTimestamp.html
---

# TimestreamTimestamp
<a name="API_TimestreamTimestamp"></a>

Describes how to interpret an application-defined timestamp value from an MQTT message payload and the precision of that value.

## Contents
<a name="API_TimestreamTimestamp_Contents"></a>

 ** unit **   <a name="iot-Type-TimestreamTimestamp-unit"></a>
The precision of the timestamp value that results from the expression described in `value`.
Valid values: `SECONDS` \| `MILLISECONDS` \| `MICROSECONDS` \| `NANOSECONDS`. The default is `MILLISECONDS`.
Type: String
Required: Yes

 ** value **   <a name="iot-Type-TimestreamTimestamp-value"></a>
An expression that returns a long epoch time value.
Type: String
Required: Yes

## See Also
<a name="API_TimestreamTimestamp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/TimestreamTimestamp)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/TimestreamTimestamp)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/TimestreamTimestamp)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
