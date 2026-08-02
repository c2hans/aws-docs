---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_DeleteDistribution.html
---

# DeleteDistribution
<a name="API_DeleteDistribution"></a>

Deletes your Amazon Lightsail content delivery network (CDN) distribution.

## Request Syntax
<a name="API_DeleteDistribution_RequestSyntax"></a>

```
{
   "distributionName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteDistribution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [distributionName](#API_DeleteDistribution_RequestSyntax) **   <a name="Lightsail-DeleteDistribution-request-distributionName"></a>
The name of the distribution to delete.
Use the `GetDistributions` action to get a list of distribution names that you can specify.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

## Response Syntax
<a name="API_DeleteDistribution_ResponseSyntax"></a>

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
<a name="API_DeleteDistribution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operation](#API_DeleteDistribution_ResponseSyntax) **   <a name="Lightsail-DeleteDistribution-response-operation"></a>
An object that describes the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: [Operation](API_Operation.md) object

## Errors
<a name="API_DeleteDistribution_Errors"></a>

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
<a name="API_DeleteDistribution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/DeleteDistribution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/DeleteDistribution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/DeleteDistribution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/DeleteDistribution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/DeleteDistribution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/DeleteDistribution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/DeleteDistribution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/DeleteDistribution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/DeleteDistribution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/DeleteDistribution)
