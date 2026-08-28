---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_Resource.html
---

# Resource
<a name="API_Resource"></a>

 A system asset that's evaluated in an Audit Manager assessment.

## Contents
<a name="API_Resource_Contents"></a>

 ** arn **   <a name="auditmanager-Type-Resource-arn"></a>
 The Amazon Resource Name (ARN) for the resource.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:.*`
Required: No

 ** complianceCheck **   <a name="auditmanager-Type-Resource-complianceCheck"></a>
 The evaluation status for a resource that was assessed when collecting compliance check evidence.
+ Audit Manager classes the resource as non-compliant if Security Hub CSPM reports a *Fail* result, or if AWS Config reports a *Non-compliant* result.
+ Audit Manager classes the resource as compliant if Security Hub CSPM reports a *Pass* result, or if AWS Config reports a *Compliant* result.
+ If a compliance check isn't available or applicable, then no compliance evaluation can be made for that resource. This is the case if a resource assessment uses AWS Config or Security Hub CSPM as the underlying data source type, but those services aren't enabled. This is also the case if the resource assessment uses an underlying data source type that doesn't support compliance checks (such as manual evidence, AWS API calls, or CloudTrail).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** value **   <a name="auditmanager-Type-Resource-value"></a>
 The value of the resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: No

## See Also
<a name="API_Resource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/Resource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/Resource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/Resource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
