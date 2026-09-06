---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_AddKeyReplicationRegions.html
---

# AddKeyReplicationRegions
<a name="API_AddKeyReplicationRegions"></a>

Adds replication AWS Regions to an existing AWS Payment Cryptography key, enabling the key to be used for cryptographic operations in additional AWS Regions.

 [Multi-Region key replication](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-multi-region-replication.html) allow you to use the same key material across multiple AWS Regions, providing lower latency for applications distributed across regions. When you add Replication Regions, AWS Payment Cryptography securely replicates the key material to the specified AWS Regions.

The key must be in an active state to add Replication Regions. You can add multiple regions in a single operation, and the key will be available for use in those regions once replication is complete.

 **Cross-account use:** This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see [Resource-based policies](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html).

 **Related operations:**
+  [RemoveKeyReplicationRegions](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_RemoveKeyReplicationRegions.html)
+  [EnableDefaultKeyReplicationRegions](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_EnableDefaultKeyReplicationRegions.html)
+  [GetDefaultKeyReplicationRegions](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetDefaultKeyReplicationRegions.html)

## Request Syntax
<a name="API_AddKeyReplicationRegions_RequestSyntax"></a>

```
{
   "KeyIdentifier": "{{string}}",
   "ReplicationRegions": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_AddKeyReplicationRegions_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [KeyIdentifier](#API_AddKeyReplicationRegions_RequestSyntax) **   <a name="paymentcryptography-AddKeyReplicationRegions-request-KeyIdentifier"></a>
The key identifier (ARN or alias) of the key for which to add replication regions.
This key must exist and be in a valid state for replication operations.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

 ** [ReplicationRegions](#API_AddKeyReplicationRegions_RequestSyntax) **   <a name="paymentcryptography-AddKeyReplicationRegions-request-ReplicationRegions"></a>
The list of AWS Regions to add to the key's replication configuration.
Each region must be a valid AWS Region where AWS Payment Cryptography is available. The key will be replicated to these regions, allowing cryptographic operations to be performed closer to your applications.
Type: Array of strings
Pattern: `[a-z]{2}-[a-z]{1,16}-[0-9]+`
Required: Yes

## Response Syntax
<a name="API_AddKeyReplicationRegions_ResponseSyntax"></a>

```
{
   "Key": {
      "CreateTimestamp": number,
      "DeletePendingTimestamp": number,
      "DeleteTimestamp": number,
      "DeriveKeyUsage": "string",
      "Enabled": boolean,
      "Exportable": boolean,
      "KeyArn": "string",
      "KeyAttributes": {
         "KeyAlgorithm": "string",
         "KeyClass": "string",
         "KeyModesOfUse": {
            "Decrypt": boolean,
            "DeriveKey": boolean,
            "Encrypt": boolean,
            "Generate": boolean,
            "NoRestrictions": boolean,
            "Sign": boolean,
            "Unwrap": boolean,
            "Verify": boolean,
            "Wrap": boolean
         },
         "KeyUsage": "string"
      },
      "KeyCheckValue": "string",
      "KeyCheckValueAlgorithm": "string",
      "KeyOrigin": "string",
      "KeyState": "string",
      "MpaStatus": {
         "InitiationDate": number,
         "MpaSessionArn": "string",
         "Status": "string",
         "StatusMessage": "string"
      },
      "MultiRegionKeyType": "string",
      "PrimaryRegion": "string",
      "ReplicationStatus": {
         "string" : {
            "Status": "string",
            "StatusMessage": "string"
         }
      },
      "UsageStartTimestamp": number,
      "UsageStopTimestamp": number,
      "UsingDefaultReplicationRegions": boolean
   }
}
```

## Response Elements
<a name="API_AddKeyReplicationRegions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Key](#API_AddKeyReplicationRegions_ResponseSyntax) **   <a name="paymentcryptography-AddKeyReplicationRegions-response-Key"></a>
The updated key metadata after adding the replication regions.
This includes the current state of the key and its replication configuration.
Type: [Key](API_Key.md) object

## Errors
<a name="API_AddKeyReplicationRegions_Errors"></a>

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
This exception is thrown when the caller lacks the necessary IAM permissions to perform the requested operation. Verify that your IAM policy includes the required permissions for the specific AWS Payment Cryptography action you're attempting.
HTTP Status Code: 400

 ** ConflictException **
This request can cause an inconsistent state for the resource.
The requested operation conflicts with the current state of the resource. For example, attempting to delete a key that is currently being used, or trying to create a resource that already exists.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure.
This indicates a server-side error within the AWS Payment Cryptography service. If this error persists, contact support for assistance.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request was denied due to resource not found.
The specified key, alias, or other resource does not exist in your account or region. Verify that the resource identifier is correct and that the resource exists in the expected region.
 ** ResourceId **
The identifier of the resource that was not found.
This field contains the specific resource identifier (such as a key ARN or alias name) that could not be located.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
This request would cause a service quota to be exceeded.
You have reached the maximum number of keys, aliases, or other resources allowed in your account. Review your current usage and consider deleting unused resources or requesting a quota increase.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
You have exceeded the rate limits for AWS Payment Cryptography API calls. Implement exponential backoff and retry logic in your application to handle throttling gracefully.
HTTP Status Code: 400

 ** ValidationException **
The request was denied due to an invalid request error.
One or more parameters in your request are invalid. Check the parameter values, formats, and constraints specified in the API documentation.
HTTP Status Code: 400

## See Also
<a name="API_AddKeyReplicationRegions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/payment-cryptography-2021-09-14/AddKeyReplicationRegions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/payment-cryptography-2021-09-14/AddKeyReplicationRegions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/AddKeyReplicationRegions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/payment-cryptography-2021-09-14/AddKeyReplicationRegions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/AddKeyReplicationRegions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/payment-cryptography-2021-09-14/AddKeyReplicationRegions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/payment-cryptography-2021-09-14/AddKeyReplicationRegions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/payment-cryptography-2021-09-14/AddKeyReplicationRegions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/payment-cryptography-2021-09-14/AddKeyReplicationRegions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/AddKeyReplicationRegions)
