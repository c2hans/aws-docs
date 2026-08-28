---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_StandardsSubscriptionRequest.html
---

# StandardsSubscriptionRequest
<a name="API_StandardsSubscriptionRequest"></a>

The standard that you want to enable.

## Contents
<a name="API_StandardsSubscriptionRequest_Contents"></a>

 ** StandardsArn **   <a name="securityhub-Type-StandardsSubscriptionRequest-StandardsArn"></a>
The ARN of the standard that you want to enable. To view the list of available standards and their ARNs, use the `DescribeStandards` operation.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** StandardsInput **   <a name="securityhub-Type-StandardsSubscriptionRequest-StandardsInput"></a>
A key-value pair of input for the standard.
Type: String to string map
Key Pattern: `.*\S.*`
Value Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_StandardsSubscriptionRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/StandardsSubscriptionRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/StandardsSubscriptionRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/StandardsSubscriptionRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
