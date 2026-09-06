---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_StackResourceDetail.html
---

# StackResourceDetail
<a name="API_StackResourceDetail"></a>

Contains detailed information about the specified stack resource.

## Contents
<a name="API_StackResourceDetail_Contents"></a>

 ** LastUpdatedTimestamp **
Time the status was updated.
Type: Timestamp
Required: Yes

 ** LogicalResourceId **
The logical name of the resource specified in the template.
Type: String
Required: Yes

 ** ResourceStatus **
Current status of the resource.
Type: String
Valid Values: `CREATE_IN_PROGRESS | CREATE_FAILED | CREATE_COMPLETE | DELETE_IN_PROGRESS | DELETE_FAILED | DELETE_COMPLETE | DELETE_SKIPPED | UPDATE_IN_PROGRESS | UPDATE_FAILED | UPDATE_COMPLETE | IMPORT_FAILED | IMPORT_COMPLETE | IMPORT_IN_PROGRESS | IMPORT_ROLLBACK_IN_PROGRESS | IMPORT_ROLLBACK_FAILED | IMPORT_ROLLBACK_COMPLETE | EXPORT_FAILED | EXPORT_COMPLETE | EXPORT_IN_PROGRESS | EXPORT_ROLLBACK_IN_PROGRESS | EXPORT_ROLLBACK_FAILED | EXPORT_ROLLBACK_COMPLETE | UPDATE_ROLLBACK_IN_PROGRESS | UPDATE_ROLLBACK_COMPLETE | UPDATE_ROLLBACK_FAILED | ROLLBACK_IN_PROGRESS | ROLLBACK_COMPLETE | ROLLBACK_FAILED`
Required: Yes

 ** ResourceType **
Type of resource. For more information, see [AWS resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) in the * AWS CloudFormation User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** Description **
User defined description associated with the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** DriftInformation **
Information about whether the resource's actual configuration differs, or has *drifted*, from its expected configuration, as defined in the stack template and any values specified as template parameters. For more information, see [Detect unmanaged configuration changes to stacks and resources with drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html).
Type: [StackResourceDriftInformation](API_StackResourceDriftInformation.md) object
Required: No

 ** Metadata **
The content of the `Metadata` attribute declared for the resource. For more information, see [Metadata attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-metadata.html) in the * AWS CloudFormation User Guide*.
Type: String
Required: No

 ** ModuleInfo **
Contains information about the module from which the resource was created, if the resource was created from a module included in the stack template.
Type: [ModuleInfo](API_ModuleInfo.md) object
Required: No

 ** PhysicalResourceId **
The name or unique identifier that corresponds to a physical instance ID of a resource supported by CloudFormation.
Type: String
Required: No

 ** ResourceStatusReason **
Success/failure message associated with the resource.
Type: String
Required: No

 ** StackId **
Unique identifier of the stack.
Type: String
Required: No

 ** StackName **
The name associated with the stack.
Type: String
Required: No

## See Also
<a name="API_StackResourceDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackResourceDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackResourceDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackResourceDetail)
