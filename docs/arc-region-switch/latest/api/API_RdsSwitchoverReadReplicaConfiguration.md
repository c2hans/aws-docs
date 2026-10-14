---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_RdsSwitchoverReadReplicaConfiguration.html
---

# RdsSwitchoverReadReplicaConfiguration
<a name="API_RdsSwitchoverReadReplicaConfiguration"></a>

Configuration for switching over an Amazon RDS read replica to become the new primary database instance during a Region switch.

## Contents
<a name="API_RdsSwitchoverReadReplicaConfiguration_Contents"></a>

 ** dbInstanceArnMap **   <a name="regionswitch-Type-RdsSwitchoverReadReplicaConfiguration-dbInstanceArnMap"></a>
A map of database instance ARNs for each Region in the plan.
Type: String to string map
Key Pattern: `[a-z]{2}-[a-z-]+-\d+`
Value Pattern: `arn:aws[a-zA-Z-]*:rds:[a-z0-9-]+:\d{12}:db:[a-zA-Z][a-zA-Z0-9]*(-[a-zA-Z0-9]+)*`
Required: Yes

 ** crossAccountRole **   <a name="regionswitch-Type-RdsSwitchoverReadReplicaConfiguration-crossAccountRole"></a>
The cross-account role for the configuration.
Type: String
Pattern: `arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+`
Required: No

 ** externalId **   <a name="regionswitch-Type-RdsSwitchoverReadReplicaConfiguration-externalId"></a>
The external ID (secret key) for the configuration.
Type: String
Required: No

 ** timeoutMinutes **   <a name="regionswitch-Type-RdsSwitchoverReadReplicaConfiguration-timeoutMinutes"></a>
The timeout value specified for the configuration.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** ungraceful **   <a name="regionswitch-Type-RdsSwitchoverReadReplicaConfiguration-ungraceful"></a>
The ungraceful execution settings for the configuration.
Type: [RdsUngraceful](API_RdsUngraceful.md) object
Required: No

## See Also
<a name="API_RdsSwitchoverReadReplicaConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/RdsSwitchoverReadReplicaConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/RdsSwitchoverReadReplicaConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/RdsSwitchoverReadReplicaConfiguration)
