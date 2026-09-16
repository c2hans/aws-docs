---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteResourceDataSync.html
---

# DeleteResourceDataSync
<a name="API_DeleteResourceDataSync"></a>

Deletes a resource data sync configuration. After the configuration is deleted, changes to data on managed nodes are no longer synced to or from the target. Deleting a sync configuration doesn't delete data.

## Request Syntax
<a name="API_DeleteResourceDataSync_RequestSyntax"></a>

```
{
   "SyncName": "{{string}}",
   "SyncType": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteResourceDataSync_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [SyncName](#API_DeleteResourceDataSync_RequestSyntax) **   <a name="systemsmanager-DeleteResourceDataSync-request-SyncName"></a>
The name of the configuration to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [SyncType](#API_DeleteResourceDataSync_RequestSyntax) **   <a name="systemsmanager-DeleteResourceDataSync-request-SyncType"></a>
Specify the type of resource data sync to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## Response Elements
<a name="API_DeleteResourceDataSync_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteResourceDataSync_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** ResourceDataSyncInvalidConfigurationException **
The specified sync configuration is invalid.
HTTP Status Code: 400

 ** ResourceDataSyncNotFoundException **
The specified sync name wasn't found.
HTTP Status Code: 400

## Examples
<a name="API_DeleteResourceDataSync_Examples"></a>

### Example
<a name="API_DeleteResourceDataSync_Example_1"></a>

This example illustrates one usage of DeleteResourceDataSync.

#### Sample Request
<a name="API_DeleteResourceDataSync_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.DeleteResourceDataSync
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240330T144518Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240330/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 28

{
    "SyncName": "exampleSync"
}
```

#### Sample Response
<a name="API_DeleteResourceDataSync_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_DeleteResourceDataSync_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DeleteResourceDataSync)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DeleteResourceDataSync)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DeleteResourceDataSync)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DeleteResourceDataSync)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DeleteResourceDataSync)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DeleteResourceDataSync)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DeleteResourceDataSync)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DeleteResourceDataSync)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DeleteResourceDataSync)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DeleteResourceDataSync)
