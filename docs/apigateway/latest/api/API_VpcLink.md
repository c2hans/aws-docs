---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_VpcLink.html
---

# VpcLink
<a name="API_VpcLink"></a>

An API Gateway VPC link for a RestApi to access resources in an Amazon Virtual Private Cloud (VPC).

## Contents
<a name="API_VpcLink_Contents"></a>

 ** description **   <a name="apigw-Type-VpcLink-description"></a>
The description of the VPC link.
Type: String
Required: No

 ** id **   <a name="apigw-Type-VpcLink-id"></a>
The identifier of the VpcLink. It is used in an Integration to reference this VpcLink.
Type: String
Required: No

 ** name **   <a name="apigw-Type-VpcLink-name"></a>
The name used to label and identify the VPC link.
Type: String
Required: No

 ** status **   <a name="apigw-Type-VpcLink-status"></a>
The status of the VPC link. The valid values are `AVAILABLE`, `PENDING`, `DELETING`, or `FAILED`. Deploying an API will wait if the status is `PENDING` and will fail if the status is `DELETING`.
Type: String
Valid Values: `AVAILABLE | PENDING | DELETING | FAILED`
Required: No

 ** statusMessage **   <a name="apigw-Type-VpcLink-statusMessage"></a>
A description about the VPC link status.
Type: String
Required: No

 ** tags **   <a name="apigw-Type-VpcLink-tags"></a>
The collection of tags. Each tag element is associated with a given resource.
Type: String to string map
Required: No

 ** targetArns **   <a name="apigw-Type-VpcLink-targetArns"></a>
The ARN of the network load balancer of the VPC targeted by the VPC link. The network load balancer must be owned by the same AWS account of the API owner.
Type: Array of strings
Required: No

## See Also
<a name="API_VpcLink_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/VpcLink)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/VpcLink)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/VpcLink)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
