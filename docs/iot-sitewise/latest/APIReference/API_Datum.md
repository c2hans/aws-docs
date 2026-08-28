---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_Datum.html
---

# Datum
<a name="API_Datum"></a>

Represents a single data point in a query result.

## Contents
<a name="API_Datum_Contents"></a>

 ** arrayValue **   <a name="iotsitewise-Type-Datum-arrayValue"></a>
Indicates if the data point is an array.
Type: Array of [Datum](#API_Datum) objects
Required: No

 ** nullValue **   <a name="iotsitewise-Type-Datum-nullValue"></a>
Indicates if the data point is null.
Type: Boolean
Required: No

 ** rowValue **   <a name="iotsitewise-Type-Datum-rowValue"></a>
Indicates if the data point is a row.
Type: [Row](API_Row.md) object
Required: No

 ** scalarValue **   <a name="iotsitewise-Type-Datum-scalarValue"></a>
Indicates if the data point is a scalar value such as integer, string, double, or Boolean.
Type: String
Required: No

## See Also
<a name="API_Datum_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/Datum)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/Datum)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/Datum)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
