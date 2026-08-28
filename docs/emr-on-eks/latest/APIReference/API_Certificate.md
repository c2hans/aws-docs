---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_Certificate.html
---

# Certificate
<a name="API_Certificate"></a>

The entity representing certificate data generated for managed endpoint.

## Contents
<a name="API_Certificate_Contents"></a>

 ** certificateArn **   <a name="emroneks-Type-Certificate-certificateArn"></a>
The ARN of the certificate generated for managed endpoint.
Type: String
Length Constraints: Minimum length of 44. Maximum length of 2048.
Pattern: `^arn:(aws[a-zA-Z0-9-]*):acm:.+:(\d{12}):certificate/.+$`
Required: No

 ** certificateData **   <a name="emroneks-Type-Certificate-certificateData"></a>
The base64 encoded PEM certificate data generated for managed endpoint.
Type: String
Length Constraints: Maximum length of 5000.
Pattern: `^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{4}|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$`
Required: No

## See Also
<a name="API_Certificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/Certificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/Certificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/Certificate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR on EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-on-eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
