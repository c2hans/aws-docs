---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CustomerManagedFleetConfiguration.html
---

# CustomerManagedFleetConfiguration
<a name="API_CustomerManagedFleetConfiguration"></a>

The configuration details for a customer managed fleet.

## Contents
<a name="API_CustomerManagedFleetConfiguration_Contents"></a>

 ** mode **   <a name="deadlinecloud-Type-CustomerManagedFleetConfiguration-mode"></a>
The Auto Scaling mode for the customer managed fleet.
Type: String
Valid Values: `NO_SCALING | EVENT_BASED_AUTO_SCALING`
Required: Yes

 ** workerCapabilities **   <a name="deadlinecloud-Type-CustomerManagedFleetConfiguration-workerCapabilities"></a>
The worker capabilities for the customer managed fleet.
Type: [CustomerManagedWorkerCapabilities](API_CustomerManagedWorkerCapabilities.md) object
Required: Yes

 ** autoScalingConfiguration **   <a name="deadlinecloud-Type-CustomerManagedFleetConfiguration-autoScalingConfiguration"></a>
The auto scaling configuration settings for the customer managed fleet.
Type: [CustomerManagedAutoScalingConfiguration](API_CustomerManagedAutoScalingConfiguration.md) object
Required: No

 ** storageProfileId **   <a name="deadlinecloud-Type-CustomerManagedFleetConfiguration-storageProfileId"></a>
The storage profile ID for the customer managed fleet.
Type: String
Pattern: `sp-[0-9a-f]{32}`
Required: No

 ** tagPropagationMode **   <a name="deadlinecloud-Type-CustomerManagedFleetConfiguration-tagPropagationMode"></a>
The tag propagation mode for the customer managed fleet.
Type: String
Valid Values: `NO_PROPAGATION | PROPAGATE_TAGS_TO_WORKERS_AT_LAUNCH`
Required: No

## See Also
<a name="API_CustomerManagedFleetConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/CustomerManagedFleetConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/CustomerManagedFleetConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/CustomerManagedFleetConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
