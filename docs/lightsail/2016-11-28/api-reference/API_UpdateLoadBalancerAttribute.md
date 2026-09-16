---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UpdateLoadBalancerAttribute.html
---

# UpdateLoadBalancerAttribute
<a name="API_UpdateLoadBalancerAttribute"></a>

Updates the specified attribute for a load balancer. You can only update one attribute at a time.

The `update load balancer attribute` operation supports tag-based access control via resource tags applied to the resource identified by `load balancer name`. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags).

## Request Syntax
<a name="API_UpdateLoadBalancerAttribute_RequestSyntax"></a>

```
{
   "attributeName": "{{string}}",
   "attributeValue": "{{string}}",
   "loadBalancerName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateLoadBalancerAttribute_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [attributeName](#API_UpdateLoadBalancerAttribute_RequestSyntax) **   <a name="Lightsail-UpdateLoadBalancerAttribute-request-attributeName"></a>
The name of the attribute you want to update.
Type: String
Valid Values: `HealthCheckPath | SessionStickinessEnabled | SessionStickiness_LB_CookieDurationSeconds | HttpsRedirectionEnabled | TlsPolicyName`
Required: Yes

 ** [attributeValue](#API_UpdateLoadBalancerAttribute_RequestSyntax) **   <a name="Lightsail-UpdateLoadBalancerAttribute-request-attributeValue"></a>
The value that you want to specify for the attribute name.
The following values are supported depending on what you specify for the `attributeName` request parameter:
+ If you specify `HealthCheckPath` for the `attributeName` request parameter, then the `attributeValue` request parameter must be the path to ping on the target (for example, `/weather/us/wa/seattle`).
+ If you specify `SessionStickinessEnabled` for the `attributeName` request parameter, then the `attributeValue` request parameter must be `true` to activate session stickiness or `false` to deactivate session stickiness.
+ If you specify `SessionStickiness_LB_CookieDurationSeconds` for the `attributeName` request parameter, then the `attributeValue` request parameter must be an interger that represents the cookie duration in seconds.
+ If you specify `HttpsRedirectionEnabled` for the `attributeName` request parameter, then the `attributeValue` request parameter must be `true` to activate HTTP to HTTPS redirection or `false` to deactivate HTTP to HTTPS redirection.
+ If you specify `TlsPolicyName` for the `attributeName` request parameter, then the `attributeValue` request parameter must be the name of the TLS policy.

  Use the [GetLoadBalancerTlsPolicies](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetLoadBalancerTlsPolicies.html) action to get a list of TLS policy names that you can specify.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [loadBalancerName](#API_UpdateLoadBalancerAttribute_RequestSyntax) **   <a name="Lightsail-UpdateLoadBalancerAttribute-request-loadBalancerName"></a>
The name of the load balancer that you want to modify (`my-load-balancer`.
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

## Response Syntax
<a name="API_UpdateLoadBalancerAttribute_ResponseSyntax"></a>

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
<a name="API_UpdateLoadBalancerAttribute_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operations](#API_UpdateLoadBalancerAttribute_ResponseSyntax) **   <a name="Lightsail-UpdateLoadBalancerAttribute-response-operations"></a>
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: Array of [Operation](API_Operation.md) objects

## Errors
<a name="API_UpdateLoadBalancerAttribute_Errors"></a>

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
<a name="API_UpdateLoadBalancerAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/UpdateLoadBalancerAttribute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/UpdateLoadBalancerAttribute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/UpdateLoadBalancerAttribute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/UpdateLoadBalancerAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/UpdateLoadBalancerAttribute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/UpdateLoadBalancerAttribute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/UpdateLoadBalancerAttribute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/UpdateLoadBalancerAttribute)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/UpdateLoadBalancerAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/UpdateLoadBalancerAttribute)
