---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_Event.html
---

# Event
<a name="API_dax_Event"></a>

Represents a single occurrence of something interesting within the system. Some examples of events are creating a DAX cluster, adding or removing a node, or rebooting a node.

## Contents
<a name="API_dax_Event_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Date **   <a name="DDB-Type-dax_Event-Date"></a>
The date and time when the event occurred.
Type: Timestamp
Required: No

 ** Message **   <a name="DDB-Type-dax_Event-Message"></a>
A user-defined message associated with the event.
Type: String
Required: No

 ** SourceName **   <a name="DDB-Type-dax_Event-SourceName"></a>
The source of the event. For example, if the event occurred at the node level, the source would be the node ID.
Type: String
Required: No

 ** SourceType **   <a name="DDB-Type-dax_Event-SourceType"></a>
Specifies the origin of this event - a cluster, a parameter group, a node ID, etc.
Type: String
Valid Values: `CLUSTER | PARAMETER_GROUP | SUBNET_GROUP`
Required: No

## See Also
<a name="API_dax_Event_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dax-2017-04-19/Event)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dax-2017-04-19/Event)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dax-2017-04-19/Event)
