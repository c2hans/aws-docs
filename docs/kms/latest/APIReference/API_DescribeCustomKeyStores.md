---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeCustomKeyStores.html
---

# DescribeCustomKeyStores
<a name="API_DescribeCustomKeyStores"></a>

Gets information about [custom key stores](https://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html) in the account and Region.

 This operation is part of the custom key stores feature in AWS KMS, which combines the convenience and extensive integration of AWS KMS with the isolation and control of a key store that you own and manage.

By default, this operation returns information about all custom key stores in the account and Region. To get only information about a particular custom key store, use either the `CustomKeyStoreName` or `CustomKeyStoreId` parameter (but not both).

To determine whether the custom key store is connected to its AWS CloudHSM cluster or external key store proxy, use the `ConnectionState` element in the response. If an attempt to connect the custom key store failed, the `ConnectionState` value is `FAILED` and the `ConnectionErrorCode` element in the response indicates the cause of the failure. For help interpreting the `ConnectionErrorCode`, see [CustomKeyStoresListEntry](API_CustomKeyStoresListEntry.md).

Custom key stores have a `DISCONNECTED` connection state if the key store has never been connected or you used the [DisconnectCustomKeyStore](API_DisconnectCustomKeyStore.md) operation to disconnect it. Otherwise, the connection state is CONNECTED. If your custom key store connection state is `CONNECTED` but you are having trouble using it, verify that the backing store is active and available. For an AWS CloudHSM key store, verify that the associated AWS CloudHSM cluster is active and contains the minimum number of HSMs required for the operation, if any. For an external key store, verify that the external key store proxy and its associated external key manager are reachable and enabled.

 For help repairing your AWS CloudHSM key store, see the [Troubleshooting AWS CloudHSM key stores](https://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html). For help repairing your external key store, see the [Troubleshooting external key stores](https://docs.aws.amazon.com/kms/latest/developerguide/xks-troubleshooting.html). Both topics are in the * AWS Key Management Service Developer Guide*.

 **Cross-account use**: No. You cannot perform this operation on a custom key store in a different AWS account.

 **Required permissions**: [kms:DescribeCustomKeyStores](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (IAM policy)

 **Related operations:**
+  [ConnectCustomKeyStore](API_ConnectCustomKeyStore.md)
+  [CreateCustomKeyStore](API_CreateCustomKeyStore.md)
+  [DeleteCustomKeyStore](API_DeleteCustomKeyStore.md)
+  [DisconnectCustomKeyStore](API_DisconnectCustomKeyStore.md)
+  [UpdateCustomKeyStore](API_UpdateCustomKeyStore.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_DescribeCustomKeyStores_RequestSyntax"></a>

```
{
   "CustomKeyStoreId": "{{string}}",
   "CustomKeyStoreName": "{{string}}",
   "Limit": {{number}},
   "Marker": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeCustomKeyStores_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [CustomKeyStoreId](#API_DescribeCustomKeyStores_RequestSyntax) **   <a name="KMS-DescribeCustomKeyStores-request-CustomKeyStoreId"></a>
Gets only information about the specified custom key store. Enter the key store ID.
By default, this operation gets information about all custom key stores in the account and Region. To limit the output to a particular custom key store, provide either the `CustomKeyStoreId` or `CustomKeyStoreName` parameter, but not both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [CustomKeyStoreName](#API_DescribeCustomKeyStores_RequestSyntax) **   <a name="KMS-DescribeCustomKeyStores-request-CustomKeyStoreName"></a>
Gets only information about the specified custom key store. Enter the friendly name of the custom key store.
By default, this operation gets information about all custom key stores in the account and Region. To limit the output to a particular custom key store, provide either the `CustomKeyStoreId` or `CustomKeyStoreName` parameter, but not both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [Limit](#API_DescribeCustomKeyStores_RequestSyntax) **   <a name="KMS-DescribeCustomKeyStores-request-Limit"></a>
Use this parameter to specify the maximum number of items to return. When this value is present, AWS KMS does not return more than the specified number of items, but it might return fewer.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [Marker](#API_DescribeCustomKeyStores_RequestSyntax) **   <a name="KMS-DescribeCustomKeyStores-request-Marker"></a>
Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of `NextMarker` from the truncated response you just received.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\u00FF]*`
Required: No

## Response Syntax
<a name="API_DescribeCustomKeyStores_ResponseSyntax"></a>

```
{
   "CustomKeyStores": [
      {
         "CloudHsmClusterId": "string",
         "ConnectionErrorCode": "string",
         "ConnectionState": "string",
         "CreationDate": number,
         "CustomKeyStoreId": "string",
         "CustomKeyStoreName": "string",
         "CustomKeyStoreType": "string",
         "TrustAnchorCertificate": "string",
         "XksProxyConfiguration": {
            "AccessKeyId": "string",
            "Connectivity": "string",
            "UriEndpoint": "string",
            "UriPath": "string",
            "VpcEndpointServiceName": "string",
            "VpcEndpointServiceOwner": "string"
         }
      }
   ],
   "NextMarker": "string",
   "Truncated": boolean
}
```

## Response Elements
<a name="API_DescribeCustomKeyStores_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CustomKeyStores](#API_DescribeCustomKeyStores_ResponseSyntax) **   <a name="KMS-DescribeCustomKeyStores-response-CustomKeyStores"></a>
Contains metadata about each custom key store.
Type: Array of [CustomKeyStoresListEntry](API_CustomKeyStoresListEntry.md) objects

 ** [NextMarker](#API_DescribeCustomKeyStores_ResponseSyntax) **   <a name="KMS-DescribeCustomKeyStores-response-NextMarker"></a>
When `Truncated` is true, this element is present and contains the value to use for the `Marker` parameter in a subsequent request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\u00FF]*`

 ** [Truncated](#API_DescribeCustomKeyStores_ResponseSyntax) **   <a name="KMS-DescribeCustomKeyStores-response-Truncated"></a>
A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the `NextMarker` element in this response to the `Marker` parameter in a subsequent request.
Type: Boolean

## Errors
<a name="API_DescribeCustomKeyStores_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CustomKeyStoreNotFoundException **
The request was rejected because AWS KMS cannot find a custom key store with the specified key store name or ID.
HTTP Status Code: 400

 ** InvalidMarkerException **
The request was rejected because the marker that specifies where pagination should next begin is not valid.
HTTP Status Code: 400

 ** KMSInternalException **
The request was rejected because an internal exception occurred. The request can be retried.
HTTP Status Code: 500

## See Also
<a name="API_DescribeCustomKeyStores_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/DescribeCustomKeyStores)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/DescribeCustomKeyStores)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/DescribeCustomKeyStores)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/DescribeCustomKeyStores)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/DescribeCustomKeyStores)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/DescribeCustomKeyStores)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/DescribeCustomKeyStores)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/DescribeCustomKeyStores)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/DescribeCustomKeyStores)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/DescribeCustomKeyStores)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for KMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
