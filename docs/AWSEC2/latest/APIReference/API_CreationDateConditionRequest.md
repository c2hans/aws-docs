---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreationDateConditionRequest.html
---

# CreationDateConditionRequest
<a name="API_CreationDateConditionRequest"></a>

The maximum age for allowed images.

## Contents
<a name="API_CreationDateConditionRequest_Contents"></a>

 ** MaximumDaysSinceCreated **
The maximum number of days that have elapsed since the image was created. For example, a value of `300` allows images that were created within the last 300 days.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

## See Also
<a name="API_CreationDateConditionRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreationDateConditionRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreationDateConditionRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreationDateConditionRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
