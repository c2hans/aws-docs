---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeClientProperties.html
---

# DescribeClientProperties
<a name="API_DescribeClientProperties"></a>

Retrieves a list that describes one or more specified Amazon WorkSpaces clients.

## Request Syntax
<a name="API_DescribeClientProperties_RequestSyntax"></a>

```
{
   "ResourceIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeClientProperties_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ResourceIds](#API_DescribeClientProperties_RequestSyntax) **   <a name="WorkSpaces-DescribeClientProperties-request-ResourceIds"></a>
The resource identifier, in the form of directory IDs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Length Constraints: Minimum length of 1.
Required: Yes

## Response Syntax
<a name="API_DescribeClientProperties_ResponseSyntax"></a>

```
{
   "ClientPropertiesList": [
      {
         "ClientProperties": {
            "LogUploadEnabled": "string",
            "ReconnectEnabled": "string"
         },
         "ResourceId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeClientProperties_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClientPropertiesList](#API_DescribeClientProperties_ResponseSyntax) **   <a name="WorkSpaces-DescribeClientProperties-response-ClientPropertiesList"></a>
Information about the specified Amazon WorkSpaces clients.
Type: Array of [ClientPropertiesResult](API_ClientPropertiesResult.md) objects

## Errors
<a name="API_DescribeClientProperties_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

 ** InvalidParameterValuesException **
One or more parameter values are not valid.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource could not be found.
 ** message **
The resource could not be found.
 ** ResourceId **
The ID of the resource that could not be found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeClientProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/DescribeClientProperties)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/DescribeClientProperties)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/DescribeClientProperties)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/DescribeClientProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/DescribeClientProperties)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/DescribeClientProperties)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/DescribeClientProperties)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/DescribeClientProperties)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/DescribeClientProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/DescribeClientProperties)
