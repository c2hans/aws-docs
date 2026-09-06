---
source_url: https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ControlSummary.html
---

# ControlSummary
<a name="API_ControlSummary"></a>

Overview of information about a control.

## Contents
<a name="API_ControlSummary_Contents"></a>

 ** Arn **   <a name="controlcatalog-Type-ControlSummary-Arn"></a>
The Amazon Resource Name (ARN) of the control.
Type: String
Length Constraints: Minimum length of 34. Maximum length of 2048.
Pattern: `arn:(aws(?:[-a-z]*)?):(controlcatalog|controltower):[a-zA-Z0-9-]*::control/[0-9a-zA-Z_\-]+`
Required: Yes

 ** Description **   <a name="controlcatalog-Type-ControlSummary-Description"></a>
A description of the control, as it may appear in the console. Describes the functionality of the control.
Type: String
Required: Yes

 ** Name **   <a name="controlcatalog-Type-ControlSummary-Name"></a>
The display name of the control.
Type: String
Required: Yes

 ** Aliases **   <a name="controlcatalog-Type-ControlSummary-Aliases"></a>
A list of alternative identifiers for the control. These are human-readable designators, such as `SH.S3.1`. Several aliases can refer to the same control across different AWS services or compliance frameworks.
Type: Array of strings
Pattern: `[a-zA-Z0-9](?:[a-zA-Z0-9_.-]{0,254}[a-zA-Z0-9])`
Required: No

 ** Behavior **   <a name="controlcatalog-Type-ControlSummary-Behavior"></a>
An enumerated type, with the following possible values:
Type: String
Valid Values: `PREVENTIVE | PROACTIVE | DETECTIVE`
Required: No

 ** CreateTime **   <a name="controlcatalog-Type-ControlSummary-CreateTime"></a>
A timestamp that notes the time when the control was released (start of its life) as a governance capability in AWS.
Type: Timestamp
Required: No

 ** GovernedProviders **   <a name="controlcatalog-Type-ControlSummary-GovernedProviders"></a>
A list of providers whose resources are governed by this control. For example, a value of `AWS` indicates that the control governs AWS resources.
Type: Array of strings
Length Constraints: Minimum length of 2. Maximum length of 64.
Pattern: `[A-Z]{2,64}`
Required: No

 ** GovernedResources **   <a name="controlcatalog-Type-ControlSummary-GovernedResources"></a>
A list of resource types that are governed by this control. This information helps you understand which controls can govern certain types of resources, and conversely, which resources are affected when the control is implemented. For AWS controls, the resources are represented as CloudFormation resource types. For non-AWS controls, the resources are represented in a provider-specific format. If `GovernedResources` cannot be represented by available resource types, it’s returned as an empty list.
Type: Array of strings
Pattern: `[A-Za-z0-9][A-Za-z0-9.:/_-]{1,254}`
Required: No

 ** Implementation **   <a name="controlcatalog-Type-ControlSummary-Implementation"></a>
An object of type `ImplementationSummary` that describes how the control is implemented.
Type: [ImplementationSummary](API_ImplementationSummary.md) object
Required: No

 ** ParameterRequirementSummary **   <a name="controlcatalog-Type-ControlSummary-ParameterRequirementSummary"></a>
A summary that indicates whether the control requires parameters, accepts optional parameters, or does not support parameters. Use this field to determine whether you need to supply parameter values when you enable the control.
Type: String
Valid Values: `REQUIRED | OPTIONAL | NONE`
Required: No

 ** Severity **   <a name="controlcatalog-Type-ControlSummary-Severity"></a>
An enumerated type, with the following possible values:
Type: String
Valid Values: `LOW | MEDIUM | HIGH | CRITICAL`
Required: No

## See Also
<a name="API_ControlSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controlcatalog-2018-05-10/ControlSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controlcatalog-2018-05-10/ControlSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controlcatalog-2018-05-10/ControlSummary)
