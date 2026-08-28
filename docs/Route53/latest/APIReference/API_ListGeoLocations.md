---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListGeoLocations.html
---

# ListGeoLocations
<a name="API_ListGeoLocations"></a>

Retrieves a list of supported geographic locations.

Countries are listed first, and continents are listed last. If Amazon Route 53 supports subdivisions for a country (for example, states or provinces), the subdivisions for that country are listed in alphabetical order immediately after the corresponding country.

Route 53 does not perform authorization for this API because it retrieves information that is already available to the public.

For a list of supported geolocation codes, see the [GeoLocation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GeoLocation.html) data type.

## Request Syntax
<a name="API_ListGeoLocations_RequestSyntax"></a>

```
GET /2013-04-01/geolocations?maxitems={{MaxItems}}&startcontinentcode={{StartContinentCode}}&startcountrycode={{StartCountryCode}}&startsubdivisioncode={{StartSubdivisionCode}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListGeoLocations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxitems](#API_ListGeoLocations_RequestSyntax) **   <a name="Route53-ListGeoLocations-request-uri-MaxItems"></a>
(Optional) The maximum number of geolocations to be included in the response body for this request. If more than `maxitems` geolocations remain to be listed, then the value of the `IsTruncated` element in the response is `true`.

 ** [startcontinentcode](#API_ListGeoLocations_RequestSyntax) **   <a name="Route53-ListGeoLocations-request-uri-StartContinentCode"></a>
The code for the continent with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Route 53 has already returned a page or more of results, if `IsTruncated` is true, and if `NextContinentCode` from the previous response has a value, enter that value in `startcontinentcode` to return the next page of results.
Include `startcontinentcode` only if you want to list continents. Don't include `startcontinentcode` when you're listing countries or countries with their subdivisions.
Length Constraints: Fixed length of 2.

 ** [startcountrycode](#API_ListGeoLocations_RequestSyntax) **   <a name="Route53-ListGeoLocations-request-uri-StartCountryCode"></a>
The code for the country with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Route 53 has already returned a page or more of results, if `IsTruncated` is `true`, and if `NextCountryCode` from the previous response has a value, enter that value in `startcountrycode` to return the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 2.

 ** [startsubdivisioncode](#API_ListGeoLocations_RequestSyntax) **   <a name="Route53-ListGeoLocations-request-uri-StartSubdivisionCode"></a>
The code for the state of the United States with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Route 53 has already returned a page or more of results, if `IsTruncated` is `true`, and if `NextSubdivisionCode` from the previous response has a value, enter that value in `startsubdivisioncode` to return the next page of results.
To list subdivisions (U.S. states), you must include both `startcountrycode` and `startsubdivisioncode`.
Length Constraints: Minimum length of 1. Maximum length of 3.

## Request Body
<a name="API_ListGeoLocations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListGeoLocations_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListGeoLocationsResponse>
   <GeoLocationDetailsList>
      <GeoLocationDetails>
         <ContinentCode>string</ContinentCode>
         <ContinentName>string</ContinentName>
         <CountryCode>string</CountryCode>
         <CountryName>string</CountryName>
         <SubdivisionCode>string</SubdivisionCode>
         <SubdivisionName>string</SubdivisionName>
      </GeoLocationDetails>
   </GeoLocationDetailsList>
   <IsTruncated>boolean</IsTruncated>
   <MaxItems>string</MaxItems>
   <NextContinentCode>string</NextContinentCode>
   <NextCountryCode>string</NextCountryCode>
   <NextSubdivisionCode>string</NextSubdivisionCode>
</ListGeoLocationsResponse>
```

