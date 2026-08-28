---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ConformancePackDetail.html
---

# ConformancePackDetail
<a name="API_ConformancePackDetail"></a>

Returns details of a conformance pack. A conformance pack is a collection of AWS Config rules and remediation actions that can be easily deployed in an account and a region.

## Contents
<a name="API_ConformancePackDetail_Contents"></a>

 ** ConformancePackArn **   <a name="config-Type-ConformancePackDetail-ConformancePackArn"></a>
Amazon Resource Name (ARN) of the conformance pack.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** ConformancePackId **   <a name="config-Type-ConformancePackDetail-ConformancePackId"></a>
ID of the conformance pack.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** ConformancePackName **   <a name="config-Type-ConformancePackDetail-ConformancePackName"></a>
Name of the conformance pack.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z][-a-zA-Z0-9]*`
Required: Yes

 ** ConformancePackInputParameters **   <a name="config-Type-ConformancePackDetail-ConformancePackInputParameters"></a>
A list of `ConformancePackInputParameter` objects.
Type: Array of [ConformancePackInputParameter](API_ConformancePackInputParameter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 60 items.
Required: No

 ** CreatedBy **   <a name="config-Type-ConformancePackDetail-CreatedBy"></a>
The AWS service that created the conformance pack.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** DeliveryS3Bucket **   <a name="config-Type-ConformancePackDetail-DeliveryS3Bucket"></a>
The name of the Amazon S3 bucket where AWS Config stores conformance pack templates.
This field is optional.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Required: No

 ** DeliveryS3KeyPrefix **   <a name="config-Type-ConformancePackDetail-DeliveryS3KeyPrefix"></a>
The prefix for the Amazon S3 bucket.
This field is optional.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** LastUpdateRequestedTime **   <a name="config-Type-ConformancePackDetail-LastUpdateRequestedTime"></a>
The last time a conformation pack update was requested.
Type: Timestamp
Required: No

 ** TemplateSSMDocumentDetails **   <a name="config-Type-ConformancePackDetail-TemplateSSMDocumentDetails"></a>
An object that contains the name or Amazon Resource Name (ARN) of the AWS Systems Manager document (SSM document) and the version of the SSM document that is used to create a conformance pack.
Type: [TemplateSSMDocumentDetails](API_TemplateSSMDocumentDetails.md) object
Required: No

## See Also
<a name="API_ConformancePackDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ConformancePackDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ConformancePackDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ConformancePackDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
