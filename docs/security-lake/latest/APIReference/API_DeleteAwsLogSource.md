---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DeleteAwsLogSource.html
---

# DeleteAwsLogSource
<a name="API_DeleteAwsLogSource"></a>

Removes a natively supported AWS service as an Amazon Security Lake source. You can remove a source for one or more Regions. When you remove the source, Security Lake stops collecting data from that source in the specified Regions and accounts, and subscribers can no longer consume new data from the source. However, subscribers can still consume data that Security Lake collected from the source before removal.

You can choose any source type in any AWS Region for either accounts that are part of a trusted organization or standalone accounts.

## Request Syntax
<a name="API_DeleteAwsLogSource_RequestSyntax"></a>

```
POST /v1/datalake/logsources/aws/delete HTTP/1.1
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
<a name="API_DeleteAwsLogSource_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteAwsLogSource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [sources](#API_DeleteAwsLogSource_RequestSyntax) **   <a name="securitylake-DeleteAwsLogSource-request-sources"></a>
Specify the natively-supported AWS service to remove as a source in Security Lake.
Type: Array of [AwsLogSourceConfiguration](API_AwsLogSourceConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: Yes

## Response Syntax
<a name="API_DeleteAwsLogSource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "failed": [ "string" ]
}
```

## Response Elements
<a name="API_DeleteAwsLogSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failed](#API_DeleteAwsLogSource_ResponseSyntax) **   <a name="securitylake-DeleteAwsLogSource-response-failed"></a>
Deletion of the AWS sources failed as the account is not a part of the organization.
Type: Array of strings
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

## Errors
<a name="API_DeleteAwsLogSource_Errors"></a>

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
<a name="API_DeleteAwsLogSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securitylake-2018-05-10/DeleteAwsLogSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securitylake-2018-05-10/DeleteAwsLogSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/DeleteAwsLogSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securitylake-2018-05-10/DeleteAwsLogSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/DeleteAwsLogSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securitylake-2018-05-10/DeleteAwsLogSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securitylake-2018-05-10/DeleteAwsLogSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securitylake-2018-05-10/DeleteAwsLogSource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securitylake-2018-05-10/DeleteAwsLogSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/DeleteAwsLogSource)
