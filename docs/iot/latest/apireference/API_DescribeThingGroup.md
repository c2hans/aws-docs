---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeThingGroup.html
---

# DescribeThingGroup
<a name="API_DescribeThingGroup"></a>

Describe a thing group.

Requires permission to access the [DescribeThingGroup](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DescribeThingGroup_RequestSyntax"></a>

```
GET /thing-groups/{{thingGroupName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeThingGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [thingGroupName](#API_DescribeThingGroup_RequestSyntax) **   <a name="iot-DescribeThingGroup-request-uri-thingGroupName"></a>
The name of the thing group.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_DescribeThingGroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeThingGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "indexName": "string",
   "queryString": "string",
   "queryVersion": "string",
   "status": "string",
   "thingGroupArn": "string",
   "thingGroupId": "string",
   "thingGroupMetadata": {
      "creationDate": number,
      "parentGroupName": "string",
      "rootToParentThingGroups": [
         {
            "groupArn": "string",
            "groupName": "string"
         }
      ]
   },
   "thingGroupName": "string",
   "thingGroupProperties": {
      "attributePayload": {
         "attributes": {
            "string" : "string"
         },
         "merge": boolean
      },
      "thingGroupDescription": "string"
   },
   "version": number
}
```

## Response Elements
<a name="API_DescribeThingGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [indexName](#API_DescribeThingGroup_ResponseSyntax) **   <a name="iot-DescribeThingGroup-response-indexName"></a>
The dynamic thing group index name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

 ** [queryString](#API_DescribeThingGroup_ResponseSyntax) **   <a name="iot-DescribeThingGroup-response-queryString"></a>
The dynamic thing group search query string.
Type: String
Length Constraints: Minimum length of 1.

 ** [queryVersion](#API_DescribeThingGroup_ResponseSyntax) **   <a name="iot-DescribeThingGroup-response-queryVersion"></a>
The dynamic thing group query version.
Type: String

 ** [status](#API_DescribeThingGroup_ResponseSyntax) **   <a name="iot-DescribeThingGroup-response-status"></a>
The dynamic thing group status.
Type: String
Valid Values: `ACTIVE | BUILDING | REBUILDING`

 ** [thingGroupArn](#API_DescribeThingGroup_ResponseSyntax) **   <a name="iot-DescribeThingGroup-response-thingGroupArn"></a>
The thing group ARN.
Type: String

 ** [thingGroupId](#API_DescribeThingGroup_ResponseSyntax) **   <a name="iot-DescribeThingGroup-response-thingGroupId"></a>
The thing group ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\-]+`

 ** [thingGroupMetadata](#API_DescribeThingGroup_ResponseSyntax) **   <a name="iot-DescribeThingGroup-response-thingGroupMetadata"></a>
Thing group metadata.
Type: [ThingGroupMetadata](API_ThingGroupMetadata.md) object

 ** [thingGroupName](#API_DescribeThingGroup_ResponseSyntax) **   <a name="iot-DescribeThingGroup-response-thingGroupName"></a>
The name of the thing group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

 ** [thingGroupProperties](#API_DescribeThingGroup_ResponseSyntax) **   <a name="iot-DescribeThingGroup-response-thingGroupProperties"></a>
The thing group properties.
Type: [ThingGroupProperties](API_ThingGroupProperties.md) object

 ** [version](#API_DescribeThingGroup_ResponseSyntax) **   <a name="iot-DescribeThingGroup-response-version"></a>
The version of the thing group.
Type: Long

## Errors
<a name="API_DescribeThingGroup_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_DescribeThingGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DescribeThingGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DescribeThingGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DescribeThingGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DescribeThingGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DescribeThingGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DescribeThingGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DescribeThingGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DescribeThingGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DescribeThingGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DescribeThingGroup)
