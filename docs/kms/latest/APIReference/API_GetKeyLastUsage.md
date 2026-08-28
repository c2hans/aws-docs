---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_GetKeyLastUsage.html
---

# GetKeyLastUsage
<a name="API_GetKeyLastUsage"></a>

Returns usage information about the last successful cryptographic operation performed with a specified KMS key, including the operation type, timestamp, and associated AWS CloudTrail event ID.

The `TrackingStartDate` in the `GetKeyLastUsage` response indicates the date from which AWS KMS began recording cryptographic activity for a given key. Use this value together with `KeyCreationDate` to understand the key's usage history:
+ If the `KeyLastUsage` response element is *present*, the key has been used for a successful cryptographic operation since the `TrackingStartDate`. The response includes the operation type, timestamp, and associated CloudTrail event ID.
+ If the `KeyLastUsage` response element is *empty* and `KeyCreationDate` is on or after `TrackingStartDate`, the key has not been used for a successful cryptographic operation since it was created.
+ If the `KeyLastUsage` response element is *empty* and `KeyCreationDate` is before `TrackingStartDate`, there is no record of the key being used for a successful cryptographic operation since the `TrackingStartDate`. However, the key may have been used before tracking began. To determine whether the key was used before the `TrackingStartDate`, examine your past AWS CloudTrail logs.

For multi-Region KMS keys, primary and replica keys track last usage independently. Each key in a multi-Region key set maintains its own usage information.

The `ReEncrypt` operation uses two keys: a source key for decryption and a destination key for encryption. Usage information is recorded for both keys independently, each with the AWS CloudTrail event ID from the respective key owner's account.

**Note**
Do not use `GetKeyLastUsage` as the sole indicator when scheduling a key for deletion. Instead, first [disable the key](https://docs.aws.amazon.com/kms/latest/developerguide/enabling-keys.html) and monitor AWS CloudTrail for `DisabledException` entries, as there could be infrequent workflows that are dependent on the key. By looking for this exception, you can identify potential dependencies and workload failures before they occur. AWS CloudTrail remains the authoritative source for all API calls made to your key.

 **Cross-account use**: No. You cannot perform this operation on a KMS key in a different AWS account.

 **Required permissions**: [kms:GetKeyLastUsage](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy)

 **Related operations:**
+  [DescribeKey](API_DescribeKey.md)
+  [DisableKey](API_DisableKey.md)
+  [ScheduleKeyDeletion](API_ScheduleKeyDeletion.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_GetKeyLastUsage_RequestSyntax"></a>

```
{
   "KeyId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetKeyLastUsage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [KeyId](#API_GetKeyLastUsage_RequestSyntax) **   <a name="KMS-GetKeyLastUsage-request-KeyId"></a>
Identifies the KMS key to get usage information for. To specify a KMS key, use its key ID or key ARN. Alias names are not supported.
Specify the key ID or key ARN of the KMS key.
For example:
+ Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
+ Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
To get the key ID and key ARN for a KMS key, use [ListKeys](API_ListKeys.md) or [DescribeKey](API_DescribeKey.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Response Syntax
<a name="API_GetKeyLastUsage_ResponseSyntax"></a>

```
{
   "KeyCreationDate": number,
   "KeyId": "string",
   "KeyLastUsage": {
      "CloudTrailEventId": "string",
      "KmsRequestId": "string",
      "Operation": "string",
      "Timestamp": number
   },
   "TrackingStartDate": number
}
```

## Response Elements
<a name="API_GetKeyLastUsage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [KeyCreationDate](#API_GetKeyLastUsage_ResponseSyntax) **   <a name="KMS-GetKeyLastUsage-response-KeyCreationDate"></a>
The date and time when the KMS key was created.
Type: Timestamp

 ** [KeyId](#API_GetKeyLastUsage_ResponseSyntax) **   <a name="KMS-GetKeyLastUsage-response-KeyId"></a>
The globally unique identifier for the KMS key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [KeyLastUsage](#API_GetKeyLastUsage_ResponseSyntax) **   <a name="KMS-GetKeyLastUsage-response-KeyLastUsage"></a>
Contains usage information about the last time the KMS key was used for a successful cryptographic operation. If the key has not been used since tracking began, this response element is an empty object.
Type: [KeyLastUsageData](API_KeyLastUsageData.md) object

 ** [TrackingStartDate](#API_GetKeyLastUsage_ResponseSyntax) **   <a name="KMS-GetKeyLastUsage-response-TrackingStartDate"></a>
The date from which AWS KMS began recording cryptographic activity for this key, or the date the KMS key was created, whichever is later.
Type: Timestamp

## Errors
<a name="API_GetKeyLastUsage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependencyTimeoutException **
The system timed out while trying to fulfill the request. You can retry the request.
HTTP Status Code: 500

 ** InvalidArnException **
The request was rejected because a specified ARN, or an ARN in a key policy, is not valid.
HTTP Status Code: 400

 ** KMSInternalException **
The request was rejected because an internal exception occurred. The request can be retried.
HTTP Status Code: 500

 ** NotFoundException **
The request was rejected because the specified entity or resource could not be found.
HTTP Status Code: 400

## See Also
<a name="API_GetKeyLastUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/GetKeyLastUsage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/GetKeyLastUsage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/GetKeyLastUsage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/GetKeyLastUsage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/GetKeyLastUsage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/GetKeyLastUsage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/GetKeyLastUsage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/GetKeyLastUsage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/GetKeyLastUsage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/GetKeyLastUsage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for KMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
