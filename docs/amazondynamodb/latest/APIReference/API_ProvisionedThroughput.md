---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ProvisionedThroughput.html
---

# ProvisionedThroughput
<a name="API_ProvisionedThroughput"></a>

Represents the provisioned throughput settings for the specified global secondary index. You must use `ProvisionedThroughput` or `OnDemandThroughput` based on your table’s capacity mode.

For current minimum and maximum provisioned throughput values, see [Service, Account, and Table Quotas](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html) in the *Amazon DynamoDB Developer Guide*.

## Contents
<a name="API_ProvisionedThroughput_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ReadCapacityUnits **   <a name="DDB-Type-ProvisionedThroughput-ReadCapacityUnits"></a>
The maximum number of strongly consistent reads consumed per second before DynamoDB returns a `ThrottlingException`. For more information, see [Specifying Read and Write Requirements](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProvisionedThroughput.html) in the *Amazon DynamoDB Developer Guide*.
If read/write capacity mode is `PAY_PER_REQUEST` the value is set to 0.
Type: Long
Valid Range: Minimum value of 1.
Required: Yes

 ** WriteCapacityUnits **   <a name="DDB-Type-ProvisionedThroughput-WriteCapacityUnits"></a>
The maximum number of writes consumed per second before DynamoDB returns a `ThrottlingException`. For more information, see [Specifying Read and Write Requirements](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProvisionedThroughput.html) in the *Amazon DynamoDB Developer Guide*.
If read/write capacity mode is `PAY_PER_REQUEST` the value is set to 0.
Type: Long
Valid Range: Minimum value of 1.
Required: Yes

## See Also
<a name="API_ProvisionedThroughput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ProvisionedThroughput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ProvisionedThroughput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ProvisionedThroughput)
