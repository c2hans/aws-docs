---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_CapacitySpecification.html
---

# CapacitySpecification
<a name="API_CapacitySpecification"></a>

Amazon Keyspaces has two read/write capacity modes for processing reads and writes on your tables:
+ On-demand (default)
+ Provisioned

The read/write capacity mode that you choose controls how you are charged for read and write throughput and how table throughput capacity is managed.

For more information, see [Read/write capacity modes](https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.html) in the *Amazon Keyspaces Developer Guide*.

## Contents
<a name="API_CapacitySpecification_Contents"></a>

 ** throughputMode **   <a name="keyspaces-Type-CapacitySpecification-throughputMode"></a>
The read/write throughput capacity mode for a table. The options are:
+  `throughputMode:PAY_PER_REQUEST` and
+  `throughputMode:PROVISIONED` - Provisioned capacity mode requires `readCapacityUnits` and `writeCapacityUnits` as input.
The default is `throughput_mode:PAY_PER_REQUEST`.
For more information, see [Read/write capacity modes](https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.html) in the *Amazon Keyspaces Developer Guide*.
Type: String
Valid Values: `PAY_PER_REQUEST | PROVISIONED`
Required: Yes

 ** readCapacityUnits **   <a name="keyspaces-Type-CapacitySpecification-readCapacityUnits"></a>
The throughput capacity specified for `read` operations defined in `read capacity units` `(RCUs)`.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** writeCapacityUnits **   <a name="keyspaces-Type-CapacitySpecification-writeCapacityUnits"></a>
The throughput capacity specified for `write` operations defined in `write capacity units` `(WCUs)`.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_CapacitySpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/CapacitySpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/CapacitySpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/CapacitySpecification)
