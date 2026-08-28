---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_OciIamRole.html
---

# OciIamRole
<a name="API_OciIamRole"></a>

Information about an AWS Identity and Access Management (IAM) service role used for Autonomous Database integration with Oracle Cloud Infrastructure (OCI).

## Contents
<a name="API_OciIamRole_Contents"></a>

 ** awsIntegration **   <a name="odb-Type-OciIamRole-awsIntegration"></a>
The AWS integration configuration settings for the AWS Identity and Access Management (IAM) service role.
Type: String
Valid Values: `KmsTde | SecretsManager`
Required: No

 ** iamRoleArn **   <a name="odb-Type-OciIamRole-iamRoleArn"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) service role.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):iam::[0-9]{12}:role/.+`
Required: No

 ** status **   <a name="odb-Type-OciIamRole-status"></a>
The current lifecycle status of the IAM service role.
Type: String
Valid Values: `PROVISIONING | AVAILABLE | PROVISION_FAILED | TERMINATING | TERMINATE_FAILED`
Required: No

 ** statusReason **   <a name="odb-Type-OciIamRole-statusReason"></a>
Additional information about the current status of the IAM service role, if applicable.
Type: String
Required: No

## See Also
<a name="API_OciIamRole_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/OciIamRole)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/OciIamRole)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/OciIamRole)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
