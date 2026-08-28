---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_AutoScalingConfiguration.html
---

# AutoScalingConfiguration
<a name="API_AutoScalingConfiguration"></a>

Describes an AWS App Runner automatic scaling configuration resource.

A higher `MinSize` increases the spread of your App Runner service over more Availability Zones in the AWS Region. The tradeoff is a higher minimal cost.

A lower `MaxSize` controls your cost. The tradeoff is lower responsiveness during peak demand.

Multiple revisions of a configuration might have the same `AutoScalingConfigurationName` and different `AutoScalingConfigurationRevision` values.

## Contents
<a name="API_AutoScalingConfiguration_Contents"></a>

 ** AutoScalingConfigurationArn **   <a name="apprunner-Type-AutoScalingConfiguration-AutoScalingConfigurationArn"></a>
The Amazon Resource Name (ARN) of this auto scaling configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: No

 ** AutoScalingConfigurationName **   <a name="apprunner-Type-AutoScalingConfiguration-AutoScalingConfigurationName"></a>
The customer-provided auto scaling configuration name. It can be used in multiple revisions of a configuration.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 32.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-_]{3,31}`
Required: No

 ** AutoScalingConfigurationRevision **   <a name="apprunner-Type-AutoScalingConfiguration-AutoScalingConfigurationRevision"></a>
The revision of this auto scaling configuration. It's unique among all the active configurations (`"Status": "ACTIVE"`) that share the same `AutoScalingConfigurationName`.
Type: Integer
Required: No

 ** CreatedAt **   <a name="apprunner-Type-AutoScalingConfiguration-CreatedAt"></a>
The time when the auto scaling configuration was created. It's in Unix time stamp format.
Type: Timestamp
Required: No

 ** DeletedAt **   <a name="apprunner-Type-AutoScalingConfiguration-DeletedAt"></a>
The time when the auto scaling configuration was deleted. It's in Unix time stamp format.
Type: Timestamp
Required: No

 ** HasAssociatedService **   <a name="apprunner-Type-AutoScalingConfiguration-HasAssociatedService"></a>
Indicates if this auto scaling configuration has an App Runner service associated with it. A value of `true` indicates one or more services are associated. A value of `false` indicates no services are associated.
Type: Boolean
Required: No

 ** IsDefault **   <a name="apprunner-Type-AutoScalingConfiguration-IsDefault"></a>
Indicates if this auto scaling configuration should be used as the default for a new App Runner service that does not have an auto scaling configuration ARN specified during creation. Each account can have only one default `AutoScalingConfiguration` per region. The default `AutoScalingConfiguration` can be any revision under the same `AutoScalingConfigurationName`.
Type: Boolean
Required: No

 ** Latest **   <a name="apprunner-Type-AutoScalingConfiguration-Latest"></a>
It's set to `true` for the configuration with the highest `Revision` among all configurations that share the same `AutoScalingConfigurationName`. It's set to `false` otherwise.
Type: Boolean
Required: No

 ** MaxConcurrency **   <a name="apprunner-Type-AutoScalingConfiguration-MaxConcurrency"></a>
The maximum number of concurrent requests that an instance processes. If the number of concurrent requests exceeds this limit, App Runner scales the service up.
Type: Integer
Required: No

 ** MaxSize **   <a name="apprunner-Type-AutoScalingConfiguration-MaxSize"></a>
The maximum number of instances that a service scales up to. At most `MaxSize` instances actively serve traffic for your service.
Type: Integer
Required: No

 ** MinSize **   <a name="apprunner-Type-AutoScalingConfiguration-MinSize"></a>
The minimum number of instances that App Runner provisions for a service. The service always has at least `MinSize` provisioned instances. Some of them actively serve traffic. The rest of them (provisioned and inactive instances) are a cost-effective compute capacity reserve and are ready to be quickly activated. You pay for memory usage of all the provisioned instances. You pay for CPU usage of only the active subset.
App Runner temporarily doubles the number of provisioned instances during deployments, to maintain the same capacity for both old and new code.
Type: Integer
Required: No

 ** Status **   <a name="apprunner-Type-AutoScalingConfiguration-Status"></a>
The current state of the auto scaling configuration. If the status of a configuration revision is `INACTIVE`, it was deleted and can't be used. Inactive configuration revisions are permanently removed some time after they are deleted.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

## See Also
<a name="API_AutoScalingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/AutoScalingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/AutoScalingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/AutoScalingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Runner. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apprunner` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
