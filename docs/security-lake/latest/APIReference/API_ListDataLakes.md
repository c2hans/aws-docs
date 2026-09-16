---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_ListDataLakes.html
---

# ListDataLakes
<a name="API_ListDataLakes"></a>

Retrieves the Amazon Security Lake configuration object for the specified AWS Regions. You can use this operation to determine whether Security Lake is enabled for a Region.

## Request Syntax
<a name="API_ListDataLakes_RequestSyntax"></a>

```
GET /v1/datalakes?regions={{regions}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDataLakes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [regions](#API_ListDataLakes_RequestSyntax) **   <a name="securitylake-ListDataLakes-request-uri-regions"></a>
The list of Regions where Security Lake is enabled.
Pattern: `(us(-gov)?|af|ap|ca|eu|me|sa)-(central|north|(north(?:east|west))|south|south(?:east|west)|east|west)-\d+`

## Request Body
<a name="API_ListDataLakes_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDataLakes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "dataLakes": [
      {
         "createStatus": "string",
         "dataLakeArn": "string",
         "encryptionConfiguration": {
            "kmsKeyId": "string"
         },
         "lifecycleConfiguration": {
            "expiration": {
               "days": number
            },
            "transitions": [
               {
                  "days": number,
                  "storageClass": "string"
               }
            ]
         },
         "region": "string",
         "replicationConfiguration": {
            "regions": [ "string" ],
            "roleArn": "string"
         },
         "s3BucketArn": "string",
         "updateStatus": {
            "exception": {
               "code": "string",
               "reason": "string"
            },
            "requestId": "string",
            "status": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListDataLakes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dataLakes](#API_ListDataLakes_ResponseSyntax) **   <a name="securitylake-ListDataLakes-response-dataLakes"></a>
Retrieves the Security Lake configuration object.
Type: Array of [DataLakeResource](API_DataLakeResource.md) objects

## Errors
<a name="API_ListDataLakes_Errors"></a>

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
<a name="API_ListDataLakes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securitylake-2018-05-10/ListDataLakes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securitylake-2018-05-10/ListDataLakes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/ListDataLakes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securitylake-2018-05-10/ListDataLakes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/ListDataLakes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securitylake-2018-05-10/ListDataLakes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securitylake-2018-05-10/ListDataLakes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securitylake-2018-05-10/ListDataLakes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securitylake-2018-05-10/ListDataLakes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/ListDataLakes)
