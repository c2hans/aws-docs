---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AuthorizedPrincipal.html
---

# AuthorizedPrincipal
<a name="API_AuthorizedPrincipal"></a>

Information about an AWS account or service that has access to an Amazon OpenSearch Service domain through the use of an interface VPC endpoint.

## Contents
<a name="API_AuthorizedPrincipal_Contents"></a>

 ** Principal **   <a name="opensearchservice-Type-AuthorizedPrincipal-Principal"></a>
The [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html) that is allowed access to the domain.
Type: String
Required: No

 ** PrincipalType **   <a name="opensearchservice-Type-AuthorizedPrincipal-PrincipalType"></a>
The type of principal.
Type: String
Valid Values: `AWS_ACCOUNT | AWS_SERVICE`
Required: No

 ** ServiceOptions **   <a name="opensearchservice-Type-AuthorizedPrincipal-ServiceOptions"></a>
The options for the service, including the supported Regions for the endpoint access.
Type: [ServiceOptions](API_ServiceOptions.md) object
Required: No

## See Also
<a name="API_AuthorizedPrincipal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/AuthorizedPrincipal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/AuthorizedPrincipal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/AuthorizedPrincipal)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
