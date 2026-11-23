---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_UpdatePublisherAssociationApprovalStatus.html
---

# UpdatePublisherAssociationApprovalStatus

Records a curator's decision, `APPROVED` or `REJECTED`, on the publisher association of a registry record. Repeating the decision that the association already has changes nothing. The same `approvalStatus` with a different `approvalStatusReason` updates the reason. If you have no access to a publisher association for the registry record, the request fails with `AccessDeniedException`. The request fails with `ConflictException` if the association isn't in a status that accepts the decision, such as `SUSPENDED`, or if it changed while the request was being applied. Get the association again before you decide whether to resubmit.

## Request Syntax
<a name="API_UpdatePublisherAssociationApprovalStatus_RequestSyntax"></a>

```
PATCH /associations/{{recordArn+}} HTTP/1.1
Content-type: application/json

{
   "approvalStatus": "{{string}}",
   "approvalStatusReason": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdatePublisherAssociationApprovalStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [recordArn](#API_UpdatePublisherAssociationApprovalStatus_RequestSyntax) **   <a name="agentregistrycontrol-UpdatePublisherAssociationApprovalStatus-request-uri-recordArn"></a>
The Amazon Resource Name (ARN) of the registry record whose publisher association you're deciding on.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/[a-zA-Z0-9]{12}`
Required: Yes

## Request Body
<a name="API_UpdatePublisherAssociationApprovalStatus_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [approvalStatus](#API_UpdatePublisherAssociationApprovalStatus_RequestSyntax) **   <a name="agentregistrycontrol-UpdatePublisherAssociationApprovalStatus-request-approvalStatus"></a>
The decision on the association: `APPROVED` or `REJECTED`.
Type: String
Valid Values: `APPROVED | REJECTED`
Required: Yes

 ** [approvalStatusReason](#API_UpdatePublisherAssociationApprovalStatus_RequestSyntax) **   <a name="agentregistrycontrol-UpdatePublisherAssociationApprovalStatus-request-approvalStatusReason"></a>
The reason for the decision. Can be an empty string, and can be up to 255 characters long.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\P{C}\t\r\n]*`
Required: Yes

## Response Syntax
<a name="API_UpdatePublisherAssociationApprovalStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdatePublisherAssociationApprovalStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdatePublisherAssociationApprovalStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller is not authorized to perform the requested action.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource.
HTTP Status Code: 409

 ** InternalServerException **
The request failed due to an unexpected internal error; the caller may retry.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling; the caller may retry after a delay.
HTTP Status Code: 429

 ** ValidationException **
The request failed validation of one or more input fields.
 ** fieldList **
The list of input fields that failed validation.
 ** reason **
The reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_UpdatePublisherAssociationApprovalStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/agent-registry-control-2025-12-01/UpdatePublisherAssociationApprovalStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/agent-registry-control-2025-12-01/UpdatePublisherAssociationApprovalStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatePublisherAssociationApprovalStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/agent-registry-control-2025-12-01/UpdatePublisherAssociationApprovalStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatePublisherAssociationApprovalStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/agent-registry-control-2025-12-01/UpdatePublisherAssociationApprovalStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/agent-registry-control-2025-12-01/UpdatePublisherAssociationApprovalStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/agent-registry-control-2025-12-01/UpdatePublisherAssociationApprovalStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/agent-registry-control-2025-12-01/UpdatePublisherAssociationApprovalStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatePublisherAssociationApprovalStatus)
