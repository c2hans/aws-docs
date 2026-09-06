---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/CommonErrors.html
---

# Common Errors
<a name="CommonErrors"></a>

This section lists the errors common to the API actions of all AWS services. For errors specific to an API action for this service, see the topic for that API action.

 **AccessDeniedException**
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 **IncompleteSignature**
The request signature does not conform to AWS standards.
HTTP Status Code: 400

 **InternalFailure**   <a name="CommonErrors-InternalFailure"></a>
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 **InvalidAction**   <a name="CommonErrors-InvalidAction"></a>
The action or operation requested is invalid. Verify that the action is typed correctly.
HTTP Status Code: 400

 **InvalidClientTokenId**   <a name="CommonErrors-InvalidClientTokenId"></a>
The X.509 certificate or AWS access key ID provided does not exist in our records.
HTTP Status Code: 403

 **NotAuthorized**   <a name="CommonErrors-NotAuthorized"></a>
You do not have permission to perform this action.
HTTP Status Code: 400

 **OptInRequired**   <a name="CommonErrors-OptInRequired"></a>
The AWS access key ID needs a subscription for the service.
HTTP Status Code: 403

 **RequestExpired**   <a name="CommonErrors-RequestExpired"></a>
The request reached the service more than 15 minutes after the date stamp on the request or more than 15 minutes after the request expiration date (such as for pre-signed URLs), or the date stamp on the request is more than 15 minutes in the future.
HTTP Status Code: 400

 **ServiceUnavailable**   <a name="CommonErrors-ServiceUnavailable"></a>
The request has failed due to a temporary failure of the server.
HTTP Status Code: 503

 **ThrottlingException**   <a name="CommonErrors-ThrottlingException"></a>
The request was denied due to request throttling.
HTTP Status Code: 400

 **CallsPerSecondLimit**   <a name="CommonErrors-CallsPerSecondLimit"></a>
The request was denied due to too many calls initiated.
HTTP Status Code: 403

 **ConcurrentCallLimit**   <a name="CommonErrors-ConcurrentCallLimit"></a>
The request was denied due to too many concurrent calls initiated.
HTTP Status Code: 403

 **ValidationError**   <a name="CommonErrors-ValidationError"></a>
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400
