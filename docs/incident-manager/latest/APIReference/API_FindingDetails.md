---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_FindingDetails.html
---

# FindingDetails
<a name="API_FindingDetails"></a>

Extended textual information about the finding.

## Contents
<a name="API_FindingDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** cloudFormationStackUpdate **   <a name="IncidentManager-Type-FindingDetails-cloudFormationStackUpdate"></a>
Information about the CloudFormation stack creation or update associated with the finding.
Type: [CloudFormationStackUpdate](API_CloudFormationStackUpdate.md) object
Required: No

 ** codeDeployDeployment **   <a name="IncidentManager-Type-FindingDetails-codeDeployDeployment"></a>
Information about the CodeDeploy deployment associated with the finding.
Type: [CodeDeployDeployment](API_CodeDeployDeployment.md) object
Required: No

## See Also
<a name="API_FindingDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/FindingDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/FindingDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/FindingDetails)
