---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListAssociationVersions.html
---

# ListAssociationVersions
<a name="API_ListAssociationVersions"></a>

Retrieves all versions of an association for a specific association ID.

## Request Syntax
<a name="API_ListAssociationVersions_RequestSyntax"></a>

```
{
   "AssociationId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAssociationVersions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AssociationId](#API_ListAssociationVersions_RequestSyntax) **   <a name="systemsmanager-ListAssociationVersions-request-AssociationId"></a>
The association ID for which you want to view all versions.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** [MaxResults](#API_ListAssociationVersions_RequestSyntax) **   <a name="systemsmanager-ListAssociationVersions-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListAssociationVersions_RequestSyntax) **   <a name="systemsmanager-ListAssociationVersions-request-NextToken"></a>
A token to start the list. Use this token to get the next set of results.
Type: String
Required: No

## Response Syntax
<a name="API_ListAssociationVersions_ResponseSyntax"></a>

```
{
   "AssociationVersions": [
      {
         "ApplyOnlyAtCronInterval": boolean,
         "AssociationDispatchAssumeRole": "string",
         "AssociationId": "string",
         "AssociationName": "string",
         "AssociationVersion": "string",
         "CalendarNames": [ "string" ],
         "ComplianceSeverity": "string",
         "CreatedDate": number,
         "DocumentVersion": "string",
         "Duration": number,
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
         "Parameters": {
            "string" : [ "string" ]
         },
         "ScheduleExpression": "string",
         "ScheduleOffset": number,
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
         ]
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAssociationVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AssociationVersions](#API_ListAssociationVersions_ResponseSyntax) **   <a name="systemsmanager-ListAssociationVersions-response-AssociationVersions"></a>
Information about all versions of the association for the specified association ID.
Type: Array of [AssociationVersionInfo](API_AssociationVersionInfo.md) objects
Array Members: Minimum number of 1 item.

 ** [NextToken](#API_ListAssociationVersions_ResponseSyntax) **   <a name="systemsmanager-ListAssociationVersions-response-NextToken"></a>
The token for the next set of items to return. Use this token to get the next set of results.
Type: String

## Errors
<a name="API_ListAssociationVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AssociationDoesNotExist **
The specified association doesn't exist.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidNextToken **
The specified token isn't valid.
HTTP Status Code: 400

## Examples
<a name="API_ListAssociationVersions_Examples"></a>

### Example
<a name="API_ListAssociationVersions_Example_1"></a>

This example illustrates one usage of ListAssociationVersions.

#### Sample Request
<a name="API_ListAssociationVersions_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.ListAssociationVersions
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240325T144807Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240325/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 57

{
    "AssociationId": "fa94c678-85c6-4d40-926b-7c791EXAMPLE"
}
```

#### Sample Response
<a name="API_ListAssociationVersions_Example_1_Response"></a>

```
{
    "AssociationVersions": [
        {
            "ApplyOnlyAtCronInterval": false,
            "AssociationId": "fa94c678-85c6-4d40-926b-7c791EXAMPLE",
            "AssociationVersion": "1",
            "CreatedDate": 1561053271.583,
            "Name": "AWS-UpdateSSMAgent",
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
    ]
}
```

## See Also
<a name="API_ListAssociationVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/ListAssociationVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/ListAssociationVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ListAssociationVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/ListAssociationVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ListAssociationVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/ListAssociationVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/ListAssociationVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/ListAssociationVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/ListAssociationVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ListAssociationVersions)
