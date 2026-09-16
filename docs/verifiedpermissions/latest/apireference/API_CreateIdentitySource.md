---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreateIdentitySource.html
---

# CreateIdentitySource
<a name="API_CreateIdentitySource"></a>

Adds an identity source to a policy store–an Amazon Cognito user pool or OpenID Connect (OIDC) identity provider (IdP).

After you create an identity source, you can use the identities provided by the IdP as proxies for the principal in authorization queries that use the [IsAuthorizedWithToken](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html) or [BatchIsAuthorizedWithToken](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorizedWithToken.html) API operations. These identities take the form of tokens that contain claims about the user, such as IDs, attributes and group memberships. Identity sources provide identity (ID) tokens and access tokens. Verified Permissions derives information about your user and session from token claims. Access tokens provide action `context` to your policies, and ID tokens provide principal `Attributes`.

**Important**
Tokens from an identity source user continue to be usable until they expire. Token revocation and resource deletion have no effect on the validity of a token in your policy store

**Note**
To reference a user from this identity source in your Cedar policies, refer to the following syntax examples.
Amazon Cognito user pool: `Namespace::[Entity type]::[User pool ID]|[user principal attribute]`, for example `MyCorp::User::us-east-1_EXAMPLE|a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`.
OpenID Connect (OIDC) provider: `Namespace::[Entity type]::[entityIdPrefix]|[user principal attribute]`, for example `MyCorp::User::MyOIDCProvider|a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`.

