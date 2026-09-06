---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/CommonErrors.html
---

# Common Errors
<a name="CommonErrors"></a>

This section lists the errors that can occur while using AWS Secrets Manager.

 **AccessDeniedException**
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 **DecryptionFailure**   <a name="DecryptionFailure"></a>
Secrets Manager can't decrypt the protected secret text using the provided KMS key.
HTTP Status Code: 400

 **EncryptionFailure**   <a name="EncryptionFailure"></a>
Secrets Manager can't encrypt the protected secret text using the provided KMS key. Check that the KMS key is available, enabled, and not in an invalid state. For more information, see [Key state: Effect on your KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html).
HTTP Status Code: 400

 **IncompleteSignature**   <a name="IncompleteSignature"></a>
The request signature does not conform to AWS standards.
HTTP Status Code: 400

 **InternalFailure**   <a name="InternalFailure"></a>
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 **InternalServiceError**   <a name="InternalServiceError"></a>
An error occurred on the server side.
HTTP Status Code: 500

 **InvalidAction**   <a name="InvalidAction"></a>
The action or operation requested is invalid. Verify that the action is typed correctly.
HTTP Status Code: 400

 **InvalidClientTokenId**   <a name="InvalidClientTokenId"></a>
The X.509 certificate or AWS access key ID provided does not exist in our records.
HTTP Status Code: 403

 **InvalidNextTokenException**   <a name="InvalidNextTokenException"></a>
The `NextToken` value is invalid.
HTTP Status Code: 400

 **InvalidParameterException**   <a name="InvalidParameterException"></a>
The parameter name or value is invalid.
HTTP Status Code: 400

 **InvalidRequestException**   <a name="InvalidRequestException"></a>
A parameter value is not valid for the current state of the resource.
Possible causes:
+ The secret is scheduled for deletion.
+ You tried to enable rotation on a secret that doesn't already have a Lambda function ARN configured and you didn't include such an ARN as a parameter in this call.
+ The secret is managed by another service, and you must use that service to update it. For more information, see [Secrets managed by other AWS services](https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html).
HTTP Status Code: 400

 **LimitExceededException**   <a name="LimitExceededException"></a>
The request failed because it would exceed one of the Secrets Manager quotas.
HTTP Status Code: 400

 **MalformedPolicyDocumentException**   <a name="MalformedPolicyDocumentException"></a>
The resource policy has syntax errors.
HTTP Status Code: 400

 **NotAuthorized**   <a name="NotAuthorized"></a>
You do not have permission to perform this action.
HTTP Status Code: 400

 **OptInRequired**   <a name="OptInRequired"></a>
The AWS access key ID needs a subscription for the service.
HTTP Status Code: 403

 **PreconditionNotMetException**   <a name="PreconditionNotMetException"></a>
The request failed because you did not complete all the prerequisite steps.
HTTP Status Code: 400

 **PublicPolicyException**   <a name="PublicPolicyException"></a>
The `BlockPublicPolicy` parameter is set to true, and the resource policy did not prevent broad access to the secret.
HTTP Status Code: 400

 **RequestExpired**   <a name="RequestExpired"></a>
The request reached the service more than 15 minutes after the date stamp on the request or more than 15 minutes after the request expiration date (such as for pre-signed URLs), or the date stamp on the request is more than 15 minutes in the future.
HTTP Status Code: 400

 **ResourceExistsException**   <a name="ResourceExistsException"></a>
A resource with the ID you requested already exists.
HTTP Status Code: 400

 **ResourceNotFoundException**   <a name="ResourceNotFoundException"></a>
Secrets Manager can't find the resource that you asked for.
HTTP Status Code: 400

 **ServiceUnavailable**   <a name="ServiceUnavailable"></a>
The request has failed due to a temporary failure of the server.
HTTP Status Code: 503

 **ThrottlingException**   <a name="ThrottlingException"></a>
The request was denied due to request throttling.
HTTP Status Code: 400

 **ValidationError**   <a name="ValidationError"></a>
The input fails to satisfy the constraints specified by the service.
HTTP Status Code: 400

 **ValidationException**   <a name="ValidationException"></a>
The input fails to satisfy the constraints specified by the service.
HTTP Status Code: 400
