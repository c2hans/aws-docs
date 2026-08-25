---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_AssociationExecution.html
---

# AssociationExecution
<a name="API_AssociationExecution"></a>

Includes information about the specified association.

## Contents
<a name="API_AssociationExecution_Contents"></a>

 ** AlarmConfiguration **   <a name="systemsmanager-Type-AssociationExecution-AlarmConfiguration"></a>
The details for the CloudWatch alarm you want to apply to an automation or command.
Type: [AlarmConfiguration](API_AlarmConfiguration.md) object
Required: No

 ** AssociationId **   <a name="systemsmanager-Type-AssociationExecution-AssociationId"></a>
The association ID.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: No

 ** AssociationVersion **   <a name="systemsmanager-Type-AssociationExecution-AssociationVersion"></a>
The association version.
Type: String
Pattern: `^(([$]LATEST)|([1-9][0-9]*))$`
Required: No

 ** CreatedTime **   <a name="systemsmanager-Type-AssociationExecution-CreatedTime"></a>
The time the execution started.
Type: Timestamp
Required: No

 ** DetailedStatus **   <a name="systemsmanager-Type-AssociationExecution-DetailedStatus"></a>
Detailed status information about the execution.
Type: String
Required: No

 ** ExecutionId **   <a name="systemsmanager-Type-AssociationExecution-ExecutionId"></a>
The execution ID for the association.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: No

 ** LastExecutionDate **   <a name="systemsmanager-Type-AssociationExecution-LastExecutionDate"></a>
The date of the last execution.
Type: Timestamp
Required: No

 ** ResourceCountByStatus **   <a name="systemsmanager-Type-AssociationExecution-ResourceCountByStatus"></a>
An aggregate status of the resources in the execution based on the status type.
Type: String
Required: No

 ** Status **   <a name="systemsmanager-Type-AssociationExecution-Status"></a>
The status of the association execution.
Type: String
Required: No

 ** TriggeredAlarms **   <a name="systemsmanager-Type-AssociationExecution-TriggeredAlarms"></a>
The CloudWatch alarms that were invoked by the association.
Type: Array of [AlarmStateInformation](API_AlarmStateInformation.md) objects
Array Members: Fixed number of 1 item.
Required: No

## See Also
<a name="API_AssociationExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/AssociationExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/AssociationExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/AssociationExecution)
