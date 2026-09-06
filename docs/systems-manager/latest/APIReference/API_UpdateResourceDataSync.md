---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateResourceDataSync.html
---

# UpdateResourceDataSync
<a name="API_UpdateResourceDataSync"></a>

Update a resource data sync. After you create a resource data sync for a Region, you can't change the account options for that sync. For example, if you create a sync in the us-east-2 (Ohio) Region and you choose the `Include only the current account` option, you can't edit that sync later and choose the `Include all accounts from my AWS Organizations configuration` option. Instead, you must delete the first resource data sync, and create a new one.

**Note**
This API operation only supports a resource data sync that was created with a SyncFromSource `SyncType`.

## Request Syntax
<a name="API_UpdateResourceDataSync_RequestSyntax"></a>

```
{
   "SyncName": "{{string}}",
   "SyncSource": {
      "AwsOrganizationsSource": {
         "OrganizationalUnits": [
            {
               "OrganizationalUnitId": "{{string}}"
            }
         ],
         "OrganizationSourceType": "{{string}}"
      },
      "EnableAllOpsDataSources": {{boolean}},
      "IncludeFutureRegions": {{boolean}},
      "SourceRegions": [ "{{string}}" ],
      "SourceType": "{{string}}"
   },
   "SyncType": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateResourceDataSync_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [SyncName](#API_UpdateResourceDataSync_RequestSyntax) **   <a name="systemsmanager-UpdateResourceDataSync-request-SyncName"></a>
The name of the resource data sync you want to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [SyncSource](#API_UpdateResourceDataSync_RequestSyntax) **   <a name="systemsmanager-UpdateResourceDataSync-request-SyncSource"></a>
Specify information about the data sources to synchronize.
Type: [ResourceDataSyncSource](API_ResourceDataSyncSource.md) object
Required: Yes

 ** [SyncType](#API_UpdateResourceDataSync_RequestSyntax) **   <a name="systemsmanager-UpdateResourceDataSync-request-SyncType"></a>
The type of resource data sync. The supported `SyncType` is SyncFromSource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Elements
<a name="API_UpdateResourceDataSync_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateResourceDataSync_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** ResourceDataSyncConflictException **
Another `UpdateResourceDataSync` request is being processed. Wait a few minutes and try again.
HTTP Status Code: 400

 ** ResourceDataSyncInvalidConfigurationException **
The specified sync configuration is invalid.
HTTP Status Code: 400

 ** ResourceDataSyncNotFoundException **
The specified sync name wasn't found.
HTTP Status Code: 400

## Examples
<a name="API_UpdateResourceDataSync_Examples"></a>

### Example
<a name="API_UpdateResourceDataSync_Example_1"></a>

This example illustrates one usage of UpdateResourceDataSync.

#### Sample Request
<a name="API_UpdateResourceDataSync_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.UpdateResourceDataSync
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240327T160454Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240327/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 161

{
    "SyncName": "exampleSync",
    "SyncType": "SyncFromSource",
    "SyncSource": {
        "SourceType": "SingleAccountMultiRegions",
        "SourceRegions": [
            "us-east-2",
            "us-west-2"
        ]
    }
}
```

#### Sample Response
<a name="API_UpdateResourceDataSync_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_UpdateResourceDataSync_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/UpdateResourceDataSync)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/UpdateResourceDataSync)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/UpdateResourceDataSync)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/UpdateResourceDataSync)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/UpdateResourceDataSync)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/UpdateResourceDataSync)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/UpdateResourceDataSync)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/UpdateResourceDataSync)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/UpdateResourceDataSync)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/UpdateResourceDataSync)
