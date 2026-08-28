---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_Types.html
---

# Data Types
<a name="API_Types"></a>

The AWS Fault Injection Simulator API contains several data types that various actions use. This section describes each data type in detail.

**Note**
The order of each element in a data type structure is not guaranteed. Applications should not assume a particular order.

The following data types are supported:
+  [Action](API_Action.md)
+  [ActionParameter](API_ActionParameter.md)
+  [ActionSummary](API_ActionSummary.md)
+  [ActionTarget](API_ActionTarget.md)
+  [CreateExperimentTemplateActionInput](API_CreateExperimentTemplateActionInput.md)
+  [CreateExperimentTemplateExperimentOptionsInput](API_CreateExperimentTemplateExperimentOptionsInput.md)
+  [CreateExperimentTemplateLogConfigurationInput](API_CreateExperimentTemplateLogConfigurationInput.md)
+  [CreateExperimentTemplateReportConfigurationInput](API_CreateExperimentTemplateReportConfigurationInput.md)
+  [CreateExperimentTemplateStopConditionInput](API_CreateExperimentTemplateStopConditionInput.md)
+  [CreateExperimentTemplateTargetInput](API_CreateExperimentTemplateTargetInput.md)
+  [Experiment](API_Experiment.md)
+  [ExperimentAction](API_ExperimentAction.md)
+  [ExperimentActionState](API_ExperimentActionState.md)
+  [ExperimentCloudWatchLogsLogConfiguration](API_ExperimentCloudWatchLogsLogConfiguration.md)
+  [ExperimentError](API_ExperimentError.md)
+  [ExperimentLogConfiguration](API_ExperimentLogConfiguration.md)
+  [ExperimentOptions](API_ExperimentOptions.md)
+  [ExperimentReport](API_ExperimentReport.md)
+  [ExperimentReportConfiguration](API_ExperimentReportConfiguration.md)
+  [ExperimentReportConfigurationCloudWatchDashboard](API_ExperimentReportConfigurationCloudWatchDashboard.md)
+  [ExperimentReportConfigurationDataSources](API_ExperimentReportConfigurationDataSources.md)
+  [ExperimentReportConfigurationOutputs](API_ExperimentReportConfigurationOutputs.md)
+  [ExperimentReportConfigurationOutputsS3Configuration](API_ExperimentReportConfigurationOutputsS3Configuration.md)
+  [ExperimentReportError](API_ExperimentReportError.md)
+  [ExperimentReportS3Report](API_ExperimentReportS3Report.md)
+  [ExperimentReportState](API_ExperimentReportState.md)
+  [ExperimentS3LogConfiguration](API_ExperimentS3LogConfiguration.md)
+  [ExperimentState](API_ExperimentState.md)
+  [ExperimentStopCondition](API_ExperimentStopCondition.md)
+  [ExperimentSummary](API_ExperimentSummary.md)
+  [ExperimentTarget](API_ExperimentTarget.md)
+  [ExperimentTargetAccountConfiguration](API_ExperimentTargetAccountConfiguration.md)
+  [ExperimentTargetAccountConfigurationSummary](API_ExperimentTargetAccountConfigurationSummary.md)
+  [ExperimentTargetFilter](API_ExperimentTargetFilter.md)
+  [ExperimentTemplate](API_ExperimentTemplate.md)
+  [ExperimentTemplateAction](API_ExperimentTemplateAction.md)
+  [ExperimentTemplateCloudWatchLogsLogConfiguration](API_ExperimentTemplateCloudWatchLogsLogConfiguration.md)
+  [ExperimentTemplateCloudWatchLogsLogConfigurationInput](API_ExperimentTemplateCloudWatchLogsLogConfigurationInput.md)
+  [ExperimentTemplateExperimentOptions](API_ExperimentTemplateExperimentOptions.md)
+  [ExperimentTemplateLogConfiguration](API_ExperimentTemplateLogConfiguration.md)
+  [ExperimentTemplateReportConfiguration](API_ExperimentTemplateReportConfiguration.md)
+  [ExperimentTemplateReportConfigurationCloudWatchDashboard](API_ExperimentTemplateReportConfigurationCloudWatchDashboard.md)
+  [ExperimentTemplateReportConfigurationDataSources](API_ExperimentTemplateReportConfigurationDataSources.md)
+  [ExperimentTemplateReportConfigurationDataSourcesInput](API_ExperimentTemplateReportConfigurationDataSourcesInput.md)
+  [ExperimentTemplateReportConfigurationOutputs](API_ExperimentTemplateReportConfigurationOutputs.md)
+  [ExperimentTemplateReportConfigurationOutputsInput](API_ExperimentTemplateReportConfigurationOutputsInput.md)
+  [ExperimentTemplateS3LogConfiguration](API_ExperimentTemplateS3LogConfiguration.md)
+  [ExperimentTemplateS3LogConfigurationInput](API_ExperimentTemplateS3LogConfigurationInput.md)
+  [ExperimentTemplateStopCondition](API_ExperimentTemplateStopCondition.md)
+  [ExperimentTemplateSummary](API_ExperimentTemplateSummary.md)
+  [ExperimentTemplateTarget](API_ExperimentTemplateTarget.md)
+  [ExperimentTemplateTargetFilter](API_ExperimentTemplateTargetFilter.md)
+  [ExperimentTemplateTargetInputFilter](API_ExperimentTemplateTargetInputFilter.md)
+  [ReportConfigurationCloudWatchDashboardInput](API_ReportConfigurationCloudWatchDashboardInput.md)
+  [ReportConfigurationS3Output](API_ReportConfigurationS3Output.md)
+  [ReportConfigurationS3OutputInput](API_ReportConfigurationS3OutputInput.md)
+  [ResolvedTarget](API_ResolvedTarget.md)
+  [SafetyLever](API_SafetyLever.md)
+  [SafetyLeverState](API_SafetyLeverState.md)
+  [StartExperimentExperimentOptionsInput](API_StartExperimentExperimentOptionsInput.md)
+  [TargetAccountConfiguration](API_TargetAccountConfiguration.md)
+  [TargetAccountConfigurationSummary](API_TargetAccountConfigurationSummary.md)
+  [TargetResourceType](API_TargetResourceType.md)
+  [TargetResourceTypeParameter](API_TargetResourceTypeParameter.md)
+  [TargetResourceTypeSummary](API_TargetResourceTypeSummary.md)
+  [UpdateExperimentTemplateActionInputItem](API_UpdateExperimentTemplateActionInputItem.md)
+  [UpdateExperimentTemplateExperimentOptionsInput](API_UpdateExperimentTemplateExperimentOptionsInput.md)
+  [UpdateExperimentTemplateLogConfigurationInput](API_UpdateExperimentTemplateLogConfigurationInput.md)
+  [UpdateExperimentTemplateReportConfigurationInput](API_UpdateExperimentTemplateReportConfigurationInput.md)
+  [UpdateExperimentTemplateStopConditionInput](API_UpdateExperimentTemplateStopConditionInput.md)
+  [UpdateExperimentTemplateTargetInput](API_UpdateExperimentTemplateTargetInput.md)
+  [UpdateSafetyLeverStateInput](API_UpdateSafetyLeverStateInput.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Fault Injection Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
