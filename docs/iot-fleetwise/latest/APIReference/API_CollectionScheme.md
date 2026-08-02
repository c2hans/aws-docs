---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CollectionScheme.html
---

# CollectionScheme
<a name="API_CollectionScheme"></a>

Specifies what data to collect and how often or when to collect it.

## Contents
<a name="API_CollectionScheme_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** conditionBasedCollectionScheme **   <a name="iotfleetwise-Type-CollectionScheme-conditionBasedCollectionScheme"></a>
Information about a collection scheme that uses a simple logical expression to recognize what data to collect.
Type: [ConditionBasedCollectionScheme](API_ConditionBasedCollectionScheme.md) object
Required: No

 ** timeBasedCollectionScheme **   <a name="iotfleetwise-Type-CollectionScheme-timeBasedCollectionScheme"></a>
Information about a collection scheme that uses a time period to decide how often to collect data.
Type: [TimeBasedCollectionScheme](API_TimeBasedCollectionScheme.md) object
Required: No

## See Also
<a name="API_CollectionScheme_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/CollectionScheme)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/CollectionScheme)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/CollectionScheme)
