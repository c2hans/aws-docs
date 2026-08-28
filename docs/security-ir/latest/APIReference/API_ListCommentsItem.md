---
source_url: https://docs.aws.amazon.com/security-ir/latest/APIReference/API_ListCommentsItem.html
---

# ListCommentsItem
<a name="API_ListCommentsItem"></a>

## Contents
<a name="API_ListCommentsItem_Contents"></a>

 ** commentId **   <a name="securityir-Type-ListCommentsItem-commentId"></a>

Type: String
Length Constraints: Fixed length of 6.
Pattern: `\d{6}`
Required: Yes

 ** body **   <a name="securityir-Type-ListCommentsItem-body"></a>

Type: String
Length Constraints: Minimum length of 1. Maximum length of 12000.
Required: No

 ** createdDate **   <a name="securityir-Type-ListCommentsItem-createdDate"></a>

Type: Timestamp
Required: No

 ** creator **   <a name="securityir-Type-ListCommentsItem-creator"></a>

Type: String
Pattern: `.*((^AWS Responder)|(^\d{12}$)|(^arn:([^:]*aws[^:]*):(?:(?:iam)::\d{12}:(?:user|role|group|root)(?:(?:/[^/]+)+)?|(?:sts)::\d{12}:assumed-role/[^/]+/[^/]+)$)|(^security-ir.amazonaws.com)).*`
Required: No

 ** lastUpdatedBy **   <a name="securityir-Type-ListCommentsItem-lastUpdatedBy"></a>

Type: String
Pattern: `.*((^AWS Responder)|(^\d{12}$)|(^arn:([^:]*aws[^:]*):(?:(?:iam)::\d{12}:(?:user|role|group|root)(?:(?:/[^/]+)+)?|(?:sts)::\d{12}:assumed-role/[^/]+/[^/]+)$)|(^security-ir.amazonaws.com)).*`
Required: No

 ** lastUpdatedDate **   <a name="securityir-Type-ListCommentsItem-lastUpdatedDate"></a>

Type: Timestamp
Required: No

## See Also
<a name="API_ListCommentsItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/security-ir-2018-05-10/ListCommentsItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/security-ir-2018-05-10/ListCommentsItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/security-ir-2018-05-10/ListCommentsItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Incident Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-ir` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
