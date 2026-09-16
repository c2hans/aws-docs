---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateIdentitySource.html
---

# UpdateIdentitySource
<a name="API_UpdateIdentitySource"></a>

Updates the specified identity source to use a new identity provider (IdP), or to change the mapping of identities from the IdP to a different principal entity type.

**Note**
Verified Permissions is * [eventually consistent](https://wikipedia.org/wiki/Eventual_consistency) *. It can take a few seconds for a new or changed element to propagate through the service and be visible in the results of other Verified Permissions operations.

## Request Syntax
<a name="API_UpdateIdentitySource_RequestSyntax"></a>

```
{
   "identitySourceId": "{{string}}",
   "policyStoreId": "{{string}}",
   "principalEntityType": "{{string}}",
   "updateConfiguration": { ... }
}
```

## Request Parameters
<a name="API_UpdateIdentitySource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [identitySourceId](#API_UpdateIdentitySource_RequestSyntax) **   <a name="verifiedpermissions-UpdateIdentitySource-request-identitySourceId"></a>
Specifies the ID of the identity source that you want to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-]*`
Required: Yes

 ** [policyStoreId](#API_UpdateIdentitySource_RequestSyntax) **   <a name="verifiedpermissions-UpdateIdentitySource-request-policyStoreId"></a>
Specifies the ID of the policy store that contains the identity source that you want to update.
To specify a policy store, use its ID or alias name. When using an alias name, prefix it with `policy-store-alias/`. For example:
+ ID: `PSEXAMPLEabcdefg111111`
+ Alias name: `policy-store-alias/example-policy-store`
To view aliases, use [ListPolicyStoreAliases](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`
Required: Yes

 ** [updateConfiguration](#API_UpdateIdentitySource_RequestSyntax) **   <a name="verifiedpermissions-UpdateIdentitySource-request-updateConfiguration"></a>
Specifies the details required to communicate with the identity provider (IdP) associated with this identity source.
Type: [UpdateConfiguration](API_UpdateConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [principalEntityType](#API_UpdateIdentitySource_RequestSyntax) **   <a name="verifiedpermissions-UpdateIdentitySource-request-principalEntityType"></a>
Specifies the data type of principals generated for identities authenticated by the identity source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_UpdateIdentitySource_ResponseSyntax"></a>

```
{
   "createdDate": "string",
   "identitySourceId": "string",
   "lastUpdatedDate": "string",
   "policyStoreId": "string"
}
```

## Response Elements
<a name="API_UpdateIdentitySource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdDate](#API_UpdateIdentitySource_ResponseSyntax) **   <a name="verifiedpermissions-UpdateIdentitySource-response-createdDate"></a>
The date and time that the updated identity source was originally created.
Type: Timestamp

 ** [identitySourceId](#API_UpdateIdentitySource_ResponseSyntax) **   <a name="verifiedpermissions-UpdateIdentitySource-response-identitySourceId"></a>
The ID of the updated identity source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-]*`

 ** [lastUpdatedDate](#API_UpdateIdentitySource_ResponseSyntax) **   <a name="verifiedpermissions-UpdateIdentitySource-response-lastUpdatedDate"></a>
The date and time that the identity source was most recently updated.
Type: Timestamp

 ** [policyStoreId](#API_UpdateIdentitySource_ResponseSyntax) **   <a name="verifiedpermissions-UpdateIdentitySource-response-policyStoreId"></a>
The ID of the policy store that contains the updated identity source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`

## Errors
<a name="API_UpdateIdentitySource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

 ** ConflictException **
The request failed because another request to modify a resource occurred at the same time.
 ** resources **
The list of resources referenced with this failed request.
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
<a name="API_UpdateIdentitySource_Examples"></a>

### Example
<a name="API_UpdateIdentitySource_Example_1"></a>

The following example updates the configuration of the specified identity source with a new user pool configuration.

#### Sample Request
<a name="API_UpdateIdentitySource_Example_1_Request"></a>

```
POST HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: identity
X-Amz-Target: VerifiedPermissions.UpdateIdentitySource
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "identitySourceId": "ISEXAMPLEabcdefg111111",
    "policyStoreId": "PSEXAMPLEabcdefg111111",
    "updateConfiguration": {
        "cognitoUserPoolConfiguration": {
            "userPoolArn": "arn:aws:cognito-idp:us-east-1:123456789012:userpool/us-east-1_1a2b3c4d5",
            "clientIds": ["a1b2c3d4e5f6g7h8i9j0kalbmc"],
            "groupConfiguration": {
              "groupEntityType": "MyCorp::UserGroup"
            }
        }
    },
    "principalEntityType": "MyCorp::User",
    "clientToken": "a1b2c3d4-e5f6-a1b2-c3d4-TOKEN1111111"
}
```

#### Sample Response
<a name="API_UpdateIdentitySource_Example_1_Response"></a>

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
    "createdDate": "2023-05-19T20:30:28.173926Z",
    "identitySourceId": "ISEXAMPLEabcdefg111111",
    "lastUpdatedDate": "2023-05-22T20:45:59.962216Z",
    "policyStoreId":"PSEXAMPLEabcdefg111111"
}
```

### Example
<a name="API_UpdateIdentitySource_Example_2"></a>

The following example updates the configuration of the specified identity source with a new OIDC configuration.

#### Sample Request
<a name="API_UpdateIdentitySource_Example_2_Request"></a>

```
POST HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: identity
X-Amz-Target: VerifiedPermissions.UpdateIdentitySource
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "identitySourceId": "ISEXAMPLEabcdefg111111",
    "policyStoreId": "PSEXAMPLEabcdefg111111",
    "openIdConnectConfiguration": {
        "issuer": "https://auth.example.com",
        "tokenSelection": {
            "accessTokenOnly": {
                "audiences": [
                    "1example23456789",
                    "2example10111213"
                ],
                "principalIdClaim": "sub"
            }
        },
        "entityIdPrefix": "MyOIDCProvider",
        "groupConfiguration": {
            "groupClaim": "groups",
            "groupEntityType": "MyCorp::UserGroup"
        }
    },
    "principalEntityType": "MyCorp::User",
    "clientToken": "a1b2c3d4-e5f6-a1b2-c3d4-TOKEN1111111"
}
```

#### Sample Response
<a name="API_UpdateIdentitySource_Example_2_Response"></a>

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
    "createdDate": "2023-05-19T20:30:28.173926Z",
    "identitySourceId": "ISEXAMPLEabcdefg111111",
    "lastUpdatedDate": "2023-05-22T20:45:59.962216Z",
    "policyStoreId":"PSEXAMPLEabcdefg111111"
}
```

## See Also
<a name="API_UpdateIdentitySource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/verifiedpermissions-2021-12-01/UpdateIdentitySource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/verifiedpermissions-2021-12-01/UpdateIdentitySource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/UpdateIdentitySource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/verifiedpermissions-2021-12-01/UpdateIdentitySource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/UpdateIdentitySource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/verifiedpermissions-2021-12-01/UpdateIdentitySource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/verifiedpermissions-2021-12-01/UpdateIdentitySource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/verifiedpermissions-2021-12-01/UpdateIdentitySource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/verifiedpermissions-2021-12-01/UpdateIdentitySource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/UpdateIdentitySource)
