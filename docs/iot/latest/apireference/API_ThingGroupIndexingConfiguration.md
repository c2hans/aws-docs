---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ThingGroupIndexingConfiguration.html
---

# ThingGroupIndexingConfiguration
<a name="API_ThingGroupIndexingConfiguration"></a>

Thing group indexing configuration.

## Contents
<a name="API_ThingGroupIndexingConfiguration_Contents"></a>

 ** thingGroupIndexingMode **   <a name="iot-Type-ThingGroupIndexingConfiguration-thingGroupIndexingMode"></a>
Thing group indexing mode.
Type: String
Valid Values: `OFF | ON`
Required: Yes

 ** customFields **   <a name="iot-Type-ThingGroupIndexingConfiguration-customFields"></a>
A list of thing group fields to index. This list cannot contain any managed fields. Use the GetIndexingConfiguration API to get a list of managed fields.
Contains custom field names and their data type.
Type: Array of [Field](API_Field.md) objects
Required: No

 ** managedFields **   <a name="iot-Type-ThingGroupIndexingConfiguration-managedFields"></a>
Contains fields that are indexed and whose types are already known by the Fleet Indexing service. This is an optional field. For more information, see [Managed fields](https://docs.aws.amazon.com/iot/latest/developerguide/managing-fleet-index.html#managed-field) in the * AWS IoT Core Developer Guide*.
You can't modify managed fields by updating fleet indexing configuration.
Type: Array of [Field](API_Field.md) objects
Required: No

## See Also
<a name="API_ThingGroupIndexingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ThingGroupIndexingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ThingGroupIndexingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ThingGroupIndexingConfiguration)
