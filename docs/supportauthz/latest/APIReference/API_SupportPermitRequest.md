---
source_url: https://docs.aws.amazon.com/supportauthz/latest/APIReference/API_SupportPermitRequest.html
---

# SupportPermitRequest
<a name="API_SupportPermitRequest"></a>

A permit request from an AWS support operator.

## Contents
<a name="API_SupportPermitRequest_Contents"></a>

 ** createdAt **   <a name="supportauthorization-Type-SupportPermitRequest-createdAt"></a>
The timestamp when the request was created.
Type: Timestamp
Required: Yes

 ** permit **   <a name="supportauthorization-Type-SupportPermitRequest-permit"></a>
The permit definition requested by the operator.
Type: [Permit](API_Permit.md) object
Required: Yes

 ** requestArn **   <a name="supportauthorization-Type-SupportPermitRequest-requestArn"></a>
The ARN of the permit request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9:/-]{1,512}`
Required: Yes

 ** status **   <a name="supportauthorization-Type-SupportPermitRequest-status"></a>
The current status of the permit request.
Type: String
Valid Values: `PENDING | ACCEPTED | REJECTED | CANCELLED`
Required: Yes

 ** supportCaseDisplayId **   <a name="supportauthorization-Type-SupportPermitRequest-supportCaseDisplayId"></a>
The display identifier of the support case associated with the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9:/-]{1,512}`
Required: Yes

 ** updatedAt **   <a name="supportauthorization-Type-SupportPermitRequest-updatedAt"></a>
The timestamp when the request was last updated.
Type: Timestamp
Required: Yes

## See Also
<a name="API_SupportPermitRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supportauthz-2026-06-30/SupportPermitRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supportauthz-2026-06-30/SupportPermitRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supportauthz-2026-06-30/SupportPermitRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support authorization. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query supportauthz` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
