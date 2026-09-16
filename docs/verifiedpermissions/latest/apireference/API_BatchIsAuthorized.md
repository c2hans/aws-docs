---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorized.html
---

# BatchIsAuthorized
<a name="API_BatchIsAuthorized"></a>

Makes a series of decisions about multiple authorization requests for one principal or resource. Each request contains the equivalent content of an `IsAuthorized` request: principal, action, resource, and context. Either the `principal` or the `resource` parameter must be identical across all requests. For example, Verified Permissions won't evaluate a pair of requests where `bob` views `photo1` and `alice` views `photo2`. Authorization of `bob` to view `photo1` and `photo2`, or `bob` and `alice` to view `photo1`, are valid batches.

The request is evaluated against all policies in the specified policy store that match the entities that you declare. The result of the decisions is a series of `Allow` or `Deny` responses, along with the IDs of the policies that produced each decision.

The `entities` of a `BatchIsAuthorized` API request can contain up to 100 principals and up to 100 resources. The `requests` of a `BatchIsAuthorized` API request can contain up to 30 requests.

**Note**
The `BatchIsAuthorized` operation doesn't have its own IAM permission. To authorize this operation for AWS principals, include the permission `verifiedpermissions:IsAuthorized` in their IAM policies.

## Request Syntax
<a name="API_BatchIsAuthorized_RequestSyntax"></a>

```
{
   "entities": { ... },
   "policyStoreId": "{{string}}",
   "requests": [
      {
         "action": {
            "actionId": "{{string}}",
            "actionType": "{{string}}"
         },
         "context": { ... },
         "principal": {
            "entityId": "{{string}}",
            "entityType": "{{string}}"
         },
         "resource": {
            "entityId": "{{string}}",
            "entityType": "{{string}}"
         }
      }
   ]
}
```

