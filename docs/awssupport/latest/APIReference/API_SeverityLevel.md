---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_SeverityLevel.html
---

# SeverityLevel
<a name="API_SeverityLevel"></a>

A code and name pair that represents the severity level of a support case. The available values depend on the support plan for the account. For more information, see [Choosing a severity](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html#choosing-severity) in the * AWS Support User Guide*.

## Contents
<a name="API_SeverityLevel_Contents"></a>

 ** code **   <a name="AWSSupport-Type-SeverityLevel-code"></a>
The code for case severity level.
Valid values: `low` \| `normal` \| `high` \| `urgent` \| `critical`
Type: String

 ** name **   <a name="AWSSupport-Type-SeverityLevel-name"></a>
The name of the severity level that corresponds to the severity level code.
The values returned by the API are different from the values that appear in the AWS Support Center. For example, the API uses the code `low`, but the name appears as General guidance in Support Center.
The following are the API code names and how they appear in the console:
+  `low` - General guidance
+  `normal` - System impaired
+  `high` - Production system impaired
+  `urgent` - Production system down
+  `critical` - Business-critical system down
For more information, see [Choosing a severity](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html#choosing-severity) in the * AWS Support User Guide*.
Type: String

## See Also
<a name="API_SeverityLevel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/SeverityLevel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/SeverityLevel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/SeverityLevel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awssupport` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
