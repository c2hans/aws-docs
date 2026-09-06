---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_InstanceAssociationStatusInfo.html
---

# InstanceAssociationStatusInfo
<a name="API_InstanceAssociationStatusInfo"></a>

Status information about the association.

## Contents
<a name="API_InstanceAssociationStatusInfo_Contents"></a>

 ** AssociationId **   <a name="systemsmanager-Type-InstanceAssociationStatusInfo-AssociationId"></a>
The association ID.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: No

 ** AssociationName **   <a name="systemsmanager-Type-InstanceAssociationStatusInfo-AssociationName"></a>
The name of the association applied to the managed node.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: No

 ** AssociationVersion **   <a name="systemsmanager-Type-InstanceAssociationStatusInfo-AssociationVersion"></a>
The version of the association applied to the managed node.
Type: String
Pattern: `^(([$]LATEST)|([1-9][0-9]*))$`
Required: No

 ** DetailedStatus **   <a name="systemsmanager-Type-InstanceAssociationStatusInfo-DetailedStatus"></a>
Detailed status information about the association.
Type: String
Required: No

 ** DocumentVersion **   <a name="systemsmanager-Type-InstanceAssociationStatusInfo-DocumentVersion"></a>
The association document versions.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
Required: No

 ** ErrorCode **   <a name="systemsmanager-Type-InstanceAssociationStatusInfo-ErrorCode"></a>
An error code returned by the request to create the association.
Type: String
Length Constraints: Maximum length of 10.
Required: No

 ** ExecutionDate **   <a name="systemsmanager-Type-InstanceAssociationStatusInfo-ExecutionDate"></a>
The date the association ran.
Type: Timestamp
Required: No

 ** ExecutionSummary **   <a name="systemsmanager-Type-InstanceAssociationStatusInfo-ExecutionSummary"></a>
Summary information about association execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** InstanceId **   <a name="systemsmanager-Type-InstanceAssociationStatusInfo-InstanceId"></a>
The managed node ID where the association was created.
Type: String
Pattern: `(^i-(\w{8}|\w{17})$)|(^mi-\w{17}$)`
Required: No

 ** Name **   <a name="systemsmanager-Type-InstanceAssociationStatusInfo-Name"></a>
The name of the association.
Type: String
Pattern: `^[a-zA-Z0-9_\-.:/]{3,128}$`
Required: No

 ** OutputUrl **   <a name="systemsmanager-Type-InstanceAssociationStatusInfo-OutputUrl"></a>
A URL for an S3 bucket where you want to store the results of this request.
Type: [InstanceAssociationOutputUrl](API_InstanceAssociationOutputUrl.md) object
Required: No

 ** Status **   <a name="systemsmanager-Type-InstanceAssociationStatusInfo-Status"></a>
Status information about the association.
Type: String
Required: No

## See Also
<a name="API_InstanceAssociationStatusInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/InstanceAssociationStatusInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/InstanceAssociationStatusInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/InstanceAssociationStatusInfo)
