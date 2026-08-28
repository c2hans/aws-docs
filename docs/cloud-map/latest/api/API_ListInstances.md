---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_ListInstances.html
---

# ListInstances
<a name="API_ListInstances"></a>

Lists summary information about the instances that you registered by using a specified service.

## Request Syntax
<a name="API_ListInstances_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ServiceId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListInstances_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListInstances_RequestSyntax) **   <a name="cloudmap-ListInstances-request-MaxResults"></a>
The maximum number of instances that you want AWS Cloud Map to return in the response to a `ListInstances` request. If you don't specify a value for `MaxResults`, AWS Cloud Map returns up to 100 instances.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListInstances_RequestSyntax) **   <a name="cloudmap-ListInstances-request-NextToken"></a>
For the first `ListInstances` request, omit this value.
If more than `MaxResults` instances match the specified criteria, you can submit another `ListInstances` request to get the next group of results. Specify the value of `NextToken` from the previous response in the next request.
Type: String
Length Constraints: Maximum length of 4096.
Required: No

 ** [ServiceId](#API_ListInstances_RequestSyntax) **   <a name="cloudmap-ListInstances-request-ServiceId"></a>
The ID or Amazon Resource Name (ARN) of the service that you want to list instances for. For services created in a shared namespace, specify the service ARN. For more information about shared namespaces, see [Cross-account AWS Cloud Map namespace sharing](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html) in the * AWS Cloud Map Developer Guide*.
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

## Response Syntax
<a name="API_ListInstances_ResponseSyntax"></a>

```
{
   "Instances": [
      {
         "Attributes": {
            "string" : "string"
         },
         "CreatedByAccount": "string",
         "Id": "string"
      }
   ],
   "NextToken": "string",
   "ResourceOwner": "string"
}
```

## Response Elements
<a name="API_ListInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Instances](#API_ListInstances_ResponseSyntax) **   <a name="cloudmap-ListInstances-response-Instances"></a>
Summary information about the instances that are associated with the specified service.
Type: Array of [InstanceSummary](API_InstanceSummary.md) objects

 ** [NextToken](#API_ListInstances_ResponseSyntax) **   <a name="cloudmap-ListInstances-response-NextToken"></a>
If more than `MaxResults` instances match the specified criteria, you can submit another `ListInstances` request to get the next group of results. Specify the value of `NextToken` from the previous response in the next request.
Type: String
Length Constraints: Maximum length of 4096.

 ** [ResourceOwner](#API_ListInstances_ResponseSyntax) **   <a name="cloudmap-ListInstances-response-ResourceOwner"></a>
The ID of the AWS account that created the namespace that contains the specified service. If this isn't your account ID, it's the ID of the account that shared the namespace with your account.
Type: String
Length Constraints: Fixed length of 12.

## Errors
<a name="API_ListInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.
HTTP Status Code: 400

 ** ServiceNotFound **
No service exists with the specified ID.
HTTP Status Code: 400

## Examples
<a name="API_ListInstances_Examples"></a>

### ListInstances Example
<a name="API_ListInstances_Example_1"></a>

This example request lists information about all instances associated with the specified service.

#### Sample Request
<a name="API_ListInstances_Example_1_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211817Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.ListInstances
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "ServiceId": "srv-e4anhexample0004"
}
```

#### Sample Response
<a name="API_ListInstances_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1

{
    "Instances": [
        {
            "Id": "i-abcd1234",
            "Attributes": {
                "AWS_INSTANCE_IPV4": "192.0.2.44",
                "AWS_INSTANCE_PORT": "80",
                "color": "green",
                "region": "us-west-2",
                "stage": "beta"
            },
            "CreatedByAccount": "123456789012"
        },
        {
            "Id": "i-abcd1235",
            "Attributes": {
                "AWS_INSTANCE_IPV4": "192.0.2.45",
                "AWS_INSTANCE_PORT": "80",
                "color": "blue",
                "region": "us-west-2",
                "stage": "beta"
            },
            "CreatedByAccount": "123456789012"
        }
    ],
    "ResourceOwner": "123456789012"
}
```

### ListInstances Example using service ARN
<a name="API_ListInstances_Example_2"></a>

This example request lists information about all instances associated with a service in a shared namespace using the service ARN. The blue service is created by namespace consumer `111122223333` and the green service is created by the namespace owner `123456789012`.

#### Sample Request
<a name="API_ListInstances_Example_2_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211817Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.ListInstances
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "ServiceId": "arn:aws:servicediscovery:us-west-2:123456789012:service/srv-e4anhexample0004"
}
```

#### Sample Response
<a name="API_ListInstances_Example_2_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1

{
    "Instances": [
        {
            "Id": "i-abcd1234",
            "Attributes": {
                "AWS_INSTANCE_IPV4": "192.0.2.44",
                "AWS_INSTANCE_PORT": "80",
                "color": "green",
                "region": "us-west-2",
                "stage": "beta"
            },
            "CreatedByAccount": "123456789012"
        },
        {
            "Id": "i-abcd1235",
            "Attributes": {
                "AWS_INSTANCE_IPV4": "192.0.2.45",
                "AWS_INSTANCE_PORT": "80",
                "color": "blue",
                "region": "us-west-2",
                "stage": "beta"
            },
            "CreatedByAccount": "111122223333"
        }
    ],
    "ResourceOwner": "123456789012"
}
```

## See Also
<a name="API_ListInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicediscovery-2017-03-14/ListInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicediscovery-2017-03-14/ListInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/ListInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicediscovery-2017-03-14/ListInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/ListInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicediscovery-2017-03-14/ListInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicediscovery-2017-03-14/ListInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicediscovery-2017-03-14/ListInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicediscovery-2017-03-14/ListInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/ListInstances)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Map. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloud-map` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
