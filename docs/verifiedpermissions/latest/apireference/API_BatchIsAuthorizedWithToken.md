---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorizedWithToken.html
---

# BatchIsAuthorizedWithToken
<a name="API_BatchIsAuthorizedWithToken"></a>

Makes a series of decisions about multiple authorization requests for one token. The principal in this request comes from an external identity source in the form of an identity or access token, formatted as a [JSON web token (JWT)](https://wikipedia.org/wiki/JSON_Web_Token). The information in the parameters can also define additional context that Verified Permissions can include in the evaluations.

The request is evaluated against all policies in the specified policy store that match the entities that you provide in the entities declaration and in the token. The result of the decisions is a series of `Allow` or `Deny` responses, along with the IDs of the policies that produced each decision.

The `entities` of a `BatchIsAuthorizedWithToken` API request can contain up to 100 resources and up to 99 user groups. The `requests` of a `BatchIsAuthorizedWithToken` API request can contain up to 30 requests.

**Note**
The `BatchIsAuthorizedWithToken` operation doesn't have its own IAM permission. To authorize this operation for AWS principals, include the permission `verifiedpermissions:IsAuthorizedWithToken` in their IAM policies.

## Request Syntax
<a name="API_BatchIsAuthorizedWithToken_RequestSyntax"></a>

```
{
   "accessToken": "{{string}}",
   "entities": { ... },
   "identityToken": "{{string}}",
   "policyStoreId": "{{string}}",
   "requests": [
      {
         "action": {
            "actionId": "{{string}}",
            "actionType": "{{string}}"
         },
         "context": { ... },
         "resource": {
            "entityId": "{{string}}",
            "entityType": "{{string}}"
         }
      }
   ]
}
```

## Request Parameters
<a name="API_BatchIsAuthorizedWithToken_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [policyStoreId](#API_BatchIsAuthorizedWithToken_RequestSyntax) **   <a name="verifiedpermissions-BatchIsAuthorizedWithToken-request-policyStoreId"></a>
Specifies the ID of the policy store. Policies in this policy store will be used to make an authorization decision for the input.
To specify a policy store, use its ID or alias name. When using an alias name, prefix it with `policy-store-alias/`. For example:
+ ID: `PSEXAMPLEabcdefg111111`
+ Alias name: `policy-store-alias/example-policy-store`
To view aliases, use [ListPolicyStoreAliases](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`
Required: Yes

 ** [requests](#API_BatchIsAuthorizedWithToken_RequestSyntax) **   <a name="verifiedpermissions-BatchIsAuthorizedWithToken-request-requests"></a>
An array of up to 30 requests that you want Verified Permissions to evaluate.
Type: Array of [BatchIsAuthorizedWithTokenInputItem](API_BatchIsAuthorizedWithTokenInputItem.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** [accessToken](#API_BatchIsAuthorizedWithToken_RequestSyntax) **   <a name="verifiedpermissions-BatchIsAuthorizedWithToken-request-accessToken"></a>
Specifies an access token for the principal that you want to authorize in each request. This token is provided to you by the identity provider (IdP) associated with the specified identity source. You must specify either an `accessToken`, an `identityToken`, or both.
Must be an access token. Verified Permissions returns an error if the `token_use` claim in the submitted token isn't `access`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131072.
Pattern: `[A-Za-z0-9-_=]+.[A-Za-z0-9-_=]+.[A-Za-z0-9-_=]+`
Required: No

 ** [entities](#API_BatchIsAuthorizedWithToken_RequestSyntax) **   <a name="verifiedpermissions-BatchIsAuthorizedWithToken-request-entities"></a>
(Optional) Specifies the list of resources and their associated attributes that Verified Permissions can examine when evaluating the policies. These additional entities and their attributes can be referenced and checked by conditional elements in the policies in the specified policy store.
You can't include principals in this parameter, only resource and action entities. This parameter can't include any entities of a type that matches the user or group entity types that you defined in your identity source.
+ The `BatchIsAuthorizedWithToken` operation takes principal attributes from ** *only* ** the `identityToken` or `accessToken` passed to the operation.
+ For action entities, you can include only their `Identifier` and `EntityType`.
Type: [EntitiesDefinition](API_EntitiesDefinition.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [identityToken](#API_BatchIsAuthorizedWithToken_RequestSyntax) **   <a name="verifiedpermissions-BatchIsAuthorizedWithToken-request-identityToken"></a>
Specifies an identity (ID) token for the principal that you want to authorize in each request. This token is provided to you by the identity provider (IdP) associated with the specified identity source. You must specify either an `accessToken`, an `identityToken`, or both.
Must be an ID token. Verified Permissions returns an error if the `token_use` claim in the submitted token isn't `id`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131072.
Pattern: `[A-Za-z0-9-_=]+.[A-Za-z0-9-_=]+.[A-Za-z0-9-_=]+`
Required: No

## Response Syntax
<a name="API_BatchIsAuthorizedWithToken_ResponseSyntax"></a>

```
{
   "principal": {
      "entityId": "string",
      "entityType": "string"
   },
   "results": [
      {
         "decision": "string",
         "determiningPolicies": [
            {
               "policyId": "string"
            }
         ],
         "errors": [
            {
               "errorDescription": "string"
            }
         ],
         "request": {
            "action": {
               "actionId": "string",
               "actionType": "string"
            },
            "context": { ... },
            "resource": {
               "entityId": "string",
               "entityType": "string"
            }
         }
      }
   ]
}
```

## Response Elements
<a name="API_BatchIsAuthorizedWithToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [results](#API_BatchIsAuthorizedWithToken_ResponseSyntax) **   <a name="verifiedpermissions-BatchIsAuthorizedWithToken-response-results"></a>
A series of `Allow` or `Deny` decisions for each request, and the policies that produced them. These results are returned in the order they were requested.
Type: Array of [BatchIsAuthorizedWithTokenOutputItem](API_BatchIsAuthorizedWithTokenOutputItem.md) objects

 ** [principal](#API_BatchIsAuthorizedWithToken_ResponseSyntax) **   <a name="verifiedpermissions-BatchIsAuthorizedWithToken-response-principal"></a>
The identifier of the principal in the ID or access token.
Type: [EntityIdentifier](API_EntityIdentifier.md) object

## Errors
<a name="API_BatchIsAuthorizedWithToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request failed because of an internal error. Try your request again later
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request failed because it references a resource that doesn't exist.
 ** resourceId **
The unique ID of the resource referenced in the failed request.
 ** resourceType **
The resource type of the resource referenced in the failed request.
HTTP Status Code: 400

 ** ThrottlingException **
The request failed because it exceeded a throttling quota.
 ** quotaCode **
The quota code recognized by the AWS Service Quotas service.
 ** serviceCode **
The code for the AWS service that owns the quota.
HTTP Status Code: 400

 ** ValidationException **
The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.
The possible reasons include the following:
+  **UnrecognizedEntityType**

  The policy includes an entity type that isn't found in the schema.
+  **UnrecognizedActionId**

  The policy includes an action id that isn't found in the schema.
+  **InvalidActionApplication**

  The policy includes an action that, according to the schema, doesn't support the specified principal and resource.
+  **UnexpectedType**

  The policy included an operand that isn't a valid type for the specified operation.
+  **IncompatibleTypes**

  The types of elements included in a `set`, or the types of expressions used in an `if...then...else` clause aren't compatible in this context.
+  **MissingAttribute**

  The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the [has (presence of attribute test) operator](https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test) in the *Cedar Policy Language Guide*.
+  **UnsafeOptionalAttributeAccess**

  The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the [has (presence of attribute test) operator](https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test) in the *Cedar Policy Language Guide*.
+  **ImpossiblePolicy**

  Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.
+  **WrongNumberArguments**

  The policy references an extension type with the wrong number of arguments.
+  **FunctionArgumentValidationError**

  Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.
 ** fieldList **
The list of fields that aren't valid.
HTTP Status Code: 400

## Examples
<a name="API_BatchIsAuthorizedWithToken_Examples"></a>

### Example requests for multiple actions and resource
<a name="API_BatchIsAuthorizedWithToken_Example_1"></a>

The following example requests two authorization decisions for a principal from a user pool token. This variation on the PhotoFlash sample policy store has the following policy:
+  `principal in PhotoFlash::FriendGroup::"us-east-1_EXAMPLE|MyExampleGroup"`

  The user's token contains a `cognito:groups` claim that includes `MyExampleGroup`.
+  `action in [PhotoFlash::Action::"FullPhotoAccess"]`

  The actions `ViewPhoto` and `SharePhoto` have `FullPhotoAccess` as a parent in the policy store schema.
+  `resource in PhotoFlash::Album::"MyExampleAlbum1"`

  The album membership of the photos is declared in `entities`.

The result of this batch of requests is that the user can view and share a photo in an album that is authorized for their friend group, but not a photo in a different album.

#### Sample Request
<a name="API_BatchIsAuthorizedWithToken_Example_1_Request"></a>

```
POST HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: identity
X-Amz-Target: VerifiedPermissions.BatchIsAuthorizedWithToken
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
   "identityToken": "eyJra12345EXAMPLE",
   "requests": [
      {
         "action": {
            "actionType": "PhotoFlash::Action",
            "actionId": "ViewPhoto"
         },
         "resource": {
            "entityType": "PhotoFlash::Photo",
            "entityId": "VacationPhoto94.jpg"
         }
      },
      {
         "action": {
            "actionType": "PhotoFlash::Action",
            "actionId": "SharePhoto"
         },
         "resource": {
            "entityType": "PhotoFlash::Photo",
            "entityId": "VacationPhoto94.jpg"
         }
      },
      {
         "action": {
            "actionType": "PhotoFlash::Action",
            "actionId": "ViewPhoto"
         },
         "resource": {
            "entityType": "PhotoFlash::Photo",
            "entityId": "OfficePhoto94.jpg"
         }
      }
   ],
   "entities": {
      "entityList": [
         {
            "identifier": {
               "entityType": "PhotoFlash::Photo",
               "entityId": "VacationPhoto94.jpg"
            },
            "parents": [
               {
                  "entityType": "PhotoFlash::Album",
                  "entityId": "MyExampleAlbum1"
               }
            ]
         },
         {
            "identifier": {
               "entityType": "PhotoFlash::Photo",
               "entityId": "OfficePhoto94.jpg"
            },
            "parents": [
               {
                  "entityType": "PhotoFlash::Album",
                  "entityId": "MyExampleAlbum2"
               }
            ]
         }
      ]
   },
   "policyStoreId": "PSEXAMPLEabcdefg111111"
}
```

#### Sample Response
<a name="API_BatchIsAuthorizedWithToken_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
vary: origin
vary: access-control-request-method
vary: access-control-request-headers
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive

{
   "principal": {
      "entityType": "PhotoFlash::User",
      "entityId": "us-east-1_EXAMPLE|a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
   },
   "results": [
      {
         "request": {
            "action": {
               "actionType": "PhotoFlash::Action",
               "actionId": "ViewPhoto"
            },
            "resource": {
               "entityType": "PhotoFlash::Photo",
               "entityId": "VacationPhoto94.jpg"
            }
         },
         "decision": "ALLOW",
         "determiningPolicies": [
            {
               "policyId": "SPEXAMPLEabcdefg111111"
            }
         ],
         "errors": []
      },
      {
         "request": {
            "action": {
               "actionType": "PhotoFlash::Action",
               "actionId": "SharePhoto"
            },
            "resource": {
               "entityType": "PhotoFlash::Photo",
               "entityId": "VacationPhoto94.jpg"
            }
         },
         "decision": "ALLOW",
         "determiningPolicies": [
            {
               "policyId": "SPEXAMPLEabcdefg111111"
            }
         ],
         "errors": []
      },
      {
         "request": {
            "action": {
               "actionType": "PhotoFlash::Action",
               "actionId": "ViewPhoto"
            },
            "resource": {
               "entityType": "PhotoFlash::Photo",
               "entityId": "OfficePhoto94.jpg"
            }
         },
         "decision": "DENY",
         "determiningPolicies": [],
         "errors": []
      }
   ]
}
```

## See Also
<a name="API_BatchIsAuthorizedWithToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/verifiedpermissions-2021-12-01/BatchIsAuthorizedWithToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/verifiedpermissions-2021-12-01/BatchIsAuthorizedWithToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/BatchIsAuthorizedWithToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/verifiedpermissions-2021-12-01/BatchIsAuthorizedWithToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/BatchIsAuthorizedWithToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/verifiedpermissions-2021-12-01/BatchIsAuthorizedWithToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/verifiedpermissions-2021-12-01/BatchIsAuthorizedWithToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/verifiedpermissions-2021-12-01/BatchIsAuthorizedWithToken)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/verifiedpermissions-2021-12-01/BatchIsAuthorizedWithToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/BatchIsAuthorizedWithToken)
