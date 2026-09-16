---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateCustomLogSource.html
---

# CreateCustomLogSource
<a name="API_CreateCustomLogSource"></a>

Adds a third-party custom source in Amazon Security Lake, from the AWS Region where you want to create a custom source. Security Lake can collect logs and events from third-party custom sources. After creating the appropriate IAM role to invoke AWS Glue crawler, use this API to add a custom source name in Security Lake. This operation creates a partition in the Amazon S3 bucket for Security Lake as the target location for log files from the custom source. In addition, this operation also creates an associated AWS Glue table and an AWS Glue crawler.

## Request Syntax
<a name="API_CreateCustomLogSource_RequestSyntax"></a>

```
POST /v1/datalake/logsources/custom HTTP/1.1
Content-type: application/json

{
   "configuration": {
      "crawlerConfiguration": {
         "roleArn": "{{string}}"
      },
      "providerIdentity": {
         "externalId": "{{string}}",
         "principal": "{{string}}"
      }
   },
   "eventClasses": [ "{{string}}" ],
   "sourceName": "{{string}}",
   "sourceVersion": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateCustomLogSource_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateCustomLogSource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [configuration](#API_CreateCustomLogSource_RequestSyntax) **   <a name="securitylake-CreateCustomLogSource-request-configuration"></a>
The configuration used for the third-party custom source.
Type: [CustomLogSourceConfiguration](API_CustomLogSourceConfiguration.md) object
Required: Yes

 ** [eventClasses](#API_CreateCustomLogSource_RequestSyntax) **   <a name="securitylake-CreateCustomLogSource-request-eventClasses"></a>
The Open Cybersecurity Schema Framework (OCSF) event classes which describes the type of data that the custom source will send to Security Lake. For the list of supported event classes, see the [Amazon Security Lake User Guide](https://docs.aws.amazon.com/security-lake/latest/userguide/adding-custom-sources.html#ocsf-eventclass).
Type: Array of strings
Pattern: `[A-Z\_0-9]*`
Required: No

 ** [sourceName](#API_CreateCustomLogSource_RequestSyntax) **   <a name="securitylake-CreateCustomLogSource-request-sourceName"></a>
Specify the name for a third-party custom source. This must be a Regionally unique value. The `sourceName` you enter here, is used in the `LogProviderRole` name which follows the convention `AmazonSecurityLake-Provider-{name of the custom source}-{region}`. You must use a `CustomLogSource` name that is shorter than or equal to 20 characters. This ensures that the `LogProviderRole` name is below the 64 character limit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w\-\_\:\.]*`
Required: Yes

 ** [sourceVersion](#API_CreateCustomLogSource_RequestSyntax) **   <a name="securitylake-CreateCustomLogSource-request-sourceVersion"></a>
Specify the source version for the third-party custom source, to limit log collection to a specific version of custom data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[A-Za-z0-9\-\.\_]*`
Required: No

## Response Syntax
<a name="API_CreateCustomLogSource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "source": {
      "attributes": {
         "crawlerArn": "string",
         "databaseArn": "string",
         "tableArn": "string"
      },
      "provider": {
         "location": "string",
         "roleArn": "string"
      },
      "sourceName": "string",
      "sourceVersion": "string"
   }
}
```

## Response Elements
<a name="API_CreateCustomLogSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [source](#API_CreateCustomLogSource_ResponseSyntax) **   <a name="securitylake-CreateCustomLogSource-response-source"></a>
The third-party custom source that was created.
Type: [CustomLogSourceResource](API_CustomLogSourceResource.md) object

## Errors
<a name="API_CreateCustomLogSource_Errors"></a>

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
<a name="API_CreateCustomLogSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securitylake-2018-05-10/CreateCustomLogSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securitylake-2018-05-10/CreateCustomLogSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/CreateCustomLogSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securitylake-2018-05-10/CreateCustomLogSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/CreateCustomLogSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securitylake-2018-05-10/CreateCustomLogSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securitylake-2018-05-10/CreateCustomLogSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securitylake-2018-05-10/CreateCustomLogSource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securitylake-2018-05-10/CreateCustomLogSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/CreateCustomLogSource)
