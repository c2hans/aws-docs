---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_edge_Definition.html
---

# Definition
<a name="API_edge_Definition"></a>

Information about deployment details based on the deployment type.

## Contents
<a name="API_edge_Definition_Contents"></a>

 ** Checksum **   <a name="sagemaker-Type-edge_Definition-Checksum"></a>
The checksum information of the model.
Type: [Checksum](API_edge_Checksum.md) object
Required: No

 ** ModelHandle **   <a name="sagemaker-Type-edge_Definition-ModelHandle"></a>
The unique model handle.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
Required: No

 ** S3Url **   <a name="sagemaker-Type-edge_Definition-S3Url"></a>
The absolute S3 location of the model.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^s3://([^/]+)/?(.*)$`
Required: No

 ** State **   <a name="sagemaker-Type-edge_Definition-State"></a>
The desired state of the model.
Type: String
Valid Values: `DEPLOY | UNDEPLOY`
Required: No

## See Also
<a name="API_edge_Definition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-edge-2020-09-23/Definition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-edge-2020-09-23/Definition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-edge-2020-09-23/Definition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
