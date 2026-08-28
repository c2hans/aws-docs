---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_SecurityConfiguration.html
---

# SecurityConfiguration
<a name="API_SecurityConfiguration"></a>

Inputs related to the security configuration. Security configurations in Amazon EMR on EKS are templates for different security setups. You can use security configurations to configure the AWS Lake Formation integration setup. You can also create a security configuration to re-use a security setup each time you create a virtual cluster.

## Contents
<a name="API_SecurityConfiguration_Contents"></a>

 ** arn **   <a name="emroneks-Type-SecurityConfiguration-arn"></a>
The ARN (Amazon Resource Name) of the security configuration.
Type: String
Length Constraints: Minimum length of 60. Maximum length of 1024.
Pattern: `^arn:(aws[a-zA-Z0-9-]*):emr-containers:.+:(\d{12}):\/securityconfigurations\/[0-9a-zA-Z]+$`
Required: No

 ** createdAt **   <a name="emroneks-Type-SecurityConfiguration-createdAt"></a>
The date and time that the job run was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="emroneks-Type-SecurityConfiguration-createdBy"></a>
The user who created the job run.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:(aws[a-zA-Z0-9-]*):(iam|sts)::(\d{12})?:[\w/+=,.@-]+$`
Required: No

 ** id **   <a name="emroneks-Type-SecurityConfiguration-id"></a>
The ID of the security configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: No

 ** name **   <a name="emroneks-Type-SecurityConfiguration-name"></a>
The name of the security configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** securityConfigurationData **   <a name="emroneks-Type-SecurityConfiguration-securityConfigurationData"></a>
Security configuration inputs for the request.
Type: [SecurityConfigurationData](API_SecurityConfigurationData.md) object
Required: No

 ** tags **   <a name="emroneks-Type-SecurityConfiguration-tags"></a>
The tags to assign to the security configuration.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `.*\S.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_SecurityConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/SecurityConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/SecurityConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/SecurityConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR on EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-on-eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
