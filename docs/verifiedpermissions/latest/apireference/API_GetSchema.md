---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetSchema.html
---

# GetSchema
<a name="API_GetSchema"></a>

Retrieve the details for the specified schema in the specified policy store.

## Request Syntax
<a name="API_GetSchema_RequestSyntax"></a>

```
{
   "policyStoreId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetSchema_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [policyStoreId](#API_GetSchema_RequestSyntax) **   <a name="verifiedpermissions-GetSchema-request-policyStoreId"></a>
Specifies the ID of the policy store that contains the schema.
To specify a policy store, use its ID or alias name. When using an alias name, prefix it with `policy-store-alias/`. For example:
+ ID: `PSEXAMPLEabcdefg111111`
+ Alias name: `policy-store-alias/example-policy-store`
To view aliases, use [ListPolicyStoreAliases](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`
Required: Yes

## Response Syntax
<a name="API_GetSchema_ResponseSyntax"></a>

```
{
   "createdDate": "string",
   "lastUpdatedDate": "string",
   "namespaces": [ "string" ],
   "policyStoreId": "string",
   "schema": "string"
}
```

## Response Elements
<a name="API_GetSchema_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdDate](#API_GetSchema_ResponseSyntax) **   <a name="verifiedpermissions-GetSchema-response-createdDate"></a>
The date and time that the schema was originally created.
Type: Timestamp

 ** [lastUpdatedDate](#API_GetSchema_ResponseSyntax) **   <a name="verifiedpermissions-GetSchema-response-lastUpdatedDate"></a>
The date and time that the schema was most recently updated.
Type: Timestamp

 ** [policyStoreId](#API_GetSchema_ResponseSyntax) **   <a name="verifiedpermissions-GetSchema-response-policyStoreId"></a>
The ID of the policy store that contains the schema.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`

 ** [schema](#API_GetSchema_ResponseSyntax) **   <a name="verifiedpermissions-GetSchema-response-schema"></a>
The body of the schema, written in Cedar schema JSON.
Type: String
Length Constraints: Minimum length of 1.

 ** [namespaces](#API_GetSchema_ResponseSyntax) **   <a name="verifiedpermissions-GetSchema-response-namespaces"></a>
The namespaces of the entities referenced by this schema.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `.*`

## Errors
<a name="API_GetSchema_Errors"></a>

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
<a name="API_GetSchema_Examples"></a>

### Example
<a name="API_GetSchema_Example_1"></a>

The following example retrieves the current schema stored in the specified policy store.

**Note**
The JSON in the parameters of this operation are strings that can contain embedded quotation marks (`"`) within the outermost quotation mark pair. When you are calling the API directly, using a tool like the AWS CLI or Postman, you have to *stringify* the JSON object by preceding all embedded quotation marks with a backslash character ( `\"` ) and combining all lines into a single text line with no line breaks.
Example strings are displayed wrapped across multiple lines here for readability, but the operation requires the parameters be submitted as single line strings.

#### Sample Request
<a name="API_GetSchema_Example_1_Request"></a>

```
POST HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: identity
X-Amz-Target: VerifiedPermissions.GetSchema
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "policyStoreId": "PSEXAMPLEabcdefg111111"
}
```

#### Sample Response
<a name="API_GetSchema_Example_1_Response"></a>

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
    "policyStoreId":"PSEXAMPLEabcdefg111111",
    "schema": "{
        \"My::Application\": {
            \"actions\": {
                \"remoteAccess\": {
                    \"appliesTo\": {
                        \"principalTypes\": [\"Employee\"]
                    }
                }
            },
            \"entityTypes\": {
                \"Employee\": {
                    \"shape\": {
                        \"attributes\": {
                            \"jobLevel\": { \"type\": \"Long\" },
                            \"name\": { \"type\":\"String\" }
                        },
                        \"type\": \"Record\"
                    }
                }
            }
        }
    }",
    "createdDate": "2023-05-18T14:46:35.020571Z",
    "lastUpdatedDate":"2023-05-23T16:48:20.95041Z"
}
```

## See Also
<a name="API_GetSchema_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/verifiedpermissions-2021-12-01/GetSchema)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/verifiedpermissions-2021-12-01/GetSchema)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/GetSchema)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/verifiedpermissions-2021-12-01/GetSchema)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/GetSchema)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/verifiedpermissions-2021-12-01/GetSchema)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/verifiedpermissions-2021-12-01/GetSchema)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/verifiedpermissions-2021-12-01/GetSchema)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/verifiedpermissions-2021-12-01/GetSchema)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/GetSchema)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Verified Permissions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verifiedpermissions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
