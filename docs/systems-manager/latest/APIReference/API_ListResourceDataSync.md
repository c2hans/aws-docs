---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListResourceDataSync.html
---

# ListResourceDataSync
<a name="API_ListResourceDataSync"></a>

Lists your resource data sync configurations. Includes information about the last time a sync attempted to start, the last sync status, and the last time a sync successfully completed.

The number of sync configurations might be too large to return using a single call to `ListResourceDataSync`. You can limit the number of sync configurations returned by using the `MaxResults` parameter. To determine whether there are more sync configurations to list, check the value of `NextToken` in the output. If there are more sync configurations to list, you can request them by specifying the `NextToken` returned in the call to the parameter of a subsequent call.

## Request Syntax
<a name="API_ListResourceDataSync_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SyncType": "{{string}}"
}
```

## Request Parameters
<a name="API_ListResourceDataSync_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListResourceDataSync_RequestSyntax) **   <a name="systemsmanager-ListResourceDataSync-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListResourceDataSync_RequestSyntax) **   <a name="systemsmanager-ListResourceDataSync-request-NextToken"></a>
A token to start the list. Use this token to get the next set of results.
Type: String
Required: No

 ** [SyncType](#API_ListResourceDataSync_RequestSyntax) **   <a name="systemsmanager-ListResourceDataSync-request-SyncType"></a>
View a list of resource data syncs according to the sync type. Specify `SyncToDestination` to view resource data syncs that synchronize data to an Amazon S3 bucket. Specify `SyncFromSource` to view resource data syncs from AWS Organizations or from multiple AWS Regions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## Response Syntax
<a name="API_ListResourceDataSync_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ResourceDataSyncItems": [
      {
         "LastStatus": "string",
         "LastSuccessfulSyncTime": number,
         "LastSyncStatusMessage": "string",
         "LastSyncTime": number,
         "S3Destination": {
            "AWSKMSKeyARN": "string",
            "BucketName": "string",
            "DestinationDataSharing": {
               "DestinationDataSharingType": "string"
            },
            "Prefix": "string",
            "Region": "string",
            "SyncFormat": "string"
         },
         "SyncCreatedTime": number,
         "SyncLastModifiedTime": number,
         "SyncName": "string",
         "SyncSource": {
            "AwsOrganizationsSource": {
               "OrganizationalUnits": [
                  {
                     "OrganizationalUnitId": "string"
                  }
               ],
               "OrganizationSourceType": "string"
            },
            "EnableAllOpsDataSources": boolean,
            "IncludeFutureRegions": boolean,
            "SourceRegions": [ "string" ],
            "SourceType": "string",
            "State": "string"
         },
         "SyncType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListResourceDataSync_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListResourceDataSync_ResponseSyntax) **   <a name="systemsmanager-ListResourceDataSync-response-NextToken"></a>
The token for the next set of items to return. Use this token to get the next set of results.
Type: String

 ** [ResourceDataSyncItems](#API_ListResourceDataSync_ResponseSyntax) **   <a name="systemsmanager-ListResourceDataSync-response-ResourceDataSyncItems"></a>
A list of your current resource data sync configurations and their statuses.
Type: Array of [ResourceDataSyncItem](API_ResourceDataSyncItem.md) objects

## Errors
<a name="API_ListResourceDataSync_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidNextToken **
The specified token isn't valid.
HTTP Status Code: 400

 ** ResourceDataSyncInvalidConfigurationException **
The specified sync configuration is invalid.
HTTP Status Code: 400

## Examples
<a name="API_ListResourceDataSync_Examples"></a>

### Example
<a name="API_ListResourceDataSync_Example_1"></a>

This example illustrates one usage of ListResourceDataSync.

#### Sample Request
<a name="API_ListResourceDataSync_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.ListResourceDataSync
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240330T143820Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240330/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 2
```

#### Sample Response
<a name="API_ListResourceDataSync_Example_1_Response"></a>

```
{
    "ResourceDataSyncItems": [
        {
            "LastStatus": "Successful",
            "LastSuccessfulSyncTime": 1585578819.829,
            "LastSyncStatusMessage": "The sync was successfully completed",
            "LastSyncTime": 1585578819.829,
            "S3Destination": {
                "BucketName": "amzn-s3-demo-bucket",
                "Prefix": "amzn-s3-demo-bucket-prefix",
                "Region": "us-east-2",
                "SyncFormat": "JsonSerDe"
            },
            "SyncCreatedTime": 1585330479.404,
            "SyncLastModifiedTime": 1585330479.404,
            "SyncName": "exampleSync"
        }
    ]
}
```

## See Also
<a name="API_ListResourceDataSync_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/ListResourceDataSync)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/ListResourceDataSync)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ListResourceDataSync)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/ListResourceDataSync)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ListResourceDataSync)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/ListResourceDataSync)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/ListResourceDataSync)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/ListResourceDataSync)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/ListResourceDataSync)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ListResourceDataSync)
