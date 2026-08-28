---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateAwsLogSource.html
---

# CreateAwsLogSource
<a name="API_CreateAwsLogSource"></a>

Adds a natively supported AWS service as an Amazon Security Lake source. Enables source types for member accounts in required AWS Regions, based on the parameters you specify. You can choose any source type in any Region for either accounts that are part of a trusted organization or standalone accounts. Once you add an AWS service as a source, Security Lake starts collecting logs and events from it.

You can use this API only to enable natively supported AWS services as a source. Use `CreateCustomLogSource` to enable data collection from a custom source.

## Request Syntax
<a name="API_CreateAwsLogSource_RequestSyntax"></a>

```
POST /v1/datalake/logsources/aws HTTP/1.1
Content-type: application/json

{
   "sources": [
      {
         "accounts": [ "{{string}}" ],
         "regions": [ "{{string}}" ],
         "sourceName": "{{string}}",
         "sourceVersion": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateAwsLogSource_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateAwsLogSource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [sources](#API_CreateAwsLogSource_RequestSyntax) **   <a name="securitylake-CreateAwsLogSource-request-sources"></a>
Specify the natively-supported AWS service to add as a source in Security Lake.
Type: Array of [AwsLogSourceConfiguration](API_AwsLogSourceConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: Yes

## Response Syntax
<a name="API_CreateAwsLogSource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "failed": [ "string" ]
}
```

## Response Elements
<a name="API_CreateAwsLogSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failed](#API_CreateAwsLogSource_ResponseSyntax) **   <a name="securitylake-CreateAwsLogSource-response-failed"></a>
Lists all accounts in which enabling a natively supported AWS service as a Security Lake source failed. The failure occurred as these accounts are not part of an organization.
Type: Array of strings
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

## Errors
<a name="API_CreateAwsLogSource_Errors"></a>

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
<a name="API_CreateAwsLogSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securitylake-2018-05-10/CreateAwsLogSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securitylake-2018-05-10/CreateAwsLogSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/CreateAwsLogSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securitylake-2018-05-10/CreateAwsLogSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/CreateAwsLogSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securitylake-2018-05-10/CreateAwsLogSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securitylake-2018-05-10/CreateAwsLogSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securitylake-2018-05-10/CreateAwsLogSource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securitylake-2018-05-10/CreateAwsLogSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/CreateAwsLogSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Security Lake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-lake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
