---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_PropertyType.html
---

# PropertyType
<a name="API_PropertyType"></a>

Contains a property type, which can be one of `attribute`, `measurement`, `metric`, or `transform`.

## Contents
<a name="API_PropertyType_Contents"></a>

 ** attribute **   <a name="iotsitewise-Type-PropertyType-attribute"></a>
Specifies an asset attribute property. An attribute generally contains static information, such as the serial number of an [IIoT](https://en.wikipedia.org/wiki/Internet_of_things#Industrial_applications) wind turbine.
Type: [Attribute](API_Attribute.md) object
Required: No

 ** measurement **   <a name="iotsitewise-Type-PropertyType-measurement"></a>
Specifies an asset measurement property. A measurement represents a device's raw sensor data stream, such as timestamped temperature values or timestamped power values.
Type: [Measurement](API_Measurement.md) object
Required: No

 ** metric **   <a name="iotsitewise-Type-PropertyType-metric"></a>
Specifies an asset metric property. A metric contains a mathematical expression that uses aggregate functions to process all input data points over a time interval and output a single data point, such as to calculate the average hourly temperature.
Type: [Metric](API_Metric.md) object
Required: No

 ** transform **   <a name="iotsitewise-Type-PropertyType-transform"></a>
Specifies an asset transform property. A transform contains a mathematical expression that maps a property's data points from one form to another, such as a unit conversion from Celsius to Fahrenheit.
Type: [Transform](API_Transform.md) object
Required: No

## See Also
<a name="API_PropertyType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/PropertyType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/PropertyType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/PropertyType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
