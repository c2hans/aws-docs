---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_ListRelatedItems.html
---

# ListRelatedItems
<a name="API_ListRelatedItems"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

List all related items for an incident record.

## Request Syntax
<a name="API_ListRelatedItems_RequestSyntax"></a>

```
POST /listRelatedItems HTTP/1.1
Content-type: application/json

{
   "incidentRecordArn": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListRelatedItems_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListRelatedItems_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [incidentRecordArn](#API_ListRelatedItems_RequestSyntax) **   <a name="IncidentManager-ListRelatedItems-request-incidentRecordArn"></a>
The Amazon Resource Name (ARN) of the incident record containing the listed related items.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: Yes

 ** [maxResults](#API_ListRelatedItems_RequestSyntax) **   <a name="IncidentManager-ListRelatedItems-request-maxResults"></a>
The maximum number of related items per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListRelatedItems_RequestSyntax) **   <a name="IncidentManager-ListRelatedItems-request-nextToken"></a>
The pagination token for the next set of items to return. (You received this token from a previous call.)
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

## Response Syntax
<a name="API_ListRelatedItems_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "relatedItems": [
      {
         "generatedId": "string",
         "identifier": {
            "type": "string",
            "value": { ... }
         },
         "title": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRelatedItems_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListRelatedItems_ResponseSyntax) **   <a name="IncidentManager-ListRelatedItems-response-nextToken"></a>
The pagination token to use when requesting the next set of items. If there are no additional items to return, the string is null.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.

 ** [relatedItems](#API_ListRelatedItems_ResponseSyntax) **   <a name="IncidentManager-ListRelatedItems-response-relatedItems"></a>
Details about each related item.
Type: Array of [RelatedItem](API_RelatedItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_ListRelatedItems_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this operation.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## Examples
<a name="API_ListRelatedItems_Examples"></a>

### Example
<a name="API_ListRelatedItems_Example_1"></a>

This example illustrates one usage of ListRelatedItems.

#### Sample Request
<a name="API_ListRelatedItems_Example_1_Request"></a>

```
POST /listRelatedItems HTTP/1.1
Host: ssm-incidents.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-incidents.list-related-items
X-Amz-Date: 20210811T172030Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210811/us-east-1/ssm-incidents/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 130

{
	"incidentRecordArn": "arn:aws:ssm-incidents::111122223333:incident-record/example-response/78bd9919-b9ac-962d-91e0-149960600e3f"
}
```

#### Sample Response
<a name="API_ListRelatedItems_Example_1_Response"></a>

```
{
    "relatedItems": [
        {
            "identifier": {
                "type": "OTHER",
                "value": {
                    "url": "https://us-east-1.console.aws.amazon.com/systems-manager/opsitems/oi-cd91EXAMPLE/workbench?region=us-east-1"
                }
            },
            "title": "Example related item",
            "generatedId": "related-item/PARENT/F95638BAA087E072DC56189CB4D2ADEC"

        },
        {
            "identifier": {
                "type": "PARENT",
                "value": {
                    "arn": "arn:aws:ssm:us-east-1:111122223333:opsitem/oi-40089EXAMPLE"
                }
            },
            "title": "parentItem",
            "generatedId": "related-item/PARENT/F95638BAA087E072DC56189CB4D2ADEC"

        }
    ]
}
```

## See Also
<a name="API_ListRelatedItems_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-incidents-2018-05-10/ListRelatedItems)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-incidents-2018-05-10/ListRelatedItems)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/ListRelatedItems)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-incidents-2018-05-10/ListRelatedItems)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/ListRelatedItems)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-incidents-2018-05-10/ListRelatedItems)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-incidents-2018-05-10/ListRelatedItems)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-incidents-2018-05-10/ListRelatedItems)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-incidents-2018-05-10/ListRelatedItems)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/ListRelatedItems)
