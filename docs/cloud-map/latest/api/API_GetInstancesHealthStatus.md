---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_GetInstancesHealthStatus.html
---

# GetInstancesHealthStatus
<a name="API_GetInstancesHealthStatus"></a>

Gets the current health status (`Healthy`, `Unhealthy`, or `Unknown`) of one or more instances that are associated with a specified service.

**Note**
There's a brief delay between when you register an instance and when the health status for the instance is available.

## Request Syntax
<a name="API_GetInstancesHealthStatus_RequestSyntax"></a>

```
{
   "Instances": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ServiceId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetInstancesHealthStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Instances](#API_GetInstancesHealthStatus_RequestSyntax) **   <a name="cloudmap-GetInstancesHealthStatus-request-Instances"></a>
An array that contains the IDs of all the instances that you want to get the health status for.
If you omit `Instances`, AWS Cloud Map returns the health status for all the instances that are associated with the specified service.
To get the IDs for the instances that you've registered by using a specified service, submit a [ListInstances](https://docs.aws.amazon.com/cloud-map/latest/api/API_ListInstances.html) request.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Maximum length of 64.
Required: No

 ** [MaxResults](#API_GetInstancesHealthStatus_RequestSyntax) **   <a name="cloudmap-GetInstancesHealthStatus-request-MaxResults"></a>
The maximum number of instances that you want AWS Cloud Map to return in the response to a `GetInstancesHealthStatus` request. If you don't specify a value for `MaxResults`, AWS Cloud Map returns up to 100 instances.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_GetInstancesHealthStatus_RequestSyntax) **   <a name="cloudmap-GetInstancesHealthStatus-request-NextToken"></a>
For the first `GetInstancesHealthStatus` request, omit this value.
If more than `MaxResults` instances match the specified criteria, you can submit another `GetInstancesHealthStatus` request to get the next group of results. Specify the value of `NextToken` from the previous response in the next request.
Type: String
Length Constraints: Maximum length of 4096.
Required: No

 ** [ServiceId](#API_GetInstancesHealthStatus_RequestSyntax) **   <a name="cloudmap-GetInstancesHealthStatus-request-ServiceId"></a>
The ID or Amazon Resource Name (ARN) of the service that the instance is associated with. For services created in a shared namespace, specify the service ARN. For more information about shared namespaces, see [Cross-account AWS Cloud Map namespace sharing](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html) in the * AWS Cloud Map Developer Guide*.
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

## Response Syntax
<a name="API_GetInstancesHealthStatus_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Status": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetInstancesHealthStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetInstancesHealthStatus_ResponseSyntax) **   <a name="cloudmap-GetInstancesHealthStatus-response-NextToken"></a>
If more than `MaxResults` instances match the specified criteria, you can submit another `GetInstancesHealthStatus` request to get the next group of results. Specify the value of `NextToken` from the previous response in the next request.
Type: String
Length Constraints: Maximum length of 4096.

 ** [Status](#API_GetInstancesHealthStatus_ResponseSyntax) **   <a name="cloudmap-GetInstancesHealthStatus-response-Status"></a>
A complex type that contains the IDs and the health status of the instances that you specified in the `GetInstancesHealthStatus` request.
Type: String to string map
Key Length Constraints: Maximum length of 64.
Valid Values: `HEALTHY | UNHEALTHY | UNKNOWN`

## Errors
<a name="API_GetInstancesHealthStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InstanceNotFound **
No instance exists with the specified ID, or the instance was recently registered, and information about the instance hasn't propagated yet.
HTTP Status Code: 400

 ** InvalidInput **
One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.
HTTP Status Code: 400

 ** ServiceNotFound **
No service exists with the specified ID.
HTTP Status Code: 400

## Examples
<a name="API_GetInstancesHealthStatus_Examples"></a>

### GetInstancesHealthStatus Example
<a name="API_GetInstancesHealthStatus_Example_1"></a>

This example retrieves the health status for instances registered with the specified service.

#### Sample Request
<a name="API_GetInstancesHealthStatus_Example_1_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211818Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.GetInstancesHealthStatus
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "ServiceId": "srv-e4anhexample0004"
}
```

#### Sample Response
<a name="API_GetInstancesHealthStatus_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1

{
    "Status": {
        "i-abcd1234": "HEALTHY",
        "i-abcd1235": "UNHEALTHY"
    }
}
```

### GetInstancesHealthStatus Example using service ARN
<a name="API_GetInstancesHealthStatus_Example_2"></a>

This example retrieves the health status for instances registered with a service in a shared namespace using the service ARN.

#### Sample Request
<a name="API_GetInstancesHealthStatus_Example_2_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211818Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.GetInstancesHealthStatus
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "ServiceId": "arn:aws:servicediscovery:us-west-2:123456789012:service/srv-e4anhexample0004"
}
```

#### Sample Response
<a name="API_GetInstancesHealthStatus_Example_2_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1

{
    "Status": {
        "i-abcd1234": "HEALTHY",
        "i-abcd1235": "UNHEALTHY"
    }
}
```

## See Also
<a name="API_GetInstancesHealthStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicediscovery-2017-03-14/GetInstancesHealthStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicediscovery-2017-03-14/GetInstancesHealthStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/GetInstancesHealthStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicediscovery-2017-03-14/GetInstancesHealthStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/GetInstancesHealthStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicediscovery-2017-03-14/GetInstancesHealthStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicediscovery-2017-03-14/GetInstancesHealthStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicediscovery-2017-03-14/GetInstancesHealthStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicediscovery-2017-03-14/GetInstancesHealthStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/GetInstancesHealthStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Map. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloud-map` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
