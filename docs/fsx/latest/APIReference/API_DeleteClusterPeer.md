---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_DeleteClusterPeer.html
---

# DeleteClusterPeer

Deletes an Amazon FSx for NetApp ONTAP cluster peer relationship.

## Request Syntax
<a name="API_DeleteClusterPeer_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "ClusterPeerId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteClusterPeer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_DeleteClusterPeer_RequestSyntax) **   <a name="FSx-DeleteClusterPeer-request-ClientRequestToken"></a>
(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-za-z0-9_.-]{0,63}$`
Required: No

 ** [ClusterPeerId](#API_DeleteClusterPeer_RequestSyntax) **   <a name="FSx-DeleteClusterPeer-request-ClusterPeerId"></a>
The ID of the cluster peer that you are deleting.
Type: String
Pattern: `^(clusterpeer-[0-9a-f]{17})$`
Required: Yes

## Response Syntax
<a name="API_DeleteClusterPeer_ResponseSyntax"></a>

```
{
   "ClusterPeerId": "string",
   "Lifecycle": "string"
}
```

## Response Elements
<a name="API_DeleteClusterPeer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClusterPeerId](#API_DeleteClusterPeer_ResponseSyntax) **   <a name="FSx-DeleteClusterPeer-response-ClusterPeerId"></a>
The ID of the cluster peer that's being deleted.
Type: String
Pattern: `^(clusterpeer-[0-9a-f]{17})$`

 ** [Lifecycle](#API_DeleteClusterPeer_ResponseSyntax) **   <a name="FSx-DeleteClusterPeer-response-Lifecycle"></a>
The lifecycle state of the cluster peer being deleted. If the `DeleteClusterPeer` operation is successful, this value is `DELETING`.
Type: String
Valid Values: `CREATING | CREATED | DELETING | FAILED`

## Errors
<a name="API_DeleteClusterPeer_Errors"></a>

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
<a name="API_DeleteClusterPeer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/DeleteClusterPeer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/DeleteClusterPeer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DeleteClusterPeer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/DeleteClusterPeer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DeleteClusterPeer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/DeleteClusterPeer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/DeleteClusterPeer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/DeleteClusterPeer)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/DeleteClusterPeer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DeleteClusterPeer)
