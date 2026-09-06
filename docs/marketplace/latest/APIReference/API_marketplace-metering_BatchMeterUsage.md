---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-metering_BatchMeterUsage.html
---

# BatchMeterUsage
<a name="API_marketplace-metering_BatchMeterUsage"></a>

**Important**
 AWS Marketplace is introducing Concurrent Agreements, enabling buyers to make multiple purchases per AWS account. Starting June 1, 2026, new SaaS products must use `CustomerAWSAccountId` (instead of `CustomerIdentifier`), `LicenseArn` (instead of `ProductCode`) to support this feature. `BatchMeterUsage` does not support `CustomerIdentifier` for new integrations. Existing integrations continue to work. Review the new integration for Concurrent Agreements [here](https://catalog.workshops.aws/mpseller/en-US/saas/integration-for-concurrent-agreements). For additional implementation details, see [BatchMeterUsage code example with LicenseArn](https://docs.aws.amazon.com/marketplace/latest/userguide/saas-code-examples.html#saas-batchmeterusage-licensearn-example) in the * AWS Marketplace Seller Guide*.

To post metering records for customers, SaaS applications call `BatchMeterUsage`, which is used for metering SaaS flexible consumption pricing (FCP). Identical requests are idempotent and can be retried with the same records or a subset of records. Each `BatchMeterUsage` request is for only one product. If you want to meter usage for multiple products, you must make multiple `BatchMeterUsage` calls.

Usage records should be submitted in quick succession following a recorded event. Usage records aren't accepted 24 hours or more after an event. At the end of each billing cycle, a 6-hour grace period applies. We accept usage records for the previous billing month until 06:00 UTC on the first day of the next month. For example, you must submit March usage records before 06:00 UTC on April 1. On April 1 at 05:00 UTC, you can still submit records for March 31 (within the 6-hour grace period). After 06:00 UTC on April 1, March records are rejected regardless of the normal 24-hour submission window. After this grace period, we return a `TimestampOutOfBoundsException` error.

 `BatchMeterUsage` can process up to 25 `UsageRecords` at a time, and each request must be less than 1 MB in size. Optionally, you can have multiple usage allocations for usage data that's split into buckets according to predefined tags.

 `BatchMeterUsage` returns a list of `UsageRecordResult` objects, which have each `UsageRecord`. It also returns a list of `UnprocessedRecords`, which indicate errors on the service side that should be retried.

For AWS Regions that support `BatchMeterUsage`, see [BatchMeterUsage Region support](https://docs.aws.amazon.com/marketplace/latest/APIReference/metering-regions.html#batchmeterusage-region-support).

**Note**
For an example of `BatchMeterUsage`, see [ BatchMeterUsage code example](https://docs.aws.amazon.com/marketplace/latest/userguide/saas-code-examples.html#saas-batchmeterusage-example) in the * AWS Marketplace Seller Guide*.

## Request Syntax
<a name="API_marketplace-metering_BatchMeterUsage_RequestSyntax"></a>

```
{
   "ProductCode": "{{string}}",
   "UsageRecords": [
      {
         "CustomerAWSAccountId": "{{string}}",
         "CustomerIdentifier": "{{string}}",
         "Dimension": "{{string}}",
         "LicenseArn": "{{string}}",
         "Quantity": {{number}},
         "Timestamp": {{number}},
         "UsageAllocations": [
            {
               "AllocatedUsageQuantity": {{number}},
               "Tags": [
                  {
                     "Key": "{{string}}",
                     "Value": "{{string}}"
                  }
               ]
            }
         ]
      }
   ]
}
```

## Request Parameters
<a name="API_marketplace-metering_BatchMeterUsage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [UsageRecords](#API_marketplace-metering_BatchMeterUsage_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-metering_BatchMeterUsage-request-UsageRecords"></a>
The set of `UsageRecords` to submit. `BatchMeterUsage` accepts up to 25 `UsageRecords` at a time.
Type: Array of [UsageRecord](API_marketplace-metering_UsageRecord.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Required: Yes

 ** [ProductCode](#API_marketplace-metering_BatchMeterUsage_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-metering_BatchMeterUsage-request-ProductCode"></a>
Product code is used to uniquely identify a product in AWS Marketplace. The product code should be the same as the one used during the publishing of a new product.
 `ProductCode` is required only for legacy integrations that use `CustomerIdentifier`. For new integrations using `LicenseArn` (Concurrent Agreements), do NOT include `ProductCode` at the request level. The `LicenseArn` in each `UsageRecord` identifies both the product and the specific agreement.
Sending metering records with both `ProductCode` and `LicenseArn` for the same customer within the same hour will result in duplicate billing. If you are migrating from product-based metering to license-based metering, stop sending `ProductCode` before you start sending `LicenseArn`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `^[-a-zA-Z0-9/=:_.@]*$`
Required: No

## Response Syntax
<a name="API_marketplace-metering_BatchMeterUsage_ResponseSyntax"></a>

```
{
   "Results": [
      {
         "MeteringRecordId": "string",
         "Status": "string",
         "UsageRecord": {
            "CustomerAWSAccountId": "string",
            "CustomerIdentifier": "string",
            "Dimension": "string",
            "LicenseArn": "string",
            "Quantity": number,
            "Timestamp": number,
            "UsageAllocations": [
               {
                  "AllocatedUsageQuantity": number,
                  "Tags": [
                     {
                        "Key": "string",
                        "Value": "string"
                     }
                  ]
               }
            ]
         }
      }
   ],
   "UnprocessedRecords": [
      {
         "CustomerAWSAccountId": "string",
         "CustomerIdentifier": "string",
         "Dimension": "string",
         "LicenseArn": "string",
         "Quantity": number,
         "Timestamp": number,
         "UsageAllocations": [
            {
               "AllocatedUsageQuantity": number,
               "Tags": [
                  {
                     "Key": "string",
                     "Value": "string"
                  }
               ]
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_marketplace-metering_BatchMeterUsage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Results](#API_marketplace-metering_BatchMeterUsage_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-metering_BatchMeterUsage-response-Results"></a>
Contains all `UsageRecords` processed by `BatchMeterUsage`. These records were either honored by AWS Marketplace Metering Service or were invalid. Invalid records should be fixed before being resubmitted.
Type: Array of [UsageRecordResult](API_marketplace-metering_UsageRecordResult.md) objects

 ** [UnprocessedRecords](#API_marketplace-metering_BatchMeterUsage_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-metering_BatchMeterUsage-response-UnprocessedRecords"></a>
Contains all `UsageRecords` that were not processed by `BatchMeterUsage`. This is a list of `UsageRecords`. You can retry the failed request by making another `BatchMeterUsage` call with this list as input in the `BatchMeterUsageRequest`.
Type: Array of [UsageRecord](API_marketplace-metering_UsageRecord.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.

## Errors
<a name="API_marketplace-metering_BatchMeterUsage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DisabledApiException **
The API is disabled in the Region.
HTTP Status Code: 400

 ** InternalServiceErrorException **
An internal error has occurred. Retry your request. If the problem persists, post a message with details on the AWS forums.
HTTP Status Code: 500

 ** InvalidCustomerIdentifierException **
You have metered usage for a `CustomerIdentifier` that does not exist.
HTTP Status Code: 400

 ** InvalidLicenseException **
Ensure the `LicenseArn` is valid, matches the customer, and usage is within the license activation period.
HTTP Status Code: 400

 ** InvalidProductCodeException **
The product code passed does not match the product code used for publishing the product.
HTTP Status Code: 400

 ** InvalidTagException **
The tag is invalid, or the number of tags is greater than 5.
HTTP Status Code: 400

 ** InvalidUsageAllocationsException **
Sum of allocated usage quantities is not equal to the usage quantity.
HTTP Status Code: 400

 ** InvalidUsageDimensionException **
The usage dimension does not match one of the `UsageDimensions` associated with products.
HTTP Status Code: 400

 ** ThrottlingException **
The calls to the API are throttled.
HTTP Status Code: 400

 ** TimestampOutOfBoundsException **
The `timestamp` value passed in the `UsageRecord` is out of allowed range.
For `BatchMeterUsage`, if any of the records are outside of the allowed range, the entire batch is not processed. You must remove invalid records and try again.
HTTP Status Code: 400

## See Also
<a name="API_marketplace-metering_BatchMeterUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/meteringmarketplace-2016-01-14/BatchMeterUsage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/meteringmarketplace-2016-01-14/BatchMeterUsage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/meteringmarketplace-2016-01-14/BatchMeterUsage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/meteringmarketplace-2016-01-14/BatchMeterUsage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/meteringmarketplace-2016-01-14/BatchMeterUsage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/meteringmarketplace-2016-01-14/BatchMeterUsage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/meteringmarketplace-2016-01-14/BatchMeterUsage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/meteringmarketplace-2016-01-14/BatchMeterUsage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/meteringmarketplace-2016-01-14/BatchMeterUsage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/meteringmarketplace-2016-01-14/BatchMeterUsage)
