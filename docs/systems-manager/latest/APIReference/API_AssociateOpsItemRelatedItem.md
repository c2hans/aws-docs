---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_AssociateOpsItemRelatedItem.html
---

# AssociateOpsItemRelatedItem
<a name="API_AssociateOpsItemRelatedItem"></a>

Associates a related item to a Systems Manager OpsCenter OpsItem. For example, you can associate an Incident Manager incident or analysis with an OpsItem. Incident Manager and OpsCenter are tools in AWS Systems Manager.

## Request Syntax
<a name="API_AssociateOpsItemRelatedItem_RequestSyntax"></a>

```
{
   "AssociationType": "{{string}}",
   "OpsItemId": "{{string}}",
   "ResourceType": "{{string}}",
   "ResourceUri": "{{string}}"
}
```

## Request Parameters
<a name="API_AssociateOpsItemRelatedItem_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AssociationType](#API_AssociateOpsItemRelatedItem_RequestSyntax) **   <a name="systemsmanager-AssociateOpsItemRelatedItem-request-AssociationType"></a>
The type of association that you want to create between an OpsItem and a resource. OpsCenter supports `IsParentOf` and `RelatesTo` association types.
Type: String
Required: Yes

 ** [OpsItemId](#API_AssociateOpsItemRelatedItem_RequestSyntax) **   <a name="systemsmanager-AssociateOpsItemRelatedItem-request-OpsItemId"></a>
The ID of the OpsItem to which you want to associate a resource as a related item.
Type: String
Pattern: `^(oi)-[0-9a-f]{12}$`
Required: Yes

 ** [ResourceType](#API_AssociateOpsItemRelatedItem_RequestSyntax) **   <a name="systemsmanager-AssociateOpsItemRelatedItem-request-ResourceType"></a>
The type of resource that you want to associate with an OpsItem. OpsCenter supports the following types:
 `AWS::SSMIncidents::IncidentRecord`: an Incident Manager incident.
 `AWS::SSM::Document`: a Systems Manager (SSM) document.
Type: String
Required: Yes

 ** [ResourceUri](#API_AssociateOpsItemRelatedItem_RequestSyntax) **   <a name="systemsmanager-AssociateOpsItemRelatedItem-request-ResourceUri"></a>
The Amazon Resource Name (ARN) of the AWS resource that you want to associate with the OpsItem.
Type: String
Required: Yes

## Response Syntax
<a name="API_AssociateOpsItemRelatedItem_ResponseSyntax"></a>

```
{
   "AssociationId": "string"
}
```

## Response Elements
<a name="API_AssociateOpsItemRelatedItem_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AssociationId](#API_AssociateOpsItemRelatedItem_ResponseSyntax) **   <a name="systemsmanager-AssociateOpsItemRelatedItem-response-AssociationId"></a>
The association ID.
Type: String

## Errors
<a name="API_AssociateOpsItemRelatedItem_Errors"></a>

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

 ** OpsItemLimitExceededException **
The request caused OpsItems to exceed one or more quotas.
HTTP Status Code: 400

 ** OpsItemNotFoundException **
The specified OpsItem ID doesn't exist. Verify the ID and try again.
HTTP Status Code: 400

 ** OpsItemRelatedItemAlreadyExistsException **
The Amazon Resource Name (ARN) is already associated with the OpsItem.
HTTP Status Code: 400

## Examples
<a name="API_AssociateOpsItemRelatedItem_Examples"></a>

### Example
<a name="API_AssociateOpsItemRelatedItem_Example_1"></a>

This example illustrates one usage of AssociateOpsItemRelatedItem.

#### Sample Request
<a name="API_AssociateOpsItemRelatedItem_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-1.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.AssociateOpsItemRelatedItem
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm.associate-ops-item-related-item
X-Amz-Date: 20240804T181929Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240804/us-east-1/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 229

{
  "OpsItemId": "oi-649fExample",
  "AssociationType": "RelatesTo",
  "ResourceType": "AWS::SSMIncidents::IncidentRecord",
  "ResourceUri": "arn:aws:ssm-incidents::111122223333:incident-record/Test/c6bd8931-efae-a4ff-7f98-4490Example"
}
```

#### Sample Response
<a name="API_AssociateOpsItemRelatedItem_Example_1_Response"></a>

```
{
        "AssociationId": "61d7178d-a30d-4bc5-9b4e-a9e74EXAMPLE"
    }
```

## See Also
<a name="API_AssociateOpsItemRelatedItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/AssociateOpsItemRelatedItem)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/AssociateOpsItemRelatedItem)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/AssociateOpsItemRelatedItem)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/AssociateOpsItemRelatedItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/AssociateOpsItemRelatedItem)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/AssociateOpsItemRelatedItem)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/AssociateOpsItemRelatedItem)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/AssociateOpsItemRelatedItem)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/AssociateOpsItemRelatedItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/AssociateOpsItemRelatedItem)
