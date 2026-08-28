---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_DomainNameAccessAssociation.html
---

# DomainNameAccessAssociation
<a name="API_DomainNameAccessAssociation"></a>

Represents a domain name access association between an access association source and a private custom domain name. With a domain name access association, an access association source can invoke a private custom domain name while isolated from the public internet.

## Contents
<a name="API_DomainNameAccessAssociation_Contents"></a>

 ** accessAssociationSource **   <a name="apigw-Type-DomainNameAccessAssociation-accessAssociationSource"></a>
 The identifier of the domain name access association source. For a VPCE, the value is the VPC endpoint ID.
Type: String
Required: No

 ** accessAssociationSourceType **   <a name="apigw-Type-DomainNameAccessAssociation-accessAssociationSourceType"></a>
 The type of the domain name access association source.
Type: String
Valid Values: `VPCE`
Required: No

 ** domainNameAccessAssociationArn **   <a name="apigw-Type-DomainNameAccessAssociation-domainNameAccessAssociationArn"></a>
The ARN of the domain name access association resource.
Type: String
Required: No

 ** domainNameArn **   <a name="apigw-Type-DomainNameAccessAssociation-domainNameArn"></a>
The ARN of the domain name.
Type: String
Required: No

 ** tags **   <a name="apigw-Type-DomainNameAccessAssociation-tags"></a>
 The collection of tags. Each tag element is associated with a given resource.
Type: String to string map
Required: No

## See Also
<a name="API_DomainNameAccessAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/DomainNameAccessAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/DomainNameAccessAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/DomainNameAccessAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
