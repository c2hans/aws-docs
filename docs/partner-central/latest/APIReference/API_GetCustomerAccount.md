---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_GetCustomerAccount.html
---

# GetCustomerAccount

Use `GetCustomerAccount` to retrieve the details of a customer account, including the customer information that you provided, the enrichment status, and the enrichment information that AWS provides when the status is `ENRICHED`.

## Request Syntax
<a name="API_GetCustomerAccount_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "Identifier": "{{string}}"
}
```

## Request Parameters
<a name="API_GetCustomerAccount_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_GetCustomerAccount_RequestSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccount-request-Catalog"></a>
Specifies the catalog for the request. Valid values:
+  `AWS`: Production.
+  `Sandbox`: Testing environments.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [Identifier](#API_GetCustomerAccount_RequestSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccount-request-Identifier"></a>
Specifies the ARN or the identifier of the customer account.
Type: String
Pattern: `(arn:.*|cust-acc-[0-9a-z]{13})`
Required: Yes

## Response Syntax
<a name="API_GetCustomerAccount_ResponseSyntax"></a>

```
{
   "Account": {
      "Address": {
         "City": "string",
         "CountryCode": "string",
         "PostalCode": "string",
         "StateOrRegion": "string",
         "StreetAddress": "string"
      },
      "CompanyName": "string",
      "Domain": "string",
      "Duns": "string",
      "Industry": "string",
      "OtherIndustry": "string",
      "ParentCompanyName": "string",
      "WebsiteUrl": "string"
   },
   "Arn": "string",
   "AwsEnrichment": {
      "Customer": {
         "AccountName": "string",
         "CompanySize": "string",
         "Country": "string",
         "CustomerAccountPlanningQualification": "string",
         "EligiblePrograms": [ "string" ],
         "Geo": "string",
         "Industry": "string",
         "Region": "string",
         "Sector": "string",
         "Segment": "string",
         "SubIndustry": "string",
         "SubRegion": "string"
      },
      "Insights": {
         "MarketplaceEngagementScore": "string",
         "SolutionCategory": "string",
         "SolutionScore": "string",
         "SolutionSubCategory": "string"
      }
   },
   "Catalog": "string",
   "CreatedDate": "string",
   "EnrichmentStatus": "string",
   "ExistingCustomerAccountArn": "string",
   "Id": "string",
   "Issues": [
      {
         "Code": "string",
         "Message": "string",
         "Severity": "string"
      }
   ],
   "LastModifiedDate": "string",
   "Message": "string",
   "PartnerAccountIdentifier": "string",
   "ReasonCode": "string",
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetCustomerAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Account](#API_GetCustomerAccount_ResponseSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccount-response-Account"></a>
The details of the customer that you provided.
Type: [CustomerAccountData](API_CustomerAccountData.md) object

 ** [Arn](#API_GetCustomerAccount_ResponseSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccount-response-Arn"></a>
The Amazon Resource Name (ARN) of the customer account.
Type: String
Pattern: `arn:[a-z\-]*:partnercentral:[a-z0-9\-]*:[0-9]{12}:catalog/[a-zA-Z]+/customer-account/cust-acc-[0-9a-z]{13}`

 ** [Catalog](#API_GetCustomerAccount_ResponseSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccount-response-Catalog"></a>
The catalog that the customer account belongs to.
Type: String
Pattern: `[a-zA-Z]+`

 ** [CreatedDate](#API_GetCustomerAccount_ResponseSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccount-response-CreatedDate"></a>
The date and time when the customer account was created.
Type: Timestamp

 ** [EnrichmentStatus](#API_GetCustomerAccount_ResponseSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccount-response-EnrichmentStatus"></a>
The enrichment status of the customer account.
Type: String
Valid Values: `PENDING | ENRICHED | NO_MATCH_FOUND | ACTION_REQUIRED`

 ** [Id](#API_GetCustomerAccount_ResponseSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccount-response-Id"></a>
The unique identifier of the customer account.
Type: String
Pattern: `cust-acc-[0-9a-z]{13}`

 ** [LastModifiedDate](#API_GetCustomerAccount_ResponseSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccount-response-LastModifiedDate"></a>
The date and time when the customer account was last modified.
Type: Timestamp

 ** [AwsEnrichment](#API_GetCustomerAccount_ResponseSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccount-response-AwsEnrichment"></a>
Enrichment information that AWS provides about the customer. Present only when `EnrichmentStatus` is `ENRICHED`.
Type: [AwsEnrichment](API_AwsEnrichment.md) object

 ** [ExistingCustomerAccountArn](#API_GetCustomerAccount_ResponseSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccount-response-ExistingCustomerAccountArn"></a>
The ARN of the customer account that already maps this customer. Present only when `ReasonCode` is `DUPLICATE_CUSTOMER_MATCH`.
Type: String
Pattern: `arn:[a-z\-]*:partnercentral:[a-z0-9\-]*:[0-9]{12}:catalog/[a-zA-Z]+/customer-account/cust-acc-[0-9a-z]{13}`

 ** [Issues](#API_GetCustomerAccount_ResponseSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccount-response-Issues"></a>
The issues found with the customer account. Present only when there is at least one issue.
Type: Array of [Issue](API_Issue.md) objects

 ** [Message](#API_GetCustomerAccount_ResponseSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccount-response-Message"></a>
A description of the problem and the steps that you can take to resolve it.
Type: String

 ** [PartnerAccountIdentifier](#API_GetCustomerAccount_ResponseSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccount-response-PartnerAccountIdentifier"></a>
Your own identifier for the customer account, if you provided one.
Type: String
Pattern: `(?s).{0,64}`

 ** [ReasonCode](#API_GetCustomerAccount_ResponseSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccount-response-ReasonCode"></a>
The reason that the customer account needs your action. Present only when `EnrichmentStatus` is `ACTION_REQUIRED`.
Type: String
Valid Values: `DUPLICATE_CUSTOMER_MATCH | PROCESSING_ERROR`

 ** [Tags](#API_GetCustomerAccount_ResponseSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccount-response-Tags"></a>
The tags on the customer account. This member is absent if the tags can't be retrieved, which is different from an account that has no tags.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.

## Errors
<a name="API_GetCustomerAccount_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
This error occurs when you don't have permission to perform the requested action.
You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.
 ** Message **
A message that describes why access was denied.
 ** Reason **
The reason why access was denied for the requested operation.
HTTP Status Code: 400

 ** InternalServerException **
This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.
Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.
 ** Message **
A message that describes the internal error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.
Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.
 ** Message **
A message that describes which resource the service couldn't find.
HTTP Status Code: 400

 ** ThrottlingException **
This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.
This error occurs when there are too many requests sent. Review the provided [Quotas](https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html) and retry after the provided delay.
 ** Message **
A message that describes why the service throttled the request.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by the service or business validation rules.
Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.
 ** ErrorList **
A list of issues that were discovered in the submitted request or the resource state.
 ** Message **
A message that describes the validation error.
 ** Reason **
The primary reason for this validation exception to occur.
+  *REQUEST\_VALIDATION\_FAILED:* The request format is not valid.

  Fix: Verify your request payload includes all required fields, uses correct data types and string formats.
+  *BUSINESS\_VALIDATION\_FAILED:* The requested change doesn't pass the business validation rules.

  Fix: Check that your change aligns with the business rules defined by AWS Partner Central.
HTTP Status Code: 400

## See Also
<a name="API_GetCustomerAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/GetCustomerAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/GetCustomerAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/GetCustomerAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/GetCustomerAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/GetCustomerAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/GetCustomerAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/GetCustomerAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/GetCustomerAccount)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/GetCustomerAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/GetCustomerAccount)
