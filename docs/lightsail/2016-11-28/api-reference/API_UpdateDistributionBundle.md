---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UpdateDistributionBundle.html
---

# UpdateDistributionBundle
<a name="API_UpdateDistributionBundle"></a>

Updates the bundle of your Amazon Lightsail content delivery network (CDN) distribution.

A distribution bundle specifies the monthly network transfer quota and monthly cost of your distribution.

Update your distribution's bundle if your distribution is going over its monthly network transfer quota and is incurring an overage fee.

You can update your distribution's bundle only one time within your monthly AWS billing cycle. To determine if you can update your distribution's bundle, use the `GetDistributions` action. The `ableToUpdateBundle` parameter in the result will indicate whether you can currently update your distribution's bundle.

## Request Syntax
<a name="API_UpdateDistributionBundle_RequestSyntax"></a>

```
{
   "bundleId": "{{string}}",
   "distributionName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateDistributionBundle_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [bundleId](#API_UpdateDistributionBundle_RequestSyntax) **   <a name="Lightsail-UpdateDistributionBundle-request-bundleId"></a>
The bundle ID of the new bundle to apply to your distribution.
Use the `GetDistributionBundles` action to get a list of distribution bundle IDs that you can specify.
Type: String
Required: No

 ** [distributionName](#API_UpdateDistributionBundle_RequestSyntax) **   <a name="Lightsail-UpdateDistributionBundle-request-distributionName"></a>
The name of the distribution for which to update the bundle.
Use the `GetDistributions` action to get a list of distribution names that you can specify.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

## Response Syntax
<a name="API_UpdateDistributionBundle_ResponseSyntax"></a>

```
{
   "operation": {
      "createdAt": number,
      "errorCode": "string",
      "errorDetails": "string",
      "id": "string",
      "isTerminal": boolean,
      "location": {
         "availabilityZone": "string",
         "regionName": "string"
      },
      "operationDetails": "string",
      "operationType": "string",
      "resourceName": "string",
      "resourceType": "string",
      "status": "string",
      "statusChangedAt": number
   }
}
```

## Response Elements
<a name="API_UpdateDistributionBundle_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operation](#API_UpdateDistributionBundle_ResponseSyntax) **   <a name="Lightsail-UpdateDistributionBundle-response-operation"></a>
An object that describes the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: [Operation](API_Operation.md) object

## Errors
<a name="API_UpdateDistributionBundle_Errors"></a>

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
<a name="API_UpdateDistributionBundle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/UpdateDistributionBundle)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/UpdateDistributionBundle)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/UpdateDistributionBundle)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/UpdateDistributionBundle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/UpdateDistributionBundle)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/UpdateDistributionBundle)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/UpdateDistributionBundle)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/UpdateDistributionBundle)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/UpdateDistributionBundle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/UpdateDistributionBundle)
