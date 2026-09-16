---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteTrafficPolicyInstance.html
---

# DeleteTrafficPolicyInstance
<a name="API_DeleteTrafficPolicyInstance"></a>

Deletes a traffic policy instance and all of the resource record sets that Amazon Route 53 created when you created the instance.

**Note**
In the Route 53 console, traffic policy instances are known as policy records.

## Request Syntax
<a name="API_DeleteTrafficPolicyInstance_RequestSyntax"></a>

```
DELETE /2013-04-01/trafficpolicyinstance/{{Id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteTrafficPolicyInstance_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_DeleteTrafficPolicyInstance_RequestSyntax) **   <a name="Route53-DeleteTrafficPolicyInstance-request-uri-Id"></a>
The ID of the traffic policy instance that you want to delete.
When you delete a traffic policy instance, Amazon Route 53 also deletes all of the resource record sets that were created when you created the traffic policy instance.
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: Yes

## Request Body
<a name="API_DeleteTrafficPolicyInstance_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteTrafficPolicyInstance_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteTrafficPolicyInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteTrafficPolicyInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchTrafficPolicyInstance **
No traffic policy instance exists with the specified ID.
 ** message **

HTTP Status Code: 404

 ** PriorRequestNotComplete **
If Amazon Route 53 can't process a request before the next request arrives, it will reject subsequent requests for the same hosted zone and return an `HTTP 400 error` (`Bad request`). If Route 53 returns this error repeatedly for the same request, we recommend that you wait, in intervals of increasing duration, before you try the request again.
HTTP Status Code: 400

## Examples
<a name="API_DeleteTrafficPolicyInstance_Examples"></a>

### Example Request
<a name="API_DeleteTrafficPolicyInstance_Example_1"></a>

This example illustrates one usage of DeleteTrafficPolicyInstance.

```
DELETE /2013-04-01/trafficpolicyinstance/12131415-abac-5432-caba-6f5e4d3c2b1a
```

### Example Response
<a name="API_DeleteTrafficPolicyInstance_Example_2"></a>

This example illustrates one usage of DeleteTrafficPolicyInstance.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<DeleteTrafficPolicyInstanceResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
</DeleteTrafficPolicyInstanceResponse>
```

## See Also
<a name="API_DeleteTrafficPolicyInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/DeleteTrafficPolicyInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/DeleteTrafficPolicyInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/DeleteTrafficPolicyInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/DeleteTrafficPolicyInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/DeleteTrafficPolicyInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/DeleteTrafficPolicyInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/DeleteTrafficPolicyInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/DeleteTrafficPolicyInstance)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/DeleteTrafficPolicyInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/DeleteTrafficPolicyInstance)
