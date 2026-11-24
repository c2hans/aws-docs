---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_UpdateStorageVirtualMachinePeer.html
---

# UpdateStorageVirtualMachinePeer

Updates an Amazon FSx for NetApp ONTAP storage virtual machine (SVM) peer relationship.

## Request Syntax
<a name="API_UpdateStorageVirtualMachinePeer_RequestSyntax"></a>

```
{
   "Applications": [ "{{string}}" ],
   "ClientRequestToken": "{{string}}",
   "PeerSvmAlias": "{{string}}",
   "State": "{{string}}",
   "StorageVirtualMachinePeerId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateStorageVirtualMachinePeer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Applications](#API_UpdateStorageVirtualMachinePeer_RequestSyntax) **   <a name="FSx-UpdateStorageVirtualMachinePeer-request-Applications"></a>
Specifies the applications that the SVM peer relationship authorizes. The applications that you specify replace the existing applications.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Valid Values: `SNAPMIRROR | FILE_COPY | LUN_COPY | FLEXCACHE`
Required: No

 ** [ClientRequestToken](#API_UpdateStorageVirtualMachinePeer_RequestSyntax) **   <a name="FSx-UpdateStorageVirtualMachinePeer-request-ClientRequestToken"></a>
(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-za-z0-9_.-]{0,63}$`
Required: No

 ** [PeerSvmAlias](#API_UpdateStorageVirtualMachinePeer_RequestSyntax) **   <a name="FSx-UpdateStorageVirtualMachinePeer-request-PeerSvmAlias"></a>
Specifies the name that the local cluster uses to identify the peer SVM.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 41.
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,41}$`
Required: No

 ** [State](#API_UpdateStorageVirtualMachinePeer_RequestSyntax) **   <a name="FSx-UpdateStorageVirtualMachinePeer-request-State"></a>
Specifies the state to set for the SVM peer relationship:
+  `PEERED` – Accepts a pending peering request, or resumes a suspended SVM peer relationship.
+  `SUSPENDED` – Suspends the SVM peer relationship.
+  `REJECTED` – Rejects a pending peering request.
Type: String
Valid Values: `PEERED | REJECTED | SUSPENDED`
Required: No

 ** [StorageVirtualMachinePeerId](#API_UpdateStorageVirtualMachinePeer_RequestSyntax) **   <a name="FSx-UpdateStorageVirtualMachinePeer-request-StorageVirtualMachinePeerId"></a>
The ID of the SVM peer that you want to update.
Type: String
Pattern: `^(svmpeer-[0-9a-f]{17})$`
Required: Yes

## Response Syntax
<a name="API_UpdateStorageVirtualMachinePeer_ResponseSyntax"></a>

```
{
   "StorageVirtualMachinePeer": {
      "Applications": [ "string" ],
      "FileSystemId": "string",
      "Lifecycle": "string",
      "LifecycleTransitionReason": {
         "Message": "string",
         "OntapError": {
            "Code": "string",
            "Message": "string"
         }
      },
      "PeerClusterName": "string",
      "PeerSvmAlias": "string",
      "PeerSvmName": "string",
      "ResourceARN": "string",
      "State": "string",
      "StorageVirtualMachineId": "string",
      "StorageVirtualMachinePeerId": "string",
      "Tags": [
         {
            "Key": "string",
            "Value": "string"
         }
      ],
      "UUID": "string"
   }
}
```

## Response Elements
<a name="API_UpdateStorageVirtualMachinePeer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [StorageVirtualMachinePeer](#API_UpdateStorageVirtualMachinePeer_ResponseSyntax) **   <a name="FSx-UpdateStorageVirtualMachinePeer-response-StorageVirtualMachinePeer"></a>
A description of the SVM peer that was just updated.
Type: [StorageVirtualMachinePeer](API_StorageVirtualMachinePeer.md) object

## Errors
<a name="API_UpdateStorageVirtualMachinePeer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **
A generic error indicating a failure with a client request.
 ** Message **
A detailed error message.
HTTP Status Code: 400

 ** IncompatibleParameterError **
The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.
 ** Message **
A detailed error message.
 ** Parameter **
A parameter that is incompatible with the earlier request.
HTTP Status Code: 400

 ** InternalServerError **
A generic error indicating a server-side failure.
 ** Message **
A detailed error message.
HTTP Status Code: 500

 ** StorageVirtualMachinePeerNotFound **
No Amazon FSx storage virtual machine (SVM) peers were found based on the supplied parameters.
 ** Message **
A detailed error message.
HTTP Status Code: 400

## See Also
<a name="API_UpdateStorageVirtualMachinePeer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/UpdateStorageVirtualMachinePeer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/UpdateStorageVirtualMachinePeer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/UpdateStorageVirtualMachinePeer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/UpdateStorageVirtualMachinePeer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/UpdateStorageVirtualMachinePeer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/UpdateStorageVirtualMachinePeer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/UpdateStorageVirtualMachinePeer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/UpdateStorageVirtualMachinePeer)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/UpdateStorageVirtualMachinePeer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/UpdateStorageVirtualMachinePeer)
