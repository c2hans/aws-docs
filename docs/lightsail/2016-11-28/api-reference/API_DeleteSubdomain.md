---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_DeleteSubdomain.html
---

# DeleteSubdomain
<a name="API_DeleteSubdomain"></a>

Deletes a Lightsail subdomain.

The subdomain must be in the `UNATTACHED` or `CREATE_FAILED` state. To delete a subdomain that's associated with a resource, first disassociate it by using the `UpdateSubdomainAssociation` action.

When you delete a top-level subdomain that has nested subdomains, the nested subdomains continue to work, and the top-level subdomain changes to the `IMPLICIT` state.

**Note**
After you delete a subdomain that was associated with a resource, the subdomain isn't available to other accounts for at least 30 days.

## Request Syntax
<a name="API_DeleteSubdomain_RequestSyntax"></a>

```
{
   "subdomainName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteSubdomain_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [subdomainName](#API_DeleteSubdomain_RequestSyntax) **   <a name="Lightsail-DeleteSubdomain-request-subdomainName"></a>
The subdomain to delete (for example, `mysite` or `blog.mysite`), not its web address.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteSubdomain_ResponseSyntax"></a>

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
<a name="API_DeleteSubdomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operation](#API_DeleteSubdomain_ResponseSyntax) **   <a name="Lightsail-DeleteSubdomain-response-operation"></a>
An object that describes the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: [Operation](API_Operation.md) object

 ** [subdomain](#API_DeleteSubdomain_ResponseSyntax) **   <a name="Lightsail-DeleteSubdomain-response-subdomain"></a>
An object that describes the top-level subdomain in the `IMPLICIT` state.
This parameter is returned only when you delete a top-level subdomain that has nested subdomains.
Type: [Subdomain](API_Subdomain.md) object

## Errors
<a name="API_DeleteSubdomain_Errors"></a>

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
<a name="API_DeleteSubdomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/DeleteSubdomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/DeleteSubdomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/DeleteSubdomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/DeleteSubdomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/DeleteSubdomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/DeleteSubdomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/DeleteSubdomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/DeleteSubdomain)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/DeleteSubdomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/DeleteSubdomain)
