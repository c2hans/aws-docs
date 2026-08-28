---
source_url: https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_DataPoint.html
---

# DataPoint
<a name="API_DataPoint"></a>

A timestamp, and a single numerical value, which together represent a measurement at a particular point in time.

## Contents
<a name="API_DataPoint_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Timestamp **   <a name="performanceinsights-Type-DataPoint-Timestamp"></a>
The time, in epoch format, associated with a particular `Value`.
Type: Timestamp
Required: Yes

 ** Value **   <a name="performanceinsights-Type-DataPoint-Value"></a>
The actual value associated with a particular `Timestamp`.
Type: Double
Required: Yes

## See Also
<a name="API_DataPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pi-2018-02-27/DataPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pi-2018-02-27/DataPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pi-2018-02-27/DataPoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS Performance Insights. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query performance-insights` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
