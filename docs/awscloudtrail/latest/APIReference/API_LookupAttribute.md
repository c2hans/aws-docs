---
source_url: https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_LookupAttribute.html
---

# LookupAttribute
<a name="API_LookupAttribute"></a>

Specifies an attribute and value that filter the events returned.

## Contents
<a name="API_LookupAttribute_Contents"></a>

 ** AttributeKey **   <a name="awscloudtrail-Type-LookupAttribute-AttributeKey"></a>
Specifies an attribute on which to filter the events returned.
Type: String
Valid Values: `EventId | EventName | ReadOnly | Username | ResourceType | ResourceName | EventSource | AccessKeyId`
Required: Yes

 ** AttributeValue **   <a name="awscloudtrail-Type-LookupAttribute-AttributeValue"></a>
Specifies a value for the specified `AttributeKey`.
The maximum length for the `AttributeValue` is 2000 characters. The following characters ('`_`', '` `', '`,`', '`\\n`') count as two characters towards the 2000 character limit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: Yes

## See Also
<a name="API_LookupAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/LookupAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/LookupAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/LookupAttribute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudTrail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awscloudtrail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
