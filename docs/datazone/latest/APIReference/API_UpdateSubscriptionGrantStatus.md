---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_UpdateSubscriptionGrantStatus.html
---

# UpdateSubscriptionGrantStatus
<a name="API_UpdateSubscriptionGrantStatus"></a>

Updates the status of the specified subscription grant status in Amazon DataZone.

## Request Syntax
<a name="API_UpdateSubscriptionGrantStatus_RequestSyntax"></a>

```
PATCH /v2/domains/{{domainIdentifier}}/subscription-grants/{{identifier}}/status/{{assetIdentifier}} HTTP/1.1
Content-type: application/json

{
   "failureCause": {
      "message": "{{string}}"
   },
   "status": "{{string}}",
   "targetName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateSubscriptionGrantStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assetIdentifier](#API_UpdateSubscriptionGrantStatus_RequestSyntax) **   <a name="datazone-UpdateSubscriptionGrantStatus-request-uri-assetIdentifier"></a>
The identifier of the asset the subscription grant status of which is to be updated.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [domainIdentifier](#API_UpdateSubscriptionGrantStatus_RequestSyntax) **   <a name="datazone-UpdateSubscriptionGrantStatus-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain in which a subscription grant status is to be updated.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_UpdateSubscriptionGrantStatus_RequestSyntax) **   <a name="datazone-UpdateSubscriptionGrantStatus-request-uri-identifier"></a>
The identifier of the subscription grant the status of which is to be updated.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_UpdateSubscriptionGrantStatus_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [failureCause](#API_UpdateSubscriptionGrantStatus_RequestSyntax) **   <a name="datazone-UpdateSubscriptionGrantStatus-request-failureCause"></a>
Specifies the error message that is returned if the operation cannot be successfully completed.
Type: [FailureCause](API_FailureCause.md) object
Required: No

 ** [status](#API_UpdateSubscriptionGrantStatus_RequestSyntax) **   <a name="datazone-UpdateSubscriptionGrantStatus-request-status"></a>
The status to be updated as part of the `UpdateSubscriptionGrantStatus` action.
Type: String
Valid Values: `GRANT_PENDING | REVOKE_PENDING | GRANT_IN_PROGRESS | REVOKE_IN_PROGRESS | GRANTED | REVOKED | GRANT_FAILED | REVOKE_FAILED`
Required: Yes

 ** [targetName](#API_UpdateSubscriptionGrantStatus_RequestSyntax) **   <a name="datazone-UpdateSubscriptionGrantStatus-request-targetName"></a>
The target name to be updated as part of the `UpdateSubscriptionGrantStatus` action.
Type: String
Required: No

## Response Syntax
<a name="API_UpdateSubscriptionGrantStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "assets": [
      {
         "assetId": "string",
         "assetRevision": "string",
         "assetScope": {
            "assetId": "string",
            "errorMessage": "string",
            "filterIds": [ "string" ],
            "scopeName": "string",
            "status": "string"
         },
         "failureCause": {
            "message": "string"
         },
         "failureTimestamp": number,
         "grantedTimestamp": number,
         "permissions": { ... },
         "status": "string",
         "targetName": "string"
      }
   ],
   "createdAt": number,
   "createdBy": "string",
   "domainId": "string",
   "environmentId": "string",
   "grantedEntity": { ... },
   "id": "string",
   "status": "string",
   "subscriptionId": "string",
   "subscriptionTargetId": "string",
   "updatedAt": number,
   "updatedBy": "string"
}
```

## Response Elements
<a name="API_UpdateSubscriptionGrantStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assets](#API_UpdateSubscriptionGrantStatus_ResponseSyntax) **   <a name="datazone-UpdateSubscriptionGrantStatus-response-assets"></a>
The details of the asset for which the subscription grant is created.
Type: Array of [SubscribedAsset](API_SubscribedAsset.md) objects

 ** [createdAt](#API_UpdateSubscriptionGrantStatus_ResponseSyntax) **   <a name="datazone-UpdateSubscriptionGrantStatus-response-createdAt"></a>
The timestamp of when the subscription grant status was created.
Type: Timestamp

 ** [createdBy](#API_UpdateSubscriptionGrantStatus_ResponseSyntax) **   <a name="datazone-UpdateSubscriptionGrantStatus-response-createdBy"></a>
The Amazon DataZone domain user who created the subscription grant status.
Type: String

 ** [domainId](#API_UpdateSubscriptionGrantStatus_ResponseSyntax) **   <a name="datazone-UpdateSubscriptionGrantStatus-response-domainId"></a>
The identifier of the Amazon DataZone domain in which a subscription grant status is to be updated.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [environmentId](#API_UpdateSubscriptionGrantStatus_ResponseSyntax) **   <a name="datazone-UpdateSubscriptionGrantStatus-response-environmentId"></a>
The ID of the environment in which the subscription grant is updated.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [grantedEntity](#API_UpdateSubscriptionGrantStatus_ResponseSyntax) **   <a name="datazone-UpdateSubscriptionGrantStatus-response-grantedEntity"></a>
The granted entity to be updated as part of the `UpdateSubscriptionGrantStatus` action.
Type: [GrantedEntity](API_GrantedEntity.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [id](#API_UpdateSubscriptionGrantStatus_ResponseSyntax) **   <a name="datazone-UpdateSubscriptionGrantStatus-response-id"></a>
The identifier of the subscription grant.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [status](#API_UpdateSubscriptionGrantStatus_ResponseSyntax) **   <a name="datazone-UpdateSubscriptionGrantStatus-response-status"></a>
The status to be updated as part of the `UpdateSubscriptionGrantStatus` action.
Type: String
Valid Values: `PENDING | IN_PROGRESS | GRANT_FAILED | REVOKE_FAILED | GRANT_AND_REVOKE_FAILED | COMPLETED | INACCESSIBLE`

 ** [subscriptionId](#API_UpdateSubscriptionGrantStatus_ResponseSyntax) **   <a name="datazone-UpdateSubscriptionGrantStatus-response-subscriptionId"></a>
 *This parameter has been deprecated.*
The identifier of the subscription.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [subscriptionTargetId](#API_UpdateSubscriptionGrantStatus_ResponseSyntax) **   <a name="datazone-UpdateSubscriptionGrantStatus-response-subscriptionTargetId"></a>
The identifier of the subscription target whose subscription grant status is to be updated.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [updatedAt](#API_UpdateSubscriptionGrantStatus_ResponseSyntax) **   <a name="datazone-UpdateSubscriptionGrantStatus-response-updatedAt"></a>
The timestamp of when the subscription grant status is to be updated.
Type: Timestamp

 ** [updatedBy](#API_UpdateSubscriptionGrantStatus_ResponseSyntax) **   <a name="datazone-UpdateSubscriptionGrantStatus-response-updatedBy"></a>
The Amazon DataZone user who updated the subscription grant status.
Type: String

## Errors
<a name="API_UpdateSubscriptionGrantStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict while performing this action.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateSubscriptionGrantStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/UpdateSubscriptionGrantStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/UpdateSubscriptionGrantStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/UpdateSubscriptionGrantStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/UpdateSubscriptionGrantStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/UpdateSubscriptionGrantStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/UpdateSubscriptionGrantStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/UpdateSubscriptionGrantStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/UpdateSubscriptionGrantStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/UpdateSubscriptionGrantStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/UpdateSubscriptionGrantStatus)
