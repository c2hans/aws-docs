---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DisassociateOpsItemRelatedItem.html
---

# DisassociateOpsItemRelatedItem
<a name="API_DisassociateOpsItemRelatedItem"></a>

Deletes the association between an OpsItem and a related item. For example, this API operation can delete an Incident Manager incident from an OpsItem. Incident Manager is a tool in AWS Systems Manager.

## Request Syntax
<a name="API_DisassociateOpsItemRelatedItem_RequestSyntax"></a>

```
{
   "AssociationId": "{{string}}",
   "OpsItemId": "{{string}}"
}
```

## Request Parameters
<a name="API_DisassociateOpsItemRelatedItem_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AssociationId](#API_DisassociateOpsItemRelatedItem_RequestSyntax) **   <a name="systemsmanager-DisassociateOpsItemRelatedItem-request-AssociationId"></a>
The ID of the association for which you want to delete an association between the OpsItem and a related item.
Type: String
Required: Yes

 ** [OpsItemId](#API_DisassociateOpsItemRelatedItem_RequestSyntax) **   <a name="systemsmanager-DisassociateOpsItemRelatedItem-request-OpsItemId"></a>
The ID of the OpsItem for which you want to delete an association between the OpsItem and a related item.
Type: String
Pattern: `^(oi)-[0-9a-f]{12}$`
Required: Yes

## Response Elements
<a name="API_DisassociateOpsItemRelatedItem_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisassociateOpsItemRelatedItem_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** OpsItemConflictException **
The specified OpsItem is in the process of being deleted.
HTTP Status Code: 400

 ** OpsItemInvalidParameterException **
A specified parameter argument isn't valid. Verify the available arguments and try again.
HTTP Status Code: 400

 ** OpsItemNotFoundException **
The specified OpsItem ID doesn't exist. Verify the ID and try again.
HTTP Status Code: 400

 ** OpsItemRelatedItemAssociationNotFoundException **
The association wasn't found using the parameters you specified in the call. Verify the information and try again.
HTTP Status Code: 400

## Examples
<a name="API_DisassociateOpsItemRelatedItem_Examples"></a>

### Example
<a name="API_DisassociateOpsItemRelatedItem_Example_1"></a>

This example illustrates one usage of DisassociateOpsItemRelatedItem.

#### Sample Request
<a name="API_DisassociateOpsItemRelatedItem_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-1.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.DisassociateOpsItemRelatedItem
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm.disassociate-ops-item-related-item
X-Amz-Date: 20240910T182919Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240910/us-east-1/ssm/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 89

{
	"OpsItemId": "oi-f99f2EXAMPLE",
	"AssociationId": "e2036148-cccb-490e-ac2a-390e5EXAMPLE"
}
```

#### Sample Response
<a name="API_DisassociateOpsItemRelatedItem_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_DisassociateOpsItemRelatedItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DisassociateOpsItemRelatedItem)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DisassociateOpsItemRelatedItem)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DisassociateOpsItemRelatedItem)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DisassociateOpsItemRelatedItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DisassociateOpsItemRelatedItem)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DisassociateOpsItemRelatedItem)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DisassociateOpsItemRelatedItem)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DisassociateOpsItemRelatedItem)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DisassociateOpsItemRelatedItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DisassociateOpsItemRelatedItem)
