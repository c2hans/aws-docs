---
source_url: https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_UpdateZonalAutoshiftConfiguration.html
---

# UpdateZonalAutoshiftConfiguration
<a name="API_UpdateZonalAutoshiftConfiguration"></a>

The zonal autoshift configuration for a resource includes the practice run configuration and the status for running autoshifts, zonal autoshift status. When a resource has a practice run configuration, ARC starts weekly zonal shifts for the resource, to shift traffic away from an Availability Zone. Weekly practice runs help you to make sure that your application can continue to operate normally with the loss of one Availability Zone.

You can update the zonal autoshift status to enable or disable zonal autoshift. When zonal autoshift is `ENABLED`, you authorize AWS to shift away resource traffic for an application from an Availability Zone during events, on your behalf, to help reduce time to recovery. Traffic is also shifted away for the required weekly practice runs.

## Request Syntax
<a name="API_UpdateZonalAutoshiftConfiguration_RequestSyntax"></a>

```
PUT /managedresources/{{resourceIdentifier}} HTTP/1.1
Content-type: application/json

{
   "zonalAutoshiftStatus": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateZonalAutoshiftConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceIdentifier](#API_UpdateZonalAutoshiftConfiguration_RequestSyntax) **   <a name="zonalshift-UpdateZonalAutoshiftConfiguration-request-uri-resourceIdentifier"></a>
The identifier for the resource that you want to update the zonal autoshift configuration for. The identifier is the Amazon Resource Name (ARN) for the resource.
Length Constraints: Minimum length of 8. Maximum length of 1024.
Required: Yes

## Request Body
<a name="API_UpdateZonalAutoshiftConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [zonalAutoshiftStatus](#API_UpdateZonalAutoshiftConfiguration_RequestSyntax) **   <a name="zonalshift-UpdateZonalAutoshiftConfiguration-request-zonalAutoshiftStatus"></a>
The zonal autoshift status for the resource that you want to update the zonal autoshift configuration for. Choose `ENABLED` to authorize AWS to shift away resource traffic for an application from an Availability Zone during events, on your behalf, to help reduce time to recovery.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

## Response Syntax
<a name="API_UpdateZonalAutoshiftConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "resourceIdentifier": "string",
   "zonalAutoshiftStatus": "string"
}
```

## Response Elements
<a name="API_UpdateZonalAutoshiftConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [resourceIdentifier](#API_UpdateZonalAutoshiftConfiguration_ResponseSyntax) **   <a name="zonalshift-UpdateZonalAutoshiftConfiguration-response-resourceIdentifier"></a>
The identifier for the resource that you updated the zonal autoshift configuration for. The identifier is the Amazon Resource Name (ARN) for the resource.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.

 ** [zonalAutoshiftStatus](#API_UpdateZonalAutoshiftConfiguration_ResponseSyntax) **   <a name="zonalshift-UpdateZonalAutoshiftConfiguration-response-zonalAutoshiftStatus"></a>
The updated zonal autoshift status for the resource.
Type: String
Valid Values: `ENABLED | DISABLED`

## Errors
<a name="API_UpdateZonalAutoshiftConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource.
 ** reason **
The reason for the conflict exception.
 ** zonalShiftId **
The zonal shift ID associated with the conflict exception.
HTTP Status Code: 409

 ** InternalServerException **
There was an internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The input requested a resource that was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_UpdateZonalAutoshiftConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/arc-zonal-shift-2022-10-30/UpdateZonalAutoshiftConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/arc-zonal-shift-2022-10-30/UpdateZonalAutoshiftConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-zonal-shift-2022-10-30/UpdateZonalAutoshiftConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/arc-zonal-shift-2022-10-30/UpdateZonalAutoshiftConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-zonal-shift-2022-10-30/UpdateZonalAutoshiftConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/arc-zonal-shift-2022-10-30/UpdateZonalAutoshiftConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/arc-zonal-shift-2022-10-30/UpdateZonalAutoshiftConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/arc-zonal-shift-2022-10-30/UpdateZonalAutoshiftConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/arc-zonal-shift-2022-10-30/UpdateZonalAutoshiftConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-zonal-shift-2022-10-30/UpdateZonalAutoshiftConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-zonal-shift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
