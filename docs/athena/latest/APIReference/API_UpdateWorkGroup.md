---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_UpdateWorkGroup.html
---

# UpdateWorkGroup
<a name="API_UpdateWorkGroup"></a>

Updates the workgroup with the specified name. The workgroup's name cannot be changed. Only `ConfigurationUpdates` can be specified.

## Request Syntax
<a name="API_UpdateWorkGroup_RequestSyntax"></a>

```
{
   "ConfigurationUpdates": {
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
      "ManagedQueryResultsConfigurationUpdates": {
         "Enabled": {{boolean}},
         "EncryptionConfiguration": {
            "KmsKey": "{{string}}"
         },
         "RemoveEncryptionConfiguration": {{boolean}}
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
      "RemoveBytesScannedCutoffPerQuery": {{boolean}},
      "RemoveCustomerContentEncryptionConfiguration": {{boolean}},
      "RequesterPaysEnabled": {{boolean}},
      "ResultConfigurationUpdates": {
         "AclConfiguration": {
            "S3AclOption": "{{string}}"
         },
         "EncryptionConfiguration": {
            "EncryptionOption": "{{string}}",
            "KmsKey": "{{string}}"
         },
         "ExpectedBucketOwner": "{{string}}",
         "OutputLocation": "{{string}}",
         "RemoveAclConfiguration": {{boolean}},
         "RemoveEncryptionConfiguration": {{boolean}},
         "RemoveExpectedBucketOwner": {{boolean}},
         "RemoveOutputLocation": {{boolean}}
      }
   },
   "Description": "{{string}}",
   "State": "{{string}}",
   "WorkGroup": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateWorkGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigurationUpdates](#API_UpdateWorkGroup_RequestSyntax) **   <a name="athena-UpdateWorkGroup-request-ConfigurationUpdates"></a>
Contains configuration updates for an Athena SQL workgroup.
Type: [WorkGroupConfigurationUpdates](API_WorkGroupConfigurationUpdates.md) object
Required: No

 ** [Description](#API_UpdateWorkGroup_RequestSyntax) **   <a name="athena-UpdateWorkGroup-request-Description"></a>
The workgroup description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [State](#API_UpdateWorkGroup_RequestSyntax) **   <a name="athena-UpdateWorkGroup-request-State"></a>
The workgroup state that will be updated for the given workgroup.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [WorkGroup](#API_UpdateWorkGroup_RequestSyntax) **   <a name="athena-UpdateWorkGroup-request-WorkGroup"></a>
The specified workgroup that will be updated.
Type: String
Pattern: `[a-zA-Z0-9._-]{1,128}`
Required: Yes

## Response Elements
<a name="API_UpdateWorkGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateWorkGroup_Errors"></a>

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
<a name="API_UpdateWorkGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/athena-2017-05-18/UpdateWorkGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/athena-2017-05-18/UpdateWorkGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/UpdateWorkGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/athena-2017-05-18/UpdateWorkGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/UpdateWorkGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/athena-2017-05-18/UpdateWorkGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/athena-2017-05-18/UpdateWorkGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/athena-2017-05-18/UpdateWorkGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/UpdateWorkGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/UpdateWorkGroup)
