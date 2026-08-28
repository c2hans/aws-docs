---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_LakeFormationConfiguration.html
---

# LakeFormationConfiguration
<a name="API_LakeFormationConfiguration"></a>

 AWS Lake Formation related configuration inputs for the security configuration.

## Contents
<a name="API_LakeFormationConfiguration_Contents"></a>

 ** authorizedSessionTagValue **   <a name="emroneks-Type-LakeFormationConfiguration-authorizedSessionTagValue"></a>
The session tag to authorize Amazon EMR on EKS for API calls to AWS Lake Formation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9 ]+`
Required: No

 ** queryEngineRoleArn **   <a name="emroneks-Type-LakeFormationConfiguration-queryEngineRoleArn"></a>
The query engine IAM role ARN that is tied to the secure Spark job. The `QueryEngine` role assumes the `JobExecutionRole` to execute all the Lake Formation calls.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:(aws[a-zA-Z0-9-]*):iam::(\d{12})?:(role((\u002F)|(\u002F[\u0021-\u007F]+\u002F))[\w+=,.@-]+)$`
Required: No

 ** secureNamespaceInfo **   <a name="emroneks-Type-LakeFormationConfiguration-secureNamespaceInfo"></a>
The namespace input of the system job.
Type: [SecureNamespaceInfo](API_SecureNamespaceInfo.md) object
Required: No

## See Also
<a name="API_LakeFormationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/LakeFormationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/LakeFormationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/LakeFormationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR on EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-on-eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
