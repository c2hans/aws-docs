---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateKeyPair.html
---

# CreateKeyPair
<a name="API_CreateKeyPair"></a>

Creates a custom SSH key pair that you can use with an Amazon Lightsail instance.

**Note**
Use the [DownloadDefaultKeyPair](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_DownloadDefaultKeyPair.html) action to create a Lightsail default key pair in an AWS Region where a default key pair does not currently exist.

The `create key pair` operation supports tag-based access control via request tags. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags).

## Request Syntax
<a name="API_CreateKeyPair_RequestSyntax"></a>

```
{
   "keyPairName": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateKeyPair_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [keyPairName](#API_CreateKeyPair_RequestSyntax) **   <a name="Lightsail-CreateKeyPair-request-keyPairName"></a>
The name for your new key pair.
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

 ** [tags](#API_CreateKeyPair_RequestSyntax) **   <a name="Lightsail-CreateKeyPair-request-tags"></a>
The tag keys and optional values to add to the resource during create.
Use the `TagResource` action to tag a resource after it's created.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateKeyPair_ResponseSyntax"></a>

```
{
   "keyPair": {
      "arn": "string",
      "createdAt": number,
      "fingerprint": "string",
      "location": {
         "availabilityZone": "string",
         "regionName": "string"
      },
      "name": "string",
      "resourceType": "string",
      "supportCode": "string",
      "tags": [
         {
            "key": "string",
            "value": "string"
         }
      ]
   },
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
   },
   "privateKeyBase64": "string",
   "publicKeyBase64": "string"
}
```

## Response Elements
<a name="API_CreateKeyPair_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [keyPair](#API_CreateKeyPair_ResponseSyntax) **   <a name="Lightsail-CreateKeyPair-response-keyPair"></a>
An array of key-value pairs containing information about the new key pair you just created.
Type: [KeyPair](API_KeyPair.md) object

 ** [operation](#API_CreateKeyPair_ResponseSyntax) **   <a name="Lightsail-CreateKeyPair-response-operation"></a>
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: [Operation](API_Operation.md) object

 ** [privateKeyBase64](#API_CreateKeyPair_ResponseSyntax) **   <a name="Lightsail-CreateKeyPair-response-privateKeyBase64"></a>
A base64-encoded RSA private key.
Type: String

 ** [publicKeyBase64](#API_CreateKeyPair_ResponseSyntax) **   <a name="Lightsail-CreateKeyPair-response-publicKeyBase64"></a>
A base64-encoded public key of the `ssh-rsa` type.
Type: String

## Errors
<a name="API_CreateKeyPair_Errors"></a>

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
<a name="API_CreateKeyPair_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/CreateKeyPair)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/CreateKeyPair)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/CreateKeyPair)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/CreateKeyPair)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/CreateKeyPair)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/CreateKeyPair)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/CreateKeyPair)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/CreateKeyPair)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/CreateKeyPair)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/CreateKeyPair)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
