---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchGetPolicy.html
---

# BatchGetPolicy
<a name="API_BatchGetPolicy"></a>

Retrieves information about a group (batch) of policies.

**Note**
The `BatchGetPolicy` operation doesn't have its own IAM permission. To authorize this operation for AWS principals, include the permission `verifiedpermissions:GetPolicy` in their IAM policies.

## Request Syntax
<a name="API_BatchGetPolicy_RequestSyntax"></a>

```
{
   "requests": [
      {
         "policyId": "{{string}}",
         "policyStoreId": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_BatchGetPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [requests](#API_BatchGetPolicy_RequestSyntax) **   <a name="verifiedpermissions-BatchGetPolicy-request-requests"></a>
An array of up to 100 policies you want information about.
Type: Array of [BatchGetPolicyInputItem](API_BatchGetPolicyInputItem.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

## Response Syntax
<a name="API_BatchGetPolicy_ResponseSyntax"></a>

```
{
   "errors": [
      {
         "code": "string",
         "message": "string",
         "policyId": "string",
         "policyStoreId": "string"
      }
   ],
   "results": [
      {
         "createdDate": "string",
         "definition": { ... },
         "lastUpdatedDate": "string",
         "name": "string",
         "policyId": "string",
         "policyStoreId": "string",
         "policyType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchGetPolicy_ResponseSyntax) **   <a name="verifiedpermissions-BatchGetPolicy-response-errors"></a>
Information about the policies from the request that resulted in an error. These results are returned in the order they were requested.
Type: Array of [BatchGetPolicyErrorItem](API_BatchGetPolicyErrorItem.md) objects

 ** [results](#API_BatchGetPolicy_ResponseSyntax) **   <a name="verifiedpermissions-BatchGetPolicy-response-results"></a>
Information about the policies listed in the request that were successfully returned. These results are returned in the order they were requested.
Type: Array of [BatchGetPolicyOutputItem](API_BatchGetPolicyOutputItem.md) objects

## Errors
<a name="API_BatchGetPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request failed because of an internal error. Try your request again later
HTTP Status Code: 500

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
<a name="API_BatchGetPolicy_Examples"></a>

### Example
<a name="API_BatchGetPolicy_Example_1"></a>

The following example retrieves information about the specified policies contained in the specified policy stores. .

#### Sample Request
<a name="API_BatchGetPolicy_Example_1_Request"></a>

```
POST HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: identity
X-Amz-Target: VerifiedPermissions.BatchGetPolicy
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
{
    "requests": [
        {
            "policyId": "SPEXAMPLEabcdefg111111",
            "policyStoreId": "PSEXAMPLEabcdefg111111"
        },
        {
            "policyId": "SPEXAMPLEabcdefg222222",
            "policyStoreId": "PSEXAMPLEabcdefg111111"
        },
        {
            "policyId": "SPEXAMPLEabcdefg333333",
            "policyStoreId": "PSEXAMPLEabcdefg111111"
        }
    ]
}
}
```

#### Sample Response
<a name="API_BatchGetPolicy_Example_1_Response"></a>

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
            "policyStoreId": "PSEXAMPLEabcdefg111111",
            "policyId": "SPEXAMPLEabcdefg111111",
            "policyType": "STATIC",
            "name": "name/example-policy",
            "definition": {
                "static": {
                    "description": "Users can manage account resources in any account they own.",
                    "statement": "permit (principal, action in PhotoFlash::Action::\"ManageAccount\",resource) when { resource in principal.Account };"
                }
            },
            "createdDate": "2024-10-18T18:53:39.258153Z",
            "lastUpdatedDate": "2024-10-18T18:53:39.258153Z"
        },
        {
            "policyStoreId": "PSEXAMPLEabcdefg111111",
            "policyId": "SPEXAMPLEabcdefg222222",
            "policyType": "STATIC",
            "name": "name/example-policy-2",
            "definition": {
                "static": {
                    "description": "User alice can't delete any photos.",
                    "statement": "forbid (principal == PhotoFlash::User::\"alice\", action in [PhotoFlash::Action::\"DeletePhoto\"], resource);"
                }
            },
            "createdDate": "2024-10-18T18:57:03.305027Z",
            "lastUpdatedDate": "2024-10-18T18:57:03.305027Z"
        },
        {
            "policyStoreId": "PSEXAMPLEabcdefg111111",
            "policyId": "SPEXAMPLEabcdefg333333",
            "policyType": "STATIC",
            "definition": {
                "static": {
                    "description": "User alice can view and delete photos.",
                    "statement": "permit (principal == PhotoFlash::User::\"alice\", action in [PhotoFlash::Action::\"DeletePhoto\", PhotoFlash::Action::\"ViewPhoto\"], resource);"
                }
            },
            "createdDate": "2024-10-18T18:57:48.005343Z",
            "lastUpdatedDate": "2024-10-18T18:57:48.005343Z"
        }
    ]
}
```

## See Also
<a name="API_BatchGetPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/verifiedpermissions-2021-12-01/BatchGetPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/verifiedpermissions-2021-12-01/BatchGetPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/BatchGetPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/verifiedpermissions-2021-12-01/BatchGetPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/BatchGetPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/verifiedpermissions-2021-12-01/BatchGetPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/verifiedpermissions-2021-12-01/BatchGetPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/verifiedpermissions-2021-12-01/BatchGetPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/verifiedpermissions-2021-12-01/BatchGetPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/BatchGetPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Verified Permissions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verifiedpermissions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
