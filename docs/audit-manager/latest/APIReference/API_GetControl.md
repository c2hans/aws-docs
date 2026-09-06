---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetControl.html
---

# GetControl
<a name="API_GetControl"></a>

**Important**
 AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

 Gets information about a specified control.

## Request Syntax
<a name="API_GetControl_RequestSyntax"></a>

```
GET /controls/{{controlId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetControl_RequestParameters"></a>

The request uses the following URI parameters.

 ** [controlId](#API_GetControl_RequestSyntax) **   <a name="auditmanager-GetControl-request-uri-controlId"></a>
 The identifier for the control.
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

## Request Body
<a name="API_GetControl_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetControl_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "control": {
      "actionPlanInstructions": "string",
      "actionPlanTitle": "string",
      "arn": "string",
      "controlMappingSources": [
         {
            "sourceDescription": "string",
            "sourceFrequency": "string",
            "sourceId": "string",
            "sourceKeyword": {
               "keywordInputType": "string",
               "keywordValue": "string"
            },
            "sourceName": "string",
            "sourceSetUpOption": "string",
            "sourceType": "string",
            "troubleshootingText": "string"
         }
      ],
      "controlSources": "string",
      "createdAt": number,
      "createdBy": "string",
      "description": "string",
      "id": "string",
      "lastUpdatedAt": number,
      "lastUpdatedBy": "string",
      "name": "string",
      "state": "string",
      "tags": {
         "string" : "string"
      },
      "testingInformation": "string",
      "type": "string"
   }
}
```

## Response Elements
<a name="API_GetControl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [control](#API_GetControl_ResponseSyntax) **   <a name="auditmanager-GetControl-response-control"></a>
 The details of the control that the `GetControl` API returned.
Type: [Control](API_Control.md) object

## Errors
<a name="API_GetControl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 Your account isn't registered with AWS Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again.
HTTP Status Code: 403

 ** InternalServerException **
 An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The resource that's specified in the request can't be found.
 ** resourceId **
 The unique identifier for the resource.
 ** resourceType **
 The type of resource that's affected by the error.
HTTP Status Code: 404

 ** ValidationException **
 The request has invalid or missing parameters.
 ** fields **
 The fields that caused the error, if applicable.
 ** reason **
 The reason the request failed validation.
HTTP Status Code: 400

## Examples
<a name="API_GetControl_Examples"></a>

### Getting information about a control
<a name="API_GetControl_Example_1"></a>

This example shows a sample response for the `GetControl` API operation. This example returns details about a specific custom control. In this case, the control has three automated data sources. Each data source is a specific CloudTrail event (`ec2_ModifyInstanceAttribute`, `ec2_CreateImage`, and `ec2_RunInstances`).

#### Sample Response
<a name="API_GetControl_Example_1_Response"></a>

```
{
    "control": {
        "arn": "arn:aws:auditmanager:us-east-1:111122223333:control/a1b2c3d4-5678-90ab-cdef-example11111",
        "id": "a1b2c3d4-5678-90ab-cdef-example11111",
        "type": "Custom",
        "name": "1.0.1 - CloudTrail Instance Events_CUSTOM",
        "description": "CloudTrail eventName for instances",
        "testingInformation": "CloudTrail eventName:\n\n- CreateImage\n- RunInstances\n- ModifyInstanceAttribute ",
        "actionPlanTitle": "The title of my action plan",
        "actionPlanInstructions": "The details of my action plan instructions",
        "controlSources": "AWS CloudTrail",
        "controlMappingSources": [
            {
                "sourceId": "sourceid-5678-90ab-cdef-example11111",
                "sourceName": "Data source 1",
                "sourceSetUpOption": "System_Controls_Mapping",
                "sourceType": "AWS_Cloudtrail",
                "sourceKeyword": {
                    "keywordInputType": "SELECT_FROM_LIST",
                    "keywordValue": "ec2_ModifyInstanceAttribute"
                }
            },
            {
                "sourceId": "sourceid-5678-90ab-cdef-example22222",
                "sourceName": "Data source 2",
                "sourceSetUpOption": "System_Controls_Mapping",
                "sourceType": "AWS_Cloudtrail",
                "sourceKeyword": {
                    "keywordInputType": "SELECT_FROM_LIST",
                    "keywordValue": "ec2_CreateImage"
                }
            },
            {
                "sourceId": "sourceid-5678-90ab-cdef-example33333",
                "sourceName": "Data source 3",
                "sourceSetUpOption": "System_Controls_Mapping",
                "sourceType": "AWS_Cloudtrail",
                "sourceKeyword": {
                    "keywordInputType": "SELECT_FROM_LIST",
                    "keywordValue": "ec2_RunInstances"
                }
            }
        ],
        "createdAt": "2023-03-13T12:00:58.943000-07:00",
        "lastUpdatedAt": "2023-03-13T12:00:58.943000-07:00",
        "createdBy": "john-doe",
        "lastUpdatedBy": "jane-doe",
        "state": "ACTIVE",
        "tags": {
            "Department": "Legal"
        }
    }
}
```

## See Also
<a name="API_GetControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/auditmanager-2017-07-25/GetControl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/auditmanager-2017-07-25/GetControl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/GetControl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/auditmanager-2017-07-25/GetControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/GetControl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/auditmanager-2017-07-25/GetControl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/auditmanager-2017-07-25/GetControl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/auditmanager-2017-07-25/GetControl)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/auditmanager-2017-07-25/GetControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/GetControl)
