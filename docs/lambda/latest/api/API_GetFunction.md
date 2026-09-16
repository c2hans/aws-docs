---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_GetFunction.html
---

# GetFunction
<a name="API_GetFunction"></a>

Returns information about the function or function version, with a link to download the deployment package that's valid for 10 minutes. If you specify a function version, only details that are specific to that version are returned.

## Request Syntax
<a name="API_GetFunction_RequestSyntax"></a>

```
GET /2015-03-31/functions/{{FunctionName}}?Qualifier={{Qualifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetFunction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FunctionName](#API_GetFunction_RequestSyntax) **   <a name="lambda-GetFunction-request-uri-FunctionName"></a>
The name or ARN of the Lambda function, version, or alias.

**Name formats**
+  **Function name** – `my-function` (name-only), `my-function:v1` (with alias).
+  **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
+  **Partial ARN** – `123456789012:function:my-function`.
You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_\.]+)(:(\$LATEST(\.PUBLISHED)?|[a-zA-Z0-9-_]+))?`
Required: Yes

 ** [Qualifier](#API_GetFunction_RequestSyntax) **   <a name="lambda-GetFunction-request-uri-Qualifier"></a>
Specify a version or alias to get details about a published version of the function.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `\$(LATEST(\.PUBLISHED)?)|[a-zA-Z0-9-_$]+`

## Request Body
<a name="API_GetFunction_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetFunction_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Code": {
      "Error": {
         "ErrorCode": "string",
         "Message": "string"
      },
      "ImageUri": "string",
      "Location": "string",
      "RepositoryType": "string",
      "ResolvedImageUri": "string",
      "ResolvedS3Object": {
         "S3Bucket": "string",
         "S3Key": "string",
         "S3ObjectVersion": "string"
      },
      "SourceKMSKeyArn": "string"
   },
   "Concurrency": {
      "ReservedConcurrentExecutions": number
   },
   "Configuration": {
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
   },
   "Tags": {
      "string" : "string"
   },
   "TagsError": {
      "ErrorCode": "string",
      "Message": "string"
   }
}
```

## Response Elements
<a name="API_GetFunction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Code](#API_GetFunction_ResponseSyntax) **   <a name="lambda-GetFunction-response-Code"></a>
The deployment package of the function or version.
Type: [FunctionCodeLocation](API_FunctionCodeLocation.md) object

 ** [Concurrency](#API_GetFunction_ResponseSyntax) **   <a name="lambda-GetFunction-response-Concurrency"></a>
The function's [reserved concurrency](https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html).
Type: [Concurrency](API_Concurrency.md) object

 ** [Configuration](#API_GetFunction_ResponseSyntax) **   <a name="lambda-GetFunction-response-Configuration"></a>
The configuration of the function or version.
Type: [FunctionConfiguration](API_FunctionConfiguration.md) object

 ** [Tags](#API_GetFunction_ResponseSyntax) **   <a name="lambda-GetFunction-response-Tags"></a>
The function's [tags](https://docs.aws.amazon.com/lambda/latest/dg/tagging.html). Lambda returns tag data only if you have explicit allow permissions for [lambda:ListTags](https://docs.aws.amazon.com/lambda/latest/api/API_ListTags.html).
Type: String to string map

 ** [TagsError](#API_GetFunction_ResponseSyntax) **   <a name="lambda-GetFunction-response-TagsError"></a>
An object that contains details about an error related to retrieving tags.
Type: [TagsError](API_TagsError.md) object

## Errors
<a name="API_GetFunction_Errors"></a>

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
<a name="API_GetFunction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/GetFunction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/GetFunction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/GetFunction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/GetFunction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/GetFunction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/GetFunction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/GetFunction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/GetFunction)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/GetFunction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/GetFunction)
