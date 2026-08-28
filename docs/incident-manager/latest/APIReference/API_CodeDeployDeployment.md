---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_CodeDeployDeployment.html
---

# CodeDeployDeployment
<a name="API_CodeDeployDeployment"></a>

Information about a CodeDeploy deployment that occurred around the time of an incident and could be a possible cause of the incident.

## Contents
<a name="API_CodeDeployDeployment_Contents"></a>

 ** deploymentGroupArn **   <a name="IncidentManager-Type-CodeDeployDeployment-deploymentGroupArn"></a>
The Amazon Resource Name (ARN) of the CodeDeploy deployment group associated with the deployment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: Yes

 ** deploymentId **   <a name="IncidentManager-Type-CodeDeployDeployment-deploymentId"></a>
The ID of the CodeDeploy deployment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: Yes

 ** startTime **   <a name="IncidentManager-Type-CodeDeployDeployment-startTime"></a>
The timestamp for when the CodeDeploy deployment began.
Type: Timestamp
Required: Yes

 ** endTime **   <a name="IncidentManager-Type-CodeDeployDeployment-endTime"></a>
The timestamp for when the CodeDeploy deployment ended. Not reported for deployments that are still in progress.
Type: Timestamp
Required: No

## See Also
<a name="API_CodeDeployDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/CodeDeployDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/CodeDeployDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/CodeDeployDeployment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
