---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ListLaunchPaths.html
---

# ListLaunchPaths
<a name="API_ListLaunchPaths"></a>

 Lists the paths to the specified product. A path describes how the user gets access to a specified product and is necessary when provisioning a product. A path also determines the constraints that are put on a product. A path is dependent on a specific product, porfolio, and principal.

**Note**
 When provisioning a product that's been added to a portfolio, you must grant your user, group, or role access to the portfolio. For more information, see [Granting users access](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_portfolios_users.html) in the *Service Catalog User Guide*.

## Request Syntax
<a name="API_ListLaunchPaths_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "PageSize": {{number}},
   "PageToken": "{{string}}",
   "ProductId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListLaunchPaths_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_ListLaunchPaths_RequestSyntax) **   <a name="servicecatalog-ListLaunchPaths-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [PageSize](#API_ListLaunchPaths_RequestSyntax) **   <a name="servicecatalog-ListLaunchPaths-request-PageSize"></a>
The maximum number of items to return with this call.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 20.
Required: No

 ** [PageToken](#API_ListLaunchPaths_RequestSyntax) **   <a name="servicecatalog-ListLaunchPaths-request-PageToken"></a>
The page token for the next set of results. To retrieve the first set of results, use null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`
Required: No

 ** [ProductId](#API_ListLaunchPaths_RequestSyntax) **   <a name="servicecatalog-ListLaunchPaths-request-ProductId"></a>
The product identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

## Response Syntax
<a name="API_ListLaunchPaths_ResponseSyntax"></a>

```
{
   "LaunchPathSummaries": [
      {
         "ConstraintSummaries": [
            {
               "Description": "string",
               "Type": "string"
            }
         ],
         "Id": "string",
         "Name": "string",
         "Tags": [
            {
               "Key": "string",
               "Value": "string"
            }
         ]
      }
   ],
   "NextPageToken": "string"
}
```

## Response Elements
<a name="API_ListLaunchPaths_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LaunchPathSummaries](#API_ListLaunchPaths_ResponseSyntax) **   <a name="servicecatalog-ListLaunchPaths-response-LaunchPathSummaries"></a>
Information about the launch path.
Type: Array of [LaunchPathSummary](API_LaunchPathSummary.md) objects

 ** [NextPageToken](#API_ListLaunchPaths_ResponseSyntax) **   <a name="servicecatalog-ListLaunchPaths-response-NextPageToken"></a>
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

## Errors
<a name="API_ListLaunchPaths_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_ListLaunchPaths_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/ListLaunchPaths)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/ListLaunchPaths)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ListLaunchPaths)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/ListLaunchPaths)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ListLaunchPaths)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListLaunchPaths)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/ListLaunchPaths)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/ListLaunchPaths)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/ListLaunchPaths)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ListLaunchPaths)
