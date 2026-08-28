---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_AnomalyResource.html
---

# AnomalyResource
<a name="API_AnomalyResource"></a>

The AWS resources in which DevOps Guru detected unusual behavior that resulted in the generation of an anomaly. When DevOps Guru detects multiple related anomalies, it creates and insight with details about the anomalous behavior and suggestions about how to correct the problem.

## Contents
<a name="API_AnomalyResource_Contents"></a>

 ** Name **   <a name="DevOpsGuru-Type-AnomalyResource-Name"></a>
The name of the AWS resource.
Type: String
Required: No

 ** Type **   <a name="DevOpsGuru-Type-AnomalyResource-Type"></a>
The type of the AWS resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z]+[a-zA-Z0-9-_:]*$`
Required: No

## See Also
<a name="API_AnomalyResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/AnomalyResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/AnomalyResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/AnomalyResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
