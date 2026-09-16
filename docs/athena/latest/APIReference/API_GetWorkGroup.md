---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_GetWorkGroup.html
---

# GetWorkGroup
<a name="API_GetWorkGroup"></a>

Returns information about the workgroup with the specified name.

## Request Syntax
<a name="API_GetWorkGroup_RequestSyntax"></a>

```
{
   "WorkGroup": "{{string}}"
}
```

## Request Parameters
<a name="API_GetWorkGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [WorkGroup](#API_GetWorkGroup_RequestSyntax) **   <a name="athena-GetWorkGroup-request-WorkGroup"></a>
The name of the workgroup.
Type: String
Pattern: `[a-zA-Z0-9._-]{1,128}`
Required: Yes

## Response Syntax
<a name="API_GetWorkGroup_ResponseSyntax"></a>

```
{
   "WorkGroup": {
      "Configuration": {
         "AdditionalConfiguration": "string",
         "BytesScannedCutoffPerQuery": number,
         "CustomerContentEncryptionConfiguration": {
            "KmsKey": "string"
         },
         "EnableMinimumEncryptionConfiguration": boolean,
         "EnforceWorkGroupConfiguration": boolean,
         "EngineConfiguration": {
            "AdditionalConfigs": {
               "string" : "string"
            },
            "Classifications": [
               {
                  "Name": "string",
                  "Properties": {
                     "string" : "string"
                  }
               }
            ],
            "CoordinatorDpuSize": number,
            "DefaultExecutorDpuSize": number,
            "MaxConcurrentDpus": number,
            "SparkProperties": {
               "string" : "string"
            }
         },
         "EngineVersion": {
            "EffectiveEngineVersion": "string",
            "SelectedEngineVersion": "string"
         },
         "ExecutionRole": "string",
         "IdentityCenterConfiguration": {
            "EnableIdentityCenter": boolean,
            "IdentityCenterInstanceArn": "string"
         },
         "ManagedQueryResultsConfiguration": {
            "Enabled": boolean,
            "EncryptionConfiguration": {
               "KmsKey": "string"
            }
         },
         "MonitoringConfiguration": {
            "CloudWatchLoggingConfiguration": {
               "Enabled": boolean,
               "LogGroup": "string",
               "LogStreamNamePrefix": "string",
               "LogTypes": {
                  "string" : [ "string" ]
               }
            },
            "ManagedLoggingConfiguration": {
               "Enabled": boolean,
               "KmsKey": "string"
            },
            "S3LoggingConfiguration": {
               "Enabled": boolean,
               "KmsKey": "string",
               "LogLocation": "string"
            }
         },
         "PublishCloudWatchMetricsEnabled": boolean,
         "QueryResultsS3AccessGrantsConfiguration": {
            "AuthenticationType": "string",
            "CreateUserLevelPrefix": boolean,
            "EnableS3AccessGrants": boolean
         },
         "RequesterPaysEnabled": boolean,
         "ResultConfiguration": {
            "AclConfiguration": {
               "S3AclOption": "string"
            },
            "EncryptionConfiguration": {
               "EncryptionOption": "string",
               "KmsKey": "string"
            },
            "ExpectedBucketOwner": "string",
            "OutputLocation": "string"
         }
      },
      "CreationTime": number,
      "Description": "string",
      "IdentityCenterApplicationArn": "string",
      "Name": "string",
      "State": "string"
   }
}
```

## Response Elements
<a name="API_GetWorkGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [WorkGroup](#API_GetWorkGroup_ResponseSyntax) **   <a name="athena-GetWorkGroup-response-WorkGroup"></a>
Information about the workgroup.
Type: [WorkGroup](API_WorkGroup.md) object

## Errors
<a name="API_GetWorkGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Indicates a platform issue, which may be due to a transient condition or outage.
HTTP Status Code: 500

 ** InvalidRequestException **
Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.
 ** AthenaErrorCode **
The error code returned when the query execution failed to process, or when the processing request for the named query failed.
HTTP Status Code: 400

## See Also
<a name="API_GetWorkGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/athena-2017-05-18/GetWorkGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/athena-2017-05-18/GetWorkGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/GetWorkGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/athena-2017-05-18/GetWorkGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/GetWorkGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/athena-2017-05-18/GetWorkGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/athena-2017-05-18/GetWorkGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/athena-2017-05-18/GetWorkGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/GetWorkGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/GetWorkGroup)
