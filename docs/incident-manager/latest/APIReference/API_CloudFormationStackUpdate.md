---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_CloudFormationStackUpdate.html
---

# CloudFormationStackUpdate
<a name="API_CloudFormationStackUpdate"></a>

Information about an AWS CloudFormation stack creation or update that occurred around the time of an incident and could be a potential cause of the incident.

## Contents
<a name="API_CloudFormationStackUpdate_Contents"></a>

 ** stackArn **   <a name="IncidentManager-Type-CloudFormationStackUpdate-stackArn"></a>
The Amazon Resource Name (ARN) of the CloudFormation stack involved in the update.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: Yes

 ** startTime **   <a name="IncidentManager-Type-CloudFormationStackUpdate-startTime"></a>
The timestamp for when the CloudFormation stack creation or update began.
Type: Timestamp
Required: Yes

 ** endTime **   <a name="IncidentManager-Type-CloudFormationStackUpdate-endTime"></a>
The timestamp for when the CloudFormation stack creation or update ended. Not reported for deployments that are still in progress.
Type: Timestamp
Required: No

## See Also
<a name="API_CloudFormationStackUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/CloudFormationStackUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/CloudFormationStackUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/CloudFormationStackUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
