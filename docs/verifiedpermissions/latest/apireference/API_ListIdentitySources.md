---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListIdentitySources.html
---

# ListIdentitySources
<a name="API_ListIdentitySources"></a>

Returns a paginated list of all of the identity sources defined in the specified policy store.

## Request Syntax
<a name="API_ListIdentitySources_RequestSyntax"></a>

```
{
   "filters": [
      {
         "principalEntityType": "{{string}}"
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "policyStoreId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListIdentitySources_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [policyStoreId](#API_ListIdentitySources_RequestSyntax) **   <a name="verifiedpermissions-ListIdentitySources-request-policyStoreId"></a>
Specifies the ID of the policy store that contains the identity sources that you want to list.
To specify a policy store, use its ID or alias name. When using an alias name, prefix it with `policy-store-alias/`. For example:
+ ID: `PSEXAMPLEabcdefg111111`
+ Alias name: `policy-store-alias/example-policy-store`
To view aliases, use [ListPolicyStoreAliases](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`
Required: Yes

 ** [filters](#API_ListIdentitySources_RequestSyntax) **   <a name="verifiedpermissions-ListIdentitySources-request-filters"></a>
Specifies characteristics of an identity source that you can use to limit the output to matching identity sources.
Type: Array of [IdentitySourceFilter](API_IdentitySourceFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [maxResults](#API_ListIdentitySources_RequestSyntax) **   <a name="verifiedpermissions-ListIdentitySources-request-maxResults"></a>
Specifies the total number of results that you want included in each response. If additional items exist beyond the number you specify, the `NextToken` response element is returned with a value (not null). Include the specified value as the `NextToken` request parameter in the next call to the operation to get the next set of results. Note that the service might return fewer results than the maximum even when there are more results available. You should check `NextToken` after every operation to ensure that you receive all of the results.
If you do not specify this parameter, the operation defaults to 10 identity sources per response. You can specify a maximum of 50 identity sources per response.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [nextToken](#API_ListIdentitySources_RequestSyntax) **   <a name="verifiedpermissions-ListIdentitySources-request-nextToken"></a>
Specifies that you want to receive the next page of results. Valid only if you received a `NextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's `NextToken` response to request the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8000.
Pattern: `[A-Za-z0-9-_=+/\.]*`
Required: No

## Response Syntax
<a name="API_ListIdentitySources_ResponseSyntax"></a>

```
{
   "identitySources": [
      {
         "configuration": { ... },
         "createdDate": "string",
         "details": {
            "clientIds": [ "string" ],
            "discoveryUrl": "string",
            "openIdIssuer": "string",
            "userPoolArn": "string"
         },
         "identitySourceId": "string",
         "lastUpdatedDate": "string",
         "policyStoreId": "string",
         "principalEntityType": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListIdentitySources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [identitySources](#API_ListIdentitySources_ResponseSyntax) **   <a name="verifiedpermissions-ListIdentitySources-response-identitySources"></a>
The list of identity sources stored in the specified policy store.
Type: Array of [IdentitySourceItem](API_IdentitySourceItem.md) objects

 ** [nextToken](#API_ListIdentitySources_ResponseSyntax) **   <a name="verifiedpermissions-ListIdentitySources-response-nextToken"></a>
If present, this value indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the `NextToken` response element comes back as `null`. This indicates that this is the last page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8000.
Pattern: `[A-Za-z0-9-_=+/\.]*`

## Errors
<a name="API_ListIdentitySources_Errors"></a>

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
<a name="API_ListIdentitySources_Examples"></a>

### Example
<a name="API_ListIdentitySources_Example_1"></a>

The following example request creates lists the identity sources currently defined in the specified policy store.

#### Sample Request
<a name="API_ListIdentitySources_Example_1_Request"></a>

```
POST HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: identity
X-Amz-Target: VerifiedPermissions.ListIdentitySources
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "policyStoreId": "PSEXAMPLEabcdefg111111"
}
```

#### Sample Response
<a name="API_ListIdentitySources_Example_1_Response"></a>

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
    "identitySources": [
        {
            "createdDate": "2023-05-19T20:29:23.66812Z",
            "details": {
                "clientIds": ["a1b2c3d4e5f6g7h8i9j0kalbmc"],
                "userPoolArn":"arn:aws:cognito-idp:us-east-1:123456789012:userpool/us-east-1_1a2b3c4d5",
                "discoveryUrl":"https://cognito-idp.us-east-1.amazonaws.com/us-east-1_1a2b3c4d5",
                "openIdIssuer":"COGNITO"
            },
            "identitySourceId":"ISEXAMPLEabcdefg111111",
            "lastUpdatedDate":"2023-05-19T20:29:23.66812Z",
            "policyStoreId":"PSEXAMPLEabcdefg111111",
            "principalEntityType":"MyCorp::User",
            "configuration": {
               "cognitoUserPoolConfiguration": {
                   "userPoolArn": "arn:aws:cognito-idp:us-east-1:123456789012:userpool/us-east-1_1a2b3c4d5",
                   "clientIds": [],
                   "issuer": "https://cognito-idp.us-east-1.amazonaws.com/us-east-1_1a2b3c4d5",
                   "groupConfiguration": {
                       "groupEntityType": "MyCorp::UserGroup"
                   }
               }
            }
        }
    ]
}
```

## See Also
<a name="API_ListIdentitySources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/verifiedpermissions-2021-12-01/ListIdentitySources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/verifiedpermissions-2021-12-01/ListIdentitySources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/ListIdentitySources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/verifiedpermissions-2021-12-01/ListIdentitySources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/ListIdentitySources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/verifiedpermissions-2021-12-01/ListIdentitySources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/verifiedpermissions-2021-12-01/ListIdentitySources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/verifiedpermissions-2021-12-01/ListIdentitySources)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/verifiedpermissions-2021-12-01/ListIdentitySources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/ListIdentitySources)
