---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_VpcIngressConnectionSummary.html
---

# VpcIngressConnectionSummary
<a name="API_VpcIngressConnectionSummary"></a>

Provides summary information about an VPC Ingress Connection, which includes its VPC Ingress Connection ARN and its associated Service ARN.

## Contents
<a name="API_VpcIngressConnectionSummary_Contents"></a>

 ** ServiceArn **   <a name="apprunner-Type-VpcIngressConnectionSummary-ServiceArn"></a>
The Amazon Resource Name (ARN) of the service associated with the VPC Ingress Connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: No

 ** VpcIngressConnectionArn **   <a name="apprunner-Type-VpcIngressConnectionSummary-VpcIngressConnectionArn"></a>
The Amazon Resource Name (ARN) of the VPC Ingress Connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: No

## See Also
<a name="API_VpcIngressConnectionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/VpcIngressConnectionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/VpcIngressConnectionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/VpcIngressConnectionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Runner. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apprunner` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
