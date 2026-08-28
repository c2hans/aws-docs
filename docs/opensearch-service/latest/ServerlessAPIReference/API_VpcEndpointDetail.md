---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_VpcEndpointDetail.html
---

# VpcEndpointDetail
<a name="API_VpcEndpointDetail"></a>

Details about an OpenSearch Serverless-managed interface endpoint.

## Contents
<a name="API_VpcEndpointDetail_Contents"></a>

 ** createdDate **   <a name="opensearchserverless-Type-VpcEndpointDetail-createdDate"></a>
The date the endpoint was created.
Type: Long
Required: No

 ** failureCode **   <a name="opensearchserverless-Type-VpcEndpointDetail-failureCode"></a>
A failure code associated with the request.
Type: String
Required: No

 ** failureMessage **   <a name="opensearchserverless-Type-VpcEndpointDetail-failureMessage"></a>
A message associated with the failure code.
Type: String
Required: No

 ** id **   <a name="opensearchserverless-Type-VpcEndpointDetail-id"></a>
The unique identifier of the endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `vpce-[0-9a-z]*`
Required: No

 ** name **   <a name="opensearchserverless-Type-VpcEndpointDetail-name"></a>
The name of the endpoint.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[a-z][a-z0-9-]+`
Required: No

 ** securityGroupIds **   <a name="opensearchserverless-Type-VpcEndpointDetail-securityGroupIds"></a>
The unique identifiers of the security groups that define the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+\-]+`
Required: No

 ** status **   <a name="opensearchserverless-Type-VpcEndpointDetail-status"></a>
The current status of the endpoint.
Type: String
Valid Values: `PENDING | DELETING | ACTIVE | FAILED`
Required: No

 ** subnetIds **   <a name="opensearchserverless-Type-VpcEndpointDetail-subnetIds"></a>
The ID of the subnets from which you access OpenSearch Serverless.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `subnet-([0-9a-f]{8}|[0-9a-f]{17})`
Required: No

 ** vpcId **   <a name="opensearchserverless-Type-VpcEndpointDetail-vpcId"></a>
The ID of the VPC from which you access OpenSearch Serverless.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `vpc-[0-9a-z]*`
Required: No

## See Also
<a name="API_VpcEndpointDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/VpcEndpointDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/VpcEndpointDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/VpcEndpointDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
