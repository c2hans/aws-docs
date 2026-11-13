---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateSubdomain.html
---

# CreateSubdomain
<a name="API_CreateSubdomain"></a>

Creates a Lightsail subdomain, such as `mysite`, with the web address `mysite.amazonlightsail.com`. After the subdomain is created, use the `UpdateSubdomainAssociation` action to associate it with a Lightsail resource.

When you create a nested subdomain, such as `blog.mysite`, and you don't already have the top-level subdomain (`mysite`), Lightsail adds the top-level subdomain to your account in the `IMPLICIT` state.

You can have up to 30 subdomains in your account. Nested subdomains, subdomains in the `CREATE_FAILED` state, and deleted subdomains that other accounts can't create yet count toward this quota. Subdomains in the `IMPLICIT` state don't count toward this quota.

## Request Syntax
<a name="API_CreateSubdomain_RequestSyntax"></a>

```
{
   "subdomainName": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateSubdomain_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [subdomainName](#API_CreateSubdomain_RequestSyntax) **   <a name="Lightsail-CreateSubdomain-request-subdomainName"></a>
The subdomain to create (for example, `mysite` or `blog.mysite`).
A subdomain can contain one or two labels separated by a period (`.`). Each label must start and end with a lowercase letter or a number, and can contain only lowercase letters, numbers, and hyphens (`-`). The name can be up to 39 characters long, including periods. Labels that start with `xn--` aren't supported, and some names are reserved.
Specify only the subdomain. A web address, such as `mysite.amazonlightsail.com`, isn't accepted.
To create a nested subdomain, you must own the top-level subdomain or be able to create it.
Type: String
Required: Yes

 ** [tags](#API_CreateSubdomain_RequestSyntax) **   <a name="Lightsail-CreateSubdomain-request-tags"></a>
The tag keys and optional values to add to the subdomain during create.
Use the `TagResource` action to tag a resource after it's created.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateSubdomain_ResponseSyntax"></a>

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
<a name="API_CreateSubdomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operation](#API_CreateSubdomain_ResponseSyntax) **   <a name="Lightsail-CreateSubdomain-response-operation"></a>
An object that describes the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: [Operation](API_Operation.md) object

 ** [subdomain](#API_CreateSubdomain_ResponseSyntax) **   <a name="Lightsail-CreateSubdomain-response-subdomain"></a>
An object that describes the subdomain that was created.
Type: [Subdomain](API_Subdomain.md) object

## Errors
<a name="API_CreateSubdomain_Errors"></a>

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
<a name="API_CreateSubdomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/CreateSubdomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/CreateSubdomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/CreateSubdomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/CreateSubdomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/CreateSubdomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/CreateSubdomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/CreateSubdomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/CreateSubdomain)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/CreateSubdomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/CreateSubdomain)
