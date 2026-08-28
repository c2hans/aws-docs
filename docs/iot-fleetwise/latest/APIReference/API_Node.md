---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_Node.html
---

# Node
<a name="API_Node"></a>

A general abstraction of a signal. A node can be specified as an actuator, attribute, branch, or sensor.

## Contents
<a name="API_Node_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** actuator **   <a name="iotfleetwise-Type-Node-actuator"></a>
Information about a node specified as an actuator.
An actuator is a digital representation of a vehicle device.
Type: [Actuator](API_Actuator.md) object
Required: No

 ** attribute **   <a name="iotfleetwise-Type-Node-attribute"></a>
Information about a node specified as an attribute.
An attribute represents static information about a vehicle.
Type: [Attribute](API_Attribute.md) object
Required: No

 ** branch **   <a name="iotfleetwise-Type-Node-branch"></a>
Information about a node specified as a branch.
A group of signals that are defined in a hierarchical structure.
Type: [Branch](API_Branch.md) object
Required: No

 ** property **   <a name="iotfleetwise-Type-Node-property"></a>
Represents a member of the complex data structure. The `datatype` of the property can be either primitive or another `struct`.
Type: [CustomProperty](API_CustomProperty.md) object
Required: No

 ** sensor **   <a name="iotfleetwise-Type-Node-sensor"></a>
An input component that reports the environmental condition of a vehicle.
You can collect data about fluid levels, temperatures, vibrations, or battery voltage from sensors.
Type: [Sensor](API_Sensor.md) object
Required: No

 ** struct **   <a name="iotfleetwise-Type-Node-struct"></a>
Represents a complex or higher-order data structure.
Type: [CustomStruct](API_CustomStruct.md) object
Required: No

## See Also
<a name="API_Node_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/Node)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/Node)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/Node)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT FleetWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-fleetwise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
