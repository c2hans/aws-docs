---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_CreateWorkGroup.html
---

# CreateWorkGroup
<a name="API_CreateWorkGroup"></a>

Creates a workgroup with the specified name. A workgroup can be an Apache Spark enabled workgroup or an Athena SQL workgroup.

## Request Syntax
<a name="API_CreateWorkGroup_RequestSyntax"></a>

```
{
   "Configuration": {
      "AdditionalConfiguration": "{{string}}",
      "BytesScannedCutoffPerQuery": {{number}},
      "CustomerContentEncryptionConfiguration": {
         "KmsKey": "{{string}}"
      },
      "EnableMinimumEncryptionConfiguration": {{boolean}},
      "EnforceWorkGroupConfiguration": {{boolean}},
      "EngineConfiguration": {
         "AdditionalConfigs": {
            "{{string}}" : "{{string}}"
         },
         "Classifications": [
            {
               "Name": "{{string}}",
               "Properties": {
                  "{{string}}" : "{{string}}"
               }
            }
         ],
         "CoordinatorDpuSize": {{number}},
         "DefaultExecutorDpuSize": {{number}},
         "MaxConcurrentDpus": {{number}},
         "SparkProperties": {
            "{{string}}" : "{{string}}"
         }
      },
      "EngineVersion": {
         "EffectiveEngineVersion": "{{string}}",
         "SelectedEngineVersion": "{{string}}"
      },
      "ExecutionRole": "{{string}}",
      "IdentityCenterConfiguration": {
         "EnableIdentityCenter": {{boolean}},
         "IdentityCenterInstanceArn": "{{string}}"
      },
      "ManagedQueryResultsConfiguration": {
         "Enabled": {{boolean}},
         "EncryptionConfiguration": {
            "KmsKey": "{{string}}"
         }
      },
      "MonitoringConfiguration": {
         "CloudWatchLoggingConfiguration": {
            "Enabled": {{boolean}},
            "LogGroup": "{{string}}",
            "LogStreamNamePrefix": "{{string}}",
            "LogTypes": {
               "{{string}}" : [ "{{string}}" ]
            }
         },
         "ManagedLoggingConfiguration": {
            "Enabled": {{boolean}},
            "KmsKey": "{{string}}"
         },
         "S3LoggingConfiguration": {
            "Enabled": {{boolean}},
            "KmsKey": "{{string}}",
            "LogLocation": "{{string}}"
         }
      },
      "PublishCloudWatchMetricsEnabled": {{boolean}},
      "QueryResultsS3AccessGrantsConfiguration": {
         "AuthenticationType": "{{string}}",
         "CreateUserLevelPrefix": {{boolean}},
         "EnableS3AccessGrants": {{boolean}}
      },
      "RequesterPaysEnabled": {{boolean}},
      "ResultConfiguration": {
         "AclConfiguration": {
            "S3AclOption": "{{string}}"
         },
         "EncryptionConfiguration": {
            "EncryptionOption": "{{string}}",
            "KmsKey": "{{string}}"
         },
         "ExpectedBucketOwner": "{{string}}",
         "OutputLocation": "{{string}}"
      }
   },
   "Description": "{{string}}",
   "Name": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateWorkGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Configuration](#API_CreateWorkGroup_RequestSyntax) **   <a name="athena-CreateWorkGroup-request-Configuration"></a>
Contains configuration information for creating an Athena SQL workgroup or Spark enabled Athena workgroup. Athena SQL workgroup configuration includes the location in Amazon S3 where query and calculation results are stored, the encryption configuration, if any, used for encrypting query results, whether the Amazon CloudWatch Metrics are enabled for the workgroup, the limit for the amount of bytes scanned (cutoff) per query, if it is specified, and whether workgroup's settings (specified with `EnforceWorkGroupConfiguration`) in the `WorkGroupConfiguration` override client-side settings. See [WorkGroupConfiguration:EnforceWorkGroupConfiguration](API_WorkGroupConfiguration.md#athena-Type-WorkGroupConfiguration-EnforceWorkGroupConfiguration).
Type: [WorkGroupConfiguration](API_WorkGroupConfiguration.md) object
Required: No

 ** [Description](#API_CreateWorkGroup_RequestSyntax) **   <a name="athena-CreateWorkGroup-request-Description"></a>
The workgroup description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [Name](#API_CreateWorkGroup_RequestSyntax) **   <a name="athena-CreateWorkGroup-request-Name"></a>
The workgroup name.
Type: String
Pattern: `[a-zA-Z0-9._-]{1,128}`
Required: Yes

 ** [Tags](#API_CreateWorkGroup_RequestSyntax) **   <a name="athena-CreateWorkGroup-request-Tags"></a>
A list of comma separated tags to add to the workgroup that is created.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Elements
<a name="API_CreateWorkGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateWorkGroup_Errors"></a>

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
<a name="API_CreateWorkGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/athena-2017-05-18/CreateWorkGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/athena-2017-05-18/CreateWorkGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/CreateWorkGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/athena-2017-05-18/CreateWorkGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/CreateWorkGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/athena-2017-05-18/CreateWorkGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/athena-2017-05-18/CreateWorkGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/athena-2017-05-18/CreateWorkGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/CreateWorkGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/CreateWorkGroup)
