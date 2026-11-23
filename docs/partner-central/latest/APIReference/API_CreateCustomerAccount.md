---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_CreateCustomerAccount.html
---

# CreateCustomerAccount

Use `CreateCustomerAccount` to map a customer account from your records to an AWS customer. Provide details about the customer, such as the company name and website. AWS then matches the account to a customer and adds enrichment information about it.

Matching runs asynchronously. The response returns the new customer account with a status of `PENDING`. Use `GetCustomerAccount` to check the result and read the enrichment information.

## Request Syntax
<a name="API_CreateCustomerAccount_RequestSyntax"></a>

```
{
   "Account": {
      "Address": {
         "City": "{{string}}",
         "CountryCode": "{{string}}",
         "PostalCode": "{{string}}",
         "StateOrRegion": "{{string}}",
         "StreetAddress": "{{string}}"
      },
      "CompanyName": "{{string}}",
      "Domain": "{{string}}",
      "Duns": "{{string}}",
      "Industry": "{{string}}",
      "OtherIndustry": "{{string}}",
      "ParentCompanyName": "{{string}}",
      "WebsiteUrl": "{{string}}"
   },
   "Catalog": "{{string}}",
   "ClientToken": "{{string}}",
   "PartnerAccountIdentifier": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateCustomerAccount_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Account](#API_CreateCustomerAccount_RequestSyntax) **   <a name="AWSPartnerCentral-CreateCustomerAccount-request-Account"></a>
Specifies the details of the customer, such as the company name, website, and address. AWS uses these details to match the account to a customer.
Type: [CustomerAccountData](API_CustomerAccountData.md) object
Required: Yes

 ** [Catalog](#API_CreateCustomerAccount_RequestSyntax) **   <a name="AWSPartnerCentral-CreateCustomerAccount-request-Catalog"></a>
Specifies the catalog for the request. Valid values:
+  `AWS`: Production.
+  `Sandbox`: Testing environments.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [ClientToken](#API_CreateCustomerAccount_RequestSyntax) **   <a name="AWSPartnerCentral-CreateCustomerAccount-request-ClientToken"></a>
Specifies a unique, case-sensitive identifier that you provide to make the request idempotent. If you retry a request with the same token, the operation returns the result of the original request instead of creating another customer account.
Type: String
Pattern: `.{1,255}`
Required: No

 ** [PartnerAccountIdentifier](#API_CreateCustomerAccount_RequestSyntax) **   <a name="AWSPartnerCentral-CreateCustomerAccount-request-PartnerAccountIdentifier"></a>
Specifies your own identifier for the customer account, such as the account ID in your CRM system. Use it to correlate the customer account with your records.
Type: String
Pattern: `(?s).{0,64}`
Required: No

 ** [Tags](#API_CreateCustomerAccount_RequestSyntax) **   <a name="AWSPartnerCentral-CreateCustomerAccount-request-Tags"></a>
Specifies the tags to add to the customer account. Each tag is a key-value pair.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateCustomerAccount_ResponseSyntax"></a>

```
{
   "Arn": "string",
   "Catalog": "string",
   "CreatedDate": "string",
   "Id": "string",
   "PartnerAccountIdentifier": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_CreateCustomerAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateCustomerAccount_ResponseSyntax) **   <a name="AWSPartnerCentral-CreateCustomerAccount-response-Arn"></a>
The Amazon Resource Name (ARN) of the customer account.
Type: String
Pattern: `arn:[a-z\-]*:partnercentral:[a-z0-9\-]*:[0-9]{12}:catalog/[a-zA-Z]+/customer-account/cust-acc-[0-9a-z]{13}`

 ** [Catalog](#API_CreateCustomerAccount_ResponseSyntax) **   <a name="AWSPartnerCentral-CreateCustomerAccount-response-Catalog"></a>
The catalog that the customer account belongs to.
Type: String
Pattern: `[a-zA-Z]+`

 ** [CreatedDate](#API_CreateCustomerAccount_ResponseSyntax) **   <a name="AWSPartnerCentral-CreateCustomerAccount-response-CreatedDate"></a>
The date and time when the customer account was created.
Type: Timestamp

 ** [Id](#API_CreateCustomerAccount_ResponseSyntax) **   <a name="AWSPartnerCentral-CreateCustomerAccount-response-Id"></a>
The unique identifier of the customer account.
Type: String
Pattern: `cust-acc-[0-9a-z]{13}`

 ** [Status](#API_CreateCustomerAccount_ResponseSyntax) **   <a name="AWSPartnerCentral-CreateCustomerAccount-response-Status"></a>
The enrichment status of the new customer account. A new account starts as `PENDING`.
Type: String
Valid Values: `PENDING | ENRICHED | NO_MATCH_FOUND | ACTION_REQUIRED`

 ** [PartnerAccountIdentifier](#API_CreateCustomerAccount_ResponseSyntax) **   <a name="AWSPartnerCentral-CreateCustomerAccount-response-PartnerAccountIdentifier"></a>
Your own identifier for the customer account, if you provided one.
Type: String
Pattern: `(?s).{0,64}`

## Errors
<a name="API_CreateCustomerAccount_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
This error occurs when you don't have permission to perform the requested action.
You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.
 ** Message **
A message that describes why access was denied.
 ** Reason **
The reason why access was denied for the requested operation.
HTTP Status Code: 400

 ** ConflictException **
This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.
Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.
 ** Message **
A message that describes the conflict.
HTTP Status Code: 400

 ** InternalServerException **
This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.
Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.
 ** Message **
A message that describes the internal error.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
This error occurs when the request would cause a service quota to be exceeded. Service quotas represent the maximum allowed use of a specific resource, and this error indicates that the request would surpass that limit.
Suggested action: Review the [Quotas](https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html) for the resource, and either reduce usage or request a quota increase.
 ** Message **
A message that describes which quota the request exceeded.
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
<a name="API_CreateCustomerAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/CreateCustomerAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/CreateCustomerAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/CreateCustomerAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/CreateCustomerAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/CreateCustomerAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/CreateCustomerAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/CreateCustomerAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/CreateCustomerAccount)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/CreateCustomerAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/CreateCustomerAccount)
