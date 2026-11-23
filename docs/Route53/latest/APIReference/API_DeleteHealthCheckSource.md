---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteHealthCheckSource.html
---

# DeleteHealthCheckSource

Deletes a health check source. Before you delete a health check source, delete or update any health checks that reference it. Otherwise, the request fails with `InvalidInput`. The request also fails with `InvalidInput` if the status of the health check source is `CREATE_PENDING` or `CREATE_IN_PROGRESS`. Wait until the status is `CREATE_COMPLETED` or `CREATE_FAILED`, and then try again.

Route 53 deletes a health check source asynchronously, and the initial `HealthCheckSourceStatus` is `DELETE_PENDING`. Call `GetHealthCheckSource` to track progress. After the deletion completes, `GetHealthCheckSource` returns `NoSuchHealthCheckSource` and the health check source no longer appears in the results of `ListHealthCheckSources`. If you delete a health check source that is already deleted, the request fails with `NoSuchHealthCheckSource`.

To use this operation, you must have the `route53:DeleteHealthCheckSource` permission. You must also have permission to create a service-linked role.

## Request Syntax
<a name="API_DeleteHealthCheckSource_RequestSyntax"></a>

```
DELETE /2013-04-01/healthchecksource/{{HealthCheckSourceId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteHealthCheckSource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [HealthCheckSourceId](#API_DeleteHealthCheckSource_RequestSyntax) **   <a name="Route53-DeleteHealthCheckSource-request-uri-HealthCheckSourceId"></a>
The ID of the health check source that you want to delete.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Request Body
<a name="API_DeleteHealthCheckSource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteHealthCheckSource_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<DeleteHealthCheckSourceResponse>
   <HealthCheckSourceId>string</HealthCheckSourceId>
   <HealthCheckSourceStatus>string</HealthCheckSourceStatus>
</DeleteHealthCheckSourceResponse>
```

## Response Elements
<a name="API_DeleteHealthCheckSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [DeleteHealthCheckSourceResponse](#API_DeleteHealthCheckSource_ResponseSyntax) **   <a name="Route53-DeleteHealthCheckSource-response-DeleteHealthCheckSourceResponse"></a>
Root level tag for the DeleteHealthCheckSourceResponse parameters.
Required: Yes

 ** [HealthCheckSourceId](#API_DeleteHealthCheckSource_ResponseSyntax) **   <a name="Route53-DeleteHealthCheckSource-response-HealthCheckSourceId"></a>
The ID of the health check source that is being deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [HealthCheckSourceStatus](#API_DeleteHealthCheckSource_ResponseSyntax) **   <a name="Route53-DeleteHealthCheckSource-response-HealthCheckSourceStatus"></a>
The status of the health check source after Route 53 accepts the delete request. The value is `DELETE_PENDING`, or the current status if deletion of the health check source was already in progress.
Type: String
Valid Values: `CREATE_PENDING | CREATE_IN_PROGRESS | CREATE_COMPLETED | CREATE_FAILED | DELETE_PENDING | DELETE_IN_PROGRESS | DELETE_COMPLETED | DELETE_FAILED`

## Errors
<a name="API_DeleteHealthCheckSource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchHealthCheckSource **
No health check source exists with the specified ID. Verify that the ID is correct and that the health check source hasn't been deleted.
HTTP Status Code: 404

 ** PriorRequestNotComplete **
If Amazon Route 53 can't process a request before the next request arrives, it will reject subsequent requests for the same hosted zone and return an `HTTP 400 error` (`Bad request`). If Route 53 returns this error repeatedly for the same request, we recommend that you wait, in intervals of increasing duration, before you try the request again.
HTTP Status Code: 400

## See Also
<a name="API_DeleteHealthCheckSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/DeleteHealthCheckSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/DeleteHealthCheckSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/DeleteHealthCheckSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/DeleteHealthCheckSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/DeleteHealthCheckSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/DeleteHealthCheckSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/DeleteHealthCheckSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/DeleteHealthCheckSource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/DeleteHealthCheckSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/DeleteHealthCheckSource)
