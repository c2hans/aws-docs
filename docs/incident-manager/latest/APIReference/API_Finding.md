---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_Finding.html
---

# Finding
<a name="API_Finding"></a>

Information about a specific AWS CodeDeploy deployment or AWS CloudFormation stack creation or update that occurred around the time of a reported incident. These activities can be investigated as a potential cause of the incident.

## Contents
<a name="API_Finding_Contents"></a>

 ** creationTime **   <a name="IncidentManager-Type-Finding-creationTime"></a>
The timestamp for when a finding was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="IncidentManager-Type-Finding-id"></a>
The ID assigned to the finding.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: Yes

 ** lastModifiedTime **   <a name="IncidentManager-Type-Finding-lastModifiedTime"></a>
The timestamp for when the finding was most recently updated with additional information.
Type: Timestamp
Required: Yes

 ** details **   <a name="IncidentManager-Type-Finding-details"></a>
Details about the finding.
Type: [FindingDetails](API_FindingDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_Finding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/Finding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/Finding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/Finding)