## Request Parameters
<a name="API_BatchIsAuthorized_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [policyStoreId](#API_BatchIsAuthorized_RequestSyntax) **   <a name="verifiedpermissions-BatchIsAuthorized-request-policyStoreId"></a>
Specifies the ID of the policy store. Policies in this policy store will be used to make the authorization decisions for the input.
To specify a policy store, use its ID or alias name. When using an alias name, prefix it with `policy-store-alias/`. For example:
+ ID: `PSEXAMPLEabcdefg111111`
+ Alias name: `policy-store-alias/example-policy-store`
To view aliases, use [ListPolicyStoreAliases](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`
Required: Yes

 ** [requests](#API_BatchIsAuthorized_RequestSyntax) **   <a name="verifiedpermissions-BatchIsAuthorized-request-requests"></a>
An array of up to 30 requests that you want Verified Permissions to evaluate.
Type: Array of [BatchIsAuthorizedInputItem](API_BatchIsAuthorizedInputItem.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** [entities](#API_BatchIsAuthorized_RequestSyntax) **   <a name="verifiedpermissions-BatchIsAuthorized-request-entities"></a>
(Optional) Specifies the list of resources and principals and their associated attributes that Verified Permissions can examine when evaluating the policies. These additional entities and their attributes can be referenced and checked by conditional elements in the policies in the specified policy store.
You can include only principal and resource entities in this parameter; you can't include actions. You must specify actions in the schema.
Type: [EntitiesDefinition](API_EntitiesDefinition.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## Response Syntax
<a name="API_BatchIsAuthorized_ResponseSyntax"></a>

```
{
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
            "principal": {
               "entityId": "string",
               "entityType": "string"
            },
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
<a name="API_BatchIsAuthorized_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [results](#API_BatchIsAuthorized_ResponseSyntax) **   <a name="verifiedpermissions-BatchIsAuthorized-response-results"></a>
A series of `Allow` or `Deny` decisions for each request, and the policies that produced them. These results are returned in the order they were requested.
Type: Array of [BatchIsAuthorizedOutputItem](API_BatchIsAuthorizedOutputItem.md) objects

## Errors
<a name="API_BatchIsAuthorized_Errors"></a>

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
<a name="API_BatchIsAuthorized_Examples"></a>

### Example requests for multiple principals and actions with one resource
<a name="API_BatchIsAuthorized_Example_1"></a>

The following example requests two authorization decisions for two principals of type `User` named `Alice` and `Annalisa`. Alice wants to perform the `ViewPhoto` operation on a resource of type `Photo` named `VacationPhoto94.jpg`. The photo is in Alice's account. Annalisa wants to delete `VacationPhoto94.jpg`.

The response shows that Alice's request was allowed by one policy and Annalisa's request was denied because the photo is in someone else's account.

#### Sample Request
<a name="API_BatchIsAuthorized_Example_1_Request"></a>

```
POST HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: identity
X-Amz-Target: VerifiedPermissions.BatchIsAuthorized
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
   "requests": [
      {
         "principal": {
            "entityType": "PhotoFlash::User",
            "entityId": "Alice"
         },
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
         "principal": {
            "entityType": "PhotoFlash::User",
            "entityId": "Annalisa"
         },
         "action": {
            "actionType": "PhotoFlash::Action",
            "actionId": "DeletePhoto"
         },
         "resource": {
            "entityType": "PhotoFlash::Photo",
            "entityId": "VacationPhoto94.jpg"
         }
      }
   ],
   "entities": {
      "entityList": [
         {
            "identifier": {
               "entityType": "PhotoFlash::User",
               "entityId": "Alice"
            },
            "attributes": {
               "Account": {
                  "entityIdentifier": {
                     "entityType": "PhotoFlash::Account",
                     "entityId": "1234"
                  }
               },
               "Email": {
                  "string": ""
               }
            },
            "parents": []
         },
         {
            "identifier": {
               "entityType": "PhotoFlash::User",
               "entityId": "Annalisa"
            },
            "attributes": {
               "Account": {
                  "entityIdentifier": {
                     "entityType": "PhotoFlash::Account",
                     "entityId": "5678"
                  }
               },
               "Email": {
                  "string": ""
               }
            },
            "parents": []
         },
         {
            "identifier": {
               "entityType": "PhotoFlash::Photo",
               "entityId": "VacationPhoto94.jpg"
            },
            "attributes": {
               "IsPrivate": {
                  "boolean": false
               },
               "Name": {
                  "string": ""
               }
            },
            "parents": [
               {
                  "entityType": "PhotoFlash::Account",
                  "entityId": "1234"
               }
            ]
         },
         {
            "identifier": {
               "entityType": "PhotoFlash::Account",
               "entityId": "1234"
            },
            "attributes": {
               "Name": {
                  "string": ""
               }
            },
            "parents": []
         }
      ]
   },
   "policyStoreId": "PSEXAMPLEabcdefg111111"
}
```

#### Sample Response
<a name="API_BatchIsAuthorized_Example_1_Response"></a>

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
   "results": [
      {
         "request": {
            "principal": {
               "entityType": "PhotoFlash::User",
               "entityId": "alice"
            },
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
            "principal": {
               "entityType": "PhotoFlash::User",
               "entityId": "annalisa"
            },
            "action": {
               "actionType": "PhotoFlash::Action",
               "actionId": "DeletePhoto"
            },
            "resource": {
               "entityType": "PhotoFlash::Photo",
               "entityId": "VacationPhoto94.jpg"
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
<a name="API_BatchIsAuthorized_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/verifiedpermissions-2021-12-01/BatchIsAuthorized)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/verifiedpermissions-2021-12-01/BatchIsAuthorized)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/BatchIsAuthorized)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/verifiedpermissions-2021-12-01/BatchIsAuthorized)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/BatchIsAuthorized)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/verifiedpermissions-2021-12-01/BatchIsAuthorized)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/verifiedpermissions-2021-12-01/BatchIsAuthorized)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/verifiedpermissions-2021-12-01/BatchIsAuthorized)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/verifiedpermissions-2021-12-01/BatchIsAuthorized)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/BatchIsAuthorized)
