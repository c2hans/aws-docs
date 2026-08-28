---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_TestGridProject.html
---

# TestGridProject
<a name="API_TestGridProject"></a>

A Selenium testing project. Projects are used to collect and collate sessions.

## Contents
<a name="API_TestGridProject_Contents"></a>

 ** arn **   <a name="devicefarm-Type-TestGridProject-arn"></a>
The ARN for the project.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** created **   <a name="devicefarm-Type-TestGridProject-created"></a>
When the project was created.
Type: Timestamp
Required: No

 ** description **   <a name="devicefarm-Type-TestGridProject-description"></a>
A human-readable description for the project.
Type: String
Required: No

 ** name **   <a name="devicefarm-Type-TestGridProject-name"></a>
A human-readable name for the project.
Type: String
Required: No

 ** vpcConfig **   <a name="devicefarm-Type-TestGridProject-vpcConfig"></a>
The VPC security groups and subnets that are attached to a project.
Type: [TestGridVpcConfig](API_TestGridVpcConfig.md) object
Required: No

## See Also
<a name="API_TestGridProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/TestGridProject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/TestGridProject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/TestGridProject)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
