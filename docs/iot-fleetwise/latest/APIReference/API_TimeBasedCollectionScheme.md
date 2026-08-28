---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_TimeBasedCollectionScheme.html
---

# TimeBasedCollectionScheme
<a name="API_TimeBasedCollectionScheme"></a>

Information about a collection scheme that uses a time period to decide how often to collect data.

## Contents
<a name="API_TimeBasedCollectionScheme_Contents"></a>

 ** periodMs **   <a name="iotfleetwise-Type-TimeBasedCollectionScheme-periodMs"></a>
The time period (in milliseconds) to decide how often to collect data. For example, if the time period is `60000`, the Edge Agent software collects data once every minute.
Type: Long
Valid Range: Minimum value of 10000. Maximum value of 86400000.
Required: Yes

## See Also
<a name="API_TimeBasedCollectionScheme_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/TimeBasedCollectionScheme)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/TimeBasedCollectionScheme)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/TimeBasedCollectionScheme)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT FleetWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-fleetwise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
