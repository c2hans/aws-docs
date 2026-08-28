---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListSites.html
---

# ListSites
<a name="API_ListSites"></a>

Lists the Outpost sites for your AWS account. Use filters to return specific results.

Use filters to return specific results. If you specify multiple filters, the results include only the resources that match all of the specified filters. For a filter where you can specify multiple values, the results include items that match any of the values that you specify for the filter.

## Request Syntax
<a name="API_ListSites_RequestSyntax"></a>

```
GET /sites?MaxResults={{MaxResults}}&NextToken={{NextToken}}&OperatingAddressCityFilter={{OperatingAddressCityFilter}}&OperatingAddressCountryCodeFilter={{OperatingAddressCountryCodeFilter}}&OperatingAddressStateOrRegionFilter={{OperatingAddressStateOrRegionFilter}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSites_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListSites_RequestSyntax) **   <a name="outposts-ListSites-request-uri-MaxResults"></a>
The maximum page size.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListSites_RequestSyntax) **   <a name="outposts-ListSites-request-uri-NextToken"></a>
The pagination token.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(\d+)##(\S+)$`

 ** [OperatingAddressCityFilter](#API_ListSites_RequestSyntax) **   <a name="outposts-ListSites-request-uri-OperatingAddressCityFilter"></a>
Filters the results by city.
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^\S[\S ]*$`

 ** [OperatingAddressCountryCodeFilter](#API_ListSites_RequestSyntax) **   <a name="outposts-ListSites-request-uri-OperatingAddressCountryCodeFilter"></a>
Filters the results by country code.
Length Constraints: Fixed length of 2.
Pattern: `^[A-Z]{2}$`

 ** [OperatingAddressStateOrRegionFilter](#API_ListSites_RequestSyntax) **   <a name="outposts-ListSites-request-uri-OperatingAddressStateOrRegionFilter"></a>
Filters the results by state or region.
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^\S[\S ]*$`

## Request Body
<a name="API_ListSites_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListSites_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Sites": [
      {
         "AccountId": "string",
         "Description": "string",
         "Name": "string",
         "Notes": "string",
         "OperatingAddressCity": "string",
         "OperatingAddressCountryCode": "string",
         "OperatingAddressStateOrRegion": "string",
         "RackPhysicalProperties": {
            "FiberOpticCableType": "string",
            "MaximumSupportedWeightLbs": "string",
            "OpticalStandard": "string",
            "PowerConnector": "string",
            "PowerDrawKva": "string",
            "PowerFeedDrop": "string",
            "PowerPhase": "string",
            "UplinkCount": "string",
            "UplinkGbps": "string"
         },
         "SiteArn": "string",
         "SiteId": "string",
         "Tags": {
            "string" : "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListSites_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListSites_ResponseSyntax) **   <a name="outposts-ListSites-response-NextToken"></a>
The pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(\d+)##(\S+)$`

 ** [Sites](#API_ListSites_ResponseSyntax) **   <a name="outposts-ListSites-response-Sites"></a>
Information about the sites.
Type: Array of [Site](API_Site.md) objects

## Errors
<a name="API_ListSites_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have permission to perform this operation.
HTTP Status Code: 403

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** ValidationException **
A parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListSites_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/ListSites)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/ListSites)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/ListSites)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/ListSites)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/ListSites)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/ListSites)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/ListSites)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/ListSites)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/ListSites)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/ListSites)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
