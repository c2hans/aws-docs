---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListOutposts.html
---

# ListOutposts
<a name="API_ListOutposts"></a>

Lists the Outposts for your AWS account.

Use filters to return specific results. If you specify multiple filters, the results include only the resources that match all of the specified filters. For a filter where you can specify multiple values, the results include items that match any of the values that you specify for the filter.

## Request Syntax
<a name="API_ListOutposts_RequestSyntax"></a>

```
GET /outposts?AvailabilityZoneFilter={{AvailabilityZoneFilter}}&AvailabilityZoneIdFilter={{AvailabilityZoneIdFilter}}&LifeCycleStatusFilter={{LifeCycleStatusFilter}}&MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListOutposts_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AvailabilityZoneFilter](#API_ListOutposts_RequestSyntax) **   <a name="outposts-ListOutposts-request-uri-AvailabilityZoneFilter"></a>
Filters the results by Availability Zone (for example, `us-east-1a`).
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^([a-zA-Z]+-){1,3}([a-zA-Z]+)?(\d+[a-zA-Z]?)?$`

 ** [AvailabilityZoneIdFilter](#API_ListOutposts_RequestSyntax) **   <a name="outposts-ListOutposts-request-uri-AvailabilityZoneIdFilter"></a>
Filters the results by AZ ID (for example, `use1-az1`).
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z]+\d-[a-zA-Z]+\d$`

 ** [LifeCycleStatusFilter](#API_ListOutposts_RequestSyntax) **   <a name="outposts-ListOutposts-request-uri-LifeCycleStatusFilter"></a>
Filters the results by the lifecycle status.
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `^[ A-Za-z]+$`

 ** [MaxResults](#API_ListOutposts_RequestSyntax) **   <a name="outposts-ListOutposts-request-uri-MaxResults"></a>
The maximum page size.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListOutposts_RequestSyntax) **   <a name="outposts-ListOutposts-request-uri-NextToken"></a>
The pagination token.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(\d+)##(\S+)$`

## Request Body
<a name="API_ListOutposts_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListOutposts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Outposts": [
      {
         "AvailabilityZone": "string",
         "AvailabilityZoneId": "string",
         "Description": "string",
         "LifeCycleStatus": "string",
         "Name": "string",
         "OutpostArn": "string",
         "OutpostId": "string",
         "OwnerId": "string",
         "SiteArn": "string",
         "SiteId": "string",
         "SupportedHardwareType": "string",
         "Tags": {
            "string" : "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListOutposts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListOutposts_ResponseSyntax) **   <a name="outposts-ListOutposts-response-NextToken"></a>
The pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(\d+)##(\S+)$`

 ** [Outposts](#API_ListOutposts_ResponseSyntax) **   <a name="outposts-ListOutposts-response-Outposts"></a>
Information about the Outposts.
Type: Array of [Outpost](API_Outpost.md) objects

## Errors
<a name="API_ListOutposts_Errors"></a>

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
<a name="API_ListOutposts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/ListOutposts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/ListOutposts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/ListOutposts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/ListOutposts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/ListOutposts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/ListOutposts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/ListOutposts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/ListOutposts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/ListOutposts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/ListOutposts)
