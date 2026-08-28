---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CollectionGroupErrorDetail.html
---

# CollectionGroupErrorDetail
<a name="API_CollectionGroupErrorDetail"></a>

Error details for a collection group operation.

## Contents
<a name="API_CollectionGroupErrorDetail_Contents"></a>

 ** errorCode **   <a name="opensearchserverless-Type-CollectionGroupErrorDetail-errorCode"></a>
The error code for the request. For example, `NOT_FOUND`.
Type: String
Required: No

 ** errorMessage **   <a name="opensearchserverless-Type-CollectionGroupErrorDetail-errorMessage"></a>
A description of the error. For example, `The specified Collection Group is not found.`
Type: String
Required: No

 ** id **   <a name="opensearchserverless-Type-CollectionGroupErrorDetail-id"></a>
If the request contains collection group IDs, the response includes the IDs provided in the request.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-z0-9]{3,40}`
Required: No

 ** name **   <a name="opensearchserverless-Type-CollectionGroupErrorDetail-name"></a>
If the request contains collection group names, the response includes the names provided in the request.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[a-z][a-z0-9-]+`
Required: No

## See Also
<a name="API_CollectionGroupErrorDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/CollectionGroupErrorDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/CollectionGroupErrorDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/CollectionGroupErrorDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
