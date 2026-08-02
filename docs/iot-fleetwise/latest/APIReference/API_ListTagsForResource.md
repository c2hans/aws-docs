---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListTagsForResource.html
---

# ListTagsForResource
<a name="API_ListTagsForResource"></a>

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

Lists the tags (metadata) you have assigned to the resource.

## Request Syntax
<a name="API_ListTagsForResource_RequestSyntax"></a>

```
{
   "ResourceARN": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTagsForResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceARN](#API_ListTagsForResource_RequestSyntax) **   <a name="iotfleetwise-ListTagsForResource-request-ResourceARN"></a>
The ARN of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:.*`
Required: Yes

## Response Syntax
<a name="API_ListTagsForResource_ResponseSyntax"></a>

```
{
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Tags](#API_ListTagsForResource_ResponseSyntax) **   <a name="iotfleetwise-ListTagsForResource-response-Tags"></a>
The list of tags assigned to the resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

## Errors
<a name="API_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request couldn't be completed because the server temporarily failed.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the command.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource wasn't found.
 ** resourceId **
The identifier of the resource that wasn't found.
 ** resourceType **
The type of resource that wasn't found.
HTTP Status Code: 400

 ** ThrottlingException **
The request couldn't be completed due to throttling.
 ** quotaCode **
The quota identifier of the applied throttling rules for this request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the command.
 ** serviceCode **
The code for the service that couldn't be completed due to throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The list of fields that fail to satisfy the constraints specified by an AWS service.
 ** reason **
The reason the input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotfleetwise-2021-06-17/ListTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotfleetwise-2021-06-17/ListTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/ListTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotfleetwise-2021-06-17/ListTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/ListTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotfleetwise-2021-06-17/ListTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotfleetwise-2021-06-17/ListTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotfleetwise-2021-06-17/ListTagsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotfleetwise-2021-06-17/ListTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/ListTagsForResource)
