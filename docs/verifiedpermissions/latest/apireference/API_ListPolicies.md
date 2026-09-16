---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicies.html
---

# ListPolicies
<a name="API_ListPolicies"></a>

Returns a paginated list of all policies stored in the specified policy store.

## Request Syntax
<a name="API_ListPolicies_RequestSyntax"></a>

```
{
   "filter": {
      "policyTemplateId": "{{string}}",
      "policyType": "{{string}}",
      "principal": { ... },
      "resource": { ... }
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "policyStoreId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListPolicies_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [policyStoreId](#API_ListPolicies_RequestSyntax) **   <a name="verifiedpermissions-ListPolicies-request-policyStoreId"></a>
Specifies the ID of the policy store you want to list policies from.
To specify a policy store, use its ID or alias name. When using an alias name, prefix it with `policy-store-alias/`. For example:
+ ID: `PSEXAMPLEabcdefg111111`
+ Alias name: `policy-store-alias/example-policy-store`
To view aliases, use [ListPolicyStoreAliases](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`
Required: Yes

 ** [filter](#API_ListPolicies_RequestSyntax) **   <a name="verifiedpermissions-ListPolicies-request-filter"></a>
Specifies a filter that limits the response to only policies that match the specified criteria. For example, you list only the policies that reference a specified principal.
Type: [PolicyFilter](API_PolicyFilter.md) object
Required: No

 ** [maxResults](#API_ListPolicies_RequestSyntax) **   <a name="verifiedpermissions-ListPolicies-request-maxResults"></a>
Specifies the total number of results that you want included in each response. If additional items exist beyond the number you specify, the `NextToken` response element is returned with a value (not null). Include the specified value as the `NextToken` request parameter in the next call to the operation to get the next set of results. Note that the service might return fewer results than the maximum even when there are more results available. You should check `NextToken` after every operation to ensure that you receive all of the results.
If you do not specify this parameter, the operation defaults to 10 policies per response. You can specify a maximum of 50 policies per response.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [nextToken](#API_ListPolicies_RequestSyntax) **   <a name="verifiedpermissions-ListPolicies-request-nextToken"></a>
Specifies that you want to receive the next page of results. Valid only if you received a `NextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's `NextToken` response to request the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8000.
Pattern: `[A-Za-z0-9-_=+/\.]*`
Required: No

## Response Syntax
<a name="API_ListPolicies_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "policies": [
      {
         "actions": [
            {
               "actionId": "string",
               "actionType": "string"
            }
         ],
         "createdDate": "string",
         "definition": { ... },
         "effect": "string",
         "lastUpdatedDate": "string",
         "name": "string",
         "policyId": "string",
         "policyStoreId": "string",
         "policyType": "string",
         "principal": {
            "entityId": "string",
            "entityType": "string"
         },
         "resource": {
            "entityId": "string",
            "entityType": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListPolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policies](#API_ListPolicies_ResponseSyntax) **   <a name="verifiedpermissions-ListPolicies-response-policies"></a>
Lists all policies that are available in the specified policy store.
Type: Array of [PolicyItem](API_PolicyItem.md) objects

 ** [nextToken](#API_ListPolicies_ResponseSyntax) **   <a name="verifiedpermissions-ListPolicies-response-nextToken"></a>
If present, this value indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the `NextToken` response element comes back as `null`. This indicates that this is the last page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8000.
Pattern: `[A-Za-z0-9-_=+/\.]*`

## Errors
<a name="API_ListPolicies_Errors"></a>

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
<a name="API_ListPolicies_Examples"></a>

### Example 1
<a name="API_ListPolicies_Example_1"></a>

The following example lists all policies in the policy store.

#### Sample Request
<a name="API_ListPolicies_Example_1_Request"></a>

```
POST HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: identity
X-Amz-Target: VerifiedPermissions.ListPolicies
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "policyStoreId": "PSEXAMPLEabcdefg111111"
}
```

#### Sample Response
<a name="API_ListPolicies_Example_1_Response"></a>

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
    "policies": [
        {
        "createdDate":"2023-05-16T20:33:01.730817Z",
        "effect": "Permit",
        "definition": {
            "static": {
                "description": "Grant members of janeFriends UserGroup access to the vacationFolder Album"
            }
        },
        "lastUpdatedDate": "2023-05-16T21:12:52.882422+00:00",
        "policyId": "SPEXAMPLEabcdefg111111",
        "policyStoreId": "PSEXAMPLEabcdefg111111",
        "policyType": "STATIC",
        "principal": {
            "entityId": "janeFriends",
            "entityType": "UserGroup"
        },
        "actions": [
            {
                "actionId": "ViewPhoto",
                "actionType": "PhotoFlash::Action"
            },
            {
                "actionId": "SharePhoto",
                "actionType": "PhotoFlash::Action"
            }
        ],
        "resource": {
            "entityId": "vacationFolder",
            "entityType": "Album"
        }
    },
    {
        "createdDate": "2023-05-16T21:19:44.528576+00:00",
        "effect": "Permit",
        "definition": {
            "static": {
                "description": "Grant everyone access to the publicFolder Album"
            }
        },
        "lastUpdatedDate": "2023-05-16T21:19:44.528576+00:00",
        "policyId": "SPEXAMPLEabcdefg222222",
        "policyStoreId": "PSEXAMPLEabcdefg111111",
        "policyType": "STATIC",
        "actions": [
            {
                "actionId": "ViewPhoto",
                "actionType": "PhotoFlash::Action"
            },
            {
                "actionId": "SharePhoto",
                "actionType": "PhotoFlash::Action"
            }
        ],
        "resource": {
            "entityId": "publicFolder",
            "entityType": "Album"
        }
    }
    ]
}
```

### Example 2
<a name="API_ListPolicies_Example_2"></a>

The following example lists all policies for a specified principal.

#### Sample Request
<a name="API_ListPolicies_Example_2_Request"></a>

```
POST HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: identity
X-Amz-Target: VerifiedPermissions.ListPolicies
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "filter": {
        "principal": {
            "identifier": {
                "entityType": "User",
                "entityId": "alice"
            }
        }
    }
}
```

#### Sample Response
<a name="API_ListPolicies_Example_2_Response"></a>

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
    "policies": [
        {
            "policyStoreId": "ps-f0ff7596-a721-4df2-8c04-45bcb8e12ccd",
            "policyId": "ip-376c8292-968e-48fb-8b77-5f695e8be789",
            "arn": "arn:aws:verifiedpermissions:123456789012::policy/ps-f0ff7596-a721-4df2-8c04-45bcb8e12ccd/ip-376c8292-968e-48fb-8b77-5f695e8be789",
            "policyType": "STATIC",
            "principal": {
                "entityType": "User",
                "entityId": "alice"
            },
            "actions": [
                {
                    "actionId": "ViewPhoto",
                    "actionType": "PhotoFlash::Action"
                },
                {
                    "actionId": "SharePhoto",
                    "actionType": "PhotoFlash::Action"
                }
            ],
            "resource": {
                "entityType": "Album",
                "entityId": "bob_folder"
            },
            "policyDefinition": {
                "static": {
                    "description": "An example policy"
                }
            },
            "createdDate": "2022-12-09T22:55:16.067533Z",
            "lastUpdatedDate": "2022-12-09T22:55:16.067533Z"
        },
        {
            "policyStoreId": "ps-f0ff7596-a721-4df2-8c04-45bcb8e12ccd",
            "policyId": "ip-9faa0844-24a0-4d81-a937-0ad7b155750a",
            "arn": "arn:aws:verifiedpermissions:123456789012::policy/ps-f0ff7596-a721-4df2-8c04-45bcb8e12ccd/ip-9faa0844-24a0-4d81-a937-0ad7b155750a",
            "policyType": "STATIC",
            "principal": {
                "entityType": "User",
                "entityId": "alice"
            },
            "actions": [
                {
                    "actionId": "ViewPhoto",
                    "actionType": "PhotoFlash::Action"
                },
                {
                    "actionId": "SharePhoto",
                    "actionType": "PhotoFlash::Action"
                }
            ],
            "resource": {
                "entityType": "Album",
                "entityId": "alice_folder"
            },
            "policyDefinition": {
                "static": {}
            },
            "createdDate": "2022-12-09T23:00:24.66266Z",
            "lastUpdatedDate": "2022-12-09T23:00:24.66266Z"
        }
    ]
}
```

### Example 3
<a name="API_ListPolicies_Example_3"></a>

The following example uses the `Filter` parameter to list only the template-linked policies in the specified policy store.

#### Sample Request
<a name="API_ListPolicies_Example_3_Request"></a>

```
POST HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: identity
X-Amz-Target: VerifiedPermissions.ListPolicies
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "filter": {
        "policyType": "TEMPLATE_LINKED"
    }
}
```

#### Sample Response
<a name="API_ListPolicies_Example_3_Response"></a>

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
    "policies": [{
        "policyStoreId": "PSEXAMPLEabcdefg111111",
        "policyId": "TPEXAMPLEabcdefg111111",
        "arn": "arn:aws:verifiedpermissions:us-east-1:123456789012:policy/PSEXAMPLEabcdefg111111/TPEXAMPLEabcdefg111111",
        "policyType": "TEMPLATE_LINKED",
        "principal": {
            "entityType": "User",
            "entityId": "alice"
        },
        "actions": [
            {
                "actionId": "ViewPhoto",
                "actionType": "PhotoFlash::Action"
            },
            {
                "actionId": "SharePhoto",
                "actionType": "PhotoFlash::Action"
            }
        ],
        "resource": {
            "entityType": "Photo",
            "entityId": "pic.jpg"
        },
        "policyDefinition": {
            "templateLinked": {
                "policyTemplateId": "PTEXAMPLEabcdefg111111",
                "principal": {
                    "entityType": "User",
                    "entityId": "alice"
                },
                "actions": [
                    {
                        "actionId": "ViewPhoto",
                        "actionType": "PhotoFlash::Action"
                    },
                    {
                        "actionId": "SharePhoto",
                        "actionType": "PhotoFlash::Action"
                    }
                ],
                "resource": {
                    "entityType": "Photo",
                    "entityId": "pic.jpg"
                }
            }
        },
        "createdDate": "2023-06-13T16:03:07.620867Z",
        "lastUpdatedDate": "2023-06-13T16:03:07.620867Z"
    }]
}
```

