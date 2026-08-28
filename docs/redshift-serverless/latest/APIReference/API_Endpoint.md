---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_Endpoint.html
---

# Endpoint
<a name="API_Endpoint"></a>

The VPC endpoint object.

## Contents
<a name="API_Endpoint_Contents"></a>

 ** address **   <a name="redshiftserverless-Type-Endpoint-address"></a>
The DNS address of the VPC endpoint.
Type: String
Required: No

 ** port **   <a name="redshiftserverless-Type-Endpoint-port"></a>
The port that Amazon Redshift Serverless listens on.
Type: Integer
Required: No

 ** vpcEndpoints **   <a name="redshiftserverless-Type-Endpoint-vpcEndpoints"></a>
An array of `VpcEndpoint` objects.
Type: Array of [VpcEndpoint](API_VpcEndpoint.md) objects
Required: No

## See Also
<a name="API_Endpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/Endpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/Endpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/Endpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
