---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_TargetHealth.html
---

# TargetHealth
<a name="API_TargetHealth"></a>

Information about the connection health of an RDS Proxy target.

## Contents
<a name="API_TargetHealth_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Description **
A description of the health of the RDS Proxy target. If the `State` is `AVAILABLE`, a description is not included.
Type: String
Required: No

 ** Reason **
The reason for the current health `State` of the RDS Proxy target.
Type: String
Valid Values: `UNREACHABLE | CONNECTION_FAILED | AUTH_FAILURE | PENDING_PROXY_CAPACITY | INVALID_REPLICATION_STATE | PROMOTED`
Required: No

 ** State **
The current state of the connection health lifecycle for the RDS Proxy target. The following is a typical lifecycle example for the states of an RDS Proxy target:
 `registering` > `unavailable` > `available` > `unavailable` > `available`
Type: String
Valid Values: `REGISTERING | AVAILABLE | UNAVAILABLE | UNUSED`
Required: No

## See Also
<a name="API_TargetHealth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/TargetHealth)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/TargetHealth)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/TargetHealth)
