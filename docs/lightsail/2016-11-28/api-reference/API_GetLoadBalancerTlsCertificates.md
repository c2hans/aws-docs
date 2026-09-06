---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetLoadBalancerTlsCertificates.html
---

# GetLoadBalancerTlsCertificates
<a name="API_GetLoadBalancerTlsCertificates"></a>

Returns information about the TLS certificates that are associated with the specified Lightsail load balancer.

TLS is just an updated, more secure version of Secure Socket Layer (SSL).

You can have a maximum of 2 certificates associated with a Lightsail load balancer. One is active and the other is inactive.

## Request Syntax
<a name="API_GetLoadBalancerTlsCertificates_RequestSyntax"></a>

```
{
   "loadBalancerName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetLoadBalancerTlsCertificates_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [loadBalancerName](#API_GetLoadBalancerTlsCertificates_RequestSyntax) **   <a name="Lightsail-GetLoadBalancerTlsCertificates-request-loadBalancerName"></a>
The name of the load balancer you associated with your SSL/TLS certificate.
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

## Response Syntax
<a name="API_GetLoadBalancerTlsCertificates_ResponseSyntax"></a>

```
{
   "tlsCertificates": [
      {
         "arn": "string",
         "createdAt": number,
         "domainName": "string",
         "domainValidationRecords": [
            {
               "dnsRecordCreationState": {
                  "code": "string",
                  "message": "string"
               },
               "domainName": "string",
               "name": "string",
               "type": "string",
               "validationStatus": "string",
               "value": "string"
            }
         ],
         "failureReason": "string",
         "isAttached": boolean,
         "issuedAt": number,
         "issuer": "string",
         "keyAlgorithm": "string",
         "loadBalancerName": "string",
         "location": {
            "availabilityZone": "string",
            "regionName": "string"
         },
         "name": "string",
         "notAfter": number,
         "notBefore": number,
         "renewalSummary": {
            "domainValidationOptions": [
               {
                  "domainName": "string",
                  "validationStatus": "string"
               }
            ],
            "renewalStatus": "string"
         },
         "resourceType": "string",
         "revocationReason": "string",
         "revokedAt": number,
         "serial": "string",
         "signatureAlgorithm": "string",
         "status": "string",
         "subject": "string",
         "subjectAlternativeNames": [ "string" ],
         "supportCode": "string",
         "tags": [
            {
               "key": "string",
               "value": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_GetLoadBalancerTlsCertificates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [tlsCertificates](#API_GetLoadBalancerTlsCertificates_ResponseSyntax) **   <a name="Lightsail-GetLoadBalancerTlsCertificates-response-tlsCertificates"></a>
An array of LoadBalancerTlsCertificate objects describing your SSL/TLS certificates.
Type: Array of [LoadBalancerTlsCertificate](API_LoadBalancerTlsCertificate.md) objects

## Errors
<a name="API_GetLoadBalancerTlsCertificates_Errors"></a>

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
<a name="API_GetLoadBalancerTlsCertificates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/GetLoadBalancerTlsCertificates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/GetLoadBalancerTlsCertificates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/GetLoadBalancerTlsCertificates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/GetLoadBalancerTlsCertificates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/GetLoadBalancerTlsCertificates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/GetLoadBalancerTlsCertificates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/GetLoadBalancerTlsCertificates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/GetLoadBalancerTlsCertificates)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/GetLoadBalancerTlsCertificates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/GetLoadBalancerTlsCertificates)
