---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteHealthCheck.html
---

# DeleteHealthCheck
<a name="API_DeleteHealthCheck"></a>

Deletes a health check.

**Important**
Amazon Route 53 does not prevent you from deleting a health check even if the health check is associated with one or more resource record sets. If you delete a health check and you don't update the associated resource record sets, the future status of the health check can't be predicted and may change. This will affect the routing of DNS queries for your DNS failover configuration. For more information, see [Replacing and Deleting Health Checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-creating-deleting.html#health-checks-deleting.html) in the *Amazon Route 53 Developer Guide*.

If you're using AWS Cloud Map and you configured Cloud Map to create a Route 53 health check when you register an instance, you can't use the Route 53 `DeleteHealthCheck` command to delete the health check. The health check is deleted automatically when you deregister the instance; there can be a delay of several hours before the health check is deleted from Route 53.

## Request Syntax
<a name="API_DeleteHealthCheck_RequestSyntax"></a>

```
DELETE /2013-04-01/healthcheck/{{HealthCheckId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteHealthCheck_RequestParameters"></a>

The request uses the following URI parameters.

 ** [HealthCheckId](#API_DeleteHealthCheck_RequestSyntax) **   <a name="Route53-DeleteHealthCheck-request-uri-HealthCheckId"></a>
The ID of the health check that you want to delete.
Length Constraints: Maximum length of 64.
Required: Yes

## Request Body
<a name="API_DeleteHealthCheck_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteHealthCheck_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteHealthCheck_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteHealthCheck_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** HealthCheckInUse **
 *This error has been deprecated.*
This error code is not in use.
 ** message **

HTTP Status Code: 400

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchHealthCheck **
No health check exists with the specified ID.
 ** message **

HTTP Status Code: 404

## Examples
<a name="API_DeleteHealthCheck_Examples"></a>

### Example Request
<a name="API_DeleteHealthCheck_Example_1"></a>

This example illustrates one usage of DeleteHealthCheck.

```
DELETE /2013-04-01/healthcheck/abcdef11-2222-3333-4444-555555fedcba
```

### Example Response
<a name="API_DeleteHealthCheck_Example_2"></a>

This example illustrates one usage of DeleteHealthCheck.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<DeleteHealthCheckResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
</DeleteHealthCheckResponse>
```

## See Also
<a name="API_DeleteHealthCheck_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/DeleteHealthCheck)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/DeleteHealthCheck)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/DeleteHealthCheck)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/DeleteHealthCheck)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/DeleteHealthCheck)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/DeleteHealthCheck)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/DeleteHealthCheck)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/DeleteHealthCheck)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/DeleteHealthCheck)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/DeleteHealthCheck)
