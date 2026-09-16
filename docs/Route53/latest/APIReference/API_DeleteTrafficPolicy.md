---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteTrafficPolicy.html
---

# DeleteTrafficPolicy
<a name="API_DeleteTrafficPolicy"></a>

Deletes a traffic policy.

When you delete a traffic policy, Route 53 sets a flag on the policy to indicate that it has been deleted. However, Route 53 never fully deletes the traffic policy. Note the following:
+ Deleted traffic policies aren't listed if you run [ListTrafficPolicies](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListTrafficPolicies.html).
+  There's no way to get a list of deleted policies.
+ If you retain the ID of the policy, you can get information about the policy, including the traffic policy document, by running [GetTrafficPolicy](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetTrafficPolicy.html).

## Request Syntax
<a name="API_DeleteTrafficPolicy_RequestSyntax"></a>

```
DELETE /2013-04-01/trafficpolicy/{{Id}}/{{Version}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteTrafficPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_DeleteTrafficPolicy_RequestSyntax) **   <a name="Route53-DeleteTrafficPolicy-request-uri-Id"></a>
The ID of the traffic policy that you want to delete.
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: Yes

 ** [Version](#API_DeleteTrafficPolicy_RequestSyntax) **   <a name="Route53-DeleteTrafficPolicy-request-uri-Version"></a>
The version number of the traffic policy that you want to delete.
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: Yes

## Request Body
<a name="API_DeleteTrafficPolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteTrafficPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteTrafficPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteTrafficPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModification **
Another user submitted a request to create, update, or delete the object at the same time that you did. Retry the request.
 ** message **

HTTP Status Code: 400

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchTrafficPolicy **
No traffic policy exists with the specified ID.
 ** message **

HTTP Status Code: 404

 ** TrafficPolicyInUse **
One or more traffic policy instances were created by using the specified traffic policy.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_DeleteTrafficPolicy_Examples"></a>

### Example Request
<a name="API_DeleteTrafficPolicy_Example_1"></a>

This example illustrates one usage of DeleteTrafficPolicy.

```
DELETE /2013-04-01/trafficpolicy/12345678-abcd-9876-fedc-1a2b3c4de5f6/2
```

### Example Response
<a name="API_DeleteTrafficPolicy_Example_2"></a>

This example illustrates one usage of DeleteTrafficPolicy.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<DeleteTrafficPolicyResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
</DeleteTrafficPolicyResponse>
```

## See Also
<a name="API_DeleteTrafficPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/DeleteTrafficPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/DeleteTrafficPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/DeleteTrafficPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/DeleteTrafficPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/DeleteTrafficPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/DeleteTrafficPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/DeleteTrafficPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/DeleteTrafficPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/DeleteTrafficPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/DeleteTrafficPolicy)
