---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetDistributionBundles.html
---

# GetDistributionBundles
<a name="API_GetDistributionBundles"></a>

Returns the bundles that can be applied to your Amazon Lightsail content delivery network (CDN) distributions.

A distribution bundle specifies the monthly network transfer quota and monthly cost of your distribution.

## Response Syntax
<a name="API_GetDistributionBundles_ResponseSyntax"></a>

```
{
   "bundles": [
      {
         "bundleId": "string",
         "isActive": boolean,
         "name": "string",
         "price": number,
         "transferPerMonthInGb": number
      }
   ]
}
```

## Response Elements
<a name="API_GetDistributionBundles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [bundles](#API_GetDistributionBundles_ResponseSyntax) **   <a name="Lightsail-GetDistributionBundles-response-bundles"></a>
An object that describes a distribution bundle.
Type: Array of [DistributionBundle](API_DistributionBundle.md) objects

## Errors
<a name="API_GetDistributionBundles_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
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

 ** ServiceException **
A general service exception.
HTTP Status Code: 500

 ** UnauthenticatedException **
Lightsail throws this exception when the user has not been authenticated.
HTTP Status Code: 400

## See Also
<a name="API_GetDistributionBundles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/GetDistributionBundles)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/GetDistributionBundles)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/GetDistributionBundles)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/GetDistributionBundles)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/GetDistributionBundles)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/GetDistributionBundles)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/GetDistributionBundles)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/GetDistributionBundles)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/GetDistributionBundles)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/GetDistributionBundles)
