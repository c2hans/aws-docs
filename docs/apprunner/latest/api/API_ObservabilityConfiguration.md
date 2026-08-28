---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_ObservabilityConfiguration.html
---

# ObservabilityConfiguration
<a name="API_ObservabilityConfiguration"></a>

Describes an AWS App Runner observability configuration resource. Multiple revisions of a configuration have the same `ObservabilityConfigurationName` and different `ObservabilityConfigurationRevision` values.

The resource is designed to configure multiple features (currently one feature, tracing). This type contains optional members that describe the configuration of these features (currently one member, `TraceConfiguration`). If a feature member isn't specified, the feature isn't enabled.

## Contents
<a name="API_ObservabilityConfiguration_Contents"></a>

 ** CreatedAt **   <a name="apprunner-Type-ObservabilityConfiguration-CreatedAt"></a>
The time when the observability configuration was created. It's in Unix time stamp format.
Type: Timestamp
Required: No

 ** DeletedAt **   <a name="apprunner-Type-ObservabilityConfiguration-DeletedAt"></a>
The time when the observability configuration was deleted. It's in Unix time stamp format.
Type: Timestamp
Required: No

 ** Latest **   <a name="apprunner-Type-ObservabilityConfiguration-Latest"></a>
It's set to `true` for the configuration with the highest `Revision` among all configurations that share the same `ObservabilityConfigurationName`. It's set to `false` otherwise.
Type: Boolean
Required: No

 ** ObservabilityConfigurationArn **   <a name="apprunner-Type-ObservabilityConfiguration-ObservabilityConfigurationArn"></a>
The Amazon Resource Name (ARN) of this observability configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: No

 ** ObservabilityConfigurationName **   <a name="apprunner-Type-ObservabilityConfiguration-ObservabilityConfigurationName"></a>
The customer-provided observability configuration name. It can be used in multiple revisions of a configuration.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 32.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-_]{3,31}`
Required: No

 ** ObservabilityConfigurationRevision **   <a name="apprunner-Type-ObservabilityConfiguration-ObservabilityConfigurationRevision"></a>
The revision of this observability configuration. It's unique among all the active configurations (`"Status": "ACTIVE"`) that share the same `ObservabilityConfigurationName`.
Type: Integer
Required: No

 ** Status **   <a name="apprunner-Type-ObservabilityConfiguration-Status"></a>
The current state of the observability configuration. If the status of a configuration revision is `INACTIVE`, it was deleted and can't be used. Inactive configuration revisions are permanently removed some time after they are deleted.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

 ** TraceConfiguration **   <a name="apprunner-Type-ObservabilityConfiguration-TraceConfiguration"></a>
The configuration of the tracing feature within this observability configuration. If not specified, tracing isn't enabled.
Type: [TraceConfiguration](API_TraceConfiguration.md) object
Required: No

## See Also
<a name="API_ObservabilityConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/ObservabilityConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/ObservabilityConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/ObservabilityConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Runner. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apprunner` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
