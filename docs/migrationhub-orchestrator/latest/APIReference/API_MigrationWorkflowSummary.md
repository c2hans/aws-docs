---
source_url: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_MigrationWorkflowSummary.html
---

# MigrationWorkflowSummary
<a name="API_MigrationWorkflowSummary"></a>

The summary of a migration workflow.

## Contents
<a name="API_MigrationWorkflowSummary_Contents"></a>

 ** adsApplicationConfigurationName **   <a name="migrationhuborchestrator-Type-MigrationWorkflowSummary-adsApplicationConfigurationName"></a>
The name of the application configured in Application Discovery Service.
Type: String
Required: No

 ** completedSteps **   <a name="migrationhuborchestrator-Type-MigrationWorkflowSummary-completedSteps"></a>
The steps completed in the migration workflow.
Type: Integer
Required: No

 ** creationTime **   <a name="migrationhuborchestrator-Type-MigrationWorkflowSummary-creationTime"></a>
The time at which the migration workflow was created.
Type: Timestamp
Required: No

 ** endTime **   <a name="migrationhuborchestrator-Type-MigrationWorkflowSummary-endTime"></a>
The time at which the migration workflow ended.
Type: Timestamp
Required: No

 ** id **   <a name="migrationhuborchestrator-Type-MigrationWorkflowSummary-id"></a>
The ID of the migration workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** name **   <a name="migrationhuborchestrator-Type-MigrationWorkflowSummary-name"></a>
The name of the migration workflow.
Type: String
Required: No

 ** status **   <a name="migrationhuborchestrator-Type-MigrationWorkflowSummary-status"></a>
The status of the migration workflow.
Type: String
Valid Values: `CREATING | NOT_STARTED | CREATION_FAILED | STARTING | IN_PROGRESS | WORKFLOW_FAILED | PAUSED | PAUSING | PAUSING_FAILED | USER_ATTENTION_REQUIRED | DELETING | DELETION_FAILED | DELETED | COMPLETED`
Required: No

 ** statusMessage **   <a name="migrationhuborchestrator-Type-MigrationWorkflowSummary-statusMessage"></a>
The status message of the migration workflow.
Type: String
Required: No

 ** templateId **   <a name="migrationhuborchestrator-Type-MigrationWorkflowSummary-templateId"></a>
The ID of the template.
Type: String
Required: No

 ** totalSteps **   <a name="migrationhuborchestrator-Type-MigrationWorkflowSummary-totalSteps"></a>
All the steps in a migration workflow.
Type: Integer
Required: No

## See Also
<a name="API_MigrationWorkflowSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhuborchestrator-2021-08-28/MigrationWorkflowSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhuborchestrator-2021-08-28/MigrationWorkflowSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhuborchestrator-2021-08-28/MigrationWorkflowSummary)
