---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeploymentStrategy.html
---

# DeploymentStrategy
<a name="API_DeploymentStrategy"></a>

## Contents
<a name="API_DeploymentStrategy_Contents"></a>

 ** DeploymentDurationInMinutes **   <a name="appconfig-Type-DeploymentStrategy-DeploymentDurationInMinutes"></a>
Total amount of time the deployment lasted.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1440.
Required: No

 ** Description **   <a name="appconfig-Type-DeploymentStrategy-Description"></a>
The description of the deployment strategy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** FinalBakeTimeInMinutes **   <a name="appconfig-Type-DeploymentStrategy-FinalBakeTimeInMinutes"></a>
The amount of time that AWS AppConfig monitored for alarms before considering the deployment to be complete and no longer eligible for automatic rollback.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1440.
Required: No

 ** GrowthFactor **   <a name="appconfig-Type-DeploymentStrategy-GrowthFactor"></a>
The percentage of targets that received a deployed configuration during each interval.
Type: Float
Valid Range: Minimum value of 1.0. Maximum value of 100.0.
Required: No

 ** GrowthType **   <a name="appconfig-Type-DeploymentStrategy-GrowthType"></a>
The algorithm used to define how percentage grew over time.
Type: String
Valid Values: `LINEAR | EXPONENTIAL`
Required: No

 ** Id **   <a name="appconfig-Type-DeploymentStrategy-Id"></a>
The deployment strategy ID.
Type: String
Pattern: `[a-z0-9]{4,7}`
Required: No

 ** Name **   <a name="appconfig-Type-DeploymentStrategy-Name"></a>
The name of the deployment strategy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** ReplicateTo **   <a name="appconfig-Type-DeploymentStrategy-ReplicateTo"></a>
Save the deployment strategy to a Systems Manager (SSM) document.
Type: String
Valid Values: `NONE | SSM_DOCUMENT`
Required: No

## See Also
<a name="API_DeploymentStrategy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/DeploymentStrategy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/DeploymentStrategy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/DeploymentStrategy)
