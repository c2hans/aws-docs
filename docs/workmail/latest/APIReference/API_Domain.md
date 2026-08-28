---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_Domain.html
---

# Domain
<a name="API_Domain"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

The domain to associate with an WorkMail organization.

When you configure a domain hosted in Amazon Route 53 (Route 53), all recommended DNS records are added to the organization when you create it. For more information, see [Adding a domain](https://docs.aws.amazon.com/workmail/latest/adminguide/add_domain.html) in the *WorkMail Administrator Guide*.

## Contents
<a name="API_Domain_Contents"></a>

 ** DomainName **   <a name="workmail-Type-Domain-DomainName"></a>
The fully qualified domain name.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9.-]+`
Required: Yes

 ** HostedZoneId **   <a name="workmail-Type-Domain-HostedZoneId"></a>
The hosted zone ID for a domain hosted in Route 53. Required when configuring a domain hosted in Route 53.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[^/\\]*`
Required: No

## See Also
<a name="API_Domain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/Domain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/Domain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/Domain)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkMail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workmail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
