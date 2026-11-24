---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateStorageVirtualMachinePeer.html
---

# CreateStorageVirtualMachinePeer

Creates a storage virtual machine (SVM) peer relationship between an SVM on an Amazon FSx for NetApp ONTAP file system and another SVM.

The `CreateStorageVirtualMachinePeer` operation returns while the SVM peer's lifecycle state is still `CREATING`. You can check the SVM peer creation status by calling the DescribeStorageVirtualMachinePeers operation.

## Request Syntax
<a name="API_CreateStorageVirtualMachinePeer_RequestSyntax"></a>

```
{
   "Applications": [ "{{string}}" ],
   "ClientRequestToken": "{{string}}",
   "PeerClusterName": "{{string}}",
   "PeerSvmAlias": "{{string}}",
   "PeerSvmName": "{{string}}",
   "StorageVirtualMachineId": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateStorageVirtualMachinePeer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Applications](#API_CreateStorageVirtualMachinePeer_RequestSyntax) **   <a name="FSx-CreateStorageVirtualMachinePeer-request-Applications"></a>
Specifies the applications that the SVM peer relationship authorizes.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Valid Values: `SNAPMIRROR | FILE_COPY | LUN_COPY | FLEXCACHE`
Required: Yes

 ** [ClientRequestToken](#API_CreateStorageVirtualMachinePeer_RequestSyntax) **   <a name="FSx-CreateStorageVirtualMachinePeer-request-ClientRequestToken"></a>
(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-za-z0-9_.-]{0,63}$`
Required: No

 ** [PeerClusterName](#API_CreateStorageVirtualMachinePeer_RequestSyntax) **   <a name="FSx-CreateStorageVirtualMachinePeer-request-PeerClusterName"></a>
Specifies the name of the peer cluster that the peer SVM is on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 44.
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,44}$`
Required: No

 ** [PeerSvmAlias](#API_CreateStorageVirtualMachinePeer_RequestSyntax) **   <a name="FSx-CreateStorageVirtualMachinePeer-request-PeerSvmAlias"></a>
Specifies the name that the local cluster uses to identify the peer SVM.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 41.
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,41}$`
Required: No

 ** [PeerSvmName](#API_CreateStorageVirtualMachinePeer_RequestSyntax) **   <a name="FSx-CreateStorageVirtualMachinePeer-request-PeerSvmName"></a>
Specifies the name of the SVM to peer with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 47.
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,47}$`
Required: Yes

 ** [StorageVirtualMachineId](#API_CreateStorageVirtualMachinePeer_RequestSyntax) **   <a name="FSx-CreateStorageVirtualMachinePeer-request-StorageVirtualMachineId"></a>
Specifies the ID of the SVM on which to create the SVM peer relationship.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `^(svm-[0-9a-f]{17,})$`
Required: Yes

 ** [Tags](#API_CreateStorageVirtualMachinePeer_RequestSyntax) **   <a name="FSx-CreateStorageVirtualMachinePeer-request-Tags"></a>
A list of `Tag` values, with a maximum of 50 elements.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateStorageVirtualMachinePeer_ResponseSyntax"></a>

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
<a name="API_CreateStorageVirtualMachinePeer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [StorageVirtualMachinePeer](#API_CreateStorageVirtualMachinePeer_ResponseSyntax) **   <a name="FSx-CreateStorageVirtualMachinePeer-response-StorageVirtualMachinePeer"></a>
A description of the SVM peer.
Type: [StorageVirtualMachinePeer](API_StorageVirtualMachinePeer.md) object

## Errors
<a name="API_CreateStorageVirtualMachinePeer_Errors"></a>

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

 ** ServiceLimitExceeded **
An error indicating that a particular service limit was exceeded. You can increase some service limits by contacting AWS Support.
 ** Limit **
Enumeration of the service limit that was exceeded.
 ** Message **
A detailed error message.
HTTP Status Code: 400

 ** StorageVirtualMachineNotFound **
No FSx for ONTAP SVMs were found based upon the supplied parameters.
 ** Message **
A detailed error message.
HTTP Status Code: 400

 ** UnsupportedOperation **
The requested operation is not supported for this resource or API.
 ** Message **
A detailed error message.
HTTP Status Code: 400

## See Also
<a name="API_CreateStorageVirtualMachinePeer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/CreateStorageVirtualMachinePeer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/CreateStorageVirtualMachinePeer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CreateStorageVirtualMachinePeer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/CreateStorageVirtualMachinePeer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CreateStorageVirtualMachinePeer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/CreateStorageVirtualMachinePeer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/CreateStorageVirtualMachinePeer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/CreateStorageVirtualMachinePeer)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/CreateStorageVirtualMachinePeer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CreateStorageVirtualMachinePeer)
