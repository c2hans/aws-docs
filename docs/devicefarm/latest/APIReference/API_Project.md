---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Project.html
---

# Project
<a name="API_Project"></a>

Represents an operating-system neutral workspace for running and managing tests.

## Contents
<a name="API_Project_Contents"></a>

 ** arn **   <a name="devicefarm-Type-Project-arn"></a>
The project's ARN.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** created **   <a name="devicefarm-Type-Project-created"></a>
When the project was created.
Type: Timestamp
Required: No

 ** defaultJobTimeoutMinutes **   <a name="devicefarm-Type-Project-defaultJobTimeoutMinutes"></a>
The default number of minutes (at the project level) a test run executes before it times out. The default value is 150 minutes.
Type: Integer
Required: No

 ** environmentVariables **   <a name="devicefarm-Type-Project-environmentVariables"></a>
Environment variables associated with the project.
Type: Array of [EnvironmentVariable](API_EnvironmentVariable.md) objects
Array Members: Minimum number of 1 item. Maximum number of 32 items.
Required: No

 ** executionRoleArn **   <a name="devicefarm-Type-Project-executionRoleArn"></a>
The IAM execution role associated with the project.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws:iam::[0-9]{12}:role/.+`
Required: No

 ** name **   <a name="devicefarm-Type-Project-name"></a>
The project's name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** vpcConfig **   <a name="devicefarm-Type-Project-vpcConfig"></a>
The VPC security groups and subnets that are attached to a project.
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

## See Also
<a name="API_Project_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/Project)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/Project)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/Project)
