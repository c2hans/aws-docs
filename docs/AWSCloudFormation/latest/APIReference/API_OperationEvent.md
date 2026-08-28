---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_OperationEvent.html
---

# OperationEvent
<a name="API_OperationEvent"></a>

Contains detailed information about an event that occurred during a CloudFormation operation.

## Contents
<a name="API_OperationEvent_Contents"></a>

 ** ClientRequestToken **
A unique identifier for the request that initiated this operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][-a-zA-Z0-9]*`
Required: No

 ** DetailedStatus **
Additional status information about the operation.
Type: String
Valid Values: `CONFIGURATION_COMPLETE | VALIDATION_FAILED`
Required: No

 ** EndTime **
The time when the event ended.
Type: Timestamp
Required: No

 ** EventId **
A unique identifier for this event.
Type: String
Required: No

 ** EventType **
The type of event.
Type: String
Valid Values: `STACK_EVENT | PROGRESS_EVENT | VALIDATION_ERROR | PROVISIONING_ERROR | HOOK_INVOCATION_ERROR`
Required: No

 ** HookFailureMode **
Specifies how Hook failures are handled.
Type: String
Valid Values: `FAIL | WARN`
Required: No

 ** HookInvocationPoint **
The point in the operation lifecycle when the Hook was invoked.
Type: String
Valid Values: `PRE_PROVISION`
Required: No

 ** HookStatus **
The status of the Hook invocation.
Type: String
Valid Values: `HOOK_IN_PROGRESS | HOOK_COMPLETE_SUCCEEDED | HOOK_COMPLETE_FAILED | HOOK_FAILED`
Required: No

 ** HookStatusReason **
Additional information about the Hook status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** HookType **
The type name of the Hook that was invoked.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** LogicalResourceId **
The logical name of the resource as specified in the template.
Type: String
Required: No

 ** OperationId **
The unique identifier of the operation this event belongs to.
Type: String
Required: No

 ** OperationStatus **
The current status of the operation.
Type: String
Valid Values: `IN_PROGRESS | SUCCEEDED | FAILED`
Required: No

 ** OperationType **
The type of operation.
Type: String
Valid Values: `CREATE_STACK | UPDATE_STACK | DELETE_STACK | CONTINUE_ROLLBACK | ROLLBACK | CREATE_CHANGESET`
Required: No

 ** PhysicalResourceId **
The name or unique identifier that corresponds to a physical instance ID of a resource.
Type: String
Required: No

 ** ResourceProperties **
The properties used to create the resource.
Type: String
Required: No

 ** ResourceStatus **
Current status of the resource.
Type: String
Valid Values: `CREATE_IN_PROGRESS | CREATE_FAILED | CREATE_COMPLETE | DELETE_IN_PROGRESS | DELETE_FAILED | DELETE_COMPLETE | DELETE_SKIPPED | UPDATE_IN_PROGRESS | UPDATE_FAILED | UPDATE_COMPLETE | IMPORT_FAILED | IMPORT_COMPLETE | IMPORT_IN_PROGRESS | IMPORT_ROLLBACK_IN_PROGRESS | IMPORT_ROLLBACK_FAILED | IMPORT_ROLLBACK_COMPLETE | EXPORT_FAILED | EXPORT_COMPLETE | EXPORT_IN_PROGRESS | EXPORT_ROLLBACK_IN_PROGRESS | EXPORT_ROLLBACK_FAILED | EXPORT_ROLLBACK_COMPLETE | UPDATE_ROLLBACK_IN_PROGRESS | UPDATE_ROLLBACK_COMPLETE | UPDATE_ROLLBACK_FAILED | ROLLBACK_IN_PROGRESS | ROLLBACK_COMPLETE | ROLLBACK_FAILED`
Required: No

 ** ResourceStatusReason **
Success or failure message associated with the resource.
Type: String
Required: No

 ** ResourceType **
Type of resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** StackId **
The unique ID name of the instance of the stack.
Type: String
Required: No

 ** StartTime **
The time when the event started.
Type: Timestamp
Required: No

 ** Timestamp **
Time the status was updated.
Type: Timestamp
Required: No

 ** ValidationFailureMode **
Specifies how validation failures are handled.
Type: String
Valid Values: `FAIL | WARN`
Required: No

 ** ValidationName **
The name of the validation that was performed.
Type: String
Required: No

 ** ValidationPath **
The path within the resource where the validation was applied.
Type: String
Required: No

 ** ValidationStatus **
The status of the validation.
Type: String
Valid Values: `FAILED | SKIPPED`
Required: No

 ** ValidationStatusReason **
Additional information about the validation status.
Type: String
Required: No

## See Also
<a name="API_OperationEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/OperationEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/OperationEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/OperationEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
