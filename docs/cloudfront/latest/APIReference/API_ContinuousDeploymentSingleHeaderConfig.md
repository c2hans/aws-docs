---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ContinuousDeploymentSingleHeaderConfig.html
---

# ContinuousDeploymentSingleHeaderConfig
<a name="API_ContinuousDeploymentSingleHeaderConfig"></a>

This configuration determines which HTTP requests are sent to the staging distribution. If the HTTP request contains a header and value that matches what you specify here, the request is sent to the staging distribution. Otherwise the request is sent to the primary distribution.

## Contents
<a name="API_ContinuousDeploymentSingleHeaderConfig_Contents"></a>

 ** Header **   <a name="cloudfront-Type-ContinuousDeploymentSingleHeaderConfig-Header"></a>
The request header name that you want CloudFront to send to your staging distribution. The header must contain the prefix `aws-cf-cd-`.
Type: String
Required: Yes

 ** Value **   <a name="cloudfront-Type-ContinuousDeploymentSingleHeaderConfig-Value"></a>
The request header value.
Type: String
Required: Yes

## See Also
<a name="API_ContinuousDeploymentSingleHeaderConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ContinuousDeploymentSingleHeaderConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ContinuousDeploymentSingleHeaderConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ContinuousDeploymentSingleHeaderConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
