---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ListRecordHistory.html
---

# ListRecordHistory
<a name="API_ListRecordHistory"></a>

Lists the specified requests or all performed requests.

## Request Syntax
<a name="API_ListRecordHistory_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "AccessLevelFilter": {
      "Key": "{{string}}",
      "Value": "{{string}}"
   },
   "PageSize": {{number}},
   "PageToken": "{{string}}",
   "SearchFilter": {
      "Key": "{{string}}",
      "Value": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_ListRecordHistory_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_ListRecordHistory_RequestSyntax) **   <a name="servicecatalog-ListRecordHistory-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [AccessLevelFilter](#API_ListRecordHistory_RequestSyntax) **   <a name="servicecatalog-ListRecordHistory-request-AccessLevelFilter"></a>
The access level to use to obtain results. The default is `User`.
Type: [AccessLevelFilter](API_AccessLevelFilter.md) object
Required: No

 ** [PageSize](#API_ListRecordHistory_RequestSyntax) **   <a name="servicecatalog-ListRecordHistory-request-PageSize"></a>
The maximum number of items to return with this call.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 20.
Required: No

 ** [PageToken](#API_ListRecordHistory_RequestSyntax) **   <a name="servicecatalog-ListRecordHistory-request-PageToken"></a>
The page token for the next set of results. To retrieve the first set of results, use null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`
Required: No

 ** [SearchFilter](#API_ListRecordHistory_RequestSyntax) **   <a name="servicecatalog-ListRecordHistory-request-SearchFilter"></a>
The search filter to scope the results.
Type: [ListRecordHistorySearchFilter](API_ListRecordHistorySearchFilter.md) object
Required: No

## Response Syntax
<a name="API_ListRecordHistory_ResponseSyntax"></a>

```
{
   "NextPageToken": "string",
   "RecordDetails": [
      {
         "CreatedTime": number,
         "LaunchRoleArn": "string",
         "PathId": "string",
         "ProductId": "string",
         "ProvisionedProductId": "string",
         "ProvisionedProductName": "string",
         "ProvisionedProductType": "string",
         "ProvisioningArtifactId": "string",
         "RecordErrors": [
            {
               "Code": "string",
               "Description": "string"
            }
         ],
         "RecordId": "string",
         "RecordTags": [
            {
               "Key": "string",
               "Value": "string"
            }
         ],
         "RecordType": "string",
         "Status": "string",
         "UpdatedTime": number
      }
   ]
}
```

## Response Elements
<a name="API_ListRecordHistory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextPageToken](#API_ListRecordHistory_ResponseSyntax) **   <a name="servicecatalog-ListRecordHistory-response-NextPageToken"></a>
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

 ** [RecordDetails](#API_ListRecordHistory_ResponseSyntax) **   <a name="servicecatalog-ListRecordHistory-response-RecordDetails"></a>
The records, in reverse chronological order.
Type: Array of [RecordDetail](API_RecordDetail.md) objects

## Errors
<a name="API_ListRecordHistory_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListRecordHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/ListRecordHistory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/ListRecordHistory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ListRecordHistory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/ListRecordHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ListRecordHistory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListRecordHistory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/ListRecordHistory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/ListRecordHistory)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/ListRecordHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ListRecordHistory)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
