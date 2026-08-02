---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateDataLakeOrganizationConfiguration.html
---

# CreateDataLakeOrganizationConfiguration
<a name="API_CreateDataLakeOrganizationConfiguration"></a>

Automatically enables Amazon Security Lake for new member accounts in your organization. Security Lake is not automatically enabled for any existing member accounts in your organization.

This operation merges the new data lake organization configuration with the existing configuration for Security Lake in your organization. If you want to create a new data lake organization configuration, you must delete the existing one using [DeleteDataLakeOrganizationConfiguration](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DeleteDataLakeOrganizationConfiguration.html).

## Request Syntax
<a name="API_CreateDataLakeOrganizationConfiguration_RequestSyntax"></a>

```
POST /v1/datalake/organization/configuration HTTP/1.1
Content-type: application/json

{
   "autoEnableNewAccount": [
      {
         "region": "{{string}}",
         "sources": [
            {
               "sourceName": "{{string}}",
               "sourceVersion": "{{string}}"
            }
         ]
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateDataLakeOrganizationConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateDataLakeOrganizationConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [autoEnableNewAccount](#API_CreateDataLakeOrganizationConfiguration_RequestSyntax) **   <a name="securitylake-CreateDataLakeOrganizationConfiguration-request-autoEnableNewAccount"></a>
Enable Security Lake with the specified configuration settings, to begin collecting security data for new accounts in your organization.
Type: Array of [DataLakeAutoEnableNewAccountConfiguration](API_DataLakeAutoEnableNewAccountConfiguration.md) objects
Array Members: Minimum number of 1 item.
Required: No

## Response Syntax
<a name="API_CreateDataLakeOrganizationConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_CreateDataLakeOrganizationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateDataLakeOrganizationConfiguration_Errors"></a>

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
<a name="API_CreateDataLakeOrganizationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securitylake-2018-05-10/CreateDataLakeOrganizationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securitylake-2018-05-10/CreateDataLakeOrganizationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/CreateDataLakeOrganizationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securitylake-2018-05-10/CreateDataLakeOrganizationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/CreateDataLakeOrganizationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securitylake-2018-05-10/CreateDataLakeOrganizationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securitylake-2018-05-10/CreateDataLakeOrganizationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securitylake-2018-05-10/CreateDataLakeOrganizationConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securitylake-2018-05-10/CreateDataLakeOrganizationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/CreateDataLakeOrganizationConfiguration)
