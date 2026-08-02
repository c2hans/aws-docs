---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_ExadataIormConfig.html
---

# ExadataIormConfig
<a name="API_ExadataIormConfig"></a>

The IORM settings of the Exadata DB system.

## Contents
<a name="API_ExadataIormConfig_Contents"></a>

 ** dbPlans **   <a name="odb-Type-ExadataIormConfig-dbPlans"></a>
An array of IORM settings for all the database in the Exadata DB system.
Type: Array of [DbIormConfig](API_DbIormConfig.md) objects
Required: No

 ** lifecycleDetails **   <a name="odb-Type-ExadataIormConfig-lifecycleDetails"></a>
Additional information about the current lifecycleState.
Type: String
Required: No

 ** lifecycleState **   <a name="odb-Type-ExadataIormConfig-lifecycleState"></a>
The current state of IORM configuration for the Exadata DB system.
Type: String
Valid Values: `BOOTSTRAPPING | DISABLED | ENABLED | FAILED | UPDATING`
Required: No

 ** objective **   <a name="odb-Type-ExadataIormConfig-objective"></a>
The current value for the IORM objective. The default is AUTO.
Type: String
Valid Values: `AUTO | BALANCED | BASIC | HIGH_THROUGHPUT | LOW_LATENCY`
Required: No

## See Also
<a name="API_ExadataIormConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/ExadataIormConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/ExadataIormConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/ExadataIormConfig)
