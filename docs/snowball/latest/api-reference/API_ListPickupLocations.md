---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_ListPickupLocations.html
---

# ListPickupLocations
<a name="API_ListPickupLocations"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

A list of locations from which the customer can choose to pickup a device.

## Request Syntax
<a name="API_ListPickupLocations_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListPickupLocations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListPickupLocations_RequestSyntax) **   <a name="Snowball-ListPickupLocations-request-MaxResults"></a>
The maximum number of locations to list per page.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListPickupLocations_RequestSyntax) **   <a name="Snowball-ListPickupLocations-request-NextToken"></a>
HTTP requests are stateless. To identify what object comes "next" in the list of `ListPickupLocationsRequest` objects, you have the option of specifying `NextToken` as the starting point for your returned list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_ListPickupLocations_ResponseSyntax"></a>

```
{
   "Addresses": [
      {
         "AddressId": "string",
         "City": "string",
         "Company": "string",
         "Country": "string",
         "IsRestricted": boolean,
         "Landmark": "string",
         "Name": "string",
         "PhoneNumber": "string",
         "PostalCode": "string",
         "PrefectureOrDistrict": "string",
         "StateOrProvince": "string",
         "Street1": "string",
         "Street2": "string",
         "Street3": "string",
         "Type": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListPickupLocations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Addresses](#API_ListPickupLocations_ResponseSyntax) **   <a name="Snowball-ListPickupLocations-response-Addresses"></a>
Information about the address of pickup locations.
Type: Array of [Address](API_Address.md) objects

 ** [NextToken](#API_ListPickupLocations_ResponseSyntax) **   <a name="Snowball-ListPickupLocations-response-NextToken"></a>
HTTP requests are stateless. To identify what object comes "next" in the list of `ListPickupLocationsResult` objects, you have the option of specifying `NextToken` as the starting point for your returned list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`

## Errors
<a name="API_ListPickupLocations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidResourceException **
The specified resource can't be found. Check the information you provided in your last request, and try again.
 ** ResourceType **
The provided resource value is invalid.
HTTP Status Code: 400

## Examples
<a name="API_ListPickupLocations_Examples"></a>

### Example
<a name="API_ListPickupLocations_Example_1"></a>

This example illustrates one usage of ListPickupLocations.

```
{
    "id": "to-get-a-list-of-locations-from-which-the-customer-can-choose-to-pickup-a-device-1482542167627",
    "title": "To get a list of locations from which the customer can choose to pickup a device.",
    "description": "Returns a specified number of Address objects. Each Address is a pickup location address for Snowball Edge devices.",
    "input": {},
    "output": {
       "Addresses": [
        {
          "City": "Seattle",
          "Name": "My Name",
          "AddressId": "ADID1234ab12-3eec-4eb3-9be6-9374c10eb51b",
          "Street1": "123 Main Street",
          "Company": "My Company",
          "PhoneNumber": "425-555-5555",
          "Country": "US",
          "PostalCode": "98101",
          "StateOrProvince": "WA"
        }
      ]
    },
    "comments": {}
}
```

## See Also
<a name="API_ListPickupLocations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snowball-2016-06-30/ListPickupLocations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snowball-2016-06-30/ListPickupLocations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/ListPickupLocations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snowball-2016-06-30/ListPickupLocations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/ListPickupLocations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snowball-2016-06-30/ListPickupLocations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snowball-2016-06-30/ListPickupLocations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snowball-2016-06-30/ListPickupLocations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/snowball-2016-06-30/ListPickupLocations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/ListPickupLocations)
