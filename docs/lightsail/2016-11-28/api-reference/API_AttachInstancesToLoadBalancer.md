---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_AttachInstancesToLoadBalancer.html
---

# AttachInstancesToLoadBalancer
<a name="API_AttachInstancesToLoadBalancer"></a>

Attaches one or more Lightsail instances to a load balancer.

After some time, the instances are attached to the load balancer and the health check status is available.

The `attach instances to load balancer` operation supports tag-based access control via resource tags applied to the resource identified by `load balancer name`. For more information, see the [Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags).

## Request Syntax
<a name="API_AttachInstancesToLoadBalancer_RequestSyntax"></a>

```
{
   "instanceNames": [ "{{string}}" ],
   "loadBalancerName": "{{string}}"
}
```

## Request Parameters
<a name="API_AttachInstancesToLoadBalancer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [instanceNames](#API_AttachInstancesToLoadBalancer_RequestSyntax) **   <a name="Lightsail-AttachInstancesToLoadBalancer-request-instanceNames"></a>
An array of strings representing the instance name(s) you want to attach to your load balancer.
An instance must be `running` before you can attach it to your load balancer.
There are no additional limits on the number of instances you can attach to your load balancer, aside from the limit of Lightsail instances you can create in your account (20).
Type: Array of strings
Pattern: `\w[\w\-]*\w`
Required: Yes

 ** [loadBalancerName](#API_AttachInstancesToLoadBalancer_RequestSyntax) **   <a name="Lightsail-AttachInstancesToLoadBalancer-request-loadBalancerName"></a>
The name of the load balancer.
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

## Response Syntax
<a name="API_AttachInstancesToLoadBalancer_ResponseSyntax"></a>

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
<a name="API_AttachInstancesToLoadBalancer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operations](#API_AttachInstancesToLoadBalancer_ResponseSyntax) **   <a name="Lightsail-AttachInstancesToLoadBalancer-response-operations"></a>
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: Array of [Operation](API_Operation.md) objects

## Errors
<a name="API_AttachInstancesToLoadBalancer_Errors"></a>

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
<a name="API_AttachInstancesToLoadBalancer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/AttachInstancesToLoadBalancer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/AttachInstancesToLoadBalancer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/AttachInstancesToLoadBalancer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/AttachInstancesToLoadBalancer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/AttachInstancesToLoadBalancer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/AttachInstancesToLoadBalancer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/AttachInstancesToLoadBalancer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/AttachInstancesToLoadBalancer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/AttachInstancesToLoadBalancer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/AttachInstancesToLoadBalancer)
