---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeploymentSummary.html
---

# DeploymentSummary
<a name="API_DeploymentSummary"></a>

Information about the deployment.

## Contents
<a name="API_DeploymentSummary_Contents"></a>

 ** CompletedAt **   <a name="appconfig-Type-DeploymentSummary-CompletedAt"></a>
Time the deployment completed.
Type: Timestamp
Required: No

 ** ConfigurationName **   <a name="appconfig-Type-DeploymentSummary-ConfigurationName"></a>
The name of the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** ConfigurationProfileId **   <a name="appconfig-Type-DeploymentSummary-ConfigurationProfileId"></a>
The ID of the configuration profile that was deployed.
Type: String
Pattern: `[a-z0-9]{4,7}`
Required: No

 ** ConfigurationVersion **   <a name="appconfig-Type-DeploymentSummary-ConfigurationVersion"></a>
The version of the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** DeploymentDurationInMinutes **   <a name="appconfig-Type-DeploymentSummary-DeploymentDurationInMinutes"></a>
Total amount of time the deployment lasted.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1440.
Required: No

 ** DeploymentNumber **   <a name="appconfig-Type-DeploymentSummary-DeploymentNumber"></a>
The sequence number of the deployment.
Type: Integer
Required: No

 ** FinalBakeTimeInMinutes **   <a name="appconfig-Type-DeploymentSummary-FinalBakeTimeInMinutes"></a>
The amount of time that AWS AppConfig monitors for alarms before considering the deployment to be complete and no longer eligible for automatic rollback.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1440.
Required: No

 ** GrowthFactor **   <a name="appconfig-Type-DeploymentSummary-GrowthFactor"></a>
The percentage of targets to receive a deployed configuration during each interval.
Type: Float
Valid Range: Minimum value of 1.0. Maximum value of 100.0.
Required: No

 ** GrowthType **   <a name="appconfig-Type-DeploymentSummary-GrowthType"></a>
The algorithm used to define how percentage grows over time.
Type: String
Valid Values: `LINEAR | EXPONENTIAL`
Required: No

 ** PercentageComplete **   <a name="appconfig-Type-DeploymentSummary-PercentageComplete"></a>
The percentage of targets for which the deployment is available.
Type: Float
Valid Range: Minimum value of 1.0. Maximum value of 100.0.
Required: No

 ** StartedAt **   <a name="appconfig-Type-DeploymentSummary-StartedAt"></a>
Time the deployment started.
Type: Timestamp
Required: No

 ** State **   <a name="appconfig-Type-DeploymentSummary-State"></a>
The state of the deployment.
Type: String
Valid Values: `BAKING | VALIDATING | DEPLOYING | COMPLETE | ROLLING_BACK | ROLLED_BACK | REVERTED`
Required: No

 ** Type **   <a name="appconfig-Type-DeploymentSummary-Type"></a>
The type of deployment.
Type: String
Valid Values: `USER | MANAGED`
Required: No

 ** VersionLabel **   <a name="appconfig-Type-DeploymentSummary-VersionLabel"></a>
A user-defined label for an AWS AppConfig hosted configuration version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*[^0-9].*`
Required: No

## See Also
<a name="API_DeploymentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/DeploymentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/DeploymentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/DeploymentSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
