---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_RdsPromoteReadReplicaConfiguration.html
---

# RdsPromoteReadReplicaConfiguration
<a name="API_RdsPromoteReadReplicaConfiguration"></a>

Configuration for promoting an Amazon RDS read replica to a standalone database instance during a Region switch.

## Contents
<a name="API_RdsPromoteReadReplicaConfiguration_Contents"></a>

 ** dbInstanceArnMap **   <a name="regionswitch-Type-RdsPromoteReadReplicaConfiguration-dbInstanceArnMap"></a>
A map of database instance ARNs for each Region in the plan.
Type: String to string map
Key Pattern: `[a-z]{2}-[a-z-]+-\d+`
Value Pattern: `arn:aws[a-zA-Z-]*:rds:[a-z0-9-]+:\d{12}:db:[a-zA-Z][a-zA-Z0-9]*(-[a-zA-Z0-9]+)*`
Required: Yes

 ** crossAccountRole **   <a name="regionswitch-Type-RdsPromoteReadReplicaConfiguration-crossAccountRole"></a>
The cross-account role for the configuration.
Type: String
Pattern: `arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+`
Required: No

 ** externalId **   <a name="regionswitch-Type-RdsPromoteReadReplicaConfiguration-externalId"></a>
The external ID (secret key) for the configuration.
Type: String
Required: No

 ** timeoutMinutes **   <a name="regionswitch-Type-RdsPromoteReadReplicaConfiguration-timeoutMinutes"></a>
The timeout value specified for the configuration.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_RdsPromoteReadReplicaConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/RdsPromoteReadReplicaConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/RdsPromoteReadReplicaConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/RdsPromoteReadReplicaConfiguration)
