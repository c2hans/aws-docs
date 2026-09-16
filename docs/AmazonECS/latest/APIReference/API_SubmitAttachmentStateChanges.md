---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_SubmitAttachmentStateChanges.html
---

# SubmitAttachmentStateChanges
<a name="API_SubmitAttachmentStateChanges"></a>

**Note**
This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.

Sent to acknowledge that an attachment changed states.

## Request Syntax
<a name="API_SubmitAttachmentStateChanges_RequestSyntax"></a>

```
{
   "attachments": [
      {
         "attachmentArn": "{{string}}",
         "status": "{{string}}"
      }
   ],
   "cluster": "{{string}}"
}
```

## Request Parameters
<a name="API_SubmitAttachmentStateChanges_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [attachments](#API_SubmitAttachmentStateChanges_RequestSyntax) **   <a name="ECS-SubmitAttachmentStateChanges-request-attachments"></a>
Any attachments associated with the state change request.
Type: Array of [AttachmentStateChange](API_AttachmentStateChange.md) objects
Required: Yes

 ** [cluster](#API_SubmitAttachmentStateChanges_RequestSyntax) **   <a name="ECS-SubmitAttachmentStateChanges-request-cluster"></a>
The short name or full ARN of the cluster that hosts the container instance the attachment belongs to.
Type: String
Required: No

## Response Syntax
<a name="API_SubmitAttachmentStateChanges_ResponseSyntax"></a>

```
{
   "acknowledgment": "string"
}
```

## Response Elements
<a name="API_SubmitAttachmentStateChanges_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [acknowledgment](#API_SubmitAttachmentStateChanges_ResponseSyntax) **   <a name="ECS-SubmitAttachmentStateChanges-response-acknowledgment"></a>
Acknowledgement of the state change.
Type: String

## Errors
<a name="API_SubmitAttachmentStateChanges_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have authorization to perform the requested action.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ClientException **
These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ClusterNotFoundException **
The specified cluster wasn't found. You can view your available clusters with [ListClusters](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html). Amazon ECS clusters are Region specific.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** InvalidParameterException **
The specified parameter isn't valid. Review the available parameters for the API request.
For more information about service event errors, see [Amazon ECS service event messages](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html).
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server issue.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 500

## See Also
<a name="API_SubmitAttachmentStateChanges_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/SubmitAttachmentStateChanges)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/SubmitAttachmentStateChanges)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/SubmitAttachmentStateChanges)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/SubmitAttachmentStateChanges)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/SubmitAttachmentStateChanges)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/SubmitAttachmentStateChanges)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/SubmitAttachmentStateChanges)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/SubmitAttachmentStateChanges)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/SubmitAttachmentStateChanges)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/SubmitAttachmentStateChanges)
