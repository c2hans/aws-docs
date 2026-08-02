---
source_url: https://docs.aws.amazon.com/signer/latest/developerguide/authen-apipermissions.html
---

# Use Signer actions in IAM
<a name="authen-apipermissions"></a>

Administrators who set up access control and write permissions policies that they attach to an IAM identity (identity-based policies) can use the following table as a reference. The first column in the table lists each AWS Signer API operation. You specify actions in a policy's `Action` element. You can use the IAM policy elements in your ACM policies to express conditions. For a complete list, see [IAM JSON policy element reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#AvailableKeys) in the *IAM User Guide*.

**Note**
To specify an action, use the `signer` prefix followed by the API operation name (for example, `signer:StartSigningJob`).

**AWS Signer API Operations and Permissions**

|  API Operation  |  Required Permissions (API Actions)  |
| --- | --- |
| [https://docs.aws.amazon.com/signer/latest/api/API_AddProfilePermission.html](https://docs.aws.amazon.com/signer/latest/api/API_AddProfilePermission.html) | `signer:AddProfilePermission` |
| [https://docs.aws.amazon.com/signer/latest/api/API_CancelSigningProfile.html](https://docs.aws.amazon.com/signer/latest/api/API_CancelSigningProfile.html) | `signer:CancelSigningProfile` |
| [https://docs.aws.amazon.com/signer/latest/api/API_DescribeSigningJob.html](https://docs.aws.amazon.com/signer/latest/api/API_DescribeSigningJob.html) | `signer:DescribeSigningJob` |
| [https://docs.aws.amazon.com/signer/latest/api/API_GetRevocationStatus.html](https://docs.aws.amazon.com/signer/latest/api/API_GetRevocationStatus.html) | `signer:GetRevocationStatus` |
| [https://docs.aws.amazon.com/signer/latest/api/API_GetSigningPlatform.html](https://docs.aws.amazon.com/signer/latest/api/API_GetSigningPlatform.html) | `signer:GetSigningPlatform` |
| [https://docs.aws.amazon.com/signer/latest/api/API_GetSigningProfile.html](https://docs.aws.amazon.com/signer/latest/api/API_GetSigningProfile.html) | `signer:GetSigningProfile` |
| [https://docs.aws.amazon.com/signer/latest/api/API_ListProfilePermissions.html](https://docs.aws.amazon.com/signer/latest/api/API_ListProfilePermissions.html) | `signer:ListProfilePermissions` |
| [https://docs.aws.amazon.com/signer/latest/api/API_ListSigningJobs.html](https://docs.aws.amazon.com/signer/latest/api/API_ListSigningJobs.html) | `signer:ListSigningJobs` |
| [https://docs.aws.amazon.com/signer/latest/api/API_ListSigningPlatforms.html](https://docs.aws.amazon.com/signer/latest/api/API_ListSigningPlatforms.html) | `signer:ListSigningPlatforms` |
| [https://docs.aws.amazon.com/signer/latest/api/API_ListSigningProfiles.html](https://docs.aws.amazon.com/signer/latest/api/API_ListSigningProfiles.html) | `signer:ListSigningProfiles` |
| [https://docs.aws.amazon.com/signer/latest/api/API_ListTagsForResource.html](https://docs.aws.amazon.com/signer/latest/api/API_ListTagsForResource.html) | `signer:ListTagsForResource` |
| [https://docs.aws.amazon.com/signer/latest/api/API_PutSigningProfile.html](https://docs.aws.amazon.com/signer/latest/api/API_PutSigningProfile.html) | `signer:PutSigningProfile` |
| [https://docs.aws.amazon.com/signer/latest/api/API_RemoveProfilePermission.html](https://docs.aws.amazon.com/signer/latest/api/API_RemoveProfilePermission.html) | `signer:RemoveProfilePermission` |
| [https://docs.aws.amazon.com/signer/latest/api/API_RevokeSignature.html](https://docs.aws.amazon.com/signer/latest/api/API_RevokeSignature.html) | `signer:RevokeSignature` |
| [https://docs.aws.amazon.com/signer/latest/api/API_RevokeSigningProfile.html](https://docs.aws.amazon.com/signer/latest/api/API_RevokeSigningProfile.html) | `signer:RevokeSigningProfile` |
| [https://docs.aws.amazon.com/signer/latest/api/API_SignPayload.html](https://docs.aws.amazon.com/signer/latest/api/API_SignPayload.html) | `signer:SignPayload` |
| [https://docs.aws.amazon.com/signer/latest/api/API_StartSigningJob.html](https://docs.aws.amazon.com/signer/latest/api/API_StartSigningJob.html) | `signer:StartSigningJob` |
| [https://docs.aws.amazon.com/signer/latest/api/API_TagResource.html](https://docs.aws.amazon.com/signer/latest/api/API_TagResource.html) | `signer:TagResource` |
| [https://docs.aws.amazon.com/signer/latest/api/API_UntagResource.html](https://docs.aws.amazon.com/signer/latest/api/API_UntagResource.html) | `signer:UntagResource` |

For the actions `StartSigningJob`, `GetSigningProfile`, `CancelSigningProfile`,`RevokeSigningProfile`, and `SignPayload`, use the `signer:ProfileVersion` condition key to limit what version of a signing profile a principal has access to.

**AWS Signer API Condition Keys**

|  Condition Key  |  Description  |  APIs  |
| --- | --- | --- |
| `signer:ProfileVersion` | Limit access to a specific version of a Signing Profile  | [https://docs.aws.amazon.com/signer/latest/api/API_StartSigningJob.html](https://docs.aws.amazon.com/signer/latest/api/API_StartSigningJob.html)<br />[https://docs.aws.amazon.com/signer/latest/api/API_GetSigningProfile.html](https://docs.aws.amazon.com/signer/latest/api/API_GetSigningProfile.html)<br />[https://docs.aws.amazon.com/signer/latest/api/API_CancelSigningProfile.html](https://docs.aws.amazon.com/signer/latest/api/API_CancelSigningProfile.html)<br />[https://docs.aws.amazon.com/signer/latest/api/API_RevokeSigningProfile.html](https://docs.aws.amazon.com/signer/latest/api/API_RevokeSigningProfile.html)<br />[https://docs.aws.amazon.com/signer/latest/api/API_SignPayload.html](https://docs.aws.amazon.com/signer/latest/api/API_SignPayload.html) |
