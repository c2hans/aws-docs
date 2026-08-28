---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_WorkerCapabilities.html
---

# WorkerCapabilities
<a name="API_WorkerCapabilities"></a>

The details for worker capabilities.

## Contents
<a name="API_WorkerCapabilities_Contents"></a>

 ** amounts **   <a name="deadlinecloud-Type-WorkerCapabilities-amounts"></a>
The worker capabilities amounts on a list of worker capabilities.
Type: Array of [WorkerAmountCapability](API_WorkerAmountCapability.md) objects
Array Members: Minimum number of 2 items. Maximum number of 17 items.
Required: Yes

 ** attributes **   <a name="deadlinecloud-Type-WorkerCapabilities-attributes"></a>
The worker attribute capabilities in the list of attribute capabilities.
Type: Array of [WorkerAttributeCapability](API_WorkerAttributeCapability.md) objects
Array Members: Minimum number of 2 items. Maximum number of 17 items.
Required: Yes

## See Also
<a name="API_WorkerCapabilities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/WorkerCapabilities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/WorkerCapabilities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/WorkerCapabilities)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
