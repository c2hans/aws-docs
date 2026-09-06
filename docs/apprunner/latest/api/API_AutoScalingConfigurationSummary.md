---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_AutoScalingConfigurationSummary.html
---

# AutoScalingConfigurationSummary
<a name="API_AutoScalingConfigurationSummary"></a>

Provides summary information about an AWS App Runner automatic scaling configuration resource.

This type contains limited information about an auto scaling configuration. It includes only identification information, without configuration details. It's returned by the [ListAutoScalingConfigurations](API_ListAutoScalingConfigurations.md) action. Complete configuration information is returned by the [CreateAutoScalingConfiguration](API_CreateAutoScalingConfiguration.md), [DescribeAutoScalingConfiguration](API_DescribeAutoScalingConfiguration.md), and [DeleteAutoScalingConfiguration](API_DeleteAutoScalingConfiguration.md) actions using the [AutoScalingConfiguration](API_AutoScalingConfiguration.md) type.

## Contents
<a name="API_AutoScalingConfigurationSummary_Contents"></a>

 ** AutoScalingConfigurationArn **   <a name="apprunner-Type-AutoScalingConfigurationSummary-AutoScalingConfigurationArn"></a>
The Amazon Resource Name (ARN) of this auto scaling configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: No

 ** AutoScalingConfigurationName **   <a name="apprunner-Type-AutoScalingConfigurationSummary-AutoScalingConfigurationName"></a>
The customer-provided auto scaling configuration name. It can be used in multiple revisions of a configuration.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 32.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-_]{3,31}`
Required: No

 ** AutoScalingConfigurationRevision **   <a name="apprunner-Type-AutoScalingConfigurationSummary-AutoScalingConfigurationRevision"></a>
The revision of this auto scaling configuration. It's unique among all the active configurations (`"Status": "ACTIVE"`) with the same `AutoScalingConfigurationName`.
Type: Integer
Required: No

 ** CreatedAt **   <a name="apprunner-Type-AutoScalingConfigurationSummary-CreatedAt"></a>
The time when the auto scaling configuration was created. It's in Unix time stamp format.
Type: Timestamp
Required: No

 ** HasAssociatedService **   <a name="apprunner-Type-AutoScalingConfigurationSummary-HasAssociatedService"></a>
Indicates if this auto scaling configuration has an App Runner service associated with it. A value of `true` indicates one or more services are associated. A value of `false` indicates no services are associated.
Type: Boolean
Required: No

 ** IsDefault **   <a name="apprunner-Type-AutoScalingConfigurationSummary-IsDefault"></a>
Indicates if this auto scaling configuration should be used as the default for a new App Runner service that does not have an auto scaling configuration ARN specified during creation. Each account can have only one default `AutoScalingConfiguration` per region. The default `AutoScalingConfiguration` can be any revision under the same `AutoScalingConfigurationName`.
Type: Boolean
Required: No

 ** Status **   <a name="apprunner-Type-AutoScalingConfigurationSummary-Status"></a>
The current state of the auto scaling configuration. If the status of a configuration revision is `INACTIVE`, it was deleted and can't be used. Inactive configuration revisions are permanently removed some time after they are deleted.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

## See Also
<a name="API_AutoScalingConfigurationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/AutoScalingConfigurationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/AutoScalingConfigurationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/AutoScalingConfigurationSummary)
