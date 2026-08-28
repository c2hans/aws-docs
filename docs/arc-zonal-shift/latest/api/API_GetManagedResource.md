---
source_url: https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_GetManagedResource.html
---

# GetManagedResource
<a name="API_GetManagedResource"></a>

Get information about a resource that's been registered for zonal shifts with Amazon Application Recovery Controller in this AWS Region. Resources that are registered for zonal shifts are managed resources in ARC. You can start zonal shifts and configure zonal autoshift for managed resources.

## Request Syntax
<a name="API_GetManagedResource_RequestSyntax"></a>

```
GET /managedresources/{{resourceIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetManagedResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceIdentifier](#API_GetManagedResource_RequestSyntax) **   <a name="zonalshift-GetManagedResource-request-uri-resourceIdentifier"></a>
The identifier for the resource that AWS shifts traffic for. The identifier is the Amazon Resource Name (ARN) for the resource.
Amazon Application Recovery Controller currently supports enabling the following resources for zonal shift and zonal autoshift:
+  [Amazon EC2 Auto Scaling groups](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.ec2-auto-scaling-groups.html)
+  [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.eks.html)
+  [Application Load Balancer](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.app-load-balancers.html)
+  [Network Load Balancer](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.network-load-balancers.html)
Length Constraints: Minimum length of 8. Maximum length of 1024.
Required: Yes

## Request Body
<a name="API_GetManagedResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetManagedResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "appliedWeights": {
      "string" : number
   },
   "arn": "string",
   "autoshifts": [
      {
         "appliedStatus": "string",
         "awayFrom": "string",
         "startTime": number
      }
   ],
   "name": "string",
   "practiceRunConfiguration": {
      "allowedWindows": [ "string" ],
      "blockedDates": [ "string" ],
      "blockedWindows": [ "string" ],
      "blockingAlarms": [
         {
            "alarmIdentifier": "string",
            "type": "string"
         }
      ],
      "outcomeAlarms": [
         {
            "alarmIdentifier": "string",
            "type": "string"
         }
      ]
   },
   "zonalAutoshiftStatus": "string",
   "zonalShifts": [
      {
         "appliedStatus": "string",
         "awayFrom": "string",
         "comment": "string",
         "expiryTime": number,
         "practiceRunOutcome": "string",
         "resourceIdentifier": "string",
         "shiftType": "string",
         "startTime": number,
         "zonalShiftId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetManagedResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [appliedWeights](#API_GetManagedResource_ResponseSyntax) **   <a name="zonalshift-GetManagedResource-response-appliedWeights"></a>
A collection of key-value pairs that indicate whether resources are active in Availability Zones or not. The key name is the Availability Zone where the resource is deployed. The value is 1 or 0.
Type: String to float map
Key Length Constraints: Minimum length of 0. Maximum length of 20.
Valid Range: Minimum value of 0.0. Maximum value of 1.0.

 ** [arn](#API_GetManagedResource_ResponseSyntax) **   <a name="zonalshift-GetManagedResource-response-arn"></a>
The Amazon Resource Name (ARN) for the resource.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.
Pattern: `arn:.*`

 ** [autoshifts](#API_GetManagedResource_ResponseSyntax) **   <a name="zonalshift-GetManagedResource-response-autoshifts"></a>
An array of the autoshifts that are active for the resource.
Type: Array of [AutoshiftInResource](API_AutoshiftInResource.md) objects

 ** [name](#API_GetManagedResource_ResponseSyntax) **   <a name="zonalshift-GetManagedResource-response-name"></a>
The name of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [practiceRunConfiguration](#API_GetManagedResource_ResponseSyntax) **   <a name="zonalshift-GetManagedResource-response-practiceRunConfiguration"></a>
The practice run configuration for zonal autoshift that's associated with the resource.
Type: [PracticeRunConfiguration](API_PracticeRunConfiguration.md) object

 ** [zonalAutoshiftStatus](#API_GetManagedResource_ResponseSyntax) **   <a name="zonalshift-GetManagedResource-response-zonalAutoshiftStatus"></a>
The status for zonal autoshift for a resource. When the autoshift status is `ENABLED`, AWS shifts traffic for a resource away from an Availability Zone, on your behalf, when AWS determines that there's an issue in the Availability Zone that could potentially affect customers.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [zonalShifts](#API_GetManagedResource_ResponseSyntax) **   <a name="zonalshift-GetManagedResource-response-zonalShifts"></a>
The zonal shifts that are currently active for a resource.
Type: Array of [ZonalShiftInResource](API_ZonalShiftInResource.md) objects

## Errors
<a name="API_GetManagedResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_GetManagedResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/arc-zonal-shift-2022-10-30/GetManagedResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/arc-zonal-shift-2022-10-30/GetManagedResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-zonal-shift-2022-10-30/GetManagedResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/arc-zonal-shift-2022-10-30/GetManagedResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-zonal-shift-2022-10-30/GetManagedResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/arc-zonal-shift-2022-10-30/GetManagedResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/arc-zonal-shift-2022-10-30/GetManagedResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/arc-zonal-shift-2022-10-30/GetManagedResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/arc-zonal-shift-2022-10-30/GetManagedResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-zonal-shift-2022-10-30/GetManagedResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-zonal-shift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
