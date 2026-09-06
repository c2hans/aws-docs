---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ConfigurationOptionDescription.html
---

# ConfigurationOptionDescription
<a name="API_ConfigurationOptionDescription"></a>

Describes the possible values for a configuration option.

## Contents
<a name="API_ConfigurationOptionDescription_Contents"></a>

 ** ChangeSeverity **
An indication of which action is required if the value for this configuration option changes:
+  `NoInterruption` : There is no interruption to the environment or application availability.
+  `RestartEnvironment` : The environment is entirely restarted, all A resources are deleted and recreated, and the environment is unavailable during the process.
+  `RestartApplicationServer` : The environment is available the entire time. However, a short application outage occurs when the application servers on the running Amazon EC2 instances are restarted.
Type: String
Required: No

 ** DefaultValue **
The default value for this configuration option.
Type: String
Required: No

 ** MaxLength **
If specified, the configuration option must be a string value no longer than this value.
Type: Integer
Required: No

 ** MaxValue **
If specified, the configuration option must be a numeric value less than this value.
Type: Integer
Required: No

 ** MinValue **
If specified, the configuration option must be a numeric value greater than this value.
Type: Integer
Required: No

 ** Name **
The name of the configuration option.
Type: String
Required: No

 ** Namespace **
A unique namespace identifying the option's associated AWS resource.
Type: String
Required: No

 ** Regex **
If specified, the configuration option must be a string value that satisfies this regular expression.
Type: [OptionRestrictionRegex](API_OptionRestrictionRegex.md) object
Required: No

 ** UserDefined **
An indication of whether the user defined this configuration option:
+  `true` : This configuration option was defined by the user. It is a valid choice for specifying if this as an `Option to Remove` when updating configuration settings.
+  `false` : This configuration was not defined by the user.
 Constraint: You can remove only `UserDefined` options from a configuration.
 Valid Values: `true` \| `false`
Type: Boolean
Required: No

 ** ValueOptions.member.N **
If specified, values for the configuration option are selected from this list.
Type: Array of strings
Required: No

 ** ValueType **
An indication of which type of values this option has and whether it is allowable to select one or more than one of the possible values:
+  `Scalar` : Values for this option are a single selection from the possible values, or an unformatted string, or numeric value governed by the `MIN/MAX/Regex` constraints.
+  `List` : Values for this option are multiple selections from the possible values.
+  `Boolean` : Values for this option are either `true` or `false` .
+  `Json` : Values for this option are a JSON representation of a `ConfigDocument`.
Type: String
Valid Values: `Scalar | List`
Required: No

## See Also
<a name="API_ConfigurationOptionDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/ConfigurationOptionDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/ConfigurationOptionDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/ConfigurationOptionDescription)
