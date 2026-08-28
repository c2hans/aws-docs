---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-entitlements_GetEntitlements.html
---

# GetEntitlements
<a name="API_marketplace-entitlements_GetEntitlements"></a>

GetEntitlements retrieves entitlement values for a given product. The results can be filtered based on customer identifier, AWS account ID, license ARN, or product dimensions.

## Request Syntax
<a name="API_marketplace-entitlements_GetEntitlements_RequestSyntax"></a>

```
{
   "Filter": {
      "{{string}}" : [ "{{string}}" ]
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ProductCode": "{{string}}"
}
```

## Request Parameters
<a name="API_marketplace-entitlements_GetEntitlements_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ProductCode](#API_marketplace-entitlements_GetEntitlements_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-entitlements_GetEntitlements-request-ProductCode"></a>
Product code is used to uniquely identify a product in AWS Marketplace. The product code will be provided by AWS Marketplace when the product listing is created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [Filter](#API_marketplace-entitlements_GetEntitlements_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-entitlements_GetEntitlements-request-Filter"></a>
Filter is used to return entitlements for a specific customer or for a specific dimension. Filters are described as keys mapped to a lists of values. Filtered requests are *unioned* for each value in the value list, and then *intersected* for each filter key.
 `CustomerIdentifier` and `CustomerAWSAccountId` are mutually exclusive parameters. You must use one or the other, but not both in the same request.
If you're migrating an existing integration, use [Account Feeds](https://docs.aws.amazon.com/marketplace/latest/userguide/data-feed-account.html) to map `CustomerIdentifier` to `CustomerAWSAccountId`, and [Agreements Feeds](https://docs.aws.amazon.com/marketplace/latest/userguide/data-feed-agreements.html) to map `CustomerAWSAccountId` and `LicenseArn`.
Type: String to array of strings map
Valid Keys: `CUSTOMER_IDENTIFIER | DIMENSION | CUSTOMER_AWS_ACCOUNT_ID | LICENSE_ARN`
Array Members: Minimum number of 1 item.
Required: No

 ** [MaxResults](#API_marketplace-entitlements_GetEntitlements_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-entitlements_GetEntitlements-request-MaxResults"></a>
The maximum number of items to retrieve from the GetEntitlements operation. For pagination, use the NextToken field in subsequent calls to GetEntitlements.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [NextToken](#API_marketplace-entitlements_GetEntitlements_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-entitlements_GetEntitlements-request-NextToken"></a>
For paginated calls to GetEntitlements, pass the NextToken from the previous GetEntitlementsResult.
Type: String
Pattern: `\S+`
Required: No

## Response Syntax
<a name="API_marketplace-entitlements_GetEntitlements_ResponseSyntax"></a>

```
{
   "Entitlements": [
      {
         "CustomerAWSAccountId": "string",
         "CustomerIdentifier": "string",
         "Dimension": "string",
         "ExpirationDate": number,
         "LicenseArn": "string",
         "ProductCode": "string",
         "Value": {
            "BooleanValue": boolean,
            "DoubleValue": number,
            "IntegerValue": number,
            "StringValue": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_marketplace-entitlements_GetEntitlements_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Entitlements](#API_marketplace-entitlements_GetEntitlements_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-entitlements_GetEntitlements-response-Entitlements"></a>
The set of entitlements found through the GetEntitlements operation. If the result contains an empty set of entitlements, NextToken might still be present and should be used.
Type: Array of [Entitlement](API_marketplace-entitlements_Entitlement.md) objects
Array Members: Minimum number of 0 items.

 ** [NextToken](#API_marketplace-entitlements_GetEntitlements_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-entitlements_GetEntitlements-response-NextToken"></a>
For paginated results, use NextToken in subsequent calls to GetEntitlements. If the result contains an empty set of entitlements, NextToken might still be present and should be used.
Type: String
Pattern: `\S+`

## Errors
<a name="API_marketplace-entitlements_GetEntitlements_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceErrorException **
An internal error has occurred. Retry your request. If the problem persists, post a message with details on the AWS forums.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more parameters in your request was invalid.
HTTP Status Code: 400

 ** ThrottlingException **
The calls to the GetEntitlements API are throttled.
HTTP Status Code: 400

## See Also
<a name="API_marketplace-entitlements_GetEntitlements_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/entitlement.marketplace-2017-01-11/GetEntitlements)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/entitlement.marketplace-2017-01-11/GetEntitlements)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entitlement.marketplace-2017-01-11/GetEntitlements)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/entitlement.marketplace-2017-01-11/GetEntitlements)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entitlement.marketplace-2017-01-11/GetEntitlements)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/entitlement.marketplace-2017-01-11/GetEntitlements)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/entitlement.marketplace-2017-01-11/GetEntitlements)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/entitlement.marketplace-2017-01-11/GetEntitlements)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/entitlement.marketplace-2017-01-11/GetEntitlements)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entitlement.marketplace-2017-01-11/GetEntitlements)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
