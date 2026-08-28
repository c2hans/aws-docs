---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PriorityClass.html
---

# PriorityClass
<a name="API_PriorityClass"></a>

Priority class configuration. When included in `PriorityClasses`, these class configurations define how tasks are queued.

## Contents
<a name="API_PriorityClass_Contents"></a>

 ** Name **   <a name="sagemaker-Type-PriorityClass-Name"></a>
Name of the priority class.
Type: String
Pattern: `[a-z0-9]([-a-z0-9]*[a-z0-9]){0,39}?`
Required: Yes

 ** Weight **   <a name="sagemaker-Type-PriorityClass-Weight"></a>
Weight of the priority class. The value is within a range from 0 to 100, where 0 is the default.
A weight of 0 is the lowest priority and 100 is the highest. Weight 0 is the default.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: Yes

## See Also
<a name="API_PriorityClass_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/PriorityClass)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/PriorityClass)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/PriorityClass)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
