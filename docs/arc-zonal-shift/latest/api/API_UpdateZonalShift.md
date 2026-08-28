---
source_url: https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_UpdateZonalShift.html
---

# UpdateZonalShift
<a name="API_UpdateZonalShift"></a>

Update an active zonal shift in Amazon Application Recovery Controller in your AWS account. You can update a zonal shift to set a new expiration, or edit or replace the comment for the zonal shift.

## Request Syntax
<a name="API_UpdateZonalShift_RequestSyntax"></a>

```
PATCH /zonalshifts/{{zonalShiftId}} HTTP/1.1
Content-type: application/json

{
   "comment": "{{string}}",
   "expiresIn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateZonalShift_RequestParameters"></a>

The request uses the following URI parameters.

 ** [zonalShiftId](#API_UpdateZonalShift_RequestSyntax) **   <a name="zonalshift-UpdateZonalShift-request-uri-zonalShiftId"></a>
The identifier of a zonal shift.
Length Constraints: Minimum length of 6. Maximum length of 36.
Pattern: `[A-Za-z0-9-]+`
Required: Yes

## Request Body
<a name="API_UpdateZonalShift_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [comment](#API_UpdateZonalShift_RequestSyntax) **   <a name="zonalshift-UpdateZonalShift-request-comment"></a>
A comment that you enter about the zonal shift. Only the latest comment is retained; no comment history is maintained. A new comment overwrites any existing comment string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** [expiresIn](#API_UpdateZonalShift_RequestSyntax) **   <a name="zonalshift-UpdateZonalShift-request-expiresIn"></a>
The length of time that you want a zonal shift to be active, which ARC converts to an expiry time (expiration time). Zonal shifts are temporary. You can set a zonal shift to be active initially for up to three days (72 hours).
If you want to still keep traffic away from an Availability Zone, you can update the zonal shift and set a new expiration. You can also cancel a zonal shift, before it expires, for example, if you're ready to restore traffic to the Availability Zone.
To set a length of time for a zonal shift to be active, specify a whole number, and then one of the following, with no space:
+  **A lowercase letter m:** To specify that the value is in minutes.
+  **A lowercase letter h:** To specify that the value is in hours.
For example: `20h` means the zonal shift expires in 20 hours. `120m` means the zonal shift expires in 120 minutes (2 hours).
Type: String
Length Constraints: Minimum length of 2. Maximum length of 5.
Pattern: `([1-9][0-9]*)(m|h)`
Required: No

## Response Syntax
<a name="API_UpdateZonalShift_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "awayFrom": "string",
   "comment": "string",
   "expiryTime": number,
   "resourceIdentifier": "string",
   "startTime": number,
   "status": "string",
   "zonalShiftId": "string"
}
```

## Response Elements
<a name="API_UpdateZonalShift_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [awayFrom](#API_UpdateZonalShift_ResponseSyntax) **   <a name="zonalshift-UpdateZonalShift-response-awayFrom"></a>
The Availability Zone (for example, `use1-az1`) that traffic is moved away from for a resource when you start a zonal shift. Until the zonal shift expires or you cancel it, traffic for the resource is instead moved to other Availability Zones in the AWS Region.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20.

 ** [comment](#API_UpdateZonalShift_ResponseSyntax) **   <a name="zonalshift-UpdateZonalShift-response-comment"></a>
A comment that you enter about the zonal shift. Only the latest comment is retained; no comment history is maintained. A new comment overwrites any existing comment string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.

 ** [expiryTime](#API_UpdateZonalShift_ResponseSyntax) **   <a name="zonalshift-UpdateZonalShift-response-expiryTime"></a>
The expiry time (expiration time) for a customer-initiated zonal shift. A zonal shift is temporary and must be set to expire when you start the zonal shift. You can initially set a zonal shift to expire in a maximum of three days (72 hours). However, you can update a zonal shift to set a new expiration at any time.
When you start a zonal shift, you specify how long you want it to be active, which ARC converts to an expiry time (expiration time). You can cancel a zonal shift when you're ready to restore traffic to the Availability Zone, or just wait for it to expire. Or you can update the zonal shift to specify another length of time to expire in.
Type: Timestamp

 ** [resourceIdentifier](#API_UpdateZonalShift_ResponseSyntax) **   <a name="zonalshift-UpdateZonalShift-response-resourceIdentifier"></a>
The identifier for the resource that AWS shifts traffic for. The identifier is the Amazon Resource Name (ARN) for the resource.
Amazon Application Recovery Controller currently supports enabling the following resources for zonal shift and zonal autoshift:
+  [Amazon EC2 Auto Scaling groups](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.ec2-auto-scaling-groups.html)
+  [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.eks.html)
+  [Application Load Balancer](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.app-load-balancers.html)
+  [Network Load Balancer](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.network-load-balancers.html)
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.

 ** [startTime](#API_UpdateZonalShift_ResponseSyntax) **   <a name="zonalshift-UpdateZonalShift-response-startTime"></a>
The time (UTC) when the zonal shift starts.
Type: Timestamp

 ** [status](#API_UpdateZonalShift_ResponseSyntax) **   <a name="zonalshift-UpdateZonalShift-response-status"></a>
A status for a zonal shift.
The `Status` for a zonal shift can have one of the following values:
+  **ACTIVE:** The zonal shift has been started and is active.
+  **EXPIRED:** The zonal shift has expired (the expiry time was exceeded).
+  **CANCELED:** The zonal shift was canceled.
Type: String
Valid Values: `ACTIVE | EXPIRED | CANCELED`

 ** [zonalShiftId](#API_UpdateZonalShift_ResponseSyntax) **   <a name="zonalshift-UpdateZonalShift-response-zonalShiftId"></a>
The identifier of a zonal shift.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 36.
Pattern: `[A-Za-z0-9-]+`

## Errors
<a name="API_UpdateZonalShift_Errors"></a>

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
<a name="API_UpdateZonalShift_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/arc-zonal-shift-2022-10-30/UpdateZonalShift)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/arc-zonal-shift-2022-10-30/UpdateZonalShift)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-zonal-shift-2022-10-30/UpdateZonalShift)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/arc-zonal-shift-2022-10-30/UpdateZonalShift)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-zonal-shift-2022-10-30/UpdateZonalShift)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/arc-zonal-shift-2022-10-30/UpdateZonalShift)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/arc-zonal-shift-2022-10-30/UpdateZonalShift)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/arc-zonal-shift-2022-10-30/UpdateZonalShift)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/arc-zonal-shift-2022-10-30/UpdateZonalShift)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-zonal-shift-2022-10-30/UpdateZonalShift)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-zonal-shift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
