---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_UpdateClusterPeer.html
---

# UpdateClusterPeer

Updates an Amazon FSx for NetApp ONTAP cluster peer relationship.

## Request Syntax
<a name="API_UpdateClusterPeer_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "ClusterPeerId": "{{string}}",
   "PeerAddresses": [ "{{string}}" ],
   "PeerClusterName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateClusterPeer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_UpdateClusterPeer_RequestSyntax) **   <a name="FSx-UpdateClusterPeer-request-ClientRequestToken"></a>
(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-za-z0-9_.-]{0,63}$`
Required: No

 ** [ClusterPeerId](#API_UpdateClusterPeer_RequestSyntax) **   <a name="FSx-UpdateClusterPeer-request-ClusterPeerId"></a>
The ID of the cluster peer that you want to update.
Type: String
Pattern: `^(clusterpeer-[0-9a-f]{17})$`
Required: Yes

 ** [PeerAddresses](#API_UpdateClusterPeer_RequestSyntax) **   <a name="FSx-UpdateClusterPeer-request-PeerAddresses"></a>
Specifies the IP addresses of the intercluster logical interfaces (LIFs) on the peer cluster. The addresses that you specify replace the existing peer addresses.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 288 items.
Length Constraints: Minimum length of 1. Maximum length of 45.
Pattern: `(^((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))$|^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$)`
Required: No

 ** [PeerClusterName](#API_UpdateClusterPeer_RequestSyntax) **   <a name="FSx-UpdateClusterPeer-request-PeerClusterName"></a>
Specifies the name that the file system uses to identify the peer cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 44.
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,44}$`
Required: No

## Response Syntax
<a name="API_UpdateClusterPeer_ResponseSyntax"></a>

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
<a name="API_UpdateClusterPeer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClusterPeer](#API_UpdateClusterPeer_ResponseSyntax) **   <a name="FSx-UpdateClusterPeer-response-ClusterPeer"></a>
A description of the cluster peer that was just updated.
Type: [ClusterPeer](API_ClusterPeer.md) object

## Errors
<a name="API_UpdateClusterPeer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **
A generic error indicating a failure with a client request.
 ** Message **
A detailed error message.
HTTP Status Code: 400

 ** ClusterPeerNotFound **
No Amazon FSx cluster peers were found based on the supplied parameters.
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

## See Also
<a name="API_UpdateClusterPeer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/UpdateClusterPeer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/UpdateClusterPeer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/UpdateClusterPeer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/UpdateClusterPeer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/UpdateClusterPeer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/UpdateClusterPeer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/UpdateClusterPeer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/UpdateClusterPeer)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/UpdateClusterPeer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/UpdateClusterPeer)
