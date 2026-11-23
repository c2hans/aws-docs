---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_UpdateRevenueAttribution.html
---

# UpdateRevenueAttribution

Updates an existing revenue attribution record.

## Request Parameters
<a name="API_prm_UpdateRevenueAttribution_RequestParameters"></a>

 ** Catalog **
The catalog that the revenue attribution belongs to.
Type: String
Valid Values: `AWS | Sandbox`
Required: Yes

 ** Identifier **
The unique identifier of the revenue attribution to update. Accepts a direct ID or ARN.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 1011.
Pattern: `(arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[a-zA-Z]+/revenue-attribution/ra-[a-z0-9]{13}|ra-[a-z0-9]{13})`
Required: Yes

 ** Revision **
The current revision of the revenue attribution. Must match the server's current value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[1-9][0-9]*`
Required: Yes

 ** ClientToken **
A unique token to ensure idempotency of the update request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]{1,64}`
Required: No

 ** Context **
The complete set of key-value context attributes for the revenue attribution. This replaces the existing context. Omit to leave the existing context unchanged, or specify an empty map to remove all context attributes.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\x21-\x7E]+`
Value Length Constraints: Minimum length of 1. Maximum length of 1024.
Value Pattern: `[\x20-\x7E]+`
Required: No

 ** Description **
The updated description of the revenue attribution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\x20-\x7E]*`
Required: No

## Response Elements
<a name="API_prm_UpdateRevenueAttribution_ResponseElements"></a>

The following elements are returned by the service.

 ** Arn **
The Amazon Resource Name (ARN) of the updated revenue attribution.
Type: String

 ** Id **
The unique identifier of the updated revenue attribution.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 1011.
Pattern: `(arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[a-zA-Z]+/revenue-attribution/ra-[a-z0-9]{13}|ra-[a-z0-9]{13})`

 ** LastModifiedDate **
The date when the attribution was last modified.
Type: Timestamp

 ** Context **
The key-value context attributes associated with the revenue attribution after the update.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\x21-\x7E]+`
Value Length Constraints: Minimum length of 1. Maximum length of 1024.
Value Pattern: `[\x20-\x7E]+`

 ** Description **
The updated description of the revenue attribution.
Type: String

 ** LatestRevision **
The latest revision of the attribution after the update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[1-9][0-9]*`

## Errors
<a name="API_prm_UpdateRevenueAttribution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied due to insufficient permissions.
 ** Message **
A message that describes why access was denied.
 ** Reason **
The reason for the access denial.
HTTP Status Code: 403

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the resource.
 ** Message **
A message that describes the conflict.
 ** Reason **
The reason for the conflict.
HTTP Status Code: 409

 ** InternalServerException **
An internal server error occurred. Retry your request.
 ** Message **
A message that describes the internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
A message that describes which resource was not found.
 ** Reason **
The reason the resource was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled due to too many requests. Retry your request.
 ** Message **
A message that indicates the request rate limit was exceeded.
 ** QuotaCode **
The quota code associated with the throttling error.
 ** ServiceCode **
The service code associated with the throttling error.
HTTP Status Code: 429

 ** ValidationException **
The request failed validation due to invalid input parameters.
 ** FieldList **
A list of fields that failed validation.
 ** Message **
A message that describes the validation failure.
 ** Reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_prm_UpdateRevenueAttribution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-revenue-measurement-2022-07-26/UpdateRevenueAttribution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-revenue-measurement-2022-07-26/UpdateRevenueAttribution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/UpdateRevenueAttribution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-revenue-measurement-2022-07-26/UpdateRevenueAttribution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/UpdateRevenueAttribution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-revenue-measurement-2022-07-26/UpdateRevenueAttribution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-revenue-measurement-2022-07-26/UpdateRevenueAttribution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-revenue-measurement-2022-07-26/UpdateRevenueAttribution)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-revenue-measurement-2022-07-26/UpdateRevenueAttribution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/UpdateRevenueAttribution)
