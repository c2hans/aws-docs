---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateLoadBalancerTlsCertificate.html
---

# CreateLoadBalancerTlsCertificate
<a name="API_CreateLoadBalancerTlsCertificate"></a>

Creates an SSL/TLS certificate for an Amazon Lightsail load balancer.

TLS is just an updated, more secure version of Secure Socket Layer (SSL).

The `CreateLoadBalancerTlsCertificate` operation supports tag-based access control via resource tags applied to the resource identified by `load balancer name`. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags).

## Request Syntax
<a name="API_CreateLoadBalancerTlsCertificate_RequestSyntax"></a>

```
{
   "certificateAlternativeNames": [ "{{string}}" ],
   "certificateDomainName": "{{string}}",
   "certificateName": "{{string}}",
   "loadBalancerName": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateLoadBalancerTlsCertificate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [certificateAlternativeNames](#API_CreateLoadBalancerTlsCertificate_RequestSyntax) **   <a name="Lightsail-CreateLoadBalancerTlsCertificate-request-certificateAlternativeNames"></a>
An array of strings listing alternative domains and subdomains for your SSL/TLS certificate. Lightsail will de-dupe the names for you. You can have a maximum of 9 alternative names (in addition to the 1 primary domain). We do not support wildcards (`*.example.com`).
Type: Array of strings
Required: No

 ** [certificateDomainName](#API_CreateLoadBalancerTlsCertificate_RequestSyntax) **   <a name="Lightsail-CreateLoadBalancerTlsCertificate-request-certificateDomainName"></a>
The domain name (`example.com`) for your SSL/TLS certificate.
Type: String
Required: Yes

 ** [certificateName](#API_CreateLoadBalancerTlsCertificate_RequestSyntax) **   <a name="Lightsail-CreateLoadBalancerTlsCertificate-request-certificateName"></a>
The SSL/TLS certificate name.
You can have up to 10 certificates in your account at one time. Each Lightsail load balancer can have up to 2 certificates associated with it at one time. There is also an overall limit to the number of certificates that can be issue in a 365-day period. For more information, see [Limits](http://docs.aws.amazon.com/acm/latest/userguide/acm-limits.html).
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

 ** [loadBalancerName](#API_CreateLoadBalancerTlsCertificate_RequestSyntax) **   <a name="Lightsail-CreateLoadBalancerTlsCertificate-request-loadBalancerName"></a>
The load balancer name where you want to create the SSL/TLS certificate.
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

 ** [tags](#API_CreateLoadBalancerTlsCertificate_RequestSyntax) **   <a name="Lightsail-CreateLoadBalancerTlsCertificate-request-tags"></a>
The tag keys and optional values to add to the resource during create.
Use the `TagResource` action to tag a resource after it's created.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateLoadBalancerTlsCertificate_ResponseSyntax"></a>

```
{
   "operations": [
      {
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
   ]
}
```

## Response Elements
<a name="API_CreateLoadBalancerTlsCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operations](#API_CreateLoadBalancerTlsCertificate_ResponseSyntax) **   <a name="Lightsail-CreateLoadBalancerTlsCertificate-response-operations"></a>
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: Array of [Operation](API_Operation.md) objects

## Errors
<a name="API_CreateLoadBalancerTlsCertificate_Errors"></a>

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
<a name="API_CreateLoadBalancerTlsCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/CreateLoadBalancerTlsCertificate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/CreateLoadBalancerTlsCertificate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/CreateLoadBalancerTlsCertificate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/CreateLoadBalancerTlsCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/CreateLoadBalancerTlsCertificate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/CreateLoadBalancerTlsCertificate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/CreateLoadBalancerTlsCertificate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/CreateLoadBalancerTlsCertificate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/CreateLoadBalancerTlsCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/CreateLoadBalancerTlsCertificate)
