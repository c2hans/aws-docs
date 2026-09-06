---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateLoadBalancer.html
---

# CreateLoadBalancer
<a name="API_CreateLoadBalancer"></a>

Creates a Lightsail load balancer. To learn more about deciding whether to load balance your application, see [Configure your Lightsail instances for load balancing](https://docs.aws.amazon.com/lightsail/latest/userguide/configure-lightsail-instances-for-load-balancing). You can create up to 10 load balancers per AWS Region in your account.

When you create a load balancer, you can specify a unique name and port settings. To change additional load balancer settings, use the `UpdateLoadBalancerAttribute` operation.

The `create load balancer` operation supports tag-based access control via request tags. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags).

## Request Syntax
<a name="API_CreateLoadBalancer_RequestSyntax"></a>

```
{
   "certificateAlternativeNames": [ "{{string}}" ],
   "certificateDomainName": "{{string}}",
   "certificateName": "{{string}}",
   "healthCheckPath": "{{string}}",
   "instancePort": {{number}},
   "ipAddressType": "{{string}}",
   "loadBalancerName": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "tlsPolicyName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateLoadBalancer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [certificateAlternativeNames](#API_CreateLoadBalancer_RequestSyntax) **   <a name="Lightsail-CreateLoadBalancer-request-certificateAlternativeNames"></a>
The optional alternative domains and subdomains to use with your SSL/TLS certificate (`www.example.com`, `example.com`, `m.example.com`, `blog.example.com`).
Type: Array of strings
Required: No

 ** [certificateDomainName](#API_CreateLoadBalancer_RequestSyntax) **   <a name="Lightsail-CreateLoadBalancer-request-certificateDomainName"></a>
The domain name with which your certificate is associated (`example.com`).
If you specify `certificateDomainName`, then `certificateName` is required (and vice-versa).
Type: String
Required: No

 ** [certificateName](#API_CreateLoadBalancer_RequestSyntax) **   <a name="Lightsail-CreateLoadBalancer-request-certificateName"></a>
The name of the SSL/TLS certificate.
If you specify `certificateName`, then `certificateDomainName` is required (and vice-versa).
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** [healthCheckPath](#API_CreateLoadBalancer_RequestSyntax) **   <a name="Lightsail-CreateLoadBalancer-request-healthCheckPath"></a>
The path you provided to perform the load balancer health check. If you didn't specify a health check path, Lightsail uses the root path of your website (`"/"`).
You may want to specify a custom health check path other than the root of your application if your home page loads slowly or has a lot of media or scripting on it.
Type: String
Required: No

 ** [instancePort](#API_CreateLoadBalancer_RequestSyntax) **   <a name="Lightsail-CreateLoadBalancer-request-instancePort"></a>
The instance port where you're creating your load balancer.
Type: Integer
Valid Range: Minimum value of -1. Maximum value of 65535.
Required: Yes

 ** [ipAddressType](#API_CreateLoadBalancer_RequestSyntax) **   <a name="Lightsail-CreateLoadBalancer-request-ipAddressType"></a>
The IP address type for the load balancer.
The possible values are `ipv4` for IPv4 only, `ipv6` for IPv6 only, and `dualstack` for IPv4 and IPv6.
The default value is `dualstack`.
Type: String
Valid Values: `dualstack | ipv4 | ipv6`
Required: No

 ** [loadBalancerName](#API_CreateLoadBalancer_RequestSyntax) **   <a name="Lightsail-CreateLoadBalancer-request-loadBalancerName"></a>
The name of your load balancer.
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

 ** [tags](#API_CreateLoadBalancer_RequestSyntax) **   <a name="Lightsail-CreateLoadBalancer-request-tags"></a>
The tag keys and optional values to add to the resource during create.
Use the `TagResource` action to tag a resource after it's created.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [tlsPolicyName](#API_CreateLoadBalancer_RequestSyntax) **   <a name="Lightsail-CreateLoadBalancer-request-tlsPolicyName"></a>
The name of the TLS policy to apply to the load balancer.
Use the [GetLoadBalancerTlsPolicies](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetLoadBalancerTlsPolicies.html) action to get a list of TLS policy names that you can specify.
For more information about load balancer TLS policies, see [Configuring TLS security policies on your Amazon Lightsail load balancers](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configure-load-balancer-tls-security-policy) in the *Amazon Lightsail Developer Guide*.
Type: String
Required: No

## Response Syntax
<a name="API_CreateLoadBalancer_ResponseSyntax"></a>

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
<a name="API_CreateLoadBalancer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operations](#API_CreateLoadBalancer_ResponseSyntax) **   <a name="Lightsail-CreateLoadBalancer-response-operations"></a>
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: Array of [Operation](API_Operation.md) objects

## Errors
<a name="API_CreateLoadBalancer_Errors"></a>

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
<a name="API_CreateLoadBalancer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/CreateLoadBalancer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/CreateLoadBalancer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/CreateLoadBalancer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/CreateLoadBalancer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/CreateLoadBalancer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/CreateLoadBalancer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/CreateLoadBalancer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/CreateLoadBalancer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/CreateLoadBalancer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/CreateLoadBalancer)
