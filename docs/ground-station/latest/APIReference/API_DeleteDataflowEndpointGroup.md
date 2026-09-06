---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DeleteDataflowEndpointGroup.html
---

# DeleteDataflowEndpointGroup
<a name="API_DeleteDataflowEndpointGroup"></a>

Deletes a dataflow endpoint group.

## Request Syntax
<a name="API_DeleteDataflowEndpointGroup_RequestSyntax"></a>

```
DELETE /dataflowEndpointGroup/{{dataflowEndpointGroupId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteDataflowEndpointGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [dataflowEndpointGroupId](#API_DeleteDataflowEndpointGroup_RequestSyntax) **   <a name="groundstation-DeleteDataflowEndpointGroup-request-uri-dataflowEndpointGroupId"></a>
UUID of a dataflow endpoint group.
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Request Body
<a name="API_DeleteDataflowEndpointGroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteDataflowEndpointGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "dataflowEndpointGroupId": "string"
}
```

## Response Elements
<a name="API_DeleteDataflowEndpointGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dataflowEndpointGroupId](#API_DeleteDataflowEndpointGroup_ResponseSyntax) **   <a name="groundstation-DeleteDataflowEndpointGroup-response-dataflowEndpointGroupId"></a>
UUID of a dataflow endpoint group.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

## Errors
<a name="API_DeleteDataflowEndpointGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependencyException **
Dependency encountered an error.
 ** parameterName **
Name of the parameter that caused the exception.
HTTP Status Code: 531

 ** InvalidParameterException **
One or more parameters are not valid.
 ** parameterName **
Name of the invalid parameter.
HTTP Status Code: 431

 ** ResourceNotFoundException **
Resource was not found.
HTTP Status Code: 434

## See Also
<a name="API_DeleteDataflowEndpointGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/groundstation-2019-05-23/DeleteDataflowEndpointGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/groundstation-2019-05-23/DeleteDataflowEndpointGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/DeleteDataflowEndpointGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/groundstation-2019-05-23/DeleteDataflowEndpointGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/DeleteDataflowEndpointGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/groundstation-2019-05-23/DeleteDataflowEndpointGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/groundstation-2019-05-23/DeleteDataflowEndpointGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/groundstation-2019-05-23/DeleteDataflowEndpointGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/groundstation-2019-05-23/DeleteDataflowEndpointGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/DeleteDataflowEndpointGroup)