## Response Elements
<a name="API_ListGeoLocations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListGeoLocationsResponse](#API_ListGeoLocations_ResponseSyntax) **   <a name="Route53-ListGeoLocations-response-ListGeoLocationsResponse"></a>
Root level tag for the ListGeoLocationsResponse parameters.
Required: Yes

 ** [GeoLocationDetailsList](#API_ListGeoLocations_ResponseSyntax) **   <a name="Route53-ListGeoLocations-response-GeoLocationDetailsList"></a>
A complex type that contains one `GeoLocationDetails` element for each location that Amazon Route 53 supports for geolocation.
Type: Array of [GeoLocationDetails](API_GeoLocationDetails.md) objects

 ** [IsTruncated](#API_ListGeoLocations_ResponseSyntax) **   <a name="Route53-ListGeoLocations-response-IsTruncated"></a>
A value that indicates whether more locations remain to be listed after the last location in this response. If so, the value of `IsTruncated` is `true`. To get more values, submit another request and include the values of `NextContinentCode`, `NextCountryCode`, and `NextSubdivisionCode` in the `startcontinentcode`, `startcountrycode`, and `startsubdivisioncode`, as applicable.
Type: Boolean

 ** [MaxItems](#API_ListGeoLocations_ResponseSyntax) **   <a name="Route53-ListGeoLocations-response-MaxItems"></a>
The value that you specified for `MaxItems` in the request.
Type: String

 ** [NextContinentCode](#API_ListGeoLocations_ResponseSyntax) **   <a name="Route53-ListGeoLocations-response-NextContinentCode"></a>
If `IsTruncated` is `true`, you can make a follow-up request to display more locations. Enter the value of `NextContinentCode` in the `startcontinentcode` parameter in another `ListGeoLocations` request.
Type: String
Length Constraints: Fixed length of 2.

 ** [NextCountryCode](#API_ListGeoLocations_ResponseSyntax) **   <a name="Route53-ListGeoLocations-response-NextCountryCode"></a>
If `IsTruncated` is `true`, you can make a follow-up request to display more locations. Enter the value of `NextCountryCode` in the `startcountrycode` parameter in another `ListGeoLocations` request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2.

 ** [NextSubdivisionCode](#API_ListGeoLocations_ResponseSyntax) **   <a name="Route53-ListGeoLocations-response-NextSubdivisionCode"></a>
If `IsTruncated` is `true`, you can make a follow-up request to display more locations. Enter the value of `NextSubdivisionCode` in the `startsubdivisioncode` parameter in another `ListGeoLocations` request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 3.

## Errors
<a name="API_ListGeoLocations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_ListGeoLocations_Examples"></a>

### Example Request
<a name="API_ListGeoLocations_Example_1"></a>

The following request lists locations beginning with the United States state of Oregon.

```
GET /2013-04-01/geolocations?startcountrycode=US&startsubdivisioncode=OR&maxitems=2
```

### Example Response
<a name="API_ListGeoLocations_Example_2"></a>

This example illustrates one usage of ListGeoLocations.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<ListGeoLocationsResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <GeoLocationDetailsList>
      <GeoLocationDetails>
         <CountryCode>US</CountryCode>
         <CountryName>USA</CountryName>
         <SubdivisionCode>OR</SubdivisionCode>
         <SubdivisionName>Oregon</SubdivisionName>
      </GeoLocationDetails>
      <GeoLocationDetails>
         <CountryCode>US</CountryCode>
         <CountryName>USA</CountryName>
         <SubdivisionCode>PA</SubdivisionCode>
         <SubdivisionName>Pennsylvania</SubdivisionName>
      </GeoLocationDetails>
   </GeoLocationDetailsList>
   <IsTruncated>true</IsTruncated>
   <NextCountryCode>US</NextCountryCode>
   <NextSubdivisionCode>RI</NextSubdivisionCode>
   <MaxItems>2</MaxItems>
</ListGeoLocationsResponse>
```

### Example Follow-up Request
<a name="API_ListGeoLocations_Example_3"></a>

This example shows the follow-up request to the previous request. In this request, the value of `NextCountryCode` from the previous response is specified as the value for `startcountrycode`, and `NextSubdivisionCode` is specified as the value for `startsubdivisioncode`.

```
GET /2013-04-01/geolocations?startcountrycode=US&startsubdivisioncode=RI&maxitems=2
```

### Example Follow-up Response
<a name="API_ListGeoLocations_Example_4"></a>

This example illustrates one usage of ListGeoLocations.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<ListGeoLocationsResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <GeoLocationDetailsList>
      <GeoLocationDetails>
         <CountryCode>US</CountryCode>
         <CountryName>USA</CountryName>
         <SubdivisionCode>RI</SubdivisionCode>
         <SubdivisionName>Rhode Island</SubdivisionName>
      </GeoLocationDetails>
      <GeoLocationDetails>
         <CountryCode>US</CountryCode>
         <CountryName>USA</CountryName>
         <SubdivisionCode>SC</SubdivisionCode>
         <SubdivisionName>South Carolina</SubdivisionName>
      </GeoLocationDetails>
   </GeoLocationDetailsList>
   <IsTruncated>true</IsTruncated>
   <NextCountryCode>US</NextCountryCode>
   <NextSubdivisionCode>SD</NextSubdivisionCode>
   <MaxItems>2</MaxItems>
</ListGeoLocationsResponse>
```

## See Also
<a name="API_ListGeoLocations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/ListGeoLocations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/ListGeoLocations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ListGeoLocations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/ListGeoLocations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ListGeoLocations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/ListGeoLocations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/ListGeoLocations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/ListGeoLocations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/ListGeoLocations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ListGeoLocations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
