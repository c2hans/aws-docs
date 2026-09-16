---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html
---

# IsAuthorized
<a name="API_IsAuthorized"></a>

Makes an authorization decision about a service request described in the parameters. The information in the parameters can also define additional context that Verified Permissions can include in the evaluation. The request is evaluated against all matching policies in the specified policy store. The result of the decision is either `Allow` or `Deny`, along with a list of the policies that resulted in the decision.

## Request Syntax
<a name="API_IsAuthorized_RequestSyntax"></a>

```
{
   "action": {
      "actionId": "{{string}}",
      "actionType": "{{string}}"
   },
   "context": { ... },
   "entities": { ... },
   "policyStoreId": "{{string}}",
   "principal": {
      "entityId": "{{string}}",
      "entityType": "{{string}}"
   },
   "resource": {
      "entityId": "{{string}}",
      "entityType": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_IsAuthorized_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [policyStoreId](#API_IsAuthorized_RequestSyntax) **   <a name="verifiedpermissions-IsAuthorized-request-policyStoreId"></a>
Specifies the ID of the policy store. Policies in this policy store will be used to make an authorization decision for the input.
To specify a policy store, use its ID or alias name. When using an alias name, prefix it with `policy-store-alias/`. For example:
+ ID: `PSEXAMPLEabcdefg111111`
+ Alias name: `policy-store-alias/example-policy-store`
To view aliases, use [ListPolicyStoreAliases](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`
Required: Yes

 ** [action](#API_IsAuthorized_RequestSyntax) **   <a name="verifiedpermissions-IsAuthorized-request-action"></a>
Specifies the requested action to be authorized. For example, is the principal authorized to perform this action on the resource?
Type: [ActionIdentifier](API_ActionIdentifier.md) object
Required: No

 ** [context](#API_IsAuthorized_RequestSyntax) **   <a name="verifiedpermissions-IsAuthorized-request-context"></a>
Specifies additional context that can be used to make more granular authorization decisions.
Type: [ContextDefinition](API_ContextDefinition.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [entities](#API_IsAuthorized_RequestSyntax) **   <a name="verifiedpermissions-IsAuthorized-request-entities"></a>
(Optional) Specifies the list of resources and principals and their associated attributes that Verified Permissions can examine when evaluating the policies. These additional entities and their attributes can be referenced and checked by conditional elements in the policies in the specified policy store.
You can include only principal and resource entities in this parameter; you can't include actions. You must specify actions in the schema.
Type: [EntitiesDefinition](API_EntitiesDefinition.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [principal](#API_IsAuthorized_RequestSyntax) **   <a name="verifiedpermissions-IsAuthorized-request-principal"></a>
Specifies the principal for which the authorization decision is to be made.
Type: [EntityIdentifier](API_EntityIdentifier.md) object
Required: No

 ** [resource](#API_IsAuthorized_RequestSyntax) **   <a name="verifiedpermissions-IsAuthorized-request-resource"></a>
Specifies the resource for which the authorization decision is to be made.
Type: [EntityIdentifier](API_EntityIdentifier.md) object
Required: No

## Response Syntax
<a name="API_IsAuthorized_ResponseSyntax"></a>

```
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
   ]
}
```

## Response Elements
<a name="API_IsAuthorized_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [decision](#API_IsAuthorized_ResponseSyntax) **   <a name="verifiedpermissions-IsAuthorized-response-decision"></a>
An authorization decision that indicates if the authorization request should be allowed or denied.
Type: String
Valid Values: `ALLOW | DENY`

 ** [determiningPolicies](#API_IsAuthorized_ResponseSyntax) **   <a name="verifiedpermissions-IsAuthorized-response-determiningPolicies"></a>
The list of determining policies used to make the authorization decision. For example, if there are two matching policies, where one is a forbid and the other is a permit, then the forbid policy will be the determining policy. In the case of multiple matching permit policies then there would be multiple determining policies. In the case that no policies match, and hence the response is DENY, there would be no determining policies.
Type: Array of [DeterminingPolicyItem](API_DeterminingPolicyItem.md) objects

 ** [errors](#API_IsAuthorized_ResponseSyntax) **   <a name="verifiedpermissions-IsAuthorized-response-errors"></a>
Errors that occurred while making an authorization decision, for example, a policy references an Entity or entity Attribute that does not exist in the slice.
Type: Array of [EvaluationErrorItem](API_EvaluationErrorItem.md) objects

## Errors
<a name="API_IsAuthorized_Errors"></a>

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
<a name="API_IsAuthorized_Examples"></a>

### Example 1
<a name="API_IsAuthorized_Example_1"></a>

The following example requests an authorization decision for a principal of type `User` named `Alice`, who wants to perform the `updatePhoto` operation, on a resource of type `Photo` named `VacationPhoto94.jpg`.

The response shows that the request was allowed by one policy.

#### Sample Request
<a name="API_IsAuthorized_Example_1_Request"></a>

```
POST HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: identity
X-Amz-Target: VerifiedPermissions.IsAuthorized
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "principal": {
        "entityType": "PhotoFlash::User",
        "entityId": "alice"
    },
    "action": {
        "actionType": "Action",
        "actionId": "updatePhoto"
    },
    "resource": {
        "entityType": "PhotoFlash::Photo",
        "entityId": "VacationPhoto94.jpg"
    },
    "policyStoreId": "PSEXAMPLEabcdefg111111"
}
```

#### Sample Response
<a name="API_IsAuthorized_Example_1_Response"></a>

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
    "decision": "ALLOW",
    "determiningPolicies": [
        {
            "policyId": "SPEXAMPLEabcdefg111111"
        }
    ],
    "errors": []
}
```

### Example 2
<a name="API_IsAuthorized_Example_2"></a>

The following example is the same as the previous example, except that the principal is `User::"bob"`, and the policy store doesn't contain any policy that allows that user access to `Album::"alice_folder".` The output infers that the `Deny` was implicit because the list of `DeterminingPolicies` is empty.

#### Sample Request
<a name="API_IsAuthorized_Example_2_Request"></a>

```
POST HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: identity
X-Amz-Target: VerifiedPermissions.IsAuthorized
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "principal": {
        "entityType": "PhotoFlash::User",
        "entityId": "bob"
    },
    "action": {
        "actionType": "Action",
        "actionId": "view"
    },
    "resource": {
        "entityType": "PhotoFlash::Photo",
        "entityId": "VacationPhoto94.jpg"
    },
    "policyStoreId": "PSEXAMPLEabcdefg111111"
}
```

#### Sample Response
<a name="API_IsAuthorized_Example_2_Response"></a>

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
    "decision": "DENY",
    "determiningPolicies": [],
    "errors": []
}
```

### Example 3 - entityList
<a name="API_IsAuthorized_Example_3"></a>

The following example is a more extensive request for an authorization decision for a principal of type `User` named `alice`, who wants to perform the `updatePhoto` operation, on a resource of type `Photo` named `VacationPhoto94.jpg`. The request includes the optional `entities` element, that specifies that the photo is contained in an `Album` named `alice_folder`. Those additional entities and their attributes can be referenced and checked by conditional elements in the policies in the specified policy store.

In this example, the policy that permits access specifies that `User::"alice"` is allowed to update photos in the folder `Album::"alice_folder"`

This example uses the `entityList` parameter for [EntitiesDefinition](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EntitiesDefinition.html).

#### Sample Request
<a name="API_IsAuthorized_Example_3_Request"></a>

```
POST HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: identity
X-Amz-Target: VerifiedPermissions.IsAuthorized
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
  "policyStoreId": "PSEXAMPLEabcdefg111111",
  "principal": {
      "entityType": "PhotoFlash::User",
      "entityId": "alice"
  },
  "action": {
      "actionType": "Action",
      "actionId": "updatePhoto"
  },
  "resource": {
      "entityType": "PhotoFlash::Photo",
      "entityId": "VacationPhoto94.jpg"
  },
  "entities": {
    "entityList": [
      {
        "identifier": {
            "entityType": "PhotoFlash::Photo",
            "entityId": "VacationPhoto94.jpg"
        },
        "attributes": {},
        "parents": [
            {
                "entityType": "PhotoFlash::Album",
                "entityId": "alice_folder"
            }
        ]
      },
      {
        "identifier": {
            "entityType": "PhotoFlash::Album",
            "entityId": "alice_folder"
        }
      }
    ]
  }
}
```

#### Sample Response
<a name="API_IsAuthorized_Example_3_Response"></a>

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
    "determiningPolicies": [
        {
            "PolicyId": "SPEXAMPLEabcdefg111111"
        }
    ],
    "decision": "ALLOW",
    "errors": []
}
```

### Example 4 - entityList
<a name="API_IsAuthorized_Example_4"></a>

The following example relies on the `DigitalPetStore` sample app and the policy `Customer Role - Get Order`. To satisfy this policy, Alice must be in the `Customer` role and the `Order` must have Alice in the `owner` attribute. To define Alice and the order with these properties, we must dive deeper into the `entities` element and declare that Alice is a customer, and the order is owned by Alice. Because Alice is the customer who placed the order, Verified Permissions returns an `ALLOW` decision to their request for the action `DigitalPetStore::GetOrder`.

This example uses the `entityList` parameter for [EntitiesDefinition](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EntitiesDefinition.html).

#### Sample Request
<a name="API_IsAuthorized_Example_4_Request"></a>

```
POST HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: identity
X-Amz-Target: VerifiedPermissions.IsAuthorized
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

                {
    "principal": {
        "entityType": "DigitalPetStore::User",
        "entityId": "Alice"
    },
    "action": {
        "actionType": "DigitalPetStore::Action",
        "actionId": "GetOrder"
    },
    "resource": {
        "entityType": "DigitalPetStore::Order",
        "entityId": "1234"
    },
    "entities": {
        "entityList": [
            {
                "identifier": {
                    "entityType": "DigitalPetStore::User",
                    "entityId": "Alice"
                },
                "attributes": {
                    "memberId": {
                        "string": "5cad60b9-209c-46d6-bfb7-536c341634ca"
                        }
                },
                "parents": [
                    {
                    "entityType": "DigitalPetStore::Role",
                    "entityId": "Customer"
                    }
                ]
            },
            {
                "identifier": {
                    "entityType": "DigitalPetStore::Order",
                    "entityId": "1234"
                },
                "attributes": {
                    "owner": {
                        "entityIdentifier": {
                            "entityType": "DigitalPetStore::User",
                            "entityId": "Alice"
                        }
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
<a name="API_IsAuthorized_Example_4_Response"></a>

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
    "decision": "ALLOW",
    "determiningPolicies": [
        {
            "policyId": "SPEXAMPLEabcdefg111111"
        }
    ],
    "errors": []
}
```

### Example 5 - cedarJson
<a name="API_IsAuthorized_Example_5"></a>

The following example is a more extensive request for an authorization decision for a principal of type `User` named `alice`, who wants to perform the `updatePhoto` operation, on a resource of type `Photo` named `VacationPhoto94.jpg`. The request includes the optional `entities` element, that specifies that the photo is contained in an `Album` named `alice_folder`. Those additional entities and their attributes can be referenced and checked by conditional elements in the policies in the specified policy store.

In this example, the policy that permits access specifies that `User::"alice"` is allowed to update photos in the folder `Album::"alice_folder"`

This example uses the `cedarJson` parameter for [EntitiesDefinition](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EntitiesDefinition.html).

#### Sample Request
<a name="API_IsAuthorized_Example_5_Request"></a>

```
POST HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: identity
X-Amz-Target: VerifiedPermissions.IsAuthorized
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
  "policyStoreId": "PSEXAMPLEabcdefg111111",
  "principal": {
      "entityType": "PhotoFlash::User",
      "entityId": "alice"
  },
  "action": {
      "actionType": "Action",
      "actionId": "updatePhoto"
  },
  "resource": {
      "entityType": "PhotoFlash::Photo",
      "entityId": "VacationPhoto94.jpg"
  },
  "entities": {
    {"cedarJson": "
            [{\"uid\":{\"type\":\"PhotoFlash::Photo\",\"id\":\"VacationPhoto94.jpg\"},
                \"attrs\":{},
                \"parents\":[{\"type\":\"PhotoFlash::Album\",\"id\":\"alice_folder\"}]}
            ],
            [{\"uid\":{\"type\":\"PhotoFlash::Album\",\"id\":\"alice_folder\"},
                \"attrs\":{},
                \"parents\":[]}
            ]"
        }
  }
}
```

#### Sample Response
<a name="API_IsAuthorized_Example_5_Response"></a>

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
    "determiningPolicies": [
        {
            "PolicyId": "SPEXAMPLEabcdefg111111"
        }
    ],
    "decision": "ALLOW",
    "errors": []
}
```

### Example 6 - cedarJson
<a name="API_IsAuthorized_Example_6"></a>

The following example relies on the `DigitalPetStore` sample app and the policy `Customer Role - Get Order`. To satisfy this policy, Alice must be in the `Customer` role and the `Order` must have Alice in the `owner` attribute. To define Alice and the order with these properties, we must dive deeper into the `entities` element and declare that Alice is a customer, and the order is owned by Alice. Because Alice is the customer who placed the order, Verified Permissions returns an `ALLOW` decision to their request for the action `DigitalPetStore::GetOrder`.

This example uses the `cedarJson` parameter for [EntitiesDefinition](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EntitiesDefinition.html).

#### Sample Request
<a name="API_IsAuthorized_Example_6_Request"></a>

```
POST HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: identity
X-Amz-Target: VerifiedPermissions.IsAuthorized
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

                {
    "principal": {
        "entityType": "DigitalPetStore::User",
        "entityId": "Alice"
    },
    "action": {
        "actionType": "DigitalPetStore::Action",
        "actionId": "GetOrder"
    },
    "resource": {
        "entityType": "DigitalPetStore::Order",
        "entityId": "1234"
    },
    "entities": {
        {"cedarJson": "
            [{\"uid\":{\"type\":\"DigitalPetStore::User\",\"id\":\"Alice\"},
                \"attrs\":{\"memberId\":\"5cad60b9-209c-46d6-bfb7-536c341634ca\"},
                \"parents\":[{\"type\":\"DigitalPetStore::Role\",\"id\":\"Customer\"}]}
            ],
            [{\"uid\":{\"type\":\"DigitalPetStore::Order\",\"id\":\"1234\"},
                \"attrs\":{\"owner\":{\"type\":\"DigitalPetStore::User\",\"id\":\"Alice\"},
                \"parents\":[]}
            ]"
        }
    },
    "policyStoreId": "PSEXAMPLEabcdefg111111"
}
```

#### Sample Response
<a name="API_IsAuthorized_Example_6_Response"></a>

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
    "decision": "ALLOW",
    "determiningPolicies": [
        {
            "policyId": "SPEXAMPLEabcdefg111111"
        }
    ],
    "errors": []
}
```

## See Also
<a name="API_IsAuthorized_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/verifiedpermissions-2021-12-01/IsAuthorized)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/verifiedpermissions-2021-12-01/IsAuthorized)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/IsAuthorized)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/verifiedpermissions-2021-12-01/IsAuthorized)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/IsAuthorized)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/verifiedpermissions-2021-12-01/IsAuthorized)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/verifiedpermissions-2021-12-01/IsAuthorized)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/verifiedpermissions-2021-12-01/IsAuthorized)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/verifiedpermissions-2021-12-01/IsAuthorized)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/IsAuthorized)
