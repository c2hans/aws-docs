---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AWSDomainInformation.html
---

# AWSDomainInformation
<a name="API_AWSDomainInformation"></a>

Information about an Amazon OpenSearch Service domain.

## Contents
<a name="API_AWSDomainInformation_Contents"></a>

 ** DomainName **   <a name="opensearchservice-Type-AWSDomainInformation-DomainName"></a>
Name of the domain.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

 ** OwnerId **   <a name="opensearchservice-Type-AWSDomainInformation-OwnerId"></a>
The AWS account ID of the domain owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]+`
Required: No

 ** Region **   <a name="opensearchservice-Type-AWSDomainInformation-Region"></a>
The AWS Region in which the domain is located.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 30.
Pattern: `[a-z][a-z0-9\-]+`
Required: No

## See Also
<a name="API_AWSDomainInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/AWSDomainInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/AWSDomainInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/AWSDomainInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
