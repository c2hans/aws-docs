---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_SearchProvisionedProducts.html
---

# SearchProvisionedProducts
<a name="API_SearchProvisionedProducts"></a>

Gets information about the provisioned products that meet the specified criteria.

## Request Syntax
<a name="API_SearchProvisionedProducts_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "AccessLevelFilter": {
      "Key": "{{string}}",
      "Value": "{{string}}"
   },
   "Filters": {
      "{{string}}" : [ "{{string}}" ]
   },
   "PageSize": {{number}},
   "PageToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_SearchProvisionedProducts_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_SearchProvisionedProducts_RequestSyntax) **   <a name="servicecatalog-SearchProvisionedProducts-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [AccessLevelFilter](#API_SearchProvisionedProducts_RequestSyntax) **   <a name="servicecatalog-SearchProvisionedProducts-request-AccessLevelFilter"></a>
The access level to use to obtain results. The default is `Account`.
Type: [AccessLevelFilter](API_AccessLevelFilter.md) object
Required: No

 ** [Filters](#API_SearchProvisionedProducts_RequestSyntax) **   <a name="servicecatalog-SearchProvisionedProducts-request-Filters"></a>
The search filters.
When the key is `SearchQuery`, the searchable fields are `arn`, `createdTime`, `id`, `lastRecordId`, `idempotencyToken`, `name`, `physicalId`, `productId`, `provisioningArtifactId`, `type`, `status`, `tags`, `userArn`, `userArnSession`, `lastProvisioningRecordId`, `lastSuccessfulProvisioningRecordId`, `productName`, and `provisioningArtifactName`.
Example: `"SearchQuery":["status:AVAILABLE"]`
Type: String to array of strings map
Valid Keys: `SearchQuery`
Required: No

 ** [PageSize](#API_SearchProvisionedProducts_RequestSyntax) **   <a name="servicecatalog-SearchProvisionedProducts-request-PageSize"></a>
The maximum number of items to return with this call.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [PageToken](#API_SearchProvisionedProducts_RequestSyntax) **   <a name="servicecatalog-SearchProvisionedProducts-request-PageToken"></a>
The page token for the next set of results. To retrieve the first set of results, use null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`
Required: No

 ** [SortBy](#API_SearchProvisionedProducts_RequestSyntax) **   <a name="servicecatalog-SearchProvisionedProducts-request-SortBy"></a>
The sort field. If no value is specified, the results are not sorted. The valid values are `arn`, `id`, `name`, and `lastRecordId`.
Type: String
Required: No

 ** [SortOrder](#API_SearchProvisionedProducts_RequestSyntax) **   <a name="servicecatalog-SearchProvisionedProducts-request-SortOrder"></a>
The sort order. If no value is specified, the results are not sorted.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

## Response Syntax
<a name="API_SearchProvisionedProducts_ResponseSyntax"></a>

```
{
   "NextPageToken": "string",
   "ProvisionedProducts": [
      {
         "Arn": "string",
         "CreatedTime": number,
         "Id": "string",
         "IdempotencyToken": "string",
         "LastProvisioningRecordId": "string",
         "LastRecordId": "string",
         "LastSuccessfulProvisioningRecordId": "string",
         "LaunchRoleArn": "string",
         "Name": "string",
         "PhysicalId": "string",
         "ProductId": "string",
         "ProductName": "string",
         "ProvisioningArtifactId": "string",
         "ProvisioningArtifactName": "string",
         "Status": "string",
         "StatusMessage": "string",
         "Tags": [
            {
               "Key": "string",
               "Value": "string"
            }
         ],
         "Type": "string",
         "UserArn": "string",
         "UserArnSession": "string"
      }
   ],
   "TotalResultsCount": number
}
```

## Response Elements
<a name="API_SearchProvisionedProducts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextPageToken](#API_SearchProvisionedProducts_ResponseSyntax) **   <a name="servicecatalog-SearchProvisionedProducts-response-NextPageToken"></a>
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

 ** [ProvisionedProducts](#API_SearchProvisionedProducts_ResponseSyntax) **   <a name="servicecatalog-SearchProvisionedProducts-response-ProvisionedProducts"></a>
Information about the provisioned products.
Type: Array of [ProvisionedProductAttribute](API_ProvisionedProductAttribute.md) objects

 ** [TotalResultsCount](#API_SearchProvisionedProducts_ResponseSyntax) **   <a name="servicecatalog-SearchProvisionedProducts-response-TotalResultsCount"></a>
The number of provisioned products found.
Type: Integer

## Errors
<a name="API_SearchProvisionedProducts_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

## See Also
<a name="API_SearchProvisionedProducts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/SearchProvisionedProducts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/SearchProvisionedProducts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/SearchProvisionedProducts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/SearchProvisionedProducts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/SearchProvisionedProducts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/SearchProvisionedProducts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/SearchProvisionedProducts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/SearchProvisionedProducts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/SearchProvisionedProducts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/SearchProvisionedProducts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
