---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_RelatedFindingDetail.html
---

# RelatedFindingDetail
<a name="API_RelatedFindingDetail"></a>

Details related activities associated with a potential security event. Lists all distinct categories of evidence that are connected to the resource or the finding group.

## Contents
<a name="API_RelatedFindingDetail_Contents"></a>

 ** Arn **   <a name="detective-Type-RelatedFindingDetail-Arn"></a>
The Amazon Resource Name (ARN) of the related finding.
Type: String
Pattern: `^arn:.*`
Required: No

 ** IpAddress **   <a name="detective-Type-RelatedFindingDetail-IpAddress"></a>
The IP address of the finding.
Type: String
Required: No

 ** Type **   <a name="detective-Type-RelatedFindingDetail-Type"></a>
The type of finding.
Type: String
Required: No

## See Also
<a name="API_RelatedFindingDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/RelatedFindingDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/RelatedFindingDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/RelatedFindingDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Detective. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query detective` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
