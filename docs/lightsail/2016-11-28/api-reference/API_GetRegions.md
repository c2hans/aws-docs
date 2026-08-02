---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetRegions.html
---

# GetRegions
<a name="API_GetRegions"></a>

Returns a list of all valid regions for Amazon Lightsail. Use the `include availability zones` parameter to also return the Availability Zones in a region.

## Request Syntax
<a name="API_GetRegions_RequestSyntax"></a>

```
{
   "includeAvailabilityZones": {{boolean}},
   "includeRelationalDatabaseAvailabilityZones": {{boolean}}
}
```

## Request Parameters
<a name="API_GetRegions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [includeAvailabilityZones](#API_GetRegions_RequestSyntax) **   <a name="Lightsail-GetRegions-request-includeAvailabilityZones"></a>
A Boolean value indicating whether to also include Availability Zones in your get regions request. Availability Zones are indicated with a letter: `us-east-2a`.
Type: Boolean
Required: No

 ** [includeRelationalDatabaseAvailabilityZones](#API_GetRegions_RequestSyntax) **   <a name="Lightsail-GetRegions-request-includeRelationalDatabaseAvailabilityZones"></a>
A Boolean value indicating whether to also include Availability Zones for databases in your get regions request. Availability Zones are indicated with a letter (`us-east-2a`).
Type: Boolean
Required: No

## Response Syntax
<a name="API_GetRegions_ResponseSyntax"></a>

```
{
   "regions": [
      {
         "availabilityZones": [
            {
               "state": "string",
               "zoneName": "string"
            }
         ],
         "continentCode": "string",
         "description": "string",
         "displayName": "string",
         "name": "string",
         "relationalDatabaseAvailabilityZones": [
            {
               "state": "string",
               "zoneName": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_GetRegions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [regions](#API_GetRegions_ResponseSyntax) **   <a name="Lightsail-GetRegions-response-regions"></a>
An array of key-value pairs containing information about your get regions request.
Type: Array of [Region](API_Region.md) objects

## Errors
<a name="API_GetRegions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
HTTP Status Code: 400

 ** AccountSetupInProgressException **
Lightsail throws this exception when an account is still in the setup in progress state.
HTTP Status Code: 400

 ** InvalidInputException **
Lightsail throws this exception when user input does not conform to the validation rules of an input field.
Domain and distribution APIs are only available in the N. Virginia (`us-east-1`) AWS Region. Please set your AWS Region configuration to `us-east-1` to create, view, or edit these resources.
HTTP Status Code: 400

 ** NotFoundException **
Lightsail throws this exception when it cannot find a resource.
HTTP Status Code: 400

 ** OperationFailureException **
Lightsail throws this exception when an operation fails to execute.
HTTP Status Code: 400

 ** RegionSetupInProgressException **
Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.
 ** docs **
 [Regions and Availability Zones for Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-regions-and-availability-zones-in-amazon-lightsail.html)
 ** tip **
Opt-in Regions typically take a few minutes to finish setting up before you can work with them. Wait a few minutes and try again.
HTTP Status Code: 400

 ** ServiceException **
A general service exception.
HTTP Status Code: 500

 ** UnauthenticatedException **
Lightsail throws this exception when the user has not been authenticated.
HTTP Status Code: 400

## See Also
<a name="API_GetRegions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/GetRegions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/GetRegions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/GetRegions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/GetRegions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/GetRegions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/GetRegions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/GetRegions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/GetRegions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/GetRegions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/GetRegions)
