---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateRemoteAccessSessionConfiguration.html
---

# CreateRemoteAccessSessionConfiguration
<a name="API_CreateRemoteAccessSessionConfiguration"></a>

Configuration settings for a remote access session, including billing method.

## Contents
<a name="API_CreateRemoteAccessSessionConfiguration_Contents"></a>

 ** auxiliaryApps **   <a name="devicefarm-Type-CreateRemoteAccessSessionConfiguration-auxiliaryApps"></a>
A list of upload ARNs for app packages to be installed onto your device. (Maximum 3)
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** billingMethod **   <a name="devicefarm-Type-CreateRemoteAccessSessionConfiguration-billingMethod"></a>
The billing method for the remote access session.
Type: String
Valid Values: `METERED | UNMETERED`
Required: No

 ** deviceProxy **   <a name="devicefarm-Type-CreateRemoteAccessSessionConfiguration-deviceProxy"></a>
The device proxy to be configured on the device for the remote access session.
Type: [DeviceProxy](API_DeviceProxy.md) object
Required: No

 ** vpceConfigurationArns **   <a name="devicefarm-Type-CreateRemoteAccessSessionConfiguration-vpceConfigurationArns"></a>
An array of ARNs included in the VPC endpoint configuration.
Type: Array of strings
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

## See Also
<a name="API_CreateRemoteAccessSessionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/CreateRemoteAccessSessionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/CreateRemoteAccessSessionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/CreateRemoteAccessSessionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
