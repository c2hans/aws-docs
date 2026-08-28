---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_CreateOdbNetwork.html
---

# CreateOdbNetwork
<a name="API_CreateOdbNetwork"></a>

Creates an ODB network.

## Request Syntax
<a name="API_CreateOdbNetwork_RequestSyntax"></a>

```
{
   "availabilityZone": "{{string}}",
   "availabilityZoneId": "{{string}}",
   "backupSubnetCidr": "{{string}}",
   "clientSubnetCidr": "{{string}}",
   "clientToken": "{{string}}",
   "crossRegionS3RestoreSourcesToEnable": [ "{{string}}" ],
   "customDomainName": "{{string}}",
   "defaultDnsPrefix": "{{string}}",
   "displayName": "{{string}}",
   "kmsAccess": "{{string}}",
   "kmsPolicyDocument": "{{string}}",
   "s3Access": "{{string}}",
   "s3PolicyDocument": "{{string}}",
   "stsAccess": "{{string}}",
   "stsPolicyDocument": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "zeroEtlAccess": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateOdbNetwork_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [availabilityZone](#API_CreateOdbNetwork_RequestSyntax) **   <a name="odb-CreateOdbNetwork-request-availabilityZone"></a>
The AWS Availability Zone (AZ) where the ODB network is located.
This operation requires that you specify a value for either `availabilityZone` or `availabilityZoneId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [availabilityZoneId](#API_CreateOdbNetwork_RequestSyntax) **   <a name="odb-CreateOdbNetwork-request-availabilityZoneId"></a>
The AZ ID of the AZ where the ODB network is located.
This operation requires that you specify a value for either `availabilityZone` or `availabilityZoneId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [backupSubnetCidr](#API_CreateOdbNetwork_RequestSyntax) **   <a name="odb-CreateOdbNetwork-request-backupSubnetCidr"></a>
The CIDR range of the backup subnet for the ODB network.
Constraints:
+ Must not overlap with the CIDR range of the client subnet.
+ Must not overlap with the CIDR ranges of the VPCs that are connected to the ODB network.
+ Must not use the following CIDR ranges that are reserved by OCI:
  +  `100.106.0.0/16` and `100.107.0.0/16`
  +  `169.254.0.0/16`
  +  `224.0.0.0 - 239.255.255.255`
  +  `240.0.0.0 - 255.255.255.255`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 43.
Required: No

 ** [clientSubnetCidr](#API_CreateOdbNetwork_RequestSyntax) **   <a name="odb-CreateOdbNetwork-request-clientSubnetCidr"></a>
The CIDR range of the client subnet for the ODB network.
Constraints:
+ Must not overlap with the CIDR range of the backup subnet.
+ Must not overlap with the CIDR ranges of the VPCs that are connected to the ODB network.
+ Must not use the following CIDR ranges that are reserved by OCI:
  +  `100.106.0.0/16` and `100.107.0.0/16`
  +  `169.254.0.0/16`
  +  `224.0.0.0 - 239.255.255.255`
  +  `240.0.0.0 - 255.255.255.255`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 43.
Required: Yes

 ** [clientToken](#API_CreateOdbNetwork_RequestSyntax) **   <a name="odb-CreateOdbNetwork-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. The client token is valid for up to 24 hours after it's first used.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 64.
Pattern: `[a-zA-Z0-9_\/.=-]+`
Required: No

 ** [crossRegionS3RestoreSourcesToEnable](#API_CreateOdbNetwork_RequestSyntax) **   <a name="odb-CreateOdbNetwork-request-crossRegionS3RestoreSourcesToEnable"></a>
The cross-Region Amazon S3 restore sources to enable for the ODB network.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** [customDomainName](#API_CreateOdbNetwork_RequestSyntax) **   <a name="odb-CreateOdbNetwork-request-customDomainName"></a>
The domain name to use for the resources in the ODB network.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [defaultDnsPrefix](#API_CreateOdbNetwork_RequestSyntax) **   <a name="odb-CreateOdbNetwork-request-defaultDnsPrefix"></a>
The DNS prefix to the default DNS domain name. The default DNS domain name is oraclevcn.com.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 15.
Pattern: `[a-zA-Z][a-zA-Z0-9]*`
Required: No

 ** [displayName](#API_CreateOdbNetwork_RequestSyntax) **   <a name="odb-CreateOdbNetwork-request-displayName"></a>
A user-friendly name for the ODB network.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_](?!.*--)[a-zA-Z0-9_-]*`
Required: Yes

 ** [kmsAccess](#API_CreateOdbNetwork_RequestSyntax) **   <a name="odb-CreateOdbNetwork-request-kmsAccess"></a>
The AWS Key Management Service (KMS) access configuration for the ODB network.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [kmsPolicyDocument](#API_CreateOdbNetwork_RequestSyntax) **   <a name="odb-CreateOdbNetwork-request-kmsPolicyDocument"></a>
The AWS Key Management Service (KMS) policy document that defines permissions for key usage within the ODB network.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 20480.
Required: No

 ** [s3Access](#API_CreateOdbNetwork_RequestSyntax) **   <a name="odb-CreateOdbNetwork-request-s3Access"></a>
Specifies the configuration for Amazon S3 access from the ODB network.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [s3PolicyDocument](#API_CreateOdbNetwork_RequestSyntax) **   <a name="odb-CreateOdbNetwork-request-s3PolicyDocument"></a>
Specifies the endpoint policy for Amazon S3 access from the ODB network.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 20480.
Required: No

 ** [stsAccess](#API_CreateOdbNetwork_RequestSyntax) **   <a name="odb-CreateOdbNetwork-request-stsAccess"></a>
The AWS Security Token Service (STS) access configuration for the ODB network.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [stsPolicyDocument](#API_CreateOdbNetwork_RequestSyntax) **   <a name="odb-CreateOdbNetwork-request-stsPolicyDocument"></a>
The AWS Security Token Service (STS) policy document that defines permissions for token service usage within the ODB network.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 20480.
Required: No

 ** [tags](#API_CreateOdbNetwork_RequestSyntax) **   <a name="odb-CreateOdbNetwork-request-tags"></a>
The list of resource tags to apply to the ODB network.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [zeroEtlAccess](#API_CreateOdbNetwork_RequestSyntax) **   <a name="odb-CreateOdbNetwork-request-zeroEtlAccess"></a>
Specifies the configuration for Zero-ETL access from the ODB network.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## Response Syntax
<a name="API_CreateOdbNetwork_ResponseSyntax"></a>

```
{
   "displayName": "string",
   "odbNetworkId": "string",
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_CreateOdbNetwork_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [displayName](#API_CreateOdbNetwork_ResponseSyntax) **   <a name="odb-CreateOdbNetwork-response-displayName"></a>
The user-friendly name of the ODB network.
Type: String

 ** [odbNetworkId](#API_CreateOdbNetwork_ResponseSyntax) **   <a name="odb-CreateOdbNetwork-response-odbNetworkId"></a>
The unique identifier of the ODB network.
Type: String

 ** [status](#API_CreateOdbNetwork_ResponseSyntax) **   <a name="odb-CreateOdbNetwork-response-status"></a>
The current status of the ODB network.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS`

 ** [statusReason](#API_CreateOdbNetwork_ResponseSyntax) **   <a name="odb-CreateOdbNetwork-response-statusReason"></a>
Additional information about the status of the ODB network.
Type: String

## Errors
<a name="API_CreateOdbNetwork_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.
HTTP Status Code: 400

 ** ConflictException **
Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.
 ** resourceId **
The identifier of the resource that caused the conflict.
 ** resourceType **
The type of resource that caused the conflict.
HTTP Status Code: 400

 ** InternalServerException **
Occurs when there is an internal failure in the Oracle Database@AWS service. Wait and try again.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after an internal server error.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
You have exceeded the service quota.
 ** quotaCode **
The unqiue identifier of the service quota that was exceeded.
 ** resourceId **
The identifier of the resource that exceeded the service quota.
 ** resourceType **
The type of resource that exceeded the service quota.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after being throttled.
HTTP Status Code: 400

 ** ValidationException **
The request has failed validation because it is missing required fields or has invalid inputs.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
The reason why the validation failed.
HTTP Status Code: 400

## See Also
<a name="API_CreateOdbNetwork_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/CreateOdbNetwork)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/CreateOdbNetwork)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/CreateOdbNetwork)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/CreateOdbNetwork)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/CreateOdbNetwork)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/CreateOdbNetwork)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/CreateOdbNetwork)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/CreateOdbNetwork)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/CreateOdbNetwork)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/CreateOdbNetwork)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
