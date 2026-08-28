---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_ApplicationInstance.html
---

# ApplicationInstance
<a name="API_ApplicationInstance"></a>

An application instance on a device.

## Contents
<a name="API_ApplicationInstance_Contents"></a>

 ** ApplicationInstanceId **   <a name="panorama-Type-ApplicationInstance-ApplicationInstanceId"></a>
The application instance's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: No

 ** Arn **   <a name="panorama-Type-ApplicationInstance-Arn"></a>
The application instance's ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** CreatedTime **   <a name="panorama-Type-ApplicationInstance-CreatedTime"></a>
When the application instance was created.
Type: Timestamp
Required: No

 ** DefaultRuntimeContextDevice **   <a name="panorama-Type-ApplicationInstance-DefaultRuntimeContextDevice"></a>
The device's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: No

 ** DefaultRuntimeContextDeviceName **   <a name="panorama-Type-ApplicationInstance-DefaultRuntimeContextDeviceName"></a>
The device's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: No

 ** Description **   <a name="panorama-Type-ApplicationInstance-Description"></a>
The application instance's description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: No

 ** HealthStatus **   <a name="panorama-Type-ApplicationInstance-HealthStatus"></a>
The application instance's health status.
Type: String
Valid Values: `RUNNING | ERROR | NOT_AVAILABLE`
Required: No

 ** Name **   <a name="panorama-Type-ApplicationInstance-Name"></a>
The application instance's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: No

 ** RuntimeContextStates **   <a name="panorama-Type-ApplicationInstance-RuntimeContextStates"></a>
The application's state.
Type: Array of [ReportedRuntimeContextState](API_ReportedRuntimeContextState.md) objects
Required: No

 ** Status **   <a name="panorama-Type-ApplicationInstance-Status"></a>
The application instance's status.
Type: String
Valid Values: `DEPLOYMENT_PENDING | DEPLOYMENT_REQUESTED | DEPLOYMENT_IN_PROGRESS | DEPLOYMENT_ERROR | DEPLOYMENT_SUCCEEDED | REMOVAL_PENDING | REMOVAL_REQUESTED | REMOVAL_IN_PROGRESS | REMOVAL_FAILED | REMOVAL_SUCCEEDED | DEPLOYMENT_FAILED`
Required: No

 ** StatusDescription **   <a name="panorama-Type-ApplicationInstance-StatusDescription"></a>
The application instance's status description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Tags **   <a name="panorama-Type-ApplicationInstance-Tags"></a>
The application instance's tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `.+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.*`
Required: No

## See Also
<a name="API_ApplicationInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/ApplicationInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/ApplicationInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/ApplicationInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Panorama. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query panorama` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
