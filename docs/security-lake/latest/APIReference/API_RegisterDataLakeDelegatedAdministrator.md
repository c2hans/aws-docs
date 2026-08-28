---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_RegisterDataLakeDelegatedAdministrator.html
---

# RegisterDataLakeDelegatedAdministrator
<a name="API_RegisterDataLakeDelegatedAdministrator"></a>

Designates the Amazon Security Lake delegated administrator account for the organization. This API can only be called by the organization management account. The organization management account cannot be the delegated administrator account.

## Request Syntax
<a name="API_RegisterDataLakeDelegatedAdministrator_RequestSyntax"></a>

```
POST /v1/datalake/delegate HTTP/1.1
Content-type: application/json

{
   "accountId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RegisterDataLakeDelegatedAdministrator_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_RegisterDataLakeDelegatedAdministrator_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountId](#API_RegisterDataLakeDelegatedAdministrator_RequestSyntax) **   <a name="securitylake-RegisterDataLakeDelegatedAdministrator-request-accountId"></a>
The AWS account ID of the Security Lake delegated administrator.
Type: String
Pattern: `[\\\w\-_:/.@=+]*`
Required: Yes

## Response Syntax
<a name="API_RegisterDataLakeDelegatedAdministrator_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_RegisterDataLakeDelegatedAdministrator_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RegisterDataLakeDelegatedAdministrator_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific AWS action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.
 ** errorCode **
A coded string to provide more information about the access denied exception. You can use the error code to check the exception type.
HTTP Status Code: 403

 ** BadRequestException **
The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.
HTTP Status Code: 400

 ** ConflictException **
Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.
 ** resourceName **
The resource name.
 ** resourceType **
The resource type.
HTTP Status Code: 409

 ** InternalServerException **
Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceName **
The name of the resource that could not be found.
 ** resourceType **
The type of the resource that could not be found.
HTTP Status Code: 404

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** quotaCode **
That the rate of requests to Security Lake is exceeding the request quotas for your AWS account.
 ** retryAfterSeconds **
Retry the request after the specified time.
 ** serviceCode **
The code for the service in Service Quotas.
HTTP Status Code: 429

## See Also
<a name="API_RegisterDataLakeDelegatedAdministrator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securitylake-2018-05-10/RegisterDataLakeDelegatedAdministrator)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securitylake-2018-05-10/RegisterDataLakeDelegatedAdministrator)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/RegisterDataLakeDelegatedAdministrator)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securitylake-2018-05-10/RegisterDataLakeDelegatedAdministrator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/RegisterDataLakeDelegatedAdministrator)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securitylake-2018-05-10/RegisterDataLakeDelegatedAdministrator)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securitylake-2018-05-10/RegisterDataLakeDelegatedAdministrator)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securitylake-2018-05-10/RegisterDataLakeDelegatedAdministrator)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securitylake-2018-05-10/RegisterDataLakeDelegatedAdministrator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/RegisterDataLakeDelegatedAdministrator)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Security Lake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-lake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
