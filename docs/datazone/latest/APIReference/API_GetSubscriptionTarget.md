---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetSubscriptionTarget.html
---

# GetSubscriptionTarget
<a name="API_GetSubscriptionTarget"></a>

Gets the subscription target in Amazon DataZone.

## Request Syntax
<a name="API_GetSubscriptionTarget_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/environments/{{environmentIdentifier}}/subscription-targets/{{identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSubscriptionTarget_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_GetSubscriptionTarget_RequestSyntax) **   <a name="datazone-GetSubscriptionTarget-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain in which the subscription target exists.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [environmentIdentifier](#API_GetSubscriptionTarget_RequestSyntax) **   <a name="datazone-GetSubscriptionTarget-request-uri-environmentIdentifier"></a>
The ID of the environment associated with the subscription target.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_GetSubscriptionTarget_RequestSyntax) **   <a name="datazone-GetSubscriptionTarget-request-uri-identifier"></a>
The ID of the subscription target.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_GetSubscriptionTarget_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSubscriptionTarget_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicableAssetTypes": [ "string" ],
   "authorizedPrincipals": [ "string" ],
   "createdAt": number,
   "createdBy": "string",
   "domainId": "string",
   "environmentId": "string",
   "id": "string",
   "manageAccessRole": "string",
   "name": "string",
   "projectId": "string",
   "provider": "string",
   "subscriptionGrantCreationMode": "string",
   "subscriptionTargetConfig": [
      {
         "content": "string",
         "formName": "string"
      }
   ],
   "type": "string",
   "updatedAt": number,
   "updatedBy": "string"
}
```

## Response Elements
<a name="API_GetSubscriptionTarget_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicableAssetTypes](#API_GetSubscriptionTarget_ResponseSyntax) **   <a name="datazone-GetSubscriptionTarget-response-applicableAssetTypes"></a>
The asset types associated with the subscription target.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\.]*.*`

 ** [authorizedPrincipals](#API_GetSubscriptionTarget_ResponseSyntax) **   <a name="datazone-GetSubscriptionTarget-response-authorizedPrincipals"></a>
The authorized principals of the subscription target.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9:/._-]*`

 ** [createdAt](#API_GetSubscriptionTarget_ResponseSyntax) **   <a name="datazone-GetSubscriptionTarget-response-createdAt"></a>
The timestamp of when the subscription target was created.
Type: Timestamp

 ** [createdBy](#API_GetSubscriptionTarget_ResponseSyntax) **   <a name="datazone-GetSubscriptionTarget-response-createdBy"></a>
The Amazon DataZone user who created the subscription target.
Type: String

 ** [domainId](#API_GetSubscriptionTarget_ResponseSyntax) **   <a name="datazone-GetSubscriptionTarget-response-domainId"></a>
The ID of the Amazon DataZone domain in which the subscription target exists.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [environmentId](#API_GetSubscriptionTarget_ResponseSyntax) **   <a name="datazone-GetSubscriptionTarget-response-environmentId"></a>
The ID of the environment associated with the subscription target.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [id](#API_GetSubscriptionTarget_ResponseSyntax) **   <a name="datazone-GetSubscriptionTarget-response-id"></a>
The ID of the subscription target.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [manageAccessRole](#API_GetSubscriptionTarget_ResponseSyntax) **   <a name="datazone-GetSubscriptionTarget-response-manageAccessRole"></a>
The manage access role with which the subscription target was created.
Type: String
Pattern: `arn:aws(|-cn|-us-gov):iam::\d{12}:(role|role/service-role)/[\w+=,.@-]*`

 ** [name](#API_GetSubscriptionTarget_ResponseSyntax) **   <a name="datazone-GetSubscriptionTarget-response-name"></a>
The name of the subscription target.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [projectId](#API_GetSubscriptionTarget_ResponseSyntax) **   <a name="datazone-GetSubscriptionTarget-response-projectId"></a>
The ID of the project associated with the subscription target.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [provider](#API_GetSubscriptionTarget_ResponseSyntax) **   <a name="datazone-GetSubscriptionTarget-response-provider"></a>
The provider of the subscription target.
Type: String

 ** [subscriptionGrantCreationMode](#API_GetSubscriptionTarget_ResponseSyntax) **   <a name="datazone-GetSubscriptionTarget-response-subscriptionGrantCreationMode"></a>
 Determines the subscription grant creation mode for this target, defining if grants are auto-created upon subscription approval or managed manually.
Type: String
Valid Values: `AUTOMATIC | MANUAL`

 ** [subscriptionTargetConfig](#API_GetSubscriptionTarget_ResponseSyntax) **   <a name="datazone-GetSubscriptionTarget-response-subscriptionTargetConfig"></a>
The configuration of teh subscription target.
Type: Array of [SubscriptionTargetForm](API_SubscriptionTargetForm.md) objects

 ** [type](#API_GetSubscriptionTarget_ResponseSyntax) **   <a name="datazone-GetSubscriptionTarget-response-type"></a>
The type of the subscription target.
Type: String

 ** [updatedAt](#API_GetSubscriptionTarget_ResponseSyntax) **   <a name="datazone-GetSubscriptionTarget-response-updatedAt"></a>
The timestamp of when the subscription target was updated.
Type: Timestamp

 ** [updatedBy](#API_GetSubscriptionTarget_ResponseSyntax) **   <a name="datazone-GetSubscriptionTarget-response-updatedBy"></a>
The Amazon DataZone user who updated the subscription target.
Type: String

## Errors
<a name="API_GetSubscriptionTarget_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_GetSubscriptionTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetSubscriptionTarget)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetSubscriptionTarget)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetSubscriptionTarget)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetSubscriptionTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetSubscriptionTarget)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetSubscriptionTarget)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetSubscriptionTarget)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetSubscriptionTarget)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetSubscriptionTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetSubscriptionTarget)
