---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_DocumentInfo.html
---

# DocumentInfo
<a name="API_DocumentInfo"></a>

Represents a document that provides context for security testing.

## Contents
<a name="API_DocumentInfo_Contents"></a>

 ** artifactId **   <a name="securityagent-Type-DocumentInfo-artifactId"></a>
The unique identifier of the artifact associated with the document.
Type: String
Required: No

 ** integratedDocument **   <a name="securityagent-Type-DocumentInfo-integratedDocument"></a>
A reference to a document in an integrated third-party provider.
Type: [IntegratedDocument](API_IntegratedDocument.md) object
Required: No

 ** s3Location **   <a name="securityagent-Type-DocumentInfo-s3Location"></a>
The Amazon S3 location of the document.
Type: String
Required: No

## See Also
<a name="API_DocumentInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/DocumentInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/DocumentInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/DocumentInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
