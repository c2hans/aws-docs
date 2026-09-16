---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ListProvisionedProductPlans.html
---

# ListProvisionedProductPlans
<a name="API_ListProvisionedProductPlans"></a>

Lists the plans for the specified provisioned product or all plans to which the user has access.

## Request Syntax
<a name="API_ListProvisionedProductPlans_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "AccessLevelFilter": {
      "Key": "{{string}}",
      "Value": "{{string}}"
   },
   "PageSize": {{number}},
   "PageToken": "{{string}}",
   "ProvisionProductId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListProvisionedProductPlans_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_ListProvisionedProductPlans_RequestSyntax) **   <a name="servicecatalog-ListProvisionedProductPlans-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [AccessLevelFilter](#API_ListProvisionedProductPlans_RequestSyntax) **   <a name="servicecatalog-ListProvisionedProductPlans-request-AccessLevelFilter"></a>
The access level to use to obtain results. The default is `User`.
Type: [AccessLevelFilter](API_AccessLevelFilter.md) object
Required: No

 ** [PageSize](#API_ListProvisionedProductPlans_RequestSyntax) **   <a name="servicecatalog-ListProvisionedProductPlans-request-PageSize"></a>
The maximum number of items to return with this call.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 20.
Required: No

 ** [PageToken](#API_ListProvisionedProductPlans_RequestSyntax) **   <a name="servicecatalog-ListProvisionedProductPlans-request-PageToken"></a>
The page token for the next set of results. To retrieve the first set of results, use null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`
Required: No

 ** [ProvisionProductId](#API_ListProvisionedProductPlans_RequestSyntax) **   <a name="servicecatalog-ListProvisionedProductPlans-request-ProvisionProductId"></a>
The product identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

## Response Syntax
<a name="API_ListProvisionedProductPlans_ResponseSyntax"></a>

```
{
   "NextPageToken": "string",
   "ProvisionedProductPlans": [
      {
         "PlanId": "string",
         "PlanName": "string",
         "PlanType": "string",
         "ProvisioningArtifactId": "string",
         "ProvisionProductId": "string",
         "ProvisionProductName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListProvisionedProductPlans_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextPageToken](#API_ListProvisionedProductPlans_ResponseSyntax) **   <a name="servicecatalog-ListProvisionedProductPlans-response-NextPageToken"></a>
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

 ** [ProvisionedProductPlans](#API_ListProvisionedProductPlans_ResponseSyntax) **   <a name="servicecatalog-ListProvisionedProductPlans-response-ProvisionedProductPlans"></a>
Information about the plans.
Type: Array of [ProvisionedProductPlanSummary](API_ProvisionedProductPlanSummary.md) objects

## Errors
<a name="API_ListProvisionedProductPlans_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_ListProvisionedProductPlans_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/ListProvisionedProductPlans)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/ListProvisionedProductPlans)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ListProvisionedProductPlans)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/ListProvisionedProductPlans)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ListProvisionedProductPlans)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListProvisionedProductPlans)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/ListProvisionedProductPlans)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/ListProvisionedProductPlans)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/ListProvisionedProductPlans)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ListProvisionedProductPlans)
