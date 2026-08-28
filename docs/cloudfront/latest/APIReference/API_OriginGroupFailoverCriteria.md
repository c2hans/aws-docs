---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_OriginGroupFailoverCriteria.html
---

# OriginGroupFailoverCriteria
<a name="API_OriginGroupFailoverCriteria"></a>

A complex data type that includes information about the failover criteria for an origin group, including the status codes for which CloudFront will failover from the primary origin to the second origin.

## Contents
<a name="API_OriginGroupFailoverCriteria_Contents"></a>

 ** StatusCodes **   <a name="cloudfront-Type-OriginGroupFailoverCriteria-StatusCodes"></a>
The status codes that, when returned from the primary origin, will trigger CloudFront to failover to the second origin.
Type: [StatusCodes](API_StatusCodes.md) object
Required: Yes

## See Also
<a name="API_OriginGroupFailoverCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/OriginGroupFailoverCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/OriginGroupFailoverCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/OriginGroupFailoverCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
