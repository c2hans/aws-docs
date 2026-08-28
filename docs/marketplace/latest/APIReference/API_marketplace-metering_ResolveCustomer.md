---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-metering_ResolveCustomer.html
---

# ResolveCustomer
<a name="API_marketplace-metering_ResolveCustomer"></a>

 `ResolveCustomer` is called by a SaaS application during the registration process. When a buyer visits your website during the registration process, the buyer submits a registration token through their browser. The registration token is resolved through this API to obtain a `CustomerIdentifier` along with the `CustomerAWSAccountId`, `ProductCode`, and `LicenseArn`.

**Important**
For new SaaS product integrations, the `CustomerIdentifier` field is not populated in the `ResolveCustomer` API response. New integrations must use `CustomerAWSAccountId` and `LicenseArn` to identify customers. Existing integrations continue to work unchanged.

**Note**
To successfully resolve the token, the API must be called from the account that was used to publish the SaaS application. For an example of using `ResolveCustomer`, see [ ResolveCustomer code example](https://docs.aws.amazon.com/marketplace/latest/userguide/saas-code-examples.html#saas-resolvecustomer-example) in the * AWS Marketplace Seller Guide*.

Permission is required for this operation. Your IAM role or user performing this operation requires a policy to allow the `aws-marketplace:ResolveCustomer` action. For more information, see [Actions, resources, and condition keys for AWS Marketplace Metering Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplacemeteringservice.html) in the *Service Authorization Reference*.

For AWS Regions that support `ResolveCustomer`, see [ResolveCustomer Region support](https://docs.aws.amazon.com/marketplace/latest/APIReference/metering-regions.html#resolvecustomer-region-support).

## Request Syntax
<a name="API_marketplace-metering_ResolveCustomer_RequestSyntax"></a>

```
{
   "RegistrationToken": "{{string}}"
}
```

## Request Parameters
<a name="API_marketplace-metering_ResolveCustomer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [RegistrationToken](#API_marketplace-metering_ResolveCustomer_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-metering_ResolveCustomer-request-RegistrationToken"></a>
When a buyer visits your website during the registration process, the buyer submits a registration token through the browser. The registration token is resolved to obtain a `CustomerIdentifier` along with the `CustomerAWSAccountId`, `ProductCode`, and `LicenseArn`.
For new SaaS product integrations, the `CustomerIdentifier` field is not populated. Use `CustomerAWSAccountId` and `LicenseArn` for customer identification.
Type: String
Pattern: `[\s\S]+`
Required: Yes

## Response Syntax
<a name="API_marketplace-metering_ResolveCustomer_ResponseSyntax"></a>

```
{
   "CustomerAWSAccountId": "string",
   "CustomerIdentifier": "string",
   "LicenseArn": "string",
   "ProductCode": "string"
}
```

## Response Elements
<a name="API_marketplace-metering_ResolveCustomer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CustomerAWSAccountId](#API_marketplace-metering_ResolveCustomer_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-metering_ResolveCustomer-response-CustomerAWSAccountId"></a>
The `CustomerAWSAccountId` provides the AWS account ID associated with the `CustomerIdentifier` for the individual customer. Calls to `BatchMeterUsage` require `CustomerAWSAccountId` for each `UsageRecord`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[0-9]+$`

 ** [CustomerIdentifier](#API_marketplace-metering_ResolveCustomer_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-metering_ResolveCustomer-response-CustomerIdentifier"></a>
The `CustomerIdentifier` is used to identify an individual customer in your application.
For new SaaS product integrations, this field is not populated. Use `CustomerAWSAccountId` and `LicenseArn` to identify customers instead.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\s\S]*`

 ** [LicenseArn](#API_marketplace-metering_ResolveCustomer_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-metering_ResolveCustomer-response-LicenseArn"></a>
The `LicenseArn` is a unique identifier for a specific granted license. These are typically used for software purchased through AWS Marketplace. Calls to `BatchMeterUsage` require `LicenseArn` for each `UsageRecord`.
Once you receive the `CustomerAWSAccountId` and `LicenseArn` in the response, store that for future purposes/API calls/integrations.
Type: String
Pattern: `^arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`

 ** [ProductCode](#API_marketplace-metering_ResolveCustomer_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-metering_ResolveCustomer-response-ProductCode"></a>
The product code is returned to confirm that the buyer is registering for your product. Subsequent `BatchMeterUsage` calls should be made using this product code.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `^[-a-zA-Z0-9/=:_.@]*$`

## Errors
<a name="API_marketplace-metering_ResolveCustomer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DisabledApiException **
The API is disabled in the Region.
HTTP Status Code: 400

 ** ExpiredTokenException **
The submitted registration token has expired. This can happen if the buyer's browser takes too long to redirect to your page, the buyer has resubmitted the registration token, or your application has held on to the registration token for too long. Your SaaS registration website should redeem this token as soon as it is submitted by the buyer's browser.
HTTP Status Code: 400

 ** InternalServiceErrorException **
An internal error has occurred. Retry your request. If the problem persists, post a message with details on the AWS forums.
HTTP Status Code: 500

 ** InvalidTokenException **
Registration token is invalid.
HTTP Status Code: 400

 ** ThrottlingException **
The calls to the API are throttled.
HTTP Status Code: 400

## See Also
<a name="API_marketplace-metering_ResolveCustomer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/meteringmarketplace-2016-01-14/ResolveCustomer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/meteringmarketplace-2016-01-14/ResolveCustomer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/meteringmarketplace-2016-01-14/ResolveCustomer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/meteringmarketplace-2016-01-14/ResolveCustomer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/meteringmarketplace-2016-01-14/ResolveCustomer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/meteringmarketplace-2016-01-14/ResolveCustomer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/meteringmarketplace-2016-01-14/ResolveCustomer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/meteringmarketplace-2016-01-14/ResolveCustomer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/meteringmarketplace-2016-01-14/ResolveCustomer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/meteringmarketplace-2016-01-14/ResolveCustomer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
