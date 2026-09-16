---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_UpdateRegionSettings.html
---

# UpdateRegionSettings
<a name="API_UpdateRegionSettings"></a>

Updates the current service opt-in settings for the Region.

Use the `DescribeRegionSettings` API to determine the resource types that are supported.

## Request Syntax
<a name="API_UpdateRegionSettings_RequestSyntax"></a>

```
PUT /account-settings HTTP/1.1
Content-type: application/json

{
   "ResourceTypeManagementPreference": {
      "{{string}}" : {{boolean}}
   },
   "ResourceTypeOptInPreference": {
      "{{string}}" : {{boolean}}
   }
}
```

## URI Request Parameters
<a name="API_UpdateRegionSettings_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateRegionSettings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ResourceTypeManagementPreference](#API_UpdateRegionSettings_RequestSyntax) **   <a name="Backup-UpdateRegionSettings-request-ResourceTypeManagementPreference"></a>
Enables or disables full AWS Backup management of backups for a resource type. To enable full AWS Backup management for DynamoDB along with [AWS Backup's advanced DynamoDB backup features](https://docs.aws.amazon.com/aws-backup/latest/devguide/advanced-ddb-backup.html), follow the procedure to [ enable advanced DynamoDB backup programmatically](https://docs.aws.amazon.com/aws-backup/latest/devguide/advanced-ddb-backup.html#advanced-ddb-backup-enable-cli).
Type: String to boolean map
Key Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`
Required: No

 ** [ResourceTypeOptInPreference](#API_UpdateRegionSettings_RequestSyntax) **   <a name="Backup-UpdateRegionSettings-request-ResourceTypeOptInPreference"></a>
Updates the list of services along with the opt-in preferences for the Region.
If resource assignments are only based on tags, then service opt-in settings are applied. If a resource type is explicitly assigned to a backup plan, such as Amazon S3, Amazon EC2, or Amazon RDS, it will be included in the backup even if the opt-in is not enabled for that particular service. If both a resource type and tags are specified in a resource assignment, the resource type specified in the backup plan takes priority over the tag condition. Service opt-in settings are disregarded in this situation.
Type: String to boolean map
Key Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`
Required: No

## Response Syntax
<a name="API_UpdateRegionSettings_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateRegionSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateRegionSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
Indicates that something is wrong with a parameter's value. For example, the value is out of range.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** MissingParameterValueException **
Indicates that a required parameter is missing.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ServiceUnavailableException **
The request failed due to a temporary failure of the server.
 ** Context **

 ** Type **

HTTP Status Code: 500

## See Also
<a name="API_UpdateRegionSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/UpdateRegionSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/UpdateRegionSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/UpdateRegionSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/UpdateRegionSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/UpdateRegionSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/UpdateRegionSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/UpdateRegionSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/UpdateRegionSettings)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/UpdateRegionSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/UpdateRegionSettings)
