---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UpdateSubdomainAssociation.html
---

# UpdateSubdomainAssociation
<a name="API_UpdateSubdomainAssociation"></a>

Associates a Lightsail subdomain with a resource, disassociates it from a resource, or moves it from one resource to another resource.

Currently, you can associate a subdomain only with a Lightsail content delivery network (CDN) distribution. A resource can be associated with only one subdomain at a time.

When you associate a subdomain with a distribution, Lightsail attaches the subdomain's certificate to the distribution. You can't associate a subdomain with a distribution that uses a custom domain, which is a distribution that has a Lightsail certificate attached.

You can transfer each subdomain to another resource only once in a 24-hour period.

The update is asynchronous. The response returns the subdomain in the `ATTACHING`, `DETACHING`, or `TRANSFERRING` state, and an operation. To check when the update is complete, use the `GetSubdomains` action.

## Request Syntax
<a name="API_UpdateSubdomainAssociation_RequestSyntax"></a>

```
{
   "action": "{{string}}",
   "subdomainName": "{{string}}",
   "targetResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateSubdomainAssociation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [action](#API_UpdateSubdomainAssociation_RequestSyntax) **   <a name="Lightsail-UpdateSubdomainAssociation-request-action"></a>
The association change to make.
The following actions are possible:
+  `ASSOCIATE` – Associates the subdomain with the resource that you specify in the `targetResourceArn` parameter. The subdomain must be in the `UNATTACHED` state.
+  `DISASSOCIATE` – Disassociates the subdomain from its current resource. The subdomain must be in the `ATTACHED` state.
+  `TRANSFER` – Moves the subdomain from its current resource to the resource that you specify in the `targetResourceArn` parameter. The subdomain must be in the `ATTACHED` state. You can transfer each subdomain only once in a 24-hour period.
Type: String
Valid Values: `ASSOCIATE | DISASSOCIATE | TRANSFER`
Required: Yes

 ** [subdomainName](#API_UpdateSubdomainAssociation_RequestSyntax) **   <a name="Lightsail-UpdateSubdomainAssociation-request-subdomainName"></a>
The subdomain to update (for example, `mysite` or `blog.mysite`), not its web address.
Type: String
Required: Yes

 ** [targetResourceArn](#API_UpdateSubdomainAssociation_RequestSyntax) **   <a name="Lightsail-UpdateSubdomainAssociation-request-targetResourceArn"></a>
The Amazon Resource Name (ARN) of the resource to associate the subdomain with. The resource must be in your account.
This parameter is required when the `action` is `ASSOCIATE` or `TRANSFER`. It's ignored when the `action` is `DISASSOCIATE`.
Type: String
Required: No

## Response Syntax
<a name="API_UpdateSubdomainAssociation_ResponseSyntax"></a>

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
   },
   "subdomain": {
      "arn": "string",
      "attachedResource": {
         "arn": "string",
         "attachedAt": number,
         "name": "string"
      },
      "attachingResource": {
         "arn": "string",
         "attachedAt": number,
         "name": "string"
      },
      "children": [
         "Subdomain"
      ],
      "createdAt": number,
      "depth": number,
      "fqdn": "string",
      "location": {
         "availabilityZone": "string",
         "regionName": "string"
      },
      "parentFqdn": "string",
      "state": "string",
      "subdomainName": "string",
      "tags": [
         {
            "key": "string",
            "value": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_UpdateSubdomainAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operation](#API_UpdateSubdomainAssociation_ResponseSyntax) **   <a name="Lightsail-UpdateSubdomainAssociation-response-operation"></a>
An object that describes the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: [Operation](API_Operation.md) object

 ** [subdomain](#API_UpdateSubdomainAssociation_ResponseSyntax) **   <a name="Lightsail-UpdateSubdomainAssociation-response-subdomain"></a>
An object that describes the subdomain that was updated.
Type: [Subdomain](API_Subdomain.md) object

## Errors
<a name="API_UpdateSubdomainAssociation_Errors"></a>

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
<a name="API_UpdateSubdomainAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/UpdateSubdomainAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/UpdateSubdomainAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/UpdateSubdomainAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/UpdateSubdomainAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/UpdateSubdomainAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/UpdateSubdomainAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/UpdateSubdomainAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/UpdateSubdomainAssociation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/UpdateSubdomainAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/UpdateSubdomainAssociation)
