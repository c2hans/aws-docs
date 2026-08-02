---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_DeleteKeyPair.html
---

# DeleteKeyPair
<a name="API_DeleteKeyPair"></a>

Deletes the specified key pair by removing the public key from Amazon Lightsail.

You can delete key pairs that were created using the [ImportKeyPair](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_ImportKeyPair.html) and [CreateKeyPair](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateKeyPair.html) actions, as well as the Lightsail default key pair. A new default key pair will not be created unless you launch an instance without specifying a custom key pair, or you call the [DownloadDefaultKeyPair](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_DownloadDefaultKeyPair.html) API.

The `delete key pair` operation supports tag-based access control via resource tags applied to the resource identified by `key pair name`. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags).

## Request Syntax
<a name="API_DeleteKeyPair_RequestSyntax"></a>

```
{
   "expectedFingerprint": "{{string}}",
   "keyPairName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteKeyPair_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [expectedFingerprint](#API_DeleteKeyPair_RequestSyntax) **   <a name="Lightsail-DeleteKeyPair-request-expectedFingerprint"></a>
The RSA fingerprint of the Lightsail default key pair to delete.
The `expectedFingerprint` parameter is required only when specifying to delete a Lightsail default key pair.
Type: String
Required: No

 ** [keyPairName](#API_DeleteKeyPair_RequestSyntax) **   <a name="Lightsail-DeleteKeyPair-request-keyPairName"></a>
The name of the key pair to delete.
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

## Response Syntax
<a name="API_DeleteKeyPair_ResponseSyntax"></a>

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
<a name="API_DeleteKeyPair_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operation](#API_DeleteKeyPair_ResponseSyntax) **   <a name="Lightsail-DeleteKeyPair-response-operation"></a>
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: [Operation](API_Operation.md) object

## Errors
<a name="API_DeleteKeyPair_Errors"></a>

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
<a name="API_DeleteKeyPair_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/DeleteKeyPair)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/DeleteKeyPair)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/DeleteKeyPair)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/DeleteKeyPair)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/DeleteKeyPair)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/DeleteKeyPair)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/DeleteKeyPair)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/DeleteKeyPair)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/DeleteKeyPair)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/DeleteKeyPair)