**Note**
Verified Permissions is * [eventually consistent](https://wikipedia.org/wiki/Eventual_consistency) *. It can take a few seconds for a new or changed element to propagate through the service and be visible in the results of other Verified Permissions operations.

## Request Syntax
<a name="API_CreateIdentitySource_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "configuration": { ... },
   "policyStoreId": "{{string}}",
   "principalEntityType": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateIdentitySource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [configuration](#API_CreateIdentitySource_RequestSyntax) **   <a name="verifiedpermissions-CreateIdentitySource-request-configuration"></a>
Specifies the details required to communicate with the identity provider (IdP) associated with this identity source.
Type: [Configuration](API_Configuration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [policyStoreId](#API_CreateIdentitySource_RequestSyntax) **   <a name="verifiedpermissions-CreateIdentitySource-request-policyStoreId"></a>
Specifies the ID of the policy store in which you want to store this identity source. Only policies and requests made using this policy store can reference identities from the identity provider configured in the new identity source.
To specify a policy store, use its ID or alias name. When using an alias name, prefix it with `policy-store-alias/`. For example:
+ ID: `PSEXAMPLEabcdefg111111`
+ Alias name: `policy-store-alias/example-policy-store`
To view aliases, use [ListPolicyStoreAliases](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`
Required: Yes

 ** [clientToken](#API_CreateIdentitySource_RequestSyntax) **   <a name="verifiedpermissions-CreateIdentitySource-request-clientToken"></a>
Specifies a unique, case-sensitive ID that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a [UUID type of value.](https://wikipedia.org/wiki/Universally_unique_identifier).
If you don't provide this value, then AWS generates a random one for you.
If you retry the operation with the same `ClientToken`, but with different parameters, the retry fails with an `ConflictException` error.
Verified Permissions recognizes a `ClientToken` for eight hours. After eight hours, the next request with the same parameters performs the operation again regardless of the value of `ClientToken`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]*`
Required: No

 ** [principalEntityType](#API_CreateIdentitySource_RequestSyntax) **   <a name="verifiedpermissions-CreateIdentitySource-request-principalEntityType"></a>
Specifies the namespace and data type of the principals generated for identities authenticated by the new identity source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_CreateIdentitySource_ResponseSyntax"></a>

```
{
   "createdDate": "string",
   "identitySourceId": "string",
   "lastUpdatedDate": "string",
   "policyStoreId": "string"
}
```

## Response Elements
<a name="API_CreateIdentitySource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdDate](#API_CreateIdentitySource_ResponseSyntax) **   <a name="verifiedpermissions-CreateIdentitySource-response-createdDate"></a>
The date and time the identity source was originally created.
Type: Timestamp

 ** [identitySourceId](#API_CreateIdentitySource_ResponseSyntax) **   <a name="verifiedpermissions-CreateIdentitySource-response-identitySourceId"></a>
The unique ID of the new identity source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-]*`

 ** [lastUpdatedDate](#API_CreateIdentitySource_ResponseSyntax) **   <a name="verifiedpermissions-CreateIdentitySource-response-lastUpdatedDate"></a>
The date and time the identity source was most recently updated.
Type: Timestamp

 ** [policyStoreId](#API_CreateIdentitySource_ResponseSyntax) **   <a name="verifiedpermissions-CreateIdentitySource-response-policyStoreId"></a>
The ID of the policy store that contains the identity source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`

## Errors
<a name="API_CreateIdentitySource_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request failed because it would cause a service quota to be exceeded.
 ** quotaCode **
The quota code recognized by the AWS Service Quotas service.
 ** resourceId **
The unique ID of the resource referenced in the failed request.
 ** resourceType **
The resource type of the resource referenced in the failed request.
 ** serviceCode **
The code for the AWS service that owns the quota.
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
<a name="API_CreateIdentitySource_Examples"></a>

### Example
<a name="API_CreateIdentitySource_Example_1"></a>

The following example request creates an identity source that Verified Permissions can use to retrieve authenticated identities for authorization requests. The specified identity provider (IdP) is a Amazon Cognito user pool.

#### Sample Request
<a name="API_CreateIdentitySource_Example_1_Request"></a>

```
POST HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: identity
X-Amz-Target: VerifiedPermissions.CreateIdentitySource
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "configuration": {
        "cognitoUserPoolConfiguration": {
            "userPoolArn": "arn:aws:cognito-idp:us-east-1:123456789012:userpool/us-east-1_1a2b3c4d5",
            "clientIds": ["a1b2c3d4e5f6g7h8i9j0kalbmc"],
            "groupConfiguration": {
              "groupEntityType": "MyCorp::UserGroup"
            }
        }
    },
    "policyStoreId": "PSEXAMPLEabcdefg111111",
    "principalEntityType": "MyCorp::User",
    "clientToken": "a1b2c3d4-e5f6-a1b2-c3d4-TOKEN1111111"
}
```

#### Sample Response
<a name="API_CreateIdentitySource_Example_1_Response"></a>

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
    "createdDate":"2023-05-19T20:30:28.214829Z",
    "identitySourceId":"ISEXAMPLEabcdefg111111",
    "lastUpdatedDate":"2023-05-19T20:30:28.214829Z",
    "policyStoreId":"PSEXAMPLEabcdefg111111"
}
```

### Example
<a name="API_CreateIdentitySource_Example_2"></a>

The following example request creates an identity source that Verified Permissions can use to retrieve authenticated identities for authorization requests. The specified identity provider (IdP) is OpenID Connect (OIDC).

#### Sample Request
<a name="API_CreateIdentitySource_Example_2_Request"></a>

```
POST HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: identity
X-Amz-Target: VerifiedPermissions.CreateIdentitySource
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
	"configuration": {
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
		}
	},
    "policyStoreId": "PSEXAMPLEabcdefg111111",
    "principalEntityType": "MyCorp::User",
    "clientToken": "a1b2c3d4-e5f6-a1b2-c3d4-TOKEN1111111"
}
```

#### Sample Response
<a name="API_CreateIdentitySource_Example_2_Response"></a>

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
    "createdDate":"2023-05-19T20:30:28.214829Z",
    "identitySourceId":"ISEXAMPLEabcdefg111111",
    "lastUpdatedDate":"2023-05-19T20:30:28.214829Z",
    "policyStoreId":"PSEXAMPLEabcdefg111111"
}
```

## See Also
<a name="API_CreateIdentitySource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/verifiedpermissions-2021-12-01/CreateIdentitySource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/verifiedpermissions-2021-12-01/CreateIdentitySource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/CreateIdentitySource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/verifiedpermissions-2021-12-01/CreateIdentitySource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/CreateIdentitySource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/verifiedpermissions-2021-12-01/CreateIdentitySource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/verifiedpermissions-2021-12-01/CreateIdentitySource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/verifiedpermissions-2021-12-01/CreateIdentitySource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/verifiedpermissions-2021-12-01/CreateIdentitySource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/CreateIdentitySource)
