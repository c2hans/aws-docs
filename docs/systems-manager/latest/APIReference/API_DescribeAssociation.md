---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeAssociation.html
---

# DescribeAssociation
<a name="API_DescribeAssociation"></a>

Describes the association for the specified target or managed node. If you created the association by using the `Targets` parameter, then you must retrieve the association by using the association ID.

## Request Syntax
<a name="API_DescribeAssociation_RequestSyntax"></a>

```
{
   "AssociationId": "{{string}}",
   "AssociationVersion": "{{string}}",
   "InstanceId": "{{string}}",
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAssociation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AssociationId](#API_DescribeAssociation_RequestSyntax) **   <a name="systemsmanager-DescribeAssociation-request-AssociationId"></a>
The association ID for which you want information.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: No

 ** [AssociationVersion](#API_DescribeAssociation_RequestSyntax) **   <a name="systemsmanager-DescribeAssociation-request-AssociationVersion"></a>
Specify the association version to retrieve. To view the latest version, either specify `$LATEST` for this parameter, or omit this parameter. To view a list of all associations for a managed node, use [ListAssociations](API_ListAssociations.md). To get a list of versions for a specific association, use [ListAssociationVersions](API_ListAssociationVersions.md).
Type: String
Pattern: `^(([$]LATEST)|([1-9][0-9]*))$`
Required: No

 ** [InstanceId](#API_DescribeAssociation_RequestSyntax) **   <a name="systemsmanager-DescribeAssociation-request-InstanceId"></a>
The managed node ID.
Type: String
Pattern: `(^i-(\w{8}|\w{17})$)|(^mi-\w{17}$)`
Required: No

 ** [Name](#API_DescribeAssociation_RequestSyntax) **   <a name="systemsmanager-DescribeAssociation-request-Name"></a>
The name of the SSM document.
Type: String
Pattern: `^[a-zA-Z0-9_\-.:/]{3,128}$`
Required: No

## Response Syntax
<a name="API_DescribeAssociation_ResponseSyntax"></a>

```
{
   "AssociationDescription": {
      "AlarmConfiguration": {
         "Alarms": [
            {
               "Name": "string"
            }
         ],
         "IgnorePollAlarmFailure": boolean
      },
      "ApplyOnlyAtCronInterval": boolean,
      "AssociationDispatchAssumeRole": "string",
      "AssociationId": "string",
      "AssociationName": "string",
      "AssociationVersion": "string",
      "AutomationTargetParameterName": "string",
      "CalendarNames": [ "string" ],
      "ComplianceSeverity": "string",
      "Date": number,
      "DocumentVersion": "string",
      "Duration": number,
      "InstanceId": "string",
      "LastExecutionDate": number,
      "LastSuccessfulExecutionDate": number,
      "LastUpdateAssociationDate": number,
      "MaxConcurrency": "string",
      "MaxErrors": "string",
      "Name": "string",
      "OutputLocation": {
         "S3Location": {
            "OutputS3BucketName": "string",
            "OutputS3KeyPrefix": "string",
            "OutputS3Region": "string"
         }
      },
      "Overview": {
         "AssociationStatusAggregatedCount": {
            "string" : number
         },
         "DetailedStatus": "string",
         "Status": "string"
      },
      "Parameters": {
         "string" : [ "string" ]
      },
      "ScheduleExpression": "string",
      "ScheduleOffset": number,
      "Status": {
         "AdditionalInfo": "string",
         "Date": number,
         "Message": "string",
         "Name": "string"
      },
      "SyncCompliance": "string",
      "TargetLocations": [
         {
            "Accounts": [ "string" ],
            "ExcludeAccounts": [ "string" ],
            "ExecutionRoleName": "string",
            "IncludeChildOrganizationUnits": boolean,
            "Regions": [ "string" ],
            "TargetLocationAlarmConfiguration": {
               "Alarms": [
                  {
                     "Name": "string"
                  }
               ],
               "IgnorePollAlarmFailure": boolean
            },
            "TargetLocationMaxConcurrency": "string",
            "TargetLocationMaxErrors": "string",
            "Targets": [
               {
                  "Key": "string",
                  "Values": [ "string" ]
               }
            ],
            "TargetsMaxConcurrency": "string",
            "TargetsMaxErrors": "string"
         }
      ],
      "TargetMaps": [
         {
            "string" : [ "string" ]
         }
      ],
      "Targets": [
         {
            "Key": "string",
            "Values": [ "string" ]
         }
      ],
      "TriggeredAlarms": [
         {
            "Name": "string",
            "State": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_DescribeAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AssociationDescription](#API_DescribeAssociation_ResponseSyntax) **   <a name="systemsmanager-DescribeAssociation-response-AssociationDescription"></a>
Information about the association.
Type: [AssociationDescription](API_AssociationDescription.md) object

## Errors
<a name="API_DescribeAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AssociationDoesNotExist **
The specified association doesn't exist.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidAssociationVersion **
The version you specified isn't valid. Use ListAssociationVersions to view all versions of an association according to the association ID. Or, use the `$LATEST` parameter to view the latest version of the association.
HTTP Status Code: 400

 ** InvalidDocument **
The specified SSM document doesn't exist.
 ** Message **
The SSM document doesn't exist or the document isn't available to the user. This exception can be issued by various API operations.
HTTP Status Code: 400

 ** InvalidInstanceId **
The following problems can cause this exception:
+ You don't have permission to access the managed node.
+  AWS Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.
+ SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.
+ The managed node isn't in a valid state. Valid states are: `Running`, `Pending`, `Stopped`, and `Stopping`. Invalid states are: `Shutting-down` and `Terminated`.
HTTP Status Code: 400

## Examples
<a name="API_DescribeAssociation_Examples"></a>

### Example
<a name="API_DescribeAssociation_Example_1"></a>

This example illustrates one usage of DescribeAssociation.

#### Sample Request
<a name="API_DescribeAssociation_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.DescribeAssociation
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240324T153423Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240324/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 57

{
    "AssociationId": "fa94c678-85c6-4d40-926b-7c791EXAMPLE"
}
```

#### Sample Response
<a name="API_DescribeAssociation_Example_1_Response"></a>

```
{
    "AssociationDescription": {
        "ApplyOnlyAtCronInterval": false,
        "AssociationId": "fa94c678-85c6-4d40-926b-7c791EXAMPLE",
        "AssociationVersion": "1",
        "ComplianceSeverity": "UNSPECIFIED",
        "Date": 1561053271.583,
        "DocumentVersion": "$DEFAULT",
        "LastExecutionDate": 1582037438.692,
        "LastSuccessfulExecutionDate": 1582037438.692,
        "LastUpdateAssociationDate": 1561053271.583,
        "Name": "AWS-UpdateSSMAgent",
        "Overview": {
            "AssociationStatusAggregatedCount": {
                "Success": 3
            },
            "DetailedStatus": "Success",
            "Status": "Success"
        },
        "Parameters": {
            "allowDowngrade": [
                "false"
            ],
            "version": [
                ""
            ]
        },
        "Targets": [
            {
                "Key": "tag:ssm",
                "Values": [
                    "true"
                ]
            }
        ]
    }
}
```

## See Also
<a name="API_DescribeAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribeAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribeAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribeAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribeAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribeAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribeAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribeAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribeAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribeAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribeAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
