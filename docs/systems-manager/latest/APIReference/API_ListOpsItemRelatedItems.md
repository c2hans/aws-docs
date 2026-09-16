---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListOpsItemRelatedItems.html
---

# ListOpsItemRelatedItems
<a name="API_ListOpsItemRelatedItems"></a>

Lists all related-item resources associated with a Systems Manager OpsCenter OpsItem. OpsCenter is a tool in AWS Systems Manager.

## Request Syntax
<a name="API_ListOpsItemRelatedItems_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Key": "{{string}}",
         "Operator": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "OpsItemId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListOpsItemRelatedItems_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListOpsItemRelatedItems_RequestSyntax) **   <a name="systemsmanager-ListOpsItemRelatedItems-request-Filters"></a>
One or more OpsItem filters. Use a filter to return a more specific list of results.
Type: Array of [OpsItemRelatedItemsFilter](API_OpsItemRelatedItemsFilter.md) objects
Required: No

 ** [MaxResults](#API_ListOpsItemRelatedItems_RequestSyntax) **   <a name="systemsmanager-ListOpsItemRelatedItems-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListOpsItemRelatedItems_RequestSyntax) **   <a name="systemsmanager-ListOpsItemRelatedItems-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

 ** [OpsItemId](#API_ListOpsItemRelatedItems_RequestSyntax) **   <a name="systemsmanager-ListOpsItemRelatedItems-request-OpsItemId"></a>
The ID of the OpsItem for which you want to list all related-item resources.
Type: String
Pattern: `^(oi)-[0-9a-f]{12}$`
Required: No

## Response Syntax
<a name="API_ListOpsItemRelatedItems_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Summaries": [
      {
         "AssociationId": "string",
         "AssociationType": "string",
         "CreatedBy": {
            "Arn": "string"
         },
         "CreatedTime": number,
         "LastModifiedBy": {
            "Arn": "string"
         },
         "LastModifiedTime": number,
         "OpsItemId": "string",
         "ResourceType": "string",
         "ResourceUri": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListOpsItemRelatedItems_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListOpsItemRelatedItems_ResponseSyntax) **   <a name="systemsmanager-ListOpsItemRelatedItems-response-NextToken"></a>
The token for the next set of items to return. Use this token to get the next set of results.
Type: String

 ** [Summaries](#API_ListOpsItemRelatedItems_ResponseSyntax) **   <a name="systemsmanager-ListOpsItemRelatedItems-response-Summaries"></a>
A list of related-item resources for the specified OpsItem.
Type: Array of [OpsItemRelatedItemSummary](API_OpsItemRelatedItemSummary.md) objects

## Errors
<a name="API_ListOpsItemRelatedItems_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** OpsItemInvalidParameterException **
A specified parameter argument isn't valid. Verify the available arguments and try again.
HTTP Status Code: 400

## Examples
<a name="API_ListOpsItemRelatedItems_Examples"></a>

### Example
<a name="API_ListOpsItemRelatedItems_Example_1"></a>

This example illustrates one usage of ListOpsItemRelatedItems.

#### Sample Request
<a name="API_ListOpsItemRelatedItems_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-1.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.ListOpsItemRelatedItems
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm.list-ops-item-related-items
X-Amz-Date: 20240910T180314Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240910/us-east-1/ssm/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 32

{
	"OpsItemId": "oi-f99f2EXAMPLE"
}
```

#### Sample Response
<a name="API_ListOpsItemRelatedItems_Example_1_Response"></a>

```
{
    "Summaries": [
        {
            "OpsItemId": "oi-f99f2EXAMPLE",
            "AssociationId": "e2036148-cccb-490e-ac2a-390e5EXAMPLE",
            "ResourceType": "AWS::SSMIncidents::IncidentRecord",
            "AssociationType": "IsParentOf",
            "ResourceUri": "arn:aws:ssm-incidents::111122223333:incident-record/example-response/64bd9b45-1d0e-2622-840d-03a87a1451fa",
            "CreatedBy": {
                "Arn": "arn:aws:sts::111122223333:assumed-role/AWSServiceRoleForIncidentManager/IncidentResponse"
            },
            "CreatedTime": "2024-08-11T18:47:14.994000+00:00",
            "LastModifiedBy": {
                "Arn": "arn:aws:sts::111122223333:assumed-role/AWSServiceRoleForIncidentManager/IncidentResponse"
            },
            "LastModifiedTime": "2024-08-11T18:47:14.994000+00:00"
        }
    ]
}
```

## See Also
<a name="API_ListOpsItemRelatedItems_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/ListOpsItemRelatedItems)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/ListOpsItemRelatedItems)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ListOpsItemRelatedItems)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/ListOpsItemRelatedItems)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ListOpsItemRelatedItems)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/ListOpsItemRelatedItems)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/ListOpsItemRelatedItems)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/ListOpsItemRelatedItems)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/ListOpsItemRelatedItems)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ListOpsItemRelatedItems)
