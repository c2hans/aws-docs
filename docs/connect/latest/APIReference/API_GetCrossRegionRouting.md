---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_GetCrossRegionRouting.html
---

# GetCrossRegionRouting
<a name="API_GetCrossRegionRouting"></a>

Retrieves the current cross-region routing configuration for an Amazon Connect Global Resiliency instance enabled for global routing. This operation returns whether cross-region routing is currently enabled or disabled (isolated) for the instance.

**Note**
This operation is available only for Amazon Connect Global Resiliency instances enabled for global routing.

## Request Syntax
<a name="API_GetCrossRegionRouting_RequestSyntax"></a>

```
GET /cross-region-routing/{{InstanceId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCrossRegionRouting_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_GetCrossRegionRouting_RequestSyntax) **   <a name="connect-GetCrossRegionRouting-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `^(arn:([a-zA-Z0-9-]+):connect:[a-z]+-[a-z-]+-[0-9]+:[0-9]+:instance/)?[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_GetCrossRegionRouting_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCrossRegionRouting_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "IsolatedRegions": [ "string" ]
}
```

## Response Elements
<a name="API_GetCrossRegionRouting_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [IsolatedRegions](#API_GetCrossRegionRouting_ResponseSyntax) **   <a name="connect-GetCrossRegionRouting-response-IsolatedRegions"></a>
The list of Regions for which cross-region routing is currently disabled (isolated). When a Region appears in this list, contacts originating in that Region will not be routed to agents in other Regions, and agents in that Region will not receive contacts from other Regions.
Type: Array of strings
Length Constraints: Minimum length of 8. Maximum length of 31.
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`

## Errors
<a name="API_GetCrossRegionRouting_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_GetCrossRegionRouting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/GetCrossRegionRouting)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/GetCrossRegionRouting)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/GetCrossRegionRouting)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/GetCrossRegionRouting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/GetCrossRegionRouting)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/GetCrossRegionRouting)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/GetCrossRegionRouting)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/GetCrossRegionRouting)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/GetCrossRegionRouting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/GetCrossRegionRouting)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
