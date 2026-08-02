---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_ListFunctions.html
---

# ListFunctions
<a name="API_ListFunctions"></a>

Returns a list of Lambda functions, with the version-specific configuration of each. Lambda returns up to 50 functions per call.

Set `FunctionVersion` to `ALL` to include all published versions of each function in addition to the unpublished version.

**Note**
The `ListFunctions` operation returns a subset of the [FunctionConfiguration](API_FunctionConfiguration.md) fields. To get the additional fields (State, StateReasonCode, StateReason, LastUpdateStatus, LastUpdateStatusReason, LastUpdateStatusReasonCode, RuntimeVersionConfig) for a function or version, use [GetFunction](API_GetFunction.md).

## Request Syntax
<a name="API_ListFunctions_RequestSyntax"></a>

```
GET /2015-03-31/functions?FunctionVersion={{FunctionVersion}}&Marker={{Marker}}&MasterRegion={{MasterRegion}}&MaxItems={{MaxItems}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListFunctions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FunctionVersion](#API_ListFunctions_RequestSyntax) **   <a name="lambda-ListFunctions-request-uri-FunctionVersion"></a>
Set to `ALL` to include entries for all published versions of each function.
Valid Values: `ALL`

 ** [Marker](#API_ListFunctions_RequestSyntax) **   <a name="lambda-ListFunctions-request-uri-Marker"></a>
Specify the pagination token that's returned by a previous request to retrieve the next page of results.

 ** [MasterRegion](#API_ListFunctions_RequestSyntax) **   <a name="lambda-ListFunctions-request-uri-MasterRegion"></a>
For Lambda@Edge functions, the AWS Region of the master function. For example, `us-east-1` filters the list of functions to include only Lambda@Edge functions replicated from a master function in US East (N. Virginia). If specified, you must set `FunctionVersion` to `ALL`.
Pattern: `ALL|[a-z]{2}(-gov)?-[a-z]+-\d{1}`

 ** [MaxItems](#API_ListFunctions_RequestSyntax) **   <a name="lambda-ListFunctions-request-uri-MaxItems"></a>
The maximum number of functions to return in the response. Note that `ListFunctions` returns a maximum of 50 items in each response, even if you set the number higher.
Valid Range: Minimum value of 1. Maximum value of 10000.

## Request Body
<a name="API_ListFunctions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListFunctions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Functions": [
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
               "LocalMountPath": "string"
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
   ],
   "NextMarker": "string"
}
```

## Response Elements
<a name="API_ListFunctions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Functions](#API_ListFunctions_ResponseSyntax) **   <a name="lambda-ListFunctions-response-Functions"></a>
A list of Lambda functions.
Type: Array of [FunctionConfiguration](API_FunctionConfiguration.md) objects

 ** [NextMarker](#API_ListFunctions_ResponseSyntax) **   <a name="lambda-ListFunctions-response-NextMarker"></a>
The pagination token that's included if more results are available.
Type: String

## Errors
<a name="API_ListFunctions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
One of the parameters in the request is not valid.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 400

 ** ServiceException **
The AWS Lambda service encountered an internal error.
HTTP Status Code: 500

 ** TooManyRequestsException **
The request throughput limit was exceeded. For more information, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests).
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
HTTP Status Code: 429

## See Also
<a name="API_ListFunctions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/ListFunctions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/ListFunctions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/ListFunctions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/ListFunctions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/ListFunctions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/ListFunctions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/ListFunctions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/ListFunctions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/ListFunctions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/ListFunctions)
