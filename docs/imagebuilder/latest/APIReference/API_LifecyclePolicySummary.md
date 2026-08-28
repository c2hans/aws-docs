---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_LifecyclePolicySummary.html
---

# LifecyclePolicySummary
<a name="API_LifecyclePolicySummary"></a>

Contains a summary of lifecycle policy resources.

## Contents
<a name="API_LifecyclePolicySummary_Contents"></a>

 ** arn **   <a name="imagebuilder-Type-LifecyclePolicySummary-arn"></a>
The Amazon Resource Name (ARN) of the lifecycle policy summary resource.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^arn:aws(?:-[a-z]+)*:imagebuilder:[a-z]{2,}(?:-[a-z]+)+-[0-9]+:(?:[0-9]{12}|aws):lifecycle-policy/[a-z0-9-_]+$`
Required: No

 ** dateCreated **   <a name="imagebuilder-Type-LifecyclePolicySummary-dateCreated"></a>
The timestamp when Image Builder created the lifecycle policy resource.
Type: Timestamp
Required: No

 ** dateLastRun **   <a name="imagebuilder-Type-LifecyclePolicySummary-dateLastRun"></a>
The timestamp for the last time Image Builder ran the lifecycle policy.
Type: Timestamp
Required: No

 ** dateUpdated **   <a name="imagebuilder-Type-LifecyclePolicySummary-dateUpdated"></a>
The timestamp when Image Builder updated the lifecycle policy resource.
Type: Timestamp
Required: No

 ** description **   <a name="imagebuilder-Type-LifecyclePolicySummary-description"></a>
Optional description for the lifecycle policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** executionRole **   <a name="imagebuilder-Type-LifecyclePolicySummary-executionRole"></a>
The name or Amazon Resource Name (ARN) of the IAM role that Image Builder uses to run the lifecycle policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(?:arn:aws(?:-[a-z]+)*:iam::[0-9]{12}:role/)?[a-zA-Z_0-9+=,.@\-_/]+$`
Required: No

 ** name **   <a name="imagebuilder-Type-LifecyclePolicySummary-name"></a>
The name of the lifecycle policy.
Type: String
Pattern: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
Required: No

 ** resourceType **   <a name="imagebuilder-Type-LifecyclePolicySummary-resourceType"></a>
The type of resources the lifecycle policy targets.
Type: String
Valid Values: `AMI_IMAGE | CONTAINER_IMAGE`
Required: No

 ** status **   <a name="imagebuilder-Type-LifecyclePolicySummary-status"></a>
The lifecycle policy resource status.
Type: String
Valid Values: `DISABLED | ENABLED`
Required: No

 ** tags **   <a name="imagebuilder-Type-LifecyclePolicySummary-tags"></a>
To help manage your lifecycle policy resources, you can assign your own metadata to each resource in the form of tags. Each tag consists of a key and an optional value, both of which you define.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_LifecyclePolicySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/LifecyclePolicySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/LifecyclePolicySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/LifecyclePolicySummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
