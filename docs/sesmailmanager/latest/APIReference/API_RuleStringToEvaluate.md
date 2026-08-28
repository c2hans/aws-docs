---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleStringToEvaluate.html
---

# RuleStringToEvaluate
<a name="API_RuleStringToEvaluate"></a>

The string to evaluate in a string condition expression.

## Contents
<a name="API_RuleStringToEvaluate_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Analysis **   <a name="sesmailmanager-Type-RuleStringToEvaluate-Analysis"></a>
The Add On ARN and its returned value to evaluate in a string condition expression.
Type: [Analysis](API_Analysis.md) object
Required: No

 ** Attribute **   <a name="sesmailmanager-Type-RuleStringToEvaluate-Attribute"></a>
The email attribute to evaluate in a string condition expression.
Type: String
Valid Values: `MAIL_FROM | HELO | RECIPIENT | SENDER | FROM | SUBJECT | TO | CC`
Required: No

 ** ClientCertificateAttribute **   <a name="sesmailmanager-Type-RuleStringToEvaluate-ClientCertificateAttribute"></a>
The client certificate attribute to evaluate in a string condition expression.
Type: String
Valid Values: `CN | SAN_RFC822_NAME | SAN_DNS_NAME | SAN_DIRECTORY_NAME | SAN_UNIFORM_RESOURCE_IDENTIFIER | SAN_IP_ADDRESS | SAN_REGISTERED_ID | SERIAL_NUMBER`
Required: No

 ** MimeHeaderAttribute **   <a name="sesmailmanager-Type-RuleStringToEvaluate-MimeHeaderAttribute"></a>
The email MIME X-Header attribute to evaluate in a string condition expression.
Type: String
Pattern: `X-[a-zA-Z0-9-]{1,256}`
Required: No

## See Also
<a name="API_RuleStringToEvaluate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/RuleStringToEvaluate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/RuleStringToEvaluate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/RuleStringToEvaluate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