### Example 4
<a name="API_ListPolicies_Example_4"></a>

The following example uses the `Filter` parameter to list only those policies that were instantiated from the specified policy template.

#### Sample Request
<a name="API_ListPolicies_Example_4_Request"></a>

```
POST HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: identity
X-Amz-Target: VerifiedPermissions.ListPolicies
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "filter": {
        "policyTemplateId": "PTEXAMPLEabcdefg111111"
    }
}
```

#### Sample Response
<a name="API_ListPolicies_Example_4_Response"></a>

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
    "policies": [{
        "policyStoreId": "PSEXAMPLEabcdefg111111",
        "policyId": "TPEXAMPLEabcdefg111111",
        "arn": "arn:aws:verifiedpermissions::128716708097:policy/PSEXAMPLEabcdefg111111/TPEXAMPLEabcdefg111111",
        "policyType": "TEMPLATE_LINKED",
        "principal": {
            "entityType": "User",
            "entityId": "alice"
        },
        "actions": [
            {
                "actionId": "ViewPhoto",
                "actionType": "PhotoFlash::Action"
            },
            {
                "actionId": "SharePhoto",
                "actionType": "PhotoFlash::Action"
            }
        ],
        "resource": {
            "entityType": "Photo",
            "entityId": "pic.jpg"
        },
        "policyDefinition": {
            "templateLinked": {
                "policyTemplateId": "pt-e42e3eee-8cbc-4af6-a187-4c94773ec89b",
                "principal": {
                    "entityType": "User",
                    "entityId": "alice"
                },
                "actions": [
                    {
                        "actionId": "ViewPhoto",
                        "actionType": "PhotoFlash::Action"
                    },
                    {
                        "actionId": "SharePhoto",
                        "actionType": "PhotoFlash::Action"
                    }
                ],
                "resource": {
                    "entityType": "Photo",
                    "entityId": "pic.jpg"
                }
            }
        },
        "createdDate": "2023-03-15T16:03:07.620867Z",
        "lastUpdatedDate": "2023-03-15T16:03:07.620867Z"
    }]
}
```

## See Also
<a name="API_ListPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/verifiedpermissions-2021-12-01/ListPolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/verifiedpermissions-2021-12-01/ListPolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/ListPolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/verifiedpermissions-2021-12-01/ListPolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/ListPolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/verifiedpermissions-2021-12-01/ListPolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/verifiedpermissions-2021-12-01/ListPolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/verifiedpermissions-2021-12-01/ListPolicies)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/verifiedpermissions-2021-12-01/ListPolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/ListPolicies)
