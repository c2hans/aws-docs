---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_VpcEndpointError.html
---

# VpcEndpointError
<a name="API_VpcEndpointError"></a>

Error information when attempting to describe an Amazon OpenSearch Service-managed VPC endpoint.

## Contents
<a name="API_VpcEndpointError_Contents"></a>

 ** ErrorCode **   <a name="opensearchservice-Type-VpcEndpointError-ErrorCode"></a>
The code associated with the error.
Type: String
Valid Values: `ENDPOINT_NOT_FOUND | SERVER_ERROR`
Required: No

 ** ErrorMessage **   <a name="opensearchservice-Type-VpcEndpointError-ErrorMessage"></a>
A message describing the error.
Type: String
Required: No

 ** VpcEndpointId **   <a name="opensearchservice-Type-VpcEndpointError-VpcEndpointId"></a>
The unique identifier of the endpoint.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 256.
Pattern: `^aos-[a-zA-Z0-9]*$`
Required: No

## See Also
<a name="API_VpcEndpointError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/VpcEndpointError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/VpcEndpointError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/VpcEndpointError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
