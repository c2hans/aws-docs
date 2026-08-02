---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_DeleteDomainEntry.html
---

# DeleteDomainEntry
<a name="API_DeleteDomainEntry"></a>

Deletes a specific domain entry.

The `delete domain entry` operation supports tag-based access control via resource tags applied to the resource identified by `domain name`. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags).

## Request Syntax
<a name="API_DeleteDomainEntry_RequestSyntax"></a>

```
{
   "domainEntry": {
      "id": "{{string}}",
      "isAlias": {{boolean}},
      "name": "{{string}}",
      "options": {
         "{{string}}" : "{{string}}"
      },
      "target": "{{string}}",
      "type": "{{string}}"
   },
   "domainName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteDomainEntry_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [domainEntry](#API_DeleteDomainEntry_RequestSyntax) **   <a name="Lightsail-DeleteDomainEntry-request-domainEntry"></a>
An array of key-value pairs containing information about your domain entries.
Type: [DomainEntry](API_DomainEntry.md) object
Required: Yes

 ** [domainName](#API_DeleteDomainEntry_RequestSyntax) **   <a name="Lightsail-DeleteDomainEntry-request-domainName"></a>
The name of the domain entry to delete.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteDomainEntry_ResponseSyntax"></a>

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
<a name="API_DeleteDomainEntry_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operation](#API_DeleteDomainEntry_ResponseSyntax) **   <a name="Lightsail-DeleteDomainEntry-response-operation"></a>
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: [Operation](API_Operation.md) object

## Errors
<a name="API_DeleteDomainEntry_Errors"></a>

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
<a name="API_DeleteDomainEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/DeleteDomainEntry)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/DeleteDomainEntry)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/DeleteDomainEntry)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/DeleteDomainEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/DeleteDomainEntry)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/DeleteDomainEntry)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/DeleteDomainEntry)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/DeleteDomainEntry)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/DeleteDomainEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/DeleteDomainEntry)
