---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ListResourcePolicies.html
---

# ListResourcePolicies
<a name="API_ListResourcePolicies"></a>

Lists the resource-based policies attached to a secret. The response contains only the names of the policies, not their contents. Secrets Manager lists `default` first, followed by any other policies in alphabetical order. To get the contents of a policy, use [GetResourcePolicy](API_GetResourcePolicy.md). You can modify only the `default` policy.

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with AWS CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

 **Required permissions: ** `secretsmanager:ListResourcePolicies`. For more information, see [ IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Request Syntax
<a name="API_ListResourcePolicies_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SecretId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListResourcePolicies_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListResourcePolicies_RequestSyntax) **   <a name="SecretsManager-ListResourcePolicies-request-MaxResults"></a>
The number of results to include in the response. If you don't specify this value, the service returns up to 100 results.
If there are more results available, in the response, Secrets Manager includes `NextToken`. To get the next results, call `ListResourcePolicies` again with the value from `NextToken`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListResourcePolicies_RequestSyntax) **   <a name="SecretsManager-ListResourcePolicies-request-NextToken"></a>
A token that indicates where the output should continue from, if a previous call did not show all results. To get the next results, call `ListResourcePolicies` again with this value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [SecretId](#API_ListResourcePolicies_RequestSyntax) **   <a name="SecretsManager-ListResourcePolicies-request-SecretId"></a>
The ARN or name of the secret.
For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See [Finding a secret from a partial ARN](https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Response Syntax
<a name="API_ListResourcePolicies_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ResourcePolicies": [
      {
         "PolicyName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListResourcePolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListResourcePolicies_ResponseSyntax) **   <a name="SecretsManager-ListResourcePolicies-response-NextToken"></a>
Secrets Manager includes this value if there's more output available than what is included in the current response. To get the next results, call `ListResourcePolicies` again with this value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [ResourcePolicies](#API_ListResourcePolicies_ResponseSyntax) **   <a name="SecretsManager-ListResourcePolicies-response-ResourcePolicies"></a>
A list of the resource policies attached to the secret.
Type: Array of [ResourcePolicySummary](API_ResourcePolicySummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_ListResourcePolicies_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** InternalServiceError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidNextTokenException **
The `NextToken` value is invalid.
HTTP Status Code: 400

 ** InvalidParameterException **
The parameter name or value is invalid.
HTTP Status Code: 400

 ** InvalidRequestException **
A parameter value is not valid for the current state of the resource.
Possible causes:
+ The secret is scheduled for deletion.
+ You tried to enable rotation on a secret that doesn't already have a Lambda function ARN configured and you didn't include such an ARN as a parameter in this call.
+ The secret is managed by another service, and you must use that service to update it. For more information, see [Secrets managed by other AWS services](https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html).
HTTP Status Code: 400

 ** ResourceNotFoundException **
Secrets Manager can't find the resource that you asked for.
HTTP Status Code: 400

## Examples
<a name="API_ListResourcePolicies_Examples"></a>

### Example
<a name="API_ListResourcePolicies_Example_1"></a>

The following example shows how to list the resource policies attached to a secret. The JSON request string input and response output displays formatted code with white space and line breaks for better readability. Submit your input as a single line JSON string.

#### Sample Request
<a name="API_ListResourcePolicies_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: secretsmanager.region.domain
Accept-Encoding: identity
X-Amz-Target: secretsmanager.ListResourcePolicies
Content-Type: application/x-amz-json-1.1
User-Agent: <user-agent-string>
X-Amz-Date: <date>
Authorization: AWS4-HMAC-SHA256 Credential=<credentials>,SignedHeaders=<headers>, Signature=<signature>
Content-Length: <payload-size-bytes>

{
  "SecretId": "MyTestDatabaseSecret"
}
```

#### Sample Response
<a name="API_ListResourcePolicies_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: <date>
Content-Type: application/x-amz-json-1.1
Content-Length: <response-size-bytes>
Connection: keep-alive
x-amzn-RequestId: <request-id-guid>

{
  "ResourcePolicies": [
    {
      "PolicyName":"default"
    }
  ]
}
```

## See Also
<a name="API_ListResourcePolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/secretsmanager-2017-10-17/ListResourcePolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/secretsmanager-2017-10-17/ListResourcePolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/secretsmanager-2017-10-17/ListResourcePolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/secretsmanager-2017-10-17/ListResourcePolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/secretsmanager-2017-10-17/ListResourcePolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/secretsmanager-2017-10-17/ListResourcePolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/secretsmanager-2017-10-17/ListResourcePolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/secretsmanager-2017-10-17/ListResourcePolicies)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/secretsmanager-2017-10-17/ListResourcePolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/secretsmanager-2017-10-17/ListResourcePolicies)
