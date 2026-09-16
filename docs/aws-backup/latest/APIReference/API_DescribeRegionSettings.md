---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DescribeRegionSettings.html
---

# DescribeRegionSettings
<a name="API_DescribeRegionSettings"></a>

Returns the current service opt-in settings for the Region. If service opt-in is enabled for a service, AWS Backup tries to protect that service's resources in this Region, when the resource is included in an on-demand backup or scheduled backup plan. Otherwise, AWS Backup does not try to protect that service's resources in this Region.

## Request Syntax
<a name="API_DescribeRegionSettings_RequestSyntax"></a>

```
GET /account-settings HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeRegionSettings_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeRegionSettings_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeRegionSettings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ResourceTypeManagementPreference": {
      "string" : boolean
   },
   "ResourceTypeOptInPreference": {
      "string" : boolean
   }
}
```

## Response Elements
<a name="API_DescribeRegionSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResourceTypeManagementPreference](#API_DescribeRegionSettings_ResponseSyntax) **   <a name="Backup-DescribeRegionSettings-response-ResourceTypeManagementPreference"></a>
Returns whether AWS Backup fully manages the backups for a resource type.
For the benefits of full AWS Backup management, see [Full AWS Backup management](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html#full-management).
For a list of resource types and whether each supports full AWS Backup management, see the [Feature availability by resource](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html#features-by-resource) table.
If `"DynamoDB":false`, you can enable full AWS Backup management for DynamoDB backup by enabling [AWS Backup's advanced DynamoDB backup features](https://docs.aws.amazon.com/aws-backup/latest/devguide/advanced-ddb-backup.html#advanced-ddb-backup-enable-cli).
Type: String to boolean map
Key Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

 ** [ResourceTypeOptInPreference](#API_DescribeRegionSettings_ResponseSyntax) **   <a name="Backup-DescribeRegionSettings-response-ResourceTypeOptInPreference"></a>
The services along with the opt-in preferences in the Region.
Type: String to boolean map
Key Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

## Errors
<a name="API_DescribeRegionSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ServiceUnavailableException **
The request failed due to a temporary failure of the server.
 ** Context **

 ** Type **

HTTP Status Code: 500

## See Also
<a name="API_DescribeRegionSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/DescribeRegionSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/DescribeRegionSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/DescribeRegionSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/DescribeRegionSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/DescribeRegionSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/DescribeRegionSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/DescribeRegionSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/DescribeRegionSettings)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/DescribeRegionSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/DescribeRegionSettings)
