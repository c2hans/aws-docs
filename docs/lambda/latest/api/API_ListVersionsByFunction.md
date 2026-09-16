---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_ListVersionsByFunction.html
---

# ListVersionsByFunction
<a name="API_ListVersionsByFunction"></a>

Returns a list of [versions](https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html), with the version-specific configuration of each. Lambda returns up to 50 versions per call.

## Request Syntax
<a name="API_ListVersionsByFunction_RequestSyntax"></a>

```
GET /2015-03-31/functions/{{FunctionName}}/versions?Marker={{Marker}}&MaxItems={{MaxItems}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListVersionsByFunction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FunctionName](#API_ListVersionsByFunction_RequestSyntax) **   <a name="lambda-ListVersionsByFunction-request-uri-FunctionName"></a>
The name or ARN of the Lambda function.

**Name formats**
+  **Function name** - `MyFunction`.
+  **Function ARN** - `arn:aws:lambda:us-west-2:123456789012:function:MyFunction`.
+  **Partial ARN** - `123456789012:function:MyFunction`.
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_\.]+)(:(\$LATEST(\.PUBLISHED)?|[a-zA-Z0-9-_]+))?`
Required: Yes

 ** [Marker](#API_ListVersionsByFunction_RequestSyntax) **   <a name="lambda-ListVersionsByFunction-request-uri-Marker"></a>
Specify the pagination token that's returned by a previous request to retrieve the next page of results.

 ** [MaxItems](#API_ListVersionsByFunction_RequestSyntax) **   <a name="lambda-ListVersionsByFunction-request-uri-MaxItems"></a>
The maximum number of versions to return. Note that `ListVersionsByFunction` returns a maximum of 50 items in each response, even if you set the number higher.
Valid Range: Minimum value of 1. Maximum value of 10000.

## Request Body
<a name="API_ListVersionsByFunction_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListVersionsByFunction_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextMarker": "string",
   "Versions": [
      {
         "Architectures": [ "string" ],
         "CapacityProviderConfig": {
            "LambdaManagedInstancesCapacityProviderConfig": {
               "CapacityProviderArn": "string",
               "ExecutionEnvironmentMemoryGiBPerVCpu": number,
               "PerExecutionEnvironmentMaxConcurrency": number
            }
         },
         "CodeSha256": "string",
         "CodeSize": number,
         "ConfigSha256": "string",
         "DeadLetterConfig": {
            "TargetArn": "string"
         },
         "Description": "string",
         "DurableConfig": {
            "ExecutionTimeout": number,
            "KMSKeyArn": "string",
            "RetentionPeriodInDays": number
         },
         "Environment": {
            "Error": {
               "ErrorCode": "string",
               "Message": "string"
            },
            "Variables": {
               "string" : "string"
            }
         },
         "EphemeralStorage": {
            "Size": number
         },
         "FileSystemConfigs": [
            {
               "Arn": "string",
               "LocalMountPath": "string",
               "S3FilesConfig": {
                  "DirectS3Read": "string"
               }
            }
         ],
         "FunctionArn": "string",
         "FunctionName": "string",
         "Handler": "string",
         "ImageConfigResponse": {
            "Error": {
               "ErrorCode": "string",
               "Message": "string"
            },
            "ImageConfig": {
               "Command": [ "string" ],
               "EntryPoint": [ "string" ],
               "WorkingDirectory": "string"
            }
         },
         "KMSKeyArn": "string",
         "LastModified": "string",
         "LastUpdateStatus": "string",
         "LastUpdateStatusReason": "string",
         "LastUpdateStatusReasonCode": "string",
         "Layers": [
            {
               "Arn": "string",
               "CodeSize": number,
               "SigningJobArn": "string",
               "SigningProfileVersionArn": "string"
            }
         ],
         "LoggingConfig": {
            "ApplicationLogLevel": "string",
            "LogFormat": "string",
            "LogGroup": "string",
            "SystemLogLevel": "string"
         },
         "MasterArn": "string",
         "MemorySize": number,
         "PackageType": "string",
         "RevisionId": "string",
         "Role": "string",
         "Runtime": "string",
         "RuntimeVersionConfig": {
            "Error": {
               "ErrorCode": "string",
               "Message": "string"
            },
            "RuntimeVersionArn": "string"
         },
         "SigningJobArn": "string",
         "SigningProfileVersionArn": "string",
         "SnapStart": {
            "ApplyOn": "string",
            "OptimizationStatus": "string"
         },
         "State": "string",
         "StateReason": "string",
         "StateReasonCode": "string",
         "TenancyConfig": {
            "TenantIsolationMode": "string"
         },
         "Timeout": number,
         "TracingConfig": {
            "Mode": "string"
         },
         "Version": "string",
         "VpcConfig": {
            "Ipv6AllowedForDualStack": boolean,
            "SecurityGroupIds": [ "string" ],
            "SubnetIds": [ "string" ],
            "VpcId": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListVersionsByFunction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextMarker](#API_ListVersionsByFunction_ResponseSyntax) **   <a name="lambda-ListVersionsByFunction-response-NextMarker"></a>
The pagination token that's included if more results are available.
Type: String

 ** [Versions](#API_ListVersionsByFunction_ResponseSyntax) **   <a name="lambda-ListVersionsByFunction-response-Versions"></a>
A list of Lambda function versions.
Type: Array of [FunctionConfiguration](API_FunctionConfiguration.md) objects

## Errors
<a name="API_ListVersionsByFunction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
One of the parameters in the request is not valid.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource specified in the request does not exist.
HTTP Status Code: 404

 ** ServiceException **
The AWS Lambda service encountered an internal error.
HTTP Status Code: 500

 ** TooManyRequestsException **
The request throughput limit was exceeded. For more information, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests).
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
HTTP Status Code: 429

## See Also
<a name="API_ListVersionsByFunction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/ListVersionsByFunction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/ListVersionsByFunction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/ListVersionsByFunction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/ListVersionsByFunction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/ListVersionsByFunction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/ListVersionsByFunction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/ListVersionsByFunction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/ListVersionsByFunction)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/ListVersionsByFunction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/ListVersionsByFunction)
