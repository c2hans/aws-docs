---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeClusterPeers.html
---

# DescribeClusterPeers

Returns the description of specific Amazon FSx for NetApp ONTAP cluster peers, if a `ClusterPeerIds` value is provided. Otherwise, this operation returns all cluster peers owned by your AWS account in the AWS Region of the endpoint that you're calling.

When retrieving all cluster peers, you can optionally specify the `MaxResults` parameter to limit the number of cluster peers in a response. If more cluster peers remain, Amazon FSx returns a `NextToken` value in the response. In this case, send a later request with the `NextToken` request parameter set to the value of `NextToken` from the last response.

## Request Syntax
<a name="API_DescribeClusterPeers_RequestSyntax"></a>

```
{
   "ClusterPeerIds": [ "{{string}}" ],
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeClusterPeers_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterPeerIds](#API_DescribeClusterPeers_RequestSyntax) **   <a name="FSx-DescribeClusterPeers-request-ClusterPeerIds"></a>
The IDs of the cluster peers that you want to retrieve. If you also specify `Filters`, only cluster peers that match both the IDs and the filters are returned. If any IDs aren't found, or if a filter excludes any of them, a `ClusterPeerNotFound` error occurs.
Type: Array of strings
Array Members: Maximum number of 50 items.
Pattern: `^(clusterpeer-[0-9a-f]{17})$`
Required: No

 ** [Filters](#API_DescribeClusterPeers_RequestSyntax) **   <a name="FSx-DescribeClusterPeers-request-Filters"></a>
The filters structure. The supported name is `file-system-id`.
Type: Array of [ClusterPeerFilter](API_ClusterPeerFilter.md) objects
Array Members: Maximum number of 1 item.
Required: No

 ** [MaxResults](#API_DescribeClusterPeers_RequestSyntax) **   <a name="FSx-DescribeClusterPeers-request-MaxResults"></a>
The maximum number of resources to return in the response. This value must be an integer greater than zero.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2147483647.
Required: No

 ** [NextToken](#API_DescribeClusterPeers_RequestSyntax) **   <a name="FSx-DescribeClusterPeers-request-NextToken"></a>
(Optional) Opaque pagination token returned from a previous operation (String). If present, this token indicates from what point you can continue processing the request, where the previous `NextToken` value left off.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$`
Required: No

## Response Syntax
<a name="API_DescribeClusterPeers_ResponseSyntax"></a>

```
{
   "ClusterPeers": [
      {
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
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeClusterPeers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClusterPeers](#API_DescribeClusterPeers_ResponseSyntax) **   <a name="FSx-DescribeClusterPeers-response-ClusterPeers"></a>
Describes each cluster peer returned by the `DescribeClusterPeers` operation.
Type: Array of [ClusterPeer](API_ClusterPeer.md) objects
Array Members: Maximum number of 50 items.

 ** [NextToken](#API_DescribeClusterPeers_ResponseSyntax) **   <a name="FSx-DescribeClusterPeers-response-NextToken"></a>
(Optional) Opaque pagination token returned from a previous operation (String). If present, this token indicates from what point you can continue processing the request, where the previous `NextToken` value left off.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$`

## Errors
<a name="API_DescribeClusterPeers_Errors"></a>

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

 ** FileSystemNotFound **
No Amazon FSx file systems were found based upon supplied parameters.
 ** Message **
A detailed error message.
HTTP Status Code: 400

 ** InternalServerError **
A generic error indicating a server-side failure.
 ** Message **
A detailed error message.
HTTP Status Code: 500

## See Also
<a name="API_DescribeClusterPeers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/DescribeClusterPeers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/DescribeClusterPeers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DescribeClusterPeers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/DescribeClusterPeers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DescribeClusterPeers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/DescribeClusterPeers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/DescribeClusterPeers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/DescribeClusterPeers)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/DescribeClusterPeers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DescribeClusterPeers)
