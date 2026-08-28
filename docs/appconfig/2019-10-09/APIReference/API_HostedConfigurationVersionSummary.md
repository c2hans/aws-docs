---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_HostedConfigurationVersionSummary.html
---

# HostedConfigurationVersionSummary
<a name="API_HostedConfigurationVersionSummary"></a>

Information about the configuration.

## Contents
<a name="API_HostedConfigurationVersionSummary_Contents"></a>

 ** ApplicationId **   <a name="appconfig-Type-HostedConfigurationVersionSummary-ApplicationId"></a>
The application ID.
Type: String
Pattern: `[a-z0-9]{4,7}`
Required: No

 ** ConfigurationProfileId **   <a name="appconfig-Type-HostedConfigurationVersionSummary-ConfigurationProfileId"></a>
The configuration profile ID.
Type: String
Pattern: `[a-z0-9]{4,7}`
Required: No

 ** ContentType **   <a name="appconfig-Type-HostedConfigurationVersionSummary-ContentType"></a>
A standard MIME type describing the format of the configuration content. For more information, see [Content-Type](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.17).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Description **   <a name="appconfig-Type-HostedConfigurationVersionSummary-Description"></a>
A description of the configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** KmsKeyArn **   <a name="appconfig-Type-HostedConfigurationVersionSummary-KmsKeyArn"></a>
The Amazon Resource Name of the AWS Key Management Service key that was used to encrypt this specific version of the configuration data in the AWS AppConfig hosted configuration store.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:[a-z]+:((eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1})?:(\d{12})?:[a-zA-Z0-9-_/:.]+`
Required: No

 ** VersionLabel **   <a name="appconfig-Type-HostedConfigurationVersionSummary-VersionLabel"></a>
A user-defined label for an AWS AppConfig hosted configuration version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*[^0-9].*`
Required: No

 ** VersionNumber **   <a name="appconfig-Type-HostedConfigurationVersionSummary-VersionNumber"></a>
The configuration version.
Type: Integer
Required: No

## See Also
<a name="API_HostedConfigurationVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/HostedConfigurationVersionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/HostedConfigurationVersionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/HostedConfigurationVersionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
