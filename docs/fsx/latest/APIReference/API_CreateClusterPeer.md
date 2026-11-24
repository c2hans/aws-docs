---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateClusterPeer.html
---

# CreateClusterPeer

Creates a cluster peer relationship between an Amazon FSx for NetApp ONTAP file system and another ONTAP cluster.

The `CreateClusterPeer` operation returns while the cluster peer's lifecycle state is still `CREATING`. You can check the cluster peer creation status by calling the DescribeClusterPeers operation.

## Request Syntax
<a name="API_CreateClusterPeer_RequestSyntax"></a>

```
{
   "AllowedSvmIds": [ "{{string}}" ],
   "AllowedSvmMode": "{{string}}",
   "ClientRequestToken": "{{string}}",
   "FileSystemId": "{{string}}",
   "PassphraseSecretArn": "{{string}}",
   "PeerAddresses": [ "{{string}}" ],
   "PeerClusterName": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateClusterPeer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AllowedSvmIds](#API_CreateClusterPeer_RequestSyntax) **   <a name="FSx-CreateClusterPeer-request-AllowedSvmIds"></a>
Specifies the IDs of the SVMs on the file system that are preauthorized for SVM peering with the peer cluster. You can specify `AllowedSvmIds` only when `AllowedSvmMode` is `SPECIFIED`.
Type: Array of strings
Array Members: Maximum number of 24 items.
Length Constraints: Fixed length of 21.
Pattern: `^(svm-[0-9a-f]{17,})$`
Required: No

 ** [AllowedSvmMode](#API_CreateClusterPeer_RequestSyntax) **   <a name="FSx-CreateClusterPeer-request-AllowedSvmMode"></a>
Specifies which SVMs on the file system are preauthorized for SVM peering with the peer cluster.
+  `ALL` – All SVMs on the file system are preauthorized. You can't specify `AllowedSvmIds` along with this property.
+  `NONE` – No SVMs on the file system are preauthorized. You can't specify `AllowedSvmIds` along with this property.
+  `SPECIFIED` – Only the SVMs in `AllowedSvmIds` are preauthorized. You must specify `AllowedSvmIds` along with this property.
Type: String
Valid Values: `ALL | NONE | SPECIFIED`
Required: Yes

 ** [ClientRequestToken](#API_CreateClusterPeer_RequestSyntax) **   <a name="FSx-CreateClusterPeer-request-ClientRequestToken"></a>
(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-za-z0-9_.-]{0,63}$`
Required: No

 ** [FileSystemId](#API_CreateClusterPeer_RequestSyntax) **   <a name="FSx-CreateClusterPeer-request-FileSystemId"></a>
Specifies the ID of the Amazon FSx for NetApp ONTAP file system on which to create the cluster peer relationship.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 21.
Pattern: `^(fs-[0-9a-f]{8,})$`
Required: Yes

 ** [PassphraseSecretArn](#API_CreateClusterPeer_RequestSyntax) **   <a name="FSx-CreateClusterPeer-request-PassphraseSecretArn"></a>
Specifies the Amazon Resource Name (ARN) of the AWS Secrets Manager secret containing the cluster peering passphrase. Store the passphrase as a plaintext secret value, not as a key-value pair. The secret must be in the same AWS Region as the file system. You must use the same passphrase when you create the cluster peer relationship on the peer cluster.
Type: String
Length Constraints: Minimum length of 64. Maximum length of 1024.
Pattern: `^arn:[^:]{1,63}:secretsmanager:[a-z0-9-]+:[0-9]{12}:secret:[a-zA-Z0-9/_+=.@-]+-[a-zA-Z0-9]{6}$`
Required: Yes

 ** [PeerAddresses](#API_CreateClusterPeer_RequestSyntax) **   <a name="FSx-CreateClusterPeer-request-PeerAddresses"></a>
Specifies the IP addresses of the intercluster logical interfaces (LIFs) on the peer cluster.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 288 items.
Length Constraints: Minimum length of 1. Maximum length of 45.
Pattern: `(^((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))$|^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$)`
Required: Yes

 ** [PeerClusterName](#API_CreateClusterPeer_RequestSyntax) **   <a name="FSx-CreateClusterPeer-request-PeerClusterName"></a>
Specifies the name that the file system uses to identify the peer cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 44.
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,44}$`
Required: No

 ** [Tags](#API_CreateClusterPeer_RequestSyntax) **   <a name="FSx-CreateClusterPeer-request-Tags"></a>
A list of `Tag` values, with a maximum of 50 elements.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateClusterPeer_ResponseSyntax"></a>

```
{
   "ClusterPeer": {
      "AllowedSvmIds": [ "string" ],
      "AllowedSvmMode": "string",
      "AuthenticationStatus": {
         "InUse": "string",
         "State": "string"
      },
      "ClusterPeerId": "string",
      "FileSystemId": "string",
      "Lifecycle": "string",
      "LifecycleTransitionReason": {
         "Message": "string",
         "OntapError": {
            "Code": "string",
            "Message": "string"
         }
      },
      "PassphraseSecretArn": "string",
      "PeerAddresses": [ "string" ],
      "PeerClusterName": "string",
      "ResourceARN": "string",
      "Status": "string",
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
<a name="API_CreateClusterPeer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClusterPeer](#API_CreateClusterPeer_ResponseSyntax) **   <a name="FSx-CreateClusterPeer-response-ClusterPeer"></a>
A description of the cluster peer.
Type: [ClusterPeer](API_ClusterPeer.md) object

## Errors
<a name="API_CreateClusterPeer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **
A generic error indicating a failure with a client request.
 ** Message **
A detailed error message.
HTTP Status Code: 400

 ** FileSystemNotFound **
No Amazon FSx file systems were found based upon supplied parameters.
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

 ** UnsupportedOperation **
The requested operation is not supported for this resource or API.
 ** Message **
A detailed error message.
HTTP Status Code: 400

## See Also
<a name="API_CreateClusterPeer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/CreateClusterPeer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/CreateClusterPeer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CreateClusterPeer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/CreateClusterPeer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CreateClusterPeer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/CreateClusterPeer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/CreateClusterPeer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/CreateClusterPeer)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/CreateClusterPeer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CreateClusterPeer)
