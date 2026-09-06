---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListAssociations.html
---

# ListAssociations
<a name="API_ListAssociations"></a>

Returns all State Manager associations in the current AWS account and AWS Region. You can limit the results to a specific State Manager association document or managed node by specifying a filter. State Manager is a tool in AWS Systems Manager.

## Request Syntax
<a name="API_ListAssociations_RequestSyntax"></a>

```
{
   "AssociationFilterList": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAssociations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AssociationFilterList](#API_ListAssociations_RequestSyntax) **   <a name="systemsmanager-ListAssociations-request-AssociationFilterList"></a>
One or more filters. Use a filter to return a more specific list of results.
Filtering associations using the `InstanceID` attribute only returns legacy associations created using the `InstanceID` attribute. Associations targeting the managed node that are part of the Target Attributes `ResourceGroup` or `Tags` aren't returned.
Type: Array of [AssociationFilter](API_AssociationFilter.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [MaxResults](#API_ListAssociations_RequestSyntax) **   <a name="systemsmanager-ListAssociations-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListAssociations_RequestSyntax) **   <a name="systemsmanager-ListAssociations-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

## Response Syntax
<a name="API_ListAssociations_ResponseSyntax"></a>

```
{
   "Associations": [
      {
         "AssociationId": "string",
         "AssociationName": "string",
         "AssociationVersion": "string",
         "DocumentVersion": "string",
         "Duration": number,
         "InstanceId": "string",
         "LastExecutionDate": number,
         "Name": "string",
         "Overview": {
            "AssociationStatusAggregatedCount": {
               "string" : number
            },
            "DetailedStatus": "string",
            "Status": "string"
         },
         "ScheduleExpression": "string",
         "ScheduleOffset": number,
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
<a name="API_ListAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Associations](#API_ListAssociations_ResponseSyntax) **   <a name="systemsmanager-ListAssociations-response-Associations"></a>
The associations.
Type: Array of [Association](API_Association.md) objects

 ** [NextToken](#API_ListAssociations_ResponseSyntax) **   <a name="systemsmanager-ListAssociations-response-NextToken"></a>
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
Type: String

## Errors
<a name="API_ListAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidNextToken **
The specified token isn't valid.
HTTP Status Code: 400

## Examples
<a name="API_ListAssociations_Examples"></a>

### Example
<a name="API_ListAssociations_Example_1"></a>

This example illustrates one usage of ListAssociations.

#### Sample Request
<a name="API_ListAssociations_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.ListAssociations
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240325T143814Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240325/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 2
```

#### Sample Response
<a name="API_ListAssociations_Example_1_Response"></a>

```
{
    "Associations": [
        {
            "AssociationId": "fa94c678-85c6-4d40-926b-7c791EXAMPLE",
            "AssociationVersion": "1",
            "LastExecutionDate": 1582037438.692,
            "Name": "AWS-UpdateSSMAgent",
            "Overview": {
                "AssociationStatusAggregatedCount": {
                    "Success": 3
                },
                "DetailedStatus": "Success",
                "Status": "Success"
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
<a name="API_ListAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/ListAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/ListAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ListAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/ListAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ListAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/ListAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/ListAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/ListAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/ListAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ListAssociations)
