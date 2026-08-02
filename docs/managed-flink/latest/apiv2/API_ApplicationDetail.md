---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ApplicationDetail.html
---

# ApplicationDetail
<a name="API_ApplicationDetail"></a>

Describes the application, including the application Amazon Resource Name (ARN), status, latest version, and input and output configurations.

## Contents
<a name="API_ApplicationDetail_Contents"></a>

 ** ApplicationARN **   <a name="APIReference-Type-ApplicationDetail-ApplicationARN"></a>
The ARN of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

 ** ApplicationName **   <a name="APIReference-Type-ApplicationDetail-ApplicationName"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** ApplicationStatus **   <a name="APIReference-Type-ApplicationDetail-ApplicationStatus"></a>
The status of the application.
Type: String
Valid Values: `DELETING | STARTING | STOPPING | READY | RUNNING | UPDATING | AUTOSCALING | FORCE_STOPPING | ROLLING_BACK | MAINTENANCE | ROLLED_BACK`
Required: Yes

 ** ApplicationVersionId **   <a name="APIReference-Type-ApplicationDetail-ApplicationVersionId"></a>
Provides the current application version. Managed Service for Apache Flink updates the `ApplicationVersionId` each time you update the application.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.
Required: Yes

 ** RuntimeEnvironment **   <a name="APIReference-Type-ApplicationDetail-RuntimeEnvironment"></a>
The runtime environment for the application.
Type: String
Valid Values: `SQL-1_0 | FLINK-1_6 | FLINK-1_8 | ZEPPELIN-FLINK-1_0 | FLINK-1_11 | FLINK-1_13 | ZEPPELIN-FLINK-2_0 | FLINK-1_15 | ZEPPELIN-FLINK-3_0 | FLINK-1_18 | FLINK-1_19 | FLINK-1_20`
Required: Yes

 ** ApplicationConfigurationDescription **   <a name="APIReference-Type-ApplicationDetail-ApplicationConfigurationDescription"></a>
Describes details about the application code and starting parameters for a Managed Service for Apache Flink application.
Type: [ApplicationConfigurationDescription](API_ApplicationConfigurationDescription.md) object
Required: No

 ** ApplicationDescription **   <a name="APIReference-Type-ApplicationDetail-ApplicationDescription"></a>
The description of the application.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** ApplicationMaintenanceConfigurationDescription **   <a name="APIReference-Type-ApplicationDetail-ApplicationMaintenanceConfigurationDescription"></a>
The details of the maintenance configuration for the application.
Type: [ApplicationMaintenanceConfigurationDescription](API_ApplicationMaintenanceConfigurationDescription.md) object
Required: No

 ** ApplicationMode **   <a name="APIReference-Type-ApplicationDetail-ApplicationMode"></a>
To create a Managed Service for Apache Flink Studio notebook, you must set the mode to `INTERACTIVE`. However, for a Managed Service for Apache Flink application, the mode is optional.
Type: String
Valid Values: `STREAMING | INTERACTIVE`
Required: No

 ** ApplicationVersionCreateTimestamp **   <a name="APIReference-Type-ApplicationDetail-ApplicationVersionCreateTimestamp"></a>
The timestamp that indicates when the application version was created.
Type: Timestamp
Required: No

 ** ApplicationVersionRolledBackFrom **   <a name="APIReference-Type-ApplicationDetail-ApplicationVersionRolledBackFrom"></a>
If you reverted the application using [RollbackApplication](API_RollbackApplication.md), the application version when `RollbackApplication` was called.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.
Required: No

 ** ApplicationVersionRolledBackTo **   <a name="APIReference-Type-ApplicationDetail-ApplicationVersionRolledBackTo"></a>
The version to which you want to roll back the application.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.
Required: No

 ** ApplicationVersionUpdatedFrom **   <a name="APIReference-Type-ApplicationDetail-ApplicationVersionUpdatedFrom"></a>
The previous application version before the latest application update. [RollbackApplication](API_RollbackApplication.md) reverts the application to this version.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.
Required: No

 ** CloudWatchLoggingOptionDescriptions **   <a name="APIReference-Type-ApplicationDetail-CloudWatchLoggingOptionDescriptions"></a>
Describes the application Amazon CloudWatch logging options.
Type: Array of [CloudWatchLoggingOptionDescription](API_CloudWatchLoggingOptionDescription.md) objects
Required: No

 ** ConditionalToken **   <a name="APIReference-Type-ApplicationDetail-ConditionalToken"></a>
A value you use to implement strong concurrency for application updates.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9-_+/=]+`
Required: No

 ** CreateTimestamp **   <a name="APIReference-Type-ApplicationDetail-CreateTimestamp"></a>
The current timestamp when the application was created.
Type: Timestamp
Required: No

 ** LastUpdateTimestamp **   <a name="APIReference-Type-ApplicationDetail-LastUpdateTimestamp"></a>
The current timestamp when the application was last updated.
Type: Timestamp
Required: No

 ** ServiceExecutionRole **   <a name="APIReference-Type-ApplicationDetail-ServiceExecutionRole"></a>
Specifies the IAM role that the application uses to access external resources.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: No

## See Also
<a name="API_ApplicationDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ApplicationDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ApplicationDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ApplicationDetail)
