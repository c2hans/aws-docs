---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ManagedLogGroup.html
---

# ManagedLogGroup
<a name="API_ManagedLogGroup"></a>

The Cloudwatch Log Group created by Amazon ECS for an Express service.

## Contents
<a name="API_ManagedLogGroup_Contents"></a>

 ** logGroupName **   <a name="ECS-Type-ManagedLogGroup-logGroupName"></a>
The name of the Cloudwatch Log Group associated with the Express service.
Type: String
Required: Yes

 ** status **   <a name="ECS-Type-ManagedLogGroup-status"></a>
The status of the Cloudwatch LogGroup.
Type: String
Valid Values: `PROVISIONING | ACTIVE | DEPROVISIONING | DELETED | FAILED`
Required: Yes

 ** updatedAt **   <a name="ECS-Type-ManagedLogGroup-updatedAt"></a>
The Unix timestamp for when the Cloudwatch LogGroup was last updated
Type: Timestamp
Required: Yes

 ** arn **   <a name="ECS-Type-ManagedLogGroup-arn"></a>
The Amazon Resource Name (ARN) of the Cloudwatch Log Group associated with the Express service.
Type: String
Required: No

 ** statusReason **   <a name="ECS-Type-ManagedLogGroup-statusReason"></a>
Information about why the Cloudwatch LogGroup is in the current status.
Type: String
Required: No

## See Also
<a name="API_ManagedLogGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ManagedLogGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ManagedLogGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ManagedLogGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
