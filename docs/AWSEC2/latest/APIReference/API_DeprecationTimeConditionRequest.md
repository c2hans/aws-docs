---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeprecationTimeConditionRequest.html
---

# DeprecationTimeConditionRequest
<a name="API_DeprecationTimeConditionRequest"></a>

The maximum period since deprecation for allowed images.

## Contents
<a name="API_DeprecationTimeConditionRequest_Contents"></a>

 ** MaximumDaysSinceDeprecated **
The maximum number of days that have elapsed since the image was deprecated. Set to `0` to exclude all deprecated images.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

## See Also
<a name="API_DeprecationTimeConditionRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeprecationTimeConditionRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeprecationTimeConditionRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeprecationTimeConditionRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
